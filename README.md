# Frequency Error Analysis: Numerical vs Analytical Models

This repository provides tools to quantify and visualize the frequency discrepancies between numerical simulations and simplified analytical models based on Euler–Bernoulli beam theory. It is designed to help engineers validate the accuracy of analytical approximations against high-fidelity finite element results for structural vibration analysis.

## Contents
- [Background](#background)
- [Beam Height Definition](#beam-height-definition)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [References](#references)

---

## Background

### Vibration Modes & Modal Analysis

Structures exhibit characteristic vibration modes—each defined by a natural frequency and a mode shape. These properties can be extracted via:

- **Numerical Analysis**: Finite Element Method (FEM) simulations provide high-fidelity results but can be time-consuming.
- **Analytical Solution**: The Euler–Bernoulli beam model offers closed-form expressions for cantilever beams, enabling rapid estimates of natural frequencies and modal shape.

#### Euler–Bernoulli Beam Equation

The governing equation for transverse vibrations of an Euler–Bernoulli beam is:

```math
EI\,\frac{\partial^4 w}{\partial z^4} + \rho A\,\frac{\partial^2 w}{\partial t^2} = 0
```

where:
- $E$ is Young’s modulus  
- $I$ is the second moment of area (moment of inertia)  
- $\rho$ is the material density  
- $A$ is the cross-sectional area  
- $w(z,t)$ is the transverse displacement as a function of axial coordinate $z$ and time $t$

Cantilever boundary conditions (fixed at $z=0$, free at $z=L$) lead to characteristic frequency equations for each mode.

## Beam Height Definition

In the numerical model, a portion of the structure is embedded underground and the external nodes are fixed at that interface. To map this to the analytical cantilever model, define the effective beam length as:

```
beam height = L_total - h_fixed
```

- **L_total**: Full height of the numerical model.  
- **h_fixed**: Depth (height) of the buried section whose exteriornodes are constrained in perpendicular direction.

Use "beam height" in the analytical formulas to compute natural frequencies.

## Features

- **Cross-Section Property Calculation**: Compute area and moment of inertia from the target structure with STL format.
- **Numerical Data Extraction**: Read modal frequencies from finite element simulation outputs.  
- **Analytical Frequency Calculation**: Evaluate Euler–Bernoulli solutions for cantilever beams.  
- **Error Visualization**: Generate boxplots and scatter plots to compare numerical vs analytical frequencies.  
- **Statistical Analysis**: Summarize frequency discrepancies with boxplot and whisker plot.


## Setup Instructions

- **Python 3.9 or higher**  
- **Package manager**: pip (version 21.0+)  
- **Virtual Environment** (Recommended for dependency isolation)  

1. **Clone the repository**:

2. **Create and activate a virtual environment**:

   ```bash
   # For Windows:
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Verify installation**:

   ```bash
   python -c "import trimesh, numpy; print(f'Trimesh {trimesh.__version__}, NumPy {numpy.__version__}')"
   ```


## Usage

1. Copy all python source code in "src" and paste inside folder "Numerical_results"
 
2. Configure parameters in `main.py`:
   ```python
   base_dir  = "path/to/Numerical_results"   # Root folder with subfolders for each test case
   mode_info = { 'numerical': 1, 'analytical': 1 }  # Mode number mapping
   ```
3. Change your directory ("path/to/Numerical_results") and Run the analysis:
   ```bash
   python main.py
   ```
4. Review outputs:
   - boxplot and whisker plot in `Numerical_results/Error calculation/`  

## Repository Structure

```
├── Numerical_results/      
│   ├── den=2150_E=1.6e9_ν=0.2_thre=0.0/
│   ├── den=2150_E=1.6e9_ν=0.2_thre=0.5/
 .   .
 .   .
│   └── PrismTower.stl           # Simple prismatic STL model
│   └── (Execute Modal_Post Process.py)           # Python script for conducting modal analysis in abaqus (Not required in this program)
│   └── (PrismTower.cae and PrismTower.jnl)       # abaqus CAE for numerical simulation (Not required in this program)
│
├── src/                          # source code
│   ├── ComputeAreaInertia.py    # Cross-section properties
│   ├── ExtractNumerical.py      # Numerical data extraction
│   ├── ComputeAnalytical.py     # Analytical solutions
│   ├── FEvisualize.py           # Error visualization
│   └── main.py                  # Main workflow
│   
├── requirements.txt             # Python dependencies
└── 2022 - Martakis.pdf          # Reference methodology


```

# Advanced Usage
Within the Numerical_results/ folder, you can explore the full Abaqus simulation setup:

1. Install Abaqus (https://www.epfl.ch/schools/sti/it/abaqus/)

2. Open "PrismTower.cae" by double-clicking to inspect the geometry and mesh.

3. Run the Python script "Execute Modal_Post Process.py" to automatically perform the modal analysis; results will be saved in the same directory.

To review the natural frequencies and mode shapes from your numerical simulation, open the "Modal_Analysis_Job.odb" file in the corresponding output folder (e.g., den=2150_E=1.6e9_ν=0.2_thre=0.0). You will need Abaqus installed to view this file.

To inspect the exterior surface geometry, install MeshLab (https://www.meshlab.net/#download) and open "PrismTower.stl".

# References
Methodology based on:
Martakis P. et al. (2022) "Reducing uncertainty in seismic assessment of multiple masonry buildings based on monitored demolitions"
Visualization Methodology: Section 3.1.2 (Fig.8 (a))

## Author 
Tomoki Nagata (tomoki.nagata@epfl.ch) 