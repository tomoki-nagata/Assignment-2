from abaqus import *
from abaqusConstants import *
import job
import numpy as np
import itertools
import shutil
import os
import random

# Define parameter ranges
density_range = np.linspace(2000, 2300, 50)  # 10 values in range
young_modulus_range = np.linspace(1.3e9, 1.98e9, 1e7)  # 10 values in range
threshold_range = np.arange(0.5, 5.75, 0.25)  # 1 step in range
poisson_ratio = 0.2

# Define output directory path (Update this to match your system)
output_dir = r"E:\EESD\Schekenberg castle on cite inspection\2024-10-25 Zurich\Photogrammetry\Try extend the bottom\Variable sensitivty analysis with prism tower Fixed BCs\Boundary condition 4"

# Update with your specific model and part names
model_name = "PrismTower"
part_name = "PART-1"

# Get the model
mdb_model = mdb.models[model_name]
part = mdb_model.parts[part_name]

# Iterate through parameter variations
for i in range(10):  # Repeat 10 times
    density = random.choice(density_range)
    # density = 2150
    young_modulus = random.choice(young_modulus_range)
    # young_modulus = 1.6e9
    threshold = random.choice(threshold_range)
    # threshold = 3.75

    # Step 2: Define Material and Assign to Section
    def define_material_and_section(model, part):
        """
        Define material properties and assign them to the section.
        """
        material_name = "Material_Masonry"
        section_name = "WholeSection"

        # Create a material
        material = model.Material(name=material_name)
        material.Density(table=((density,),))
        material.Elastic(table=((young_modulus, poisson_ratio),))
        
        # Create a solid section
        section = model.HomogeneousSolidSection(name=section_name, material=material_name)
        
        # Create a set for all elements
        if part.elements:
            element_labels = [element.label for element in part.elements]
            part.SetFromElementLabels(name="AllElements", elementLabels=element_labels)
        
            # Assign the section to the entire set
            region = part.sets["AllElements"]
            part.SectionAssignment(region=region, sectionName=section_name)
        
            print("Material '{}' with density={}, E={}, nu={} assigned to section '{}'".format(
                material_name, density, young_modulus, poisson_ratio, section_name))
        else:
            print("No elements found in the part. Ensure meshing is completed before running this script.")

    # Call the function to execute Step 2
    define_material_and_section(mdb_model, part)


    # Step 3: Assemble the Parts
    def create_assembly(model):
        """
        Create an assembly and instance of the part. If an assembly exists, delete it first.
        """
        assembly = model.rootAssembly

        # ** Delete existing features if any exist**
        feature_names = list(assembly.features.keys())
        if feature_names:
            for feature in feature_names:
                del assembly.features[feature]  # Correct way to remove existing features
        
        # ** Delete existing instances if any exist**
        instance_names = list(assembly.instances.keys())
        if instance_names:
            for inst in instance_names:
                del assembly.instances[inst]  # Correct way to remove instances

        # ** Create new assembly and instance**
        assembly.DatumCsysByDefault(CARTESIAN)
        assembly.Instance(name=part_name + "_Instance", part=part, dependent=ON)
        
        print(" Assembly and instance created for part: {}".format(part_name))

    # Call the function to execute Step 3
    create_assembly(mdb_model)



    # Step 4: Create Modal Analysis Step
    def create_modal_analysis_step(model, step_name, previous_step_name, max_frequency=None, num_eigenvalues=None):
        """
        Create a modal analysis step for frequency extraction, allowing the user to specify
        either the maximum frequency or the number of eigenvalues.

        Parameters:
            model: Abaqus model object.
            step_name (str): Name of the modal analysis step.
            previous_step_name (str): Name of the previous step.
            max_frequency (float, optional): Maximum frequency to extract in Hz.
            num_eigenvalues (int, optional): Number of eigenvalues to extract.
        """
        if max_frequency and num_eigenvalues:
            raise ValueError("You can only specify either 'max_frequency' or 'num_eigenvalues', not both.")

        if max_frequency:
            model.FrequencyStep(
                name=step_name,
                previous=previous_step_name,
                maxEigen=max_frequency
            )
            print("Modal analysis step '{}' created with max frequency = {:.2f} Hz.".format(step_name, max_frequency))
        elif num_eigenvalues:
            model.FrequencyStep(
                name=step_name,
                previous=previous_step_name,
                numEigen=num_eigenvalues
            )
            print("Modal analysis step '{}' created with numEigenvalues = {}.".format(step_name, num_eigenvalues))
        else:
            raise ValueError("You must specify either 'max_frequency' or 'num_eigenvalues'.")

    # Call the function to execute Step 4
    step_name = "ModalAnalysis"
    previous_step_name = "Initial"
    num_eigenvalues = 10  # Example: Extract 10 eigenvalues
    create_modal_analysis_step(mdb_model, step_name, previous_step_name, num_eigenvalues=num_eigenvalues)


    # Get the model
    assembly = mdb_model.rootAssembly

    # Step 5: Define Boundary Conditions
    def define_boundary_conditions(model, assembly, instance_name, threshold):
        """
        Identify all nodes with a z-coordinate less than or equal to the threshold 
        and apply a fully fixed boundary condition (u1, u2, u3 = 0).
        """
        fe_instance = assembly.instances[instance_name]
        fe_nodes = fe_instance.nodes

        # Filter nodes that satisfy the z-coordinate condition
        fixed_nodes = [node for node in fe_nodes if node.coordinates[2] <= threshold]
        node_labels = [node.label for node in fixed_nodes]

        # Create an assembly set for these nodes
        assembly.Set(name='FixedNodesAssembly', nodes=fe_instance.nodes.sequenceFromLabels(node_labels))

        # Apply the displacement boundary condition to fix all translations
        model.DisplacementBC(
            name="FixedBC",
            createStepName="Initial",
            region=assembly.sets["FixedNodesAssembly"],
            u1=0.0, u2=0.0, u3=0.0,
            ur1=UNSET, ur2=UNSET, ur3=UNSET
        )
        print("Boundary condition applied: All nodes with z <= {} fixed in X, Y, and Z directions.".format(threshold))


    # Execute Step 5
    define_boundary_conditions(mdb_model, assembly, part_name + "_Instance", threshold)


    # Step 6: Check Mesh Quality
    def check_mesh_quality(part):
        """
        Checks the mesh quality by evaluating element aspect ratio and prints statistics.
        """
        elements = part.elements
        aspect_ratios = []
        
        for element in elements:
            node_coords = [node.coordinates for node in element.getNodes()]
            edge_lengths = [np.linalg.norm(np.array(node_coords[i]) - np.array(node_coords[j])) 
                            for i in range(len(node_coords)) for j in range(i+1, len(node_coords))]
            
            if edge_lengths:
                max_edge = max(edge_lengths)
                min_edge = min(edge_lengths)
                aspect_ratio = max_edge / min_edge if min_edge > 0 else float('inf')
                aspect_ratios.append(aspect_ratio)
        
        if aspect_ratios:
            avg_aspect_ratio = sum(aspect_ratios) / len(aspect_ratios)
            max_aspect_ratio = max(aspect_ratios)
            min_aspect_ratio = min(aspect_ratios)
            
            print("Mesh Quality Check:")
            print("Total Elements: {}".format(len(elements)))
            print("Average Aspect Ratio: {:.2f}".format(avg_aspect_ratio))
            print("Max Aspect Ratio: {:.2f}".format(max_aspect_ratio))
            print("Min Aspect Ratio: {:.2f}".format(min_aspect_ratio))
        else:
            print("No elements found in the mesh.")

    # Execute Step 6: Check Mesh Quality
    check_mesh_quality(part)

    # Step 7: Define Output Requests
    def define_output_requests(model, step_name):
        """
        Define field output requests to store displacement and eigenvalues.
        """
        if step_name in model.steps:
            step = model.steps[step_name]
            
            # Delete existing field output requests
            if 'F-Output-1' in model.fieldOutputRequests.keys():
                del model.fieldOutputRequests['F-Output-1']
            
            # Create new field output request for Displacement (U) and Eigenvalues (EVOL)
            model.FieldOutputRequest(
                name='F-Output-1',
                createStepName=step_name,
                variables=('U', 'EVOL'),
                # numIntervals=10
            )
            print("Output requests for displacement (U) and eigenvalues (EVOL) created in step '{}'".format(step_name))
        else:
            print("Step '{}' not found in model.".format(step_name))

    # Execute Step 7: Define Output Requests
    step_name = "ModalAnalysis"
    define_output_requests(mdb_model, step_name)


    # Change the working directory to the output folder
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the folder if it doesn't exist

    os.chdir(output_dir)  # Change the working directory

    # Step 8: Submit the Job for Modal Analysis
    def submit_modal_analysis_job(model, job_name):
        """
        Create and submit a job for modal analysis.
        """
        # Delete existing job with the same name if it exists
        if job_name in mdb.jobs.keys():
            del mdb.jobs[job_name]
        
        # Create the job
        job = mdb.Job(name="Modal_Analysis_Job", model=model.name, description="Modal Analysis Job",
                type=ANALYSIS)
        
        # Submit the job
        job.submit()
        job.waitForCompletion()
        print("Job '{}' submitted and completed successfully.".format(job_name))

    # Execute Step 8: Submit the Job
    job_name = "Modal_Analysis_Job"
    submit_modal_analysis_job(mdb_model, job_name)


    from odbAccess import *
    import numpy as np

    # Open the Abaqus ODB file
    odb_path = "Modal_Analysis_Job.odb"  # Update with actual path
    odb = openOdb(path=odb_path)

    step = odb.steps[step_name]

    # Define the 4 nodes of interest (Replace with actual node labels)
    selected_nodes = [371, 858, 820, 2388, 1357, 617, 503]  # Example nodes

    # Store mode shapes, eigenvalues, and frequencies for modes 1 to 8
    mode_shapes = {}
    eigenvalues = {}
    frequencies = {}

    for mode in range(1, 9):  # Extract from mode 1 to 8
        frame = step.frames[mode]  # Get the corresponding mode shape frame
        displacement = frame.fieldOutputs['U']  # Displacement field
        frequency = frame.frequency  # Compute frequency in Hz
        eigenvalue = (2 * np.pi * frequency) ** 2  # Convert back to eigenvalue  # Extract eigenvalue
        

        node_data = []
        for value in displacement.values:
            if value.nodeLabel in selected_nodes:
                node_data.append(np.array(value.data))  # Extract (U1, U2, U3)

        # Convert to NumPy array
        node_data = np.array(node_data)

        # Normalize mode shape (Divide by max absolute displacement)
        max_disp = np.max(np.abs(node_data))
        if max_disp > 0:
            node_data /= max_disp  # Normalize

        mode_shapes[mode] = node_data  # Store in dictionary
        eigenvalues[mode] = eigenvalue
        frequencies[mode] = frequency

    # Save mode shape vectors, eigenvalues, and frequencies to a text file
    output_file = "mode_shapes_4_nodes.txt"
    with open(output_file, "w") as f:
        f.write("Mode Shape Vectors (Normalized) for 10 Nodes\n")
        f.write("Density: {:.2f} kg/m3, Young's Modulus: {:.2e} Pa, Poisson Ratio: {:.2f}, Threshold: {:.2f}\n\n".format(density, young_modulus, poisson_ratio, threshold))
        f.write("==========================================\n\n")
        for mode, vectors in mode_shapes.items():
            f.write("Mode {}:\n".format(mode))
            f.write("Eigenvalue: {:.6f}\n".format(eigenvalues[mode]))
            f.write("Frequency (Hz): {:.6f}\n".format(frequencies[mode]))
            for i, node in enumerate(selected_nodes):
                f.write("Node {}: {}\n".format(node, vectors[i]))
            f.write("\n")

    print("Mode shapes, eigenvalues, and frequencies saved to '{}' successfully!".format(output_file))

    # Define the fixed centroid coordinates in the X and Y directions
    X_fixed = 2.0363
    Y_fixed = 2.0718

    # Define centroid Z-coordinates using:
    # Z = threshold + ((15.5 - threshold)/10) * (i-1) for i = 1, 2, ..., 11
    centroid_coords = []
    for i in range(1, 12):  # This yields 11 points from bottom (Z=threshold) to top (Z=15.5)
        Z_i = threshold + ((15.5 - threshold) / 10.0) * (i - 1)
        centroid_coords.append((X_fixed, Y_fixed, Z_i))

    # Get the instance from the ODB
    instance_name = part_name + "_INSTANCE"
    instance = odb.rootAssembly.instances[instance_name]

    # Retrieve all nodes of the instance (their coordinates remain constant)
    all_nodes = instance.nodes

    # For each centroid coordinate, find the nearest node from the instance (compute once)
    # Instead of just storing node labels, we store a tuple: (node_label, node_coordinates)
    nearest_nodes = []
    for coord in centroid_coords:
        nearest_node = min(all_nodes, key=lambda n: np.linalg.norm(np.array(n.coordinates) - np.array(coord)))
        nearest_nodes.append((nearest_node.label, nearest_node.coordinates))

    # Now, for each mode from 1 to 8, extract the displacement at these nearest nodes
    # and write the data into "Displacement vector of centoroid.txt".
    centroid_output_file = "Disp_vector_cen.txt"
    with open(centroid_output_file, "w") as f:
        f.write("Displacement Vectors (U1, U2, U3) at Nearest Nodes to Defined Centroid Coordinates\n")
        f.write("Fixed X = {:.4f}, Fixed Y = {:.4f}\n".format(X_fixed, Y_fixed))
        f.write("Threshold = {:.2f}, Top = 15.5\n\n".format(threshold))
        f.write("Defined Centroid Coordinates (for i=1 to 11):\n")
        for i, coord in enumerate(centroid_coords, start=1):
            f.write("  Point {}: (X, Y, Z) = ({:.4f}, {:.4f}, {:.4f})\n".format(i, coord[0], coord[1], coord[2]))
        f.write("\n---------------------------------------------------\n\n")
        
        # Loop over modes 1 to 8
        for mode in range(1, 9):
            f.write("Mode {}:\n".format(mode))
            # Get the corresponding frame for this mode
            frame = step.frames[mode]
            displacement_field = frame.fieldOutputs['U']
            # Build a dictionary for displacement: key = node label, value = displacement vector (U1, U2, U3)
            disp_dict = {val.nodeLabel: np.array(val.data) for val in displacement_field.values}
            
            # For each centroid, retrieve the displacement of the nearest node
            for i, (node_label, node_coord) in enumerate(nearest_nodes, start=1):
                if node_label in disp_dict:
                    disp_val = disp_dict[node_label]
                else:
                    disp_val = (None, None, None)
                f.write("  Centroid Point {}:\n".format(i))
                f.write("    Defined Coordinate: (X, Y, Z) = ({:.4f}, {:.4f}, {:.4f})\n".format(
                    centroid_coords[i-1][0], centroid_coords[i-1][1], centroid_coords[i-1][2]))
                f.write("    Nearest Node Label: {}\n".format(node_label))
                f.write("    Nearest Node Coordinate: ({:.4f}, {:.4f}, {:.4f})\n".format(
                    node_coord[0], node_coord[1], node_coord[2]))
                f.write("    Displacement (U1, U2, U3): {}\n".format(disp_val))
            f.write("\n---------------------------------------------------\n\n")
            
    print("Centroid displacement data for modes 1 to 8 saved to '{}' successfully!".format(centroid_output_file))


    # Find the top 20 nodes closest to the threshold in the z-direction from the instance in the ODB

    # Create a list of tuples containing the absolute difference and the node
    nodes_diff = [(abs(node.coordinates[2] - threshold), node) for node in instance.nodes]

    # Sort the list by the difference (smallest difference first)
    nodes_diff.sort(key=lambda x: x[0])

    # Select the top 20 nodes
    top_nodes = nodes_diff[:20]

    # Extract the displacement for each of these nodes from mode 1 (change mode_index if needed)
    mode_index = 1  # mode 1 is at index 1 in step.frames
    disp_field = step.frames[mode_index].fieldOutputs['U']

    # Prepare a list to hold results: each element is (node label, coordinates, displacement)
    results = []
    for diff, node in top_nodes:
        node_disp = None
        for value in disp_field.values:
            if value.nodeLabel == node.label:
                node_disp = value.data
                break
        if node_disp is None:
            node_disp = "Displacement not found"
        results.append((node.label, node.coordinates, node_disp))

    # Write the results to a new text file
    output_file2 = "Z_min_position_disp.txt"
    with open(output_file2, "w") as f:
        f.write("Top 20 nodes closest to z = {:.2f}\n".format(threshold))
        f.write("==========================================\n\n")
        for node_label, coordinates, displacement in results:
            f.write("Node Label: {}\n".format(node_label))
            f.write("Coordinates: {}\n".format(coordinates))
            f.write("Displacement from mode 1 (U1, U2, U3): {}\n".format(displacement))
            f.write("------------------------------------------\n")
            
    print("Top 20 nodes closest to threshold saved to '{}' successfully!".format(output_file2))


    # Define new folder for storing completed results (after job execution)
    folder_name = "den = {}, E = {}, Possion = {}, thre = {}".format(density, young_modulus, poisson_ratio, threshold)
    output_path = os.path.join(output_dir, folder_name)

    # Ensure the final storage folder exists (will be used AFTER analysis)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Close the ODB file before moving output files
    odb_name = job_name + ".odb"
    if odb_name in session.odbs:
        odb = session.odbs[odb_name]
        odb.close()
    else:
        print("ODB '{}' not found in session. Skipping close.".format(odb_name))

    # odb.close()

    # Move output files to the new directory
    output_files = ["{}.env", "{}.com", "{}.inp", "{}.sim", "{}.ipm", "{}.lck","{}.dat", "{}.msg","{}.prt","{}.sta","{}.odb", # "{}.log",
                    "mode_shapes_4_nodes.txt",  "Z_min_position_disp.txt" ,"Disp_vector_cen.txt",  "ABQcaeK.00.5840.exception", "ABQcaeK.00.35956.exception"]

    import time

    def is_file_closed(file_path):
        """Check if a file is free to move (not locked by another process)."""
        try:
            with open(file_path, 'r+'):
                return True  # File is free to move
        except IOError:
            return False  # File is still in use

    import time

    def is_file_closed(file_path):
        """Check if a file is free to move (not locked by another process)."""
        try:
            with open(file_path, 'r+'):
                return True  # File is free to move
        except IOError:
            return False  # File is still in use

    # Define retry mechanism for locked files
    for file in output_files:
        file_path = file.format(job_name)

        if os.path.exists(file_path):
            retries = 5  # Number of attempts to wait for the file to be released
            while retries > 0 and not is_file_closed(file_path):
                print("File '{}' is still in use... waiting.".format(file_path))
                time.sleep(3)  # Wait for 3 seconds before retrying
                retries -= 1
            
            # Try moving only if the file is no longer in use
            if is_file_closed(file_path):
                shutil.move(file_path, os.path.join(output_path, file_path))
                print("Moved file: '{}'".format(file_path))
            else:
                print("Skipping locked file: '{}' (still in use after retries).".format(file_path))
        else:
            print("Skipping missing file: '{}'".format(file_path))


    print("All available output files moved to:", output_path)
