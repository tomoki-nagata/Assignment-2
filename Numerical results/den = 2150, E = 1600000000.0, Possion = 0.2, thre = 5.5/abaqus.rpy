# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by nagata on Fri Apr  4 10:18:43 2025
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
#: Model: E:/EESD/Schekenberg castle on cite inspection/2024-10-25 Zurich/Photogrammetry/Try extend the bottom/Variable sensitivty analysis with prism tower Fixed BCs/Boundary condition 1/den = 2150, E = 1600000000.0, Possion = 0.2, thre = 5.5/Modal_Analysis_Job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='EVOL', outputPosition=WHOLE_ELEMENT, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.8886, 
    farPlane=44.9857, width=15.9032, height=8.56746, cameraPosition=(23.383, 
    22.0284, 29.3983), cameraUpVector=(-0.88968, 0.438737, -0.126407), 
    cameraTarget=(2.40481, 1.05014, 8.42005))
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.2155, 
    farPlane=42.5114, width=17.8709, height=9.62752, cameraPosition=(37.5096, 
    4.06327, 16.8642), cameraUpVector=(-0.543692, 0.0336502, 0.83861), 
    cameraTarget=(2.24827, 1.24921, 8.55894))
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.2316, 
    farPlane=41.3365, width=18.4718, height=9.95126, cameraPosition=(38.4557, 
    3.17384, 10.9255), cameraUpVector=(-0.394063, -0.0119878, 0.919005), 
    cameraTarget=(2.249, 1.24852, 8.55435))
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.9666, 
    farPlane=41.6013, width=21.5758, height=11.6234, viewOffsetX=-0.215211, 
    viewOffsetY=-0.267485)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.8939, 
    farPlane=41.6741, width=21.5251, height=11.5961, viewOffsetX=-0.567115, 
    viewOffsetY=-3.39866)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.8936, 
    farPlane=41.6744, width=21.5249, height=11.596, viewOffsetX=-0.412051, 
    viewOffsetY=-3.92058)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.3228, 
    farPlane=43.0155, width=21.8239, height=11.7571, cameraPosition=(39.1954, 
    1.45848, 3.44726), cameraUpVector=(-0.198375, 0.014982, 0.980012), 
    cameraTarget=(3.21701, 1.30401, 8.5256), viewOffsetX=-0.417775, 
    viewOffsetY=-3.97504)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.7245, 
    farPlane=44.1902, width=21.407, height=11.5325, cameraPosition=(38.8243, 
    3.96819, -0.257503), cameraUpVector=(-0.102926, 0.0273222, 0.994314), 
    cameraTarget=(3.60685, 1.5218, 8.3452), viewOffsetX=-0.409795, 
    viewOffsetY=-3.89911)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.6734, 
    farPlane=41.9489, width=22.0681, height=11.8887, cameraPosition=(39.0941, 
    1.06549, 6.93894), cameraUpVector=(-0.286571, -0.0434306, 0.957074), 
    cameraTarget=(2.80266, 0.983984, 8.72367), viewOffsetX=-0.422451, 
    viewOffsetY=-4.01953)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.4992, 
    farPlane=41.6426, width=21.9467, height=11.8233, cameraPosition=(38.869, 
    3.47996, 8.22301), cameraUpVector=(-0.317209, -0.0506729, 0.947001), 
    cameraTarget=(2.61642, 1.08288, 8.74109), viewOffsetX=-0.420128, 
    viewOffsetY=-3.99743)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.416, 
    farPlane=42.1967, width=21.8887, height=11.7921, cameraPosition=(39.0871, 
    2.58286, 6.37833), cameraUpVector=(-0.271334, -0.0237935, 0.962191), 
    cameraTarget=(2.85453, 1.16549, 8.7135), viewOffsetX=-0.419018, 
    viewOffsetY=-3.98687)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.5699, 
    farPlane=41.7024, width=21.996, height=11.8499, cameraPosition=(38.9469, 
    2.76245, 7.94217), cameraUpVector=(-0.311785, -0.0239576, 0.949851), 
    cameraTarget=(2.655, 1.17455, 8.74064), viewOffsetX=-0.421071, 
    viewOffsetY=-4.00641)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.5615, 
    farPlane=41.8747, width=21.9902, height=11.8468, cameraPosition=(39.0278, 
    2.1709, 7.40109), cameraUpVector=(-0.297907, -0.0238392, 0.954297), 
    cameraTarget=(2.73141, 1.14528, 8.73648), viewOffsetX=-0.42096, 
    viewOffsetY=-4.00535)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.7708, 
    farPlane=41.4764, width=22.136, height=11.9254, cameraPosition=(38.9203, 
    1.37863, 8.62225), cameraUpVector=(-0.32946, -0.036244, 0.943474), 
    cameraTarget=(2.58666, 1.04522, 8.7592), viewOffsetX=-0.423752, 
    viewOffsetY=-4.03191)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.4586, 
    farPlane=42.1915, width=21.9185, height=11.8082, cameraPosition=(39.1085, 
    1.99901, 6.43022), cameraUpVector=(-0.272444, -0.028143, 0.96176), 
    cameraTarget=(2.85659, 1.11452, 8.72837), viewOffsetX=-0.419589, 
    viewOffsetY=-3.9923)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.4145, 
    farPlane=42.1365, width=21.8878, height=11.7916, cameraPosition=(39.0616, 
    2.81132, 6.57815), cameraUpVector=(-0.276262, -0.0227346, 0.960814), 
    cameraTarget=(2.82626, 1.18482, 8.72669), viewOffsetX=-0.419, 
    viewOffsetY=-3.9867)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.5988, 
    farPlane=41.637, width=22.0162, height=11.8608, cameraPosition=(38.9302, 
    2.65339, 8.15341), cameraUpVector=(-0.316667, -0.0303058, 0.948053), 
    cameraTarget=(2.63131, 1.1408, 8.75598), viewOffsetX=-0.421458, 
    viewOffsetY=-4.01009)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.3194, 
    farPlane=42.2242, width=21.8216, height=11.7559, cameraPosition=(39.0354, 
    3.42962, 6.35461), cameraUpVector=(-0.270455, -0.0186738, 0.962551), 
    cameraTarget=(2.84407, 1.23394, 8.72602), viewOffsetX=-0.417732, 
    viewOffsetY=-3.97464)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.2475, 
    farPlane=42.5445, width=21.7715, height=11.7289, cameraPosition=(39.1029, 
    3.19455, 5.25126), cameraUpVector=(-0.241749, -0.0163166, 0.970202), 
    cameraTarget=(2.98511, 1.23238, 8.70236), viewOffsetX=-0.416773, 
    viewOffsetY=-3.96552)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.4648, 
    farPlane=41.9205, width=21.9229, height=11.8105, cameraPosition=(38.9918, 
    3.11879, 7.24629), cameraUpVector=(-0.293222, -0.0223654, 0.955783), 
    cameraTarget=(2.73842, 1.19974, 8.75135), viewOffsetX=-0.419671, 
    viewOffsetY=-3.99309)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.9072, 
    farPlane=40.0641, width=6.65156, height=3.58337, viewOffsetX=0.397749, 
    viewOffsetY=-2.7365)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.6769, 
    farPlane=40.4963, width=6.60502, height=3.55829, cameraPosition=(39.0315, 
    2.85609, 5.40893), cameraUpVector=(-0.24492, -0.0234443, 0.96926), 
    cameraTarget=(2.88684, 1.18769, 8.7311), viewOffsetX=0.394965, 
    viewOffsetY=-2.71735)
session.viewports['Viewport: 1'].view.setValues(nearPlane=33.0023, 
    farPlane=39.9303, width=6.67078, height=3.59372, cameraPosition=(38.9764, 
    3.10656, 7.59354), cameraUpVector=(-0.301763, -0.0315325, 0.952861), 
    cameraTarget=(2.71127, 1.17152, 8.75551), viewOffsetX=0.398897, 
    viewOffsetY=-2.74441)
session.viewports['Viewport: 1'].view.setValues(nearPlane=33.0674, 
    farPlane=39.865, width=5.55158, height=2.99078, viewOffsetX=0.397058, 
    viewOffsetY=-2.6578)
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('X-Plane', 
    ), viewCut=ON)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['X-Plane'].setValues(
    position=5.05)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['X-Plane'].setValues(
    position=0.202001)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.animationOptions.setValues(frameRate=62)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxAutoCompute=OFF, maxValue=0.000433231, minValue=4.77549E-07)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=0.0003)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.animationOptions.setValues(frameRate=49)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=33.0172, 
    farPlane=40.3258, width=5.54315, height=2.98624, viewOffsetX=1.71781, 
    viewOffsetY=-2.74095)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1.68514, 
    viewOffsetY=-2.78454)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1.85575, 
    viewOffsetY=-2.82813)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2.0191, 
    viewOffsetY=-2.87172)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1.71054, 
    viewOffsetY=-2.89352)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
