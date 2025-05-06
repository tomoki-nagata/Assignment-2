# ComputeAnalytical.py
import numpy as np

class AnalyticalFrequencyCalculator:
    """
    Calculates analytical frequencies for cantilever beam vibration modes.
    Uses Euler-Bernoulli beam theory to compute natural frequencies.
    """
    
    def __init__(self, analytical_mode):
        """
        Initialize calculator with specific vibration mode.
        
        Args:
            analytical_mode (int): Vibration mode number (1, 2, 3, or 4)
        """
        self.analytical_mode = analytical_mode
        # Predefined dimensionless eigenvalues for cantilever beam modes
        self.eigenvalues = {1: 1.87510407, 2: 4.69409113, 
                          3: 7.85475744, 4: 10.9955407}

    def calculate(self, df):
        """
        Compute analytical frequencies for all cases in DataFrame.
        
        Args:
            df (pd.DataFrame): Input data with beam properties
            
        Returns:
            pd.DataFrame: Input DataFrame with added 'Analytical_Frequency' column
        """
        df["Analytical_Frequency"] = df.apply(
            lambda row: self._analytical_formula(
                row["Beam height"],
                row["Young_Modulus"],
                row["Density"],
                row["Ar"],
                row["Ir"]
            ), axis=1
        )
        return df

    def _analytical_formula(self, L, E, rho, A, I):
        """
        Core formula for natural frequency calculation.
        
        Args:
            L (float): Beam length/height [m]
            E (float): Young's modulus [Pa]
            rho (float): Material density [kg/m³]
            A (float): Cross-sectional area [m²]
            I (float): Moment of inertia [m⁴]
            
        Returns:
            float: Natural frequency in Hz
            
        Formula:
            f = (β²/2π) * √((E/ρ * I)/A)
            where β = eigenvalue/L
        """
        if self.analytical_mode not in self.eigenvalues:
            raise ValueError("Invalid analytical mode")
        
        beta = self.eigenvalues[self.analytical_mode] / L
        y = E / rho  # Ratio of Young's modulus to density
        return (beta**2 / (2 * np.pi)) * np.sqrt((y * I) / A)