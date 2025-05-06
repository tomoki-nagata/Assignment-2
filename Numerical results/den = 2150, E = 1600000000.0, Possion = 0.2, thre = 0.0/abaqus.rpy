# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by nagata on Wed Mar 19 10:18:51 2025
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
#: Model: E:/EESD/Schekenberg castle on cite inspection/2024-10-25 Zurich/Photogrammetry/Try extend the bottom/Variable sensitivty analysis with prism tower Fixed BCs/den = 2150, E = 1600000000.0, Possion = 0.2, thre = 0.0/Modal_Analysis_Job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.7536, 
    farPlane=46.7806, width=15.8233, height=8.52444, cameraPosition=(16.3024, 
    3.40428, 41.9594), cameraUpVector=(-0.683334, 0.718401, -0.130209), 
    cameraTarget=(2.36252, 0.938897, 8.49508))
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.9561, 
    farPlane=46.6419, width=15.9431, height=8.58896, cameraPosition=(14.4416, 
    1.60192, 42.7588), cameraUpVector=(-0.472889, 0.857264, -0.203651), 
    cameraTarget=(2.34067, 0.917733, 8.50447))
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.8991, 
    farPlane=46.7293, width=15.9094, height=8.5708, cameraPosition=(10.9691, 
    -16.3737, 39.3458), cameraUpVector=(-0.386404, 0.897568, 0.21228), 
    cameraTarget=(2.29692, 0.691262, 8.46147))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.0048, 
    farPlane=45.8521, width=16.5634, height=8.92312, cameraPosition=(1.95238, 
    -23.4777, 35.6258), cameraUpVector=(-0.147009, 0.918718, 0.366532), 
    cameraTarget=(2.17965, 0.598869, 8.41309))
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.9564, 
    farPlane=46.9092, width=15.9433, height=8.58908, cameraPosition=(6.00432, 
    -9.65148, 43.1234), cameraUpVector=(-0.194009, 0.980471, -0.0322229), 
    cameraTarget=(2.24472, 0.820894, 8.53349))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.1872, 
    farPlane=46.7279, width=16.0798, height=8.66262, cameraPosition=(3.82222, 
    -12.0076, 42.4949), cameraUpVector=(-0.147172, 0.988849, 0.022764), 
    cameraTarget=(2.20943, 0.782787, 8.52333))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.579, 
    farPlane=46.2785, width=16.3116, height=8.78747, cameraPosition=(3.20815, 
    -20.0788, 38.28), cameraUpVector=(-0.0764169, 0.961348, 0.26452), 
    cameraTarget=(2.19909, 0.646919, 8.45238))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6407, 
    farPlane=46.2168, width=16.3481, height=8.80715, viewOffsetX=0.0712207, 
    viewOffsetY=0.0256593)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.4284, 
    farPlane=46.368, width=16.2225, height=8.73949, cameraPosition=(5.29464, 
    -20.4358, 37.8906), cameraUpVector=(-0.110063, 0.953022, 0.282198), 
    cameraTarget=(2.23356, 0.637336, 8.44893), viewOffsetX=0.0706736, 
    viewOffsetY=0.0254622)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5112, 
    farPlane=46.2851, width=16.3381, height=8.80175, viewOffsetX=0.0719115, 
    viewOffsetY=0.0292037)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.0169, 
    farPlane=46.8825, width=16.0445, height=8.6436, cameraPosition=(5.68123, 
    -10.8024, 42.8057), cameraUpVector=(-0.122793, 0.992416, -0.00571075), 
    cameraTarget=(2.24001, 0.778862, 8.53773), viewOffsetX=0.0706194, 
    viewOffsetY=0.028679)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.1594, 
    farPlane=46.7919, width=16.1292, height=8.6892, cameraPosition=(4.05342, 
    -10.0542, 43.1709), cameraUpVector=(-0.101674, 0.994273, -0.0329045), 
    cameraTarget=(2.21232, 0.792969, 8.54127), viewOffsetX=0.0709919, 
    viewOffsetY=0.0288303)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5662, 
    farPlane=46.3515, width=16.3708, height=8.81935, cameraPosition=(1.56907, 
    -19.2646, 38.8407), cameraUpVector=(-0.0902424, 0.968101, 0.233746), 
    cameraTarget=(2.16975, 0.640337, 8.44836), viewOffsetX=0.0720552, 
    viewOffsetY=0.0292621)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.411, 
    farPlane=45.5733, width=16.8725, height=9.08964, cameraPosition=(-5.20069, 
    -27.6775, 30.0109), cameraUpVector=(-0.00384972, 0.843878, 0.536522), 
    cameraTarget=(2.0562, 0.524395, 8.27959), viewOffsetX=0.0742635, 
    viewOffsetY=0.0301589)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.0941, 
    farPlane=46.8216, width=16.0905, height=8.66833, cameraPosition=(4.44181, 
    -13.4296, 41.9079), cameraUpVector=(-0.143152, 0.987505, 0.0658906), 
    cameraTarget=(2.22835, 0.742, 8.52341), viewOffsetX=0.0708213, 
    viewOffsetY=0.028761)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.7971, 
    farPlane=43.9517, width=17.6957, height=9.53316, cameraPosition=(0.351168, 
    -32.396, 23.6055), cameraUpVector=(-0.118997, 0.704013, 0.700147), 
    cameraTarget=(2.16009, 0.453213, 8.18111), viewOffsetX=0.0778867, 
    viewOffsetY=0.0316303)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.1537, 
    farPlane=41.3314, width=19.0952, height=10.2871, cameraPosition=(4.60739, 
    -35.7792, 5.855), cameraUpVector=(-0.178255, 0.268953, 0.946514), 
    cameraTarget=(2.22358, 0.419147, 7.91634), viewOffsetX=0.0840465, 
    viewOffsetY=0.0341319)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.0456, 
    farPlane=43.4395, width=41.8433, height=22.5421, viewOffsetX=1.54578, 
    viewOffsetY=2.94375)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.6784, 
    farPlane=49.3555, width=39.9393, height=21.5163, cameraPosition=(9.56653, 
    -32.4144, 27.082), cameraUpVector=(-0.293097, 0.712648, 0.637359), 
    cameraTarget=(2.61576, -1.84648, 8.70968), viewOffsetX=1.47544, 
    viewOffsetY=2.8098)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.559, 
    farPlane=51.6019, width=39.773, height=21.4267, cameraPosition=(8.91884, 
    -25.8064, 37.165), cameraUpVector=(-0.283864, 0.878351, 0.384605), 
    cameraTarget=(2.54879, -2.2773, 10.2196), viewOffsetX=1.4693, 
    viewOffsetY=2.7981)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.4498, 
    farPlane=53.8125, width=41.0136, height=22.0951, cameraPosition=(7.53742, 
    -10.5968, 47.6313), cameraUpVector=(-0.285192, 0.956595, -0.0599277), 
    cameraTarget=(2.46544, -1.63059, 12.7869), viewOffsetX=1.51513, 
    viewOffsetY=2.88538)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.1095, 
    farPlane=54.3192, width=41.9323, height=22.59, cameraPosition=(7.37934, 
    -3.42766, 49.6373), cameraUpVector=(-0.292797, 0.928121, -0.229916), 
    cameraTarget=(2.48379, -0.817911, 13.7281), viewOffsetX=1.54907, 
    viewOffsetY=2.95001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.8346, 
    farPlane=52.594, width=21.0998, height=11.367, viewOffsetX=0.854194, 
    viewOffsetY=1.71807)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
