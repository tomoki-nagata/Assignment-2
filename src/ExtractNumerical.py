# ExtractNumerical.py
import os
import re
import pandas as pd
from ComputeAreaInertia import analyze_cross_sections

class NumericalDataExtractor:
    """
    Extracts numerical simulation results from output files.
    Processes multiple folders containing simulation data.
    """

    def __init__(self, base_dir, stl_path, numerical_mode):
        """
        Initialize extractor with paths and mode number.
        
        Args:
            base_dir (str): Root directory containing simulation folders
            stl_path (str): Path to STL geometry file
            numerical_mode (int): Vibration mode number to extract
        """
        self.base_dir = base_dir
        self.stl_path = stl_path
        self.numerical_mode = numerical_mode
        self.material_pattern = re.compile(r"Density:\s*([\d\.]+)\s*kg/m3, Young's Modulus:\s*([\d\.e\+]+)\s*Pa, Poisson Ratio:\s*([\d\.]+), Threshold:\s*([\d\.]+)")
        self.mode_pattern = re.compile(rf"Mode {numerical_mode}:")
        self.eigenvalue_pattern = re.compile(r"Eigenvalue:\s*([\d\.]+)")
        self.frequency_pattern = re.compile(r"Frequency \(Hz\):\s*([\d\.]+)")

    def process_folders(self):
        """
        Process all simulation folders in base directory.
        
        Returns:
            pd.DataFrame: Extracted data with columns:
                [Beam height, Density, Young_Modulus, Frequency, Threshold, Ar, Ir]
        """
        data = []
        for folder in os.listdir(self.base_dir):
            folder_path = os.path.join(self.base_dir, folder)
            if not os.path.isdir(folder_path):
                continue

            result = self._process_folder(folder_path)
            if result:
                data.append(result)
        
        return pd.DataFrame(data, columns=["Beam height", "Density", "Young_Modulus", 
                                         "Frequency", "Threshold", "Ar", "Ir"])

    def _process_folder(self, folder_path):
        """
        Process individual simulation folder.
        
        Args:
            folder_path (str): Path to simulation folder
            
        Returns:
            list: Extracted data row or None if processing fails
        """
        file_path = os.path.join(folder_path, "mode_shapes_4_nodes.txt")
        if not os.path.isfile(file_path):
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        material_match = self.material_pattern.search(lines[1])
        if not material_match:
            return None

        density = float(material_match.group(1))
        young_modulus = float(material_match.group(2))
        threshold = float(material_match.group(4))

        mode_index = None
        for i, line in enumerate(lines):
            if self.mode_pattern.search(line):
                mode_index = i
                break

        if mode_index is None:
            return None

        eigenvalue_match = self.eigenvalue_pattern.search(lines[mode_index + 1])
        frequency_match = self.frequency_pattern.search(lines[mode_index + 2])
        if not eigenvalue_match or not frequency_match:
            return None

        frequency = float(frequency_match.group(1))
        Ar, _, Ir = analyze_cross_sections(self.stl_path, threshold)

        return [15.5 - threshold, density, young_modulus, frequency, threshold, Ar, Ir]