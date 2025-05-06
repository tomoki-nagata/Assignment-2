# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by nagata on Wed Apr  2 16:50:46 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=168.080200195312, 
    height=234.630004882812)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='Modal_Analysis_Job.odb')
#: Model: E:/EESD/Schekenberg castle on cite inspection/2024-10-25 Zurich/Photogrammetry/Try extend the bottom/Variable sensitivty analysis with prism tower Fixed BCs/Boundary condition 1/den = 2150, E = 1600000000.0, Possion = 0.2, thre = 4.0/Modal_Analysis_Job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.7806, 
    farPlane=44.4701, width=17.6136, height=9.4889, cameraPosition=(-11.9037, 
    -28.0503, 24.8117), cameraUpVector=(-0.130897, 0.805847, 0.577475))
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.3271, 
    farPlane=45.2901, width=17.3454, height=9.34441, cameraPosition=(17.6755, 
    -25.8823, 27.9298), cameraUpVector=(-0.463491, 0.639474, 0.613392), 
    cameraTarget=(3.03426, 1.09627, 8.4864))
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.3339, 
    farPlane=44.2282, width=17.9409, height=9.66521, cameraPosition=(22.6919, 
    -26.6939, 21.268), cameraUpVector=(-0.451547, 0.471919, 0.757231), 
    cameraTarget=(3.16513, 1.0751, 8.31261))
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.7166, 
    farPlane=44.9404, width=17.5758, height=9.46851, cameraPosition=(25.5376, 
    -22.8473, 24.0679), cameraUpVector=(-0.496186, 0.504813, 0.706373), 
    cameraTarget=(3.23732, 1.17268, 8.38364))
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.1491, 
    farPlane=45.5079, width=25.5206, height=13.7486, viewOffsetX=0.288692, 
    viewOffsetY=0.284269)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.4778, 
    farPlane=45.0697, width=25.8083, height=13.9036, cameraPosition=(26.2051, 
    -23.8961, 21.1156), cameraUpVector=(-0.461531, 0.451229, 0.763794), 
    cameraTarget=(3.23925, 1.16929, 8.28764), viewOffsetX=0.291947, 
    viewOffsetY=0.287474)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.3083, 
    farPlane=45.3021, width=25.6599, height=13.8236, cameraPosition=(26.7412, 
    -22.9473, 21.9903), cameraUpVector=(-0.477847, 0.460815, 0.747871), 
    cameraTarget=(3.2633, 1.17972, 8.31794), viewOffsetX=0.290268, 
    viewOffsetY=0.285821)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.8751, 
    farPlane=45.3523, width=24.4051, height=13.1477, cameraPosition=(25.8811, 
    -23.1613, 23.0319), cameraUpVector=(-0.471444, 0.498614, 0.727409), 
    cameraTarget=(3.25016, 1.17198, 8.33542), viewOffsetX=0.276074, 
    viewOffsetY=0.271844)
#: 
#: Node: PART-1_INSTANCE.702
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.04557e+00,  1.81000e+00,  5.02690e+00,      -      
#: Scale:                             4.05849e+02,  4.05849e+02,  4.05849e+02,      -      
#: Deformed coordinates (unscaled):   2.04563e+00,  1.80983e+00,  5.02685e+00,      -      
#: Deformed coordinates (scaled):     2.06950e+00,  1.73936e+00,  5.00617e+00,      -      
#: Displacement (unscaled):           5.89664e-05, -1.74056e-04, -5.10654e-05,  1.90736e-04
