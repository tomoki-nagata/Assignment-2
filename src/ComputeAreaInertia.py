import trimesh
import numpy as np
from shapely.geometry import Polygon

def compute_polygon_properties(vertices):
    """
    Compute geometric properties of a polygon using shoelace formula.
    
    Args:
        vertices (np.array): Nx2 array of polygon vertices
        
    Returns:
        tuple: (area, centroid (x,y), Ixx, Iyy, Ixy moments)
    """
        
    n = len(vertices)
    if n < 3:
        return 0.0, (0.0, 0.0), 0.0, 0.0, 0.0
    
    x = vertices[:, 0]
    y = vertices[:, 1]
    
    A = 0.0
    Sx = 0.0
    Sy = 0.0
    Ixx = 0.0
    Iyy = 0.0
    Ixy = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        xi, yi = x[i], y[i]
        xj, yj = x[j], y[j]
        
        factor = xi * yj - xj * yi
        A += factor
        Sx += factor * (yi + yj)
        Sy += factor * (xi + xj)
        Ixx += factor * (yi**2 + yi * yj + yj**2)
        Iyy += factor * (xi**2 + xi * xj + xj**2)
        Ixy += factor * (xi * yj + 2 * xi * yi + 2 * xj * yj + xj * yi)
    
    A *= 0.5
    if abs(A) < 1e-12:
        return 0.0, (0.0, 0.0), 0.0, 0.0, 0.0
    
    sign = np.sign(A)
    A_abs = abs(A)
    
    Sx /= 6 * A
    Sy /= 6 * A
    
    Ixx /= 12 * sign
    Iyy /= 12 * sign
    Ixy /= 24 * sign
    
    Cx = Sy
    Cy = Sx
    
    Ixx_centroid = Ixx - A_abs * Cy**2
    Iyy_centroid = Iyy - A_abs * Cx**2
    Ixy_centroid = Ixy - A_abs * Cx * Cy
    
    return A_abs, (Cx, Cy), Ixx_centroid, Iyy_centroid, Ixy_centroid

def validate_and_order_vertices(points):
    """
    Ensure valid polygon geometry by:
    1. Creating proper polygon from points
    2. Fixing self-intersections if needed
    3. Removing duplicate points
    
    Args:
        points (np.array): Input vertices
        
    Returns:
        np.array: Ordered, valid vertices
    """
    # Create Shapely polygon from raw points
    poly = Polygon(points)
    
    # Repair if needed (remove repeated points, ensure closure)
    if not poly.is_valid:
        poly = poly.buffer(0)  # Fix self-intersections
        
    # Extract ordered vertices (automatically closed)
    coords = np.array(poly.exterior.coords)
    
    # Remove duplicate closing point if needed
    if np.allclose(coords[0], coords[-1]):
        coords = coords[:-1]
    
    return coords

def calculate_averages(results):
    """
    Compute statistics for cross-section properties.
    
    Args:
        results (list): List of cross-section property dicts
        
    Returns:
        dict: Statistical summary (means, stddevs, min/max)
    """
    if not results:
        return None
    
    areas = [r['area'] for r in results]
    I1s = [r['I1'] for r in results]
    I2s = [r['I2'] for r in results]
    
    return {
        'avg_area': np.mean(areas),
        'avg_I1': np.mean(I1s),
        'avg_I2': np.mean(I2s),
        'std_area': np.std(areas),
        'std_I1': np.std(I1s),
        'std_I2': np.std(I2s),
        'min_area': np.min(areas),
        'max_area': np.max(areas)
    }

def analyze_cross_sections(stl_path, threshold, dz=0.1):
    """
    Analyze STL model by taking cross-sections and computing average properties.
    
    Args:
        stl_path (str): Path to STL file
        threshold (float): Z-level to start analysis
        dz (float): Spacing between cross-sections
        
    Returns:
        tuple: (avg_area, avg_I1, avg_I2) or (None, None, None) if error
    """
    try:
        mesh = trimesh.load(stl_path)
        if not mesh.is_watertight:
            print(f"Warning: {stl_path} is not watertight")
        
        z_min, z_max = threshold, mesh.bounds[1][2]
        z_levels = np.arange(z_min + dz, z_max - dz, dz)
        
        areas = []
        I1_list = []
        I2_list = []
        
        for z in z_levels:
            try:
                section = mesh.section(plane_origin=[0,0,z], plane_normal=[0,0,1])
                if not section: 
                    continue
                    
                section_2d, _ = section.to_planar()
                total_area = 0.0
                total_Ixx = 0.0
                total_Iyy = 0.0
                total_Ixy = 0.0
                
                for p in section_2d.polygons_full:
                    if isinstance(p, Polygon):
                        coords = np.array(p.exterior.coords)
                        if len(coords) > 3:
                            ordered_verts = validate_and_order_vertices(coords)
                            A, (_, _), Ixx, Iyy, Ixy = compute_polygon_properties(ordered_verts)
                            total_area += A
                            total_Ixx += Ixx
                            total_Iyy += Iyy
                            total_Ixy += Ixy
                
                if total_area > 0:
                    # Calculate principal moments for this slice
                    trace = total_Ixx + total_Iyy
                    det = total_Ixx * total_Iyy - total_Ixy**2
                    sqrt_term = np.sqrt(trace**2 - 4*det)
                    
                    I1 = (trace + sqrt_term) / 2
                    I2 = (trace - sqrt_term) / 2
                    
                    areas.append(total_area)
                    I1_list.append(I1)
                    I2_list.append(I2)
                    
            except Exception as e:
                print(f"Skipped z={z:.1f}: {str(e)}")
                continue
        
        if areas:
            return (
                np.mean(areas),  # Average area
                np.mean(I1_list),  # Average I1
                np.mean(I2_list)   # Average I2
            )
        return None, None, None
        
    except Exception as e:
        print(f"Error analyzing {stl_path}: {str(e)}")
        return None, None, None