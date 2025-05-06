# main_Frequency_Error.py
import os
import pandas as pd
from ExtractNumerical import NumericalDataExtractor
from ComputeAnalytical import AnalyticalFrequencyCalculator
from FEvisualize import ResultVisualizer

def main():
    """
    Main workflow for frequency error analysis:
    1. Extract numerical simulation results
    2. Compute analytical solutions
    3. Calculate errors
    4. Visualize results
    """
    ###  Configuration - USER SHOULD UPDATE THESE PATHS/VALUES  ############################################################################# 
    base_dir = r"C:\Users\nagata\OneDrive - epfl.ch\Documents\Course work at EPFL\Research skills in the Open Science Era\Assignment 2"
    stl_path = os.path.join(base_dir, "PrismTower.stl")
    mode_info = {
        'numerical': 1,    # Numerical mode number from simulation
        'analytical': 1    # Analytical mode number for comparison
    }
    #########################################################################################################################################

    # Data processing pipeline
    extractor = NumericalDataExtractor(base_dir, stl_path, mode_info['numerical'])
    df = extractor.process_folders()  # Get numerical results
    
    calculator = AnalyticalFrequencyCalculator(mode_info['analytical'])
    df = calculator.calculate(df)  # Add analytical frequencies
    
    # Compute percentage errors: (Numerical - Analytical)/Numerical * 100
    df["Freq_Error"] = 100*(df["Frequency"] - df["Analytical_Frequency"])/df["Frequency"]
    
    # Generate visualization plots
    visualizer = ResultVisualizer(base_dir, mode_info)
    visualizer.visualize_results(df)

if __name__ == "__main__":
    main()  # Execute the workflow