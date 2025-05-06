# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by nagata on Tue May  6 19:21:59 2025
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
#: Model: C:/Users/nagata/OneDrive - epfl.ch/Documents/Course work at EPFL/Research skills in the Open Science Era/Assignment 2/Numerical results/den = 2150, E = 1600000000.0, Possion = 0.2, thre = 2.0/Modal_Analysis_Job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.8512, 
    farPlane=47.2041, width=15.881, height=8.55553, cameraPosition=(12.1635, 
    -7.37894, 42.2118), cameraUpVector=(-0.808986, 0.587332, 0.024151), 
    cameraTarget=(2.52231, 1.3581, 8.28586))
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.2586, 
    farPlane=47.7967, width=24.1456, height=13.0079, viewOffsetX=-0.0811964, 
    viewOffsetY=-1.01513)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.7946, 
    farPlane=46.4486, width=28.3166, height=15.2549, cameraPosition=(32.6358, 
    -19.088, 18.3631), cameraUpVector=(-0.491881, 0.293926, 0.819549), 
    cameraTarget=(3.63818, 0.555724, 8.69261), viewOffsetX=-0.0952224, 
    viewOffsetY=-1.19048)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.0942, 
    farPlane=46.149, width=19.7248, height=10.6263, viewOffsetX=-0.569419, 
    viewOffsetY=0.117143)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.3679, 
    farPlane=49.0395, width=17.9954, height=9.69457, cameraPosition=(15.4662, 
    -1.33954, 44.081), cameraUpVector=(-0.879825, 0.475011, 0.0164886), 
    cameraTarget=(2.64523, 1.58676, 10.209), viewOffsetX=-0.519492, 
    viewOffsetY=0.106872)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
