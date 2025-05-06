# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by nagata on Fri Mar  7 16:15:46 2025
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
#: Model: E:/EESD/Schekenberg castle on cite inspection/2024-10-25 Zurich/Photogrammetry/Try extend the bottom/Variable sensitivty analysis with prism tower Fixed BCs/den = 2150, E = 1600000000.0, Possion = 0.2, thre = 1.75/Modal_Analysis_Job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.1446, 
    farPlane=46.7947, width=16.0546, height=8.64902, cameraPosition=(14.545, 
    -1.94657, 42.5359), cameraUpVector=(-0.590669, 0.803491, -0.0742514))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6374, 
    farPlane=46.5256, width=16.3461, height=8.80605, cameraPosition=(-0.705496, 
    0.239534, 44.6702), cameraUpVector=(-0.16119, 0.931767, -0.325313), 
    cameraTarget=(2.14314, 1.08765, 8.45667))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5116, 
    farPlane=46.4917, width=16.2717, height=8.76597, cameraPosition=(0.687247, 
    5.32348, 44.5226), cameraUpVector=(-0.090717, 0.89251, -0.441811), 
    cameraTarget=(2.17117, 1.18996, 8.4537))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5726, 
    farPlane=46.5068, width=16.3078, height=8.7854, cameraPosition=(4.76781, 
    -0.305043, 44.6773), cameraUpVector=(-0.0705841, 0.953571, -0.292782), 
    cameraTarget=(2.24466, 1.0886, 8.45649))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7461, 
    farPlane=46.3596, width=16.4104, height=8.84069, cameraPosition=(1.66769, 
    0.800748, 44.7889), cameraUpVector=(-0.0393059, 0.944583, -0.32591), 
    cameraTarget=(2.18571, 1.10963, 8.45861))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6146, 
    farPlane=46.4457, width=16.3326, height=8.7988, cameraPosition=(1.00567, 
    2.98312, 44.7278), cameraUpVector=(-0.0208553, 0.92423, -0.381265), 
    cameraTarget=(2.17289, 1.15189, 8.45743))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5527, 
    farPlane=46.5552, width=16.296, height=8.77908, cameraPosition=(-0.9527, 
    2.49622, 44.6342), cameraUpVector=(0.000538806, 0.929232, -0.369497), 
    cameraTarget=(2.13614, 1.14275, 8.45567))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.714, 
    farPlane=46.4021, width=16.3914, height=8.83049, cameraPosition=(1.04292, 
    0.832105, 44.7751), cameraUpVector=(-0.0357185, 0.944217, -0.327382), 
    cameraTarget=(2.17484, 1.11048, 8.4584))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6511, 
    farPlane=46.43, width=16.3542, height=8.81046, cameraPosition=(3.66645, 
    0.39915, 44.7581), cameraUpVector=(-0.0776133, 0.946826, -0.312246), 
    cameraTarget=(2.226, 1.10204, 8.45807))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6733, 
    farPlane=46.4525, width=16.3674, height=8.81755, cameraPosition=(0.254105, 
    0.992841, 44.7429), cameraUpVector=(-0.00770449, 0.943576, -0.331068), 
    cameraTarget=(2.16104, 1.11334, 8.45778))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.9994, 
    farPlane=46.5685, width=15.9688, height=8.60281, cameraPosition=(-0.705899, 
    5.29889, 44.4416), cameraUpVector=(0.0394415, 0.898963, -0.436245), 
    cameraTarget=(2.14562, 1.18249, 8.45294))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5056, 
    farPlane=46.3129, width=16.2682, height=8.76409, cameraPosition=(2.69417, 
    1.36082, 44.7883), cameraUpVector=(-0.00891512, 0.940704, -0.33911), 
    cameraTarget=(2.18708, 1.13447, 8.45717))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.3046, 
    farPlane=45.0293, width=17.3322, height=9.33731, cameraPosition=(-30.2642, 
    -3.82224, 24.7709), cameraUpVector=(0.320737, 0.933317, 0.16139), 
    cameraTarget=(1.67465, 1.05389, 8.14595))
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.9919, 
    farPlane=44.0581, width=18.3302, height=9.87494, cameraPosition=(-30.7999, 
    -13.9917, 14.7677), cameraUpVector=(0.150168, 0.773089, 0.616266), 
    cameraTarget=(1.66266, 0.826343, 7.92212))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.0658, 
    farPlane=47.5782, width=16.0081, height=8.62396, cameraPosition=(-10.7962, 
    -2.982, 42.4378), cameraUpVector=(0.356584, 0.928167, -0.106553), 
    cameraTarget=(2.29686, 1.1754, 8.79938))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5189, 
    farPlane=46.9854, width=16.2761, height=8.76832, cameraPosition=(-2.8815, 
    2.17766, 44.7847), cameraUpVector=(0.313101, 0.89707, -0.311823), 
    cameraTarget=(2.5061, 1.31181, 8.86142))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    ORIENT_ON_DEF, ))
#: Warning: Material orientation information is not available in the current frame for any elements in the current display group. Please make sure that the primary variable is element-based and orientations were defined in the pertinent solid/shell sections.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.8896, 
    farPlane=46.0936, width=16.4953, height=8.88647, cameraPosition=(-23.9821, 
    3.23208, 33.9378), cameraUpVector=(0.225708, 0.921684, -0.315523), 
    cameraTarget=(1.9868, 1.33776, 8.59447))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.8686, 
    farPlane=47.6762, width=16.4829, height=8.87977, cameraPosition=(9.09619, 
    -16.8372, 39.6835), cameraUpVector=(-0.356635, 0.910806, 0.207953), 
    cameraTarget=(2.57364, 0.981713, 8.69641))
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.3334, 
    farPlane=45.1386, width=18.5322, height=9.98376, cameraPosition=(2.30525, 
    -32.8101, 22.8572), cameraUpVector=(-0.557793, 0.614163, 0.558275), 
    cameraTarget=(2.31528, 0.37402, 8.05625))
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.764, 
    farPlane=44.2285, width=19.3784, height=10.4396, cameraPosition=(-15.8015, 
    -31.4264, 4.26972), cameraUpVector=(-0.383559, 0.518622, 0.764143), 
    cameraTarget=(1.4152, 0.442803, 7.13227))
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.4412, 
    farPlane=44.3892, width=19.1875, height=10.3368, cameraPosition=(-32.0946, 
    -14.3613, 4.05955), cameraUpVector=(0.0643439, 0.463764, 0.883619), 
    cameraTarget=(0.50061, 1.40073, 7.12047))
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.1581, 
    farPlane=44.2742, width=19.0201, height=10.2466, cameraPosition=(-35.3073, 
    1.87328, 14.795), cameraUpVector=(0.483872, 0.452298, 0.749195), 
    cameraTarget=(0.326671, 2.27969, 7.7017))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.637, 
    farPlane=47.2036, width=16.9375, height=9.12465, cameraPosition=(-25.6003, 
    4.11009, 33.5251), cameraUpVector=(0.842684, 0.380553, 0.380871), 
    cameraTarget=(0.80439, 2.38977, 8.62348))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6994, 
    farPlane=47.7364, width=16.3829, height=8.82589, cameraPosition=(-11.0974, 
    0.494271, 43.0934), cameraUpVector=(0.935561, 0.353113, 0.00604931), 
    cameraTarget=(1.41056, 2.23864, 9.02341))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7807, 
    farPlane=47.2817, width=16.431, height=8.85181, cameraPosition=(6.09764, 
    0.57388, 45.1691), cameraUpVector=(0.861022, 0.287763, -0.419325), 
    cameraTarget=(2.04085, 2.24156, 9.0995))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5288, 
    farPlane=47.4739, width=16.282, height=8.77154, cameraPosition=(7.65602, 
    7.33547, 44.6568), cameraUpVector=(0.775078, 0.369687, -0.512431), 
    cameraTarget=(2.09051, 2.45701, 9.08317))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5707, 
    farPlane=47.8724, width=16.3068, height=8.78488, cameraPosition=(-12.8092, 
    -6.10454, 41.393), cameraUpVector=(0.71487, 0.689863, 0.11424), 
    cameraTarget=(1.4542, 2.03913, 8.98169))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.5287, 
    farPlane=46.3412, width=16.8734, height=9.09013, cameraPosition=(30.9144, 
    -6.02554, 30.4747), cameraUpVector=(-0.153179, 0.988181, 0.00579919), 
    cameraTarget=(3.06097, 2.04203, 8.58046))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.3649, 
    farPlane=47.6264, width=16.1851, height=8.71932, cameraPosition=(9.95003, 
    -12.136, 41.5867), cameraUpVector=(-0.0482197, 0.996564, 0.0673367), 
    cameraTarget=(2.44516, 1.86254, 8.90686))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7428, 
    farPlane=47.2501, width=16.4086, height=8.83973, cameraPosition=(-1.93421, 
    0.134384, 45.0661), cameraUpVector=(-0.0714012, 0.954944, -0.288068), 
    cameraTarget=(2.07739, 2.24226, 9.01454))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7232, 
    farPlane=47.2696, width=16.397, height=8.8335, cameraPosition=(-1.93421, 
    0.134384, 45.0661), cameraUpVector=(0.0989536, 0.958063, -0.26893), 
    cameraTarget=(2.07739, 2.24226, 9.01454))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6479, 
    farPlane=47.3256, width=16.3525, height=8.80952, cameraPosition=(-1.98154, 
    5.8214, 44.9585), cameraUpVector=(0.0891295, 0.906502, -0.412688), 
    cameraTarget=(2.07592, 2.41837, 9.01121))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7307, 
    farPlane=47.2423, width=16.4015, height=8.8359, cameraPosition=(-1.16223, 
    5.03881, 45.1075), cameraUpVector=(0.0453806, 0.916002, -0.398598), 
    cameraTarget=(2.10109, 2.39433, 9.01579))
session.viewports['Viewport: 1'].view.setValues(nearPlane=25.3457, 
    farPlane=49.6123, width=14.9909, height=21.5876, cameraPosition=(-1.36707, 
    9.72243, 44.4448), cameraUpVector=(0.0145355, 0.857633, -0.514057), 
    cameraTarget=(2.0948, 2.53816, 8.99544))
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.394, 
    farPlane=47.564, width=7.08075, height=10.1966, viewOffsetX=0.684309, 
    viewOffsetY=0.142189)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5848, 
    farPlane=47.4343, width=7.13005, height=10.2676, cameraPosition=(0.725377, 
    5.54866, 45.2171), cameraUpVector=(-0.0438442, 0.908263, -0.416096), 
    cameraTarget=(2.16472, 2.38365, 9.04856), viewOffsetX=0.689074, 
    viewOffsetY=0.143179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7892, 
    farPlane=47.2461, width=7.18289, height=10.3437, cameraPosition=(1.58997, 
    2.80964, 45.3832), cameraUpVector=(0.0181526, 0.938592, -0.344551), 
    cameraTarget=(2.17564, 2.36684, 9.05534), viewOffsetX=0.69418, 
    viewOffsetY=0.14424)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6638, 
    farPlane=47.3742, width=7.15047, height=10.297, cameraPosition=(1.32824, 
    4.51833, 45.32), cameraUpVector=(0.0267378, 0.921881, -0.386549), 
    cameraTarget=(2.16636, 2.42599, 9.05469), viewOffsetX=0.691047, 
    viewOffsetY=0.143589)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7363, 
    farPlane=47.3486, width=7.1692, height=10.324, cameraPosition=(2.31804, 
    4.72211, 45.3433), cameraUpVector=(-0.0263748, 0.919148, -0.393028), 
    cameraTarget=(2.20637, 2.39124, 9.08303), viewOffsetX=0.692857, 
    viewOffsetY=0.143965)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7319, 
    farPlane=47.353, width=7.16806, height=10.3224, viewOffsetX=-0.487128, 
    viewOffsetY=1.10889)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
