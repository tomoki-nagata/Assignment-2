import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class ResultVisualizer:
    """
    A class to visualize and save frequency error analysis results.
    
    Attributes:
        base_dir (str): Base directory for saving output files
        file_name_base (str): Base name for output files
        error_folder (str): Folder name for storing error analysis results
    """
    
    def __init__(self, base_dir, mode_info):
        """
        Initialize the ResultVisualizer with directory and mode information.
        
        Args:
            base_dir (str): Base directory path
            mode_info (dict): Dictionary containing numerical and analytical mode numbers
                             Example: {'numerical': 1, 'analytical': 1}
        """
        self.base_dir = base_dir
        # Create standardized filename base using mode information
        self.file_name_base = f"Numerical mode={mode_info['numerical']}_Analytical mode={mode_info['analytical']}"
        self.error_folder = "Error calculation"

    def visualize_results(self, df):
        """
        Main method to generate and save all visualizations.
        
        Args:
            df (pd.DataFrame): DataFrame containing frequency error data
        """
        self._create_output_folder()
        self._generate_plots(df)

    def _create_output_folder(self):
        """Create output folder if it doesn't exist."""
        if not os.path.exists(self.error_folder):
            os.makedirs(self.error_folder)
            print(f"Created output folder: {self.error_folder}")

    def _generate_plots(self, df):
        """
        Generate all visualization plots.
        
        Args:
            df (pd.DataFrame): DataFrame containing the analysis results
        """
        self._plot_boxplot_by_height(df)  # Plot 1: Error by beam height
        self._plot_overall_boxplot(df)    # Plot 2: Overall error distribution

    def _plot_boxplot_by_height(self, df):
        """
        Create boxplot showing frequency error distribution for each beam height.
        
        Args:
            df (pd.DataFrame): DataFrame containing the analysis results
        """
        plt.figure(figsize=(10, 6))
        # Create boxplot with beam heights on x-axis and error percentages on y-axis
        sns.boxplot(x="Beam height", y="Freq_Error", data=df, 
                   order=sorted(df["Beam height"].unique()))
        plt.title("Frequency Error by Beam Height")
        plt.xlabel("Beam Height (m)")  # x-axis label
        plt.ylabel("Frequency Error (%)")  # y-axis label with percentage
        plt.ylim(-30, 1)  # Set consistent y-axis limits for comparison
        plt.xticks(rotation=45, ha='right')  # 45 degree rotation, right-aligned
        plt.tight_layout()
        self._save_plot("_by_beam_height.png")  # Save as PNG
        plt.close()

    def _plot_overall_boxplot(self, df):
        """
        Create boxplot showing overall frequency error distribution.
        
        Args:
            df (pd.DataFrame): DataFrame containing the analysis results
        """
        plt.figure(figsize=(6, 6))
        # Create single boxplot showing all error values
        sns.boxplot(y="Freq_Error", data=df)
        plt.title("Overall Frequency Error Distribution")
        plt.ylabel("Frequency Error (%)")  # y-axis label with percentage
        plt.ylim(-30, 1)  # Same scale as other plot for consistency
        self._save_plot("_overall.png")  # Save as PNG
        plt.close()

    def _save_plot(self, png_suffix):
        """
        Save the current matplotlib figure to a PNG file.
        
        Args:
            png_suffix (str): Suffix to add to the base filename for the PNG
        """
        # Construct full file path
        png_path = os.path.join(self.error_folder, self.file_name_base + png_suffix)
        plt.savefig(png_path, bbox_inches='tight', dpi=300)  # High quality save
        print(f"Saved plot: {png_path}")