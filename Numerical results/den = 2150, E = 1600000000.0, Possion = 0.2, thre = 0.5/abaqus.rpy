# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by nagata on Wed Apr  2 16:52:06 2025
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
#: Model: E:/EESD/Schekenberg castle on cite inspection/2024-10-25 Zurich/Photogrammetry/Try extend the bottom/Variable sensitivty analysis with prism tower Fixed BCs/Boundary condition 1/den = 2150, E = 1600000000.0, Possion = 0.2, thre = 0.5/Modal_Analysis_Job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.8082, 
    farPlane=46.5207, width=16.447, height=8.86045, cameraPosition=(2.58726, 
    -12.8883, 41.9751), cameraUpVector=(-0.24263, 0.969168, 0.0429495))
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.3321, 
    farPlane=43.3093, width=18.5312, height=9.98327, cameraPosition=(10.6935, 
    -32.9386, 19.2935), cameraUpVector=(-0.13446, 0.596936, 0.790941), 
    cameraTarget=(2.58566, 0.602816, 7.91402))
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.412, 
    farPlane=44.2294, width=27.9648, height=15.0654, viewOffsetX=0.422171, 
    viewOffsetY=-0.458864)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.0353, 
    farPlane=43.7958, width=28.5379, height=15.3741, cameraPosition=(12.6076, 
    -33.6291, 15.3155), cameraUpVector=(-0.146867, 0.499524, 0.85376), 
    cameraTarget=(2.64535, 0.500311, 7.81941), viewOffsetX=0.430823, 
    viewOffsetY=-0.468268)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.9868, 
    farPlane=43.8443, width=28.4933, height=15.3501, viewOffsetX=0.915302, 
    viewOffsetY=1.00772)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
#: 
#: Node: PART-1_INSTANCE.3618
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.23669e+00,  2.21721e+00,  4.13033e-01,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   2.23669e+00,  2.21721e+00,  4.13033e-01,      -      
#: Deformed coordinates (scaled):     2.23594e+00,  2.21700e+00,  4.13309e-01,      -      
#: Displacement (unscaled):          -1.69897e-06, -4.79952e-07,  6.20994e-07,  1.87149e-06
#: 
#: Node: PART-1_INSTANCE.3922
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.95052e+00,  2.14220e+00,  1.86660e+00,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   1.95054e+00,  2.14212e+00,  1.86661e+00,      -      
#: Deformed coordinates (scaled):     1.96117e+00,  2.10445e+00,  1.86796e+00,      -      
#: Displacement (unscaled):           2.39164e-05, -8.47580e-05,  3.04733e-06,  8.81204e-05
#: 
#: Node: PART-1_INSTANCE.3291
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.95403e+00,  2.26001e+00,  3.51043e+00,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   1.95411e+00,  2.25972e+00,  3.51045e+00,      -      
#: Deformed coordinates (scaled):     1.99217e+00,  2.13334e+00,  3.52139e+00,      -      
#: Displacement (unscaled):           8.56200e-05, -2.84351e-04,  2.46024e-05,  2.97979e-04
#: 
#: Node: PART-1_INSTANCE.702
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.04557e+00,  1.81000e+00,  5.02690e+00,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   2.04573e+00,  1.80945e+00,  5.02684e+00,      -      
#: Deformed coordinates (scaled):     2.11610e+00,  1.56597e+00,  5.00130e+00,      -      
#: Displacement (unscaled):           1.58321e-04, -5.47819e-04, -5.74626e-05,  5.73126e-04
#: 
#: Node: PART-1_INSTANCE.3598
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.05185e+00,  2.26206e+00,  6.33888e+00,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   2.05210e+00,  2.26124e+00,  6.33891e+00,      -      
#: Deformed coordinates (scaled):     2.16420e+00,  1.89534e+00,  6.35449e+00,      -      
#: Displacement (unscaled):           2.52209e-04, -8.23217e-04,  3.50564e-05,  8.61698e-04
#: 
#: Node: PART-1_INSTANCE.3174
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.97347e+00,  2.31455e+00,  8.00876e+00,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   1.97385e+00,  2.31333e+00,  8.00882e+00,      -      
#: Deformed coordinates (scaled):     2.14288e+00,  1.77010e+00,  8.03592e+00,      -      
#: Displacement (unscaled):           3.80279e-04, -1.22221e-03,  6.09637e-05,  1.28146e-03
#: 
#: Node: PART-1_INSTANCE.3320
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.03286e+00,  2.23809e+00,  9.45973e+00,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   2.03336e+00,  2.23649e+00,  9.45977e+00,      -      
#: Deformed coordinates (scaled):     2.25501e+00,  1.52268e+00,  9.47777e+00,      -      
#: Displacement (unscaled):           4.98688e-04, -1.60598e-03,  4.04786e-05,  1.68212e-03
#: 
#: Node: PART-1_INSTANCE.3487
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.19586e+00,  2.26722e+00,  1.11066e+01,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   2.19651e+00,  2.26514e+00,  1.11066e+01,      -      
#: Deformed coordinates (scaled):     2.48324e+00,  1.34488e+00,  1.11229e+01,      -      
#: Displacement (unscaled):           6.45115e-04, -2.07048e-03,  3.66439e-05,  2.16897e-03
#: 
#: Node: PART-1_INSTANCE.2583
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02487e+00,  1.81000e+00,  1.25317e+01,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   2.02563e+00,  1.80753e+00,  1.25317e+01,      -      
#: Deformed coordinates (scaled):     2.36098e+00,  7.09790e-01,  1.24976e+01,      -      
#: Displacement (unscaled):           7.54498e-04, -2.46979e-03, -7.66313e-05,  2.58361e-03
#: 
#: Node: PART-1_INSTANCE.1453
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.03088e+00,  1.81000e+00,  1.39558e+01,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   2.03176e+00,  1.80712e+00,  1.39557e+01,      -      
#: Deformed coordinates (scaled):     2.42496e+00,  5.27157e-01,  1.39217e+01,      -      
#: Displacement (unscaled):           8.84640e-04, -2.87977e-03, -7.65937e-05,  3.01356e-03
#: 
#: Node: PART-1_INSTANCE.48
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.88493e+00,  2.10872e+00,  1.55000e+01,      -      
#: Scale:                             4.45467e+02,  4.45467e+02,  4.45467e+02,      -      
#: Deformed coordinates (unscaled):   1.88597e+00,  2.10540e+00,  1.55000e+01,      -      
#: Deformed coordinates (scaled):     2.34924e+00,  6.31565e-01,  1.55105e+01,      -      
#: Displacement (unscaled):           1.04230e-03, -3.31597e-03,  2.35094e-05,  3.47600e-03
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.1192, 
    farPlane=48.464, width=24.9369, height=13.4342, cameraPosition=(8.63606, 
    -0.0450387, 45.2146), cameraUpVector=(-0.805643, 0.544394, -0.233612), 
    cameraTarget=(3.9127, -0.246806, 9.1882), viewOffsetX=0.801058, 
    viewOffsetY=0.881941)
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.7788, 
    farPlane=48.6102, width=24.6239, height=13.2656, cameraPosition=(13.0294, 
    -13.3133, 41.28), cameraUpVector=(-0.781866, 0.617564, 0.0854457), 
    cameraTarget=(3.94902, -0.655616, 8.45346), viewOffsetX=0.791004, 
    viewOffsetY=0.870872)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.4932, 
    farPlane=47.9498, width=25.2808, height=13.6195, cameraPosition=(20.4039, 
    -21.5835, 32.552), cameraUpVector=(-0.583815, 0.665869, 0.464519), 
    cameraTarget=(3.73063, -0.78668, 7.85896), viewOffsetX=0.812107, 
    viewOffsetY=0.894106)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.8993, 
    farPlane=45.4623, width=26.5738, height=14.3161, cameraPosition=(-4.4433, 
    -32.4521, 22.7534), cameraUpVector=(-0.040855, 0.720818, 0.691919), 
    cameraTarget=(2.17361, -0.306679, 7.16047), viewOffsetX=0.853642, 
    viewOffsetY=0.939835)
session.viewports['Viewport: 1'].view.setValues(nearPlane=26.7817, 
    farPlane=47.1646, width=24.6266, height=13.2671, cameraPosition=(-23.6941, 
    -1.57272, 33.5988), cameraUpVector=(0.870679, 0.264546, 0.414649), 
    cameraTarget=(1.60197, 1.54524, 7.70212), viewOffsetX=0.791093, 
    viewOffsetY=0.87097)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.1345, 
    farPlane=45.4873, width=25.8706, height=13.9373, cameraPosition=(-28.2008, 
    14.7256, 22.2081), cameraUpVector=(0.714798, -0.0595325, 0.696793), 
    cameraTarget=(2.34048, 2.01904, 7.17388), viewOffsetX=0.831054, 
    viewOffsetY=0.914966)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.4842, 
    farPlane=46.1979, width=25.2726, height=13.6151, cameraPosition=(-28.0319, 
    -6.30712, 26.8064), cameraUpVector=(0.737965, 0.271864, 0.617655), 
    cameraTarget=(1.68092, 1.58814, 7.43972), viewOffsetX=0.811844, 
    viewOffsetY=0.893816)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.2492, 
    farPlane=46.9851, width=25.0565, height=13.4987, cameraPosition=(8.25796, 
    -26.0381, 32.867), cameraUpVector=(-0.0637247, 0.892645, 0.446234), 
    cameraTarget=(2.031, -0.416678, 7.86652), viewOffsetX=0.804903, 
    viewOffsetY=0.886175)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6223, 
    farPlane=46.7952, width=25.3996, height=13.6835, cameraPosition=(25.2896, 
    -21.5458, 27.2653), cameraUpVector=(-0.367086, 0.726589, 0.580789), 
    cameraTarget=(2.8173, -0.664334, 7.79185), viewOffsetX=0.815924, 
    viewOffsetY=0.898309)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.6986, 
    farPlane=46.5147, width=25.4697, height=13.7213, cameraPosition=(13.2683, 
    -28.5184, 27.9805), cameraUpVector=(-0.329474, 0.737535, 0.589483), 
    cameraTarget=(2.45473, -0.538611, 7.47552), viewOffsetX=0.818177, 
    viewOffsetY=0.900789)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.3675, 
    farPlane=44.8457, width=6.92229, height=3.72922, viewOffsetX=0.744994, 
    viewOffsetY=1.80767)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.9451, 
    farPlane=47.0557, width=6.82271, height=3.67557, cameraPosition=(6.37872, 
    -8.54055, 44.5362), cameraUpVector=(-0.426169, 0.898344, -0.106576), 
    cameraTarget=(2.7143, -0.991007, 9.1832), viewOffsetX=0.734277, 
    viewOffsetY=1.78167)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.716, 
    farPlane=47.2848, width=9.9822, height=5.37767, viewOffsetX=0.740039, 
    viewOffsetY=1.95606)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.2625, 
    farPlane=47.1941, width=9.82456, height=5.29275, cameraPosition=(10.2353, 
    -15.0644, 41.2744), cameraUpVector=(-0.436644, 0.892976, 0.109252), 
    cameraTarget=(2.8263, -1.12033, 8.54935), viewOffsetX=0.728352, 
    viewOffsetY=1.92517)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.827, 
    farPlane=47.6296, width=15.5853, height=8.3962, viewOffsetX=0.833599, 
    viewOffsetY=1.83411)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.7156, 
    farPlane=47.4945, width=15.5229, height=8.36259, cameraPosition=(11.8074, 
    -18.1342, 39.0696), cameraUpVector=(-0.434619, 0.874347, 0.215924), 
    cameraTarget=(2.84672, -1.12236, 8.23837), viewOffsetX=0.830261, 
    viewOffsetY=1.82676)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.2576, 
    farPlane=45.428, width=16.3865, height=8.82785, cameraPosition=(32.8602, 
    -15.2071, 23.1308), cameraUpVector=(-0.558788, 0.468986, 0.683965), 
    cameraTarget=(3.81792, -0.477124, 7.01137), viewOffsetX=0.876453, 
    viewOffsetY=1.92839)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.1096, 
    farPlane=42.4785, width=17.4238, height=9.38665, cameraPosition=(27.4098, 
    -26.4899, 8.94932), cameraUpVector=(-0.229261, 0.336001, 0.913533), 
    cameraTarget=(2.69708, 0.0110168, 6.25811), viewOffsetX=0.931932, 
    viewOffsetY=2.05046)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.8638, 
    farPlane=42.2155, width=17.8462, height=9.61422, cameraPosition=(37.445, 
    -12.2302, 6.73371), cameraUpVector=(-0.3746, 0.00139572, 0.927186), 
    cameraTarget=(3.39846, 0.441923, 6.02183), viewOffsetX=0.954526, 
    viewOffsetY=2.10017)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.6302, 
    farPlane=42.8212, width=17.7154, height=9.54375, cameraPosition=(39.5542, 
    -4.6974, 10.1254), cameraUpVector=(-0.456013, -0.110145, 0.883131), 
    cameraTarget=(3.84416, 0.648422, 6.06714), viewOffsetX=0.94753, 
    viewOffsetY=2.08478)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.7705, 
    farPlane=43.681, width=28.7543, height=15.4907, viewOffsetX=1.40174, 
    viewOffsetY=2.82117)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.2473, 
    farPlane=45.2857, width=28.2655, height=15.2273, cameraPosition=(39.2418, 
    8.49006, 14.3172), cameraUpVector=(-0.490053, -0.249337, 0.835272), 
    cameraTarget=(4.59445, 1.06619, 6.27354), viewOffsetX=1.37791, 
    viewOffsetY=2.77321)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.0797, 
    farPlane=44.1135, width=29.0434, height=15.6464, cameraPosition=(38.9351, 
    11.2584, 8.86289), cameraUpVector=(-0.383174, -0.120583, 0.915771), 
    cameraTarget=(4.29524, 0.618515, 6.19339), viewOffsetX=1.41583, 
    viewOffsetY=2.84953)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.1756, 
    farPlane=43.8581, width=29.133, height=15.6947, cameraPosition=(39.2586, 
    9.77987, 7.97275), cameraUpVector=(-0.373714, -0.0671396, 0.925111), 
    cameraTarget=(4.19742, 0.40438, 6.22065), viewOffsetX=1.4202, 
    viewOffsetY=2.85832)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.8299, 
    farPlane=44.2039, width=34.6863, height=18.6864, viewOffsetX=1.02383, 
    viewOffsetY=2.52075)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.6248, 
    farPlane=43.9141, width=34.4556, height=18.5621, cameraPosition=(39.1741, 
    -7.31591, 7.41302), cameraUpVector=(-0.361989, 0.0574432, 0.930411), 
    cameraTarget=(3.59285, -0.0626867, 6.13916), viewOffsetX=1.01702, 
    viewOffsetY=2.50398)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.0401, 
    farPlane=44.1963, width=33.7977, height=18.2077, cameraPosition=(39.2499, 
    -1.48684, 1.16461), cameraUpVector=(-0.21032, -0.0644082, 0.975509), 
    cameraTarget=(3.27378, 0.290626, 5.94104), viewOffsetX=0.997601, 
    viewOffsetY=2.45617)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.1342, 
    farPlane=43.1021, width=21.3524, height=11.5031, viewOffsetX=1.41495, 
    viewOffsetY=0.477819)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.1828, 
    farPlane=43.1785, width=21.3857, height=11.521, cameraPosition=(39.1657, 
    -0.365013, 0.12858), cameraUpVector=(-0.183151, -0.102444, 0.977733), 
    cameraTarget=(3.2936, 0.334237, 5.86951), viewOffsetX=1.41715, 
    viewOffsetY=0.478565)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.696, 
    farPlane=42.0713, width=21.7376, height=11.7106, cameraPosition=(39.4402, 
    -3.42151, 7.11826), cameraUpVector=(-0.363209, -0.0191797, 0.93151), 
    cameraTarget=(3.30313, 0.231128, 6.10507), viewOffsetX=1.44047, 
    viewOffsetY=0.48644)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.6725, 
    farPlane=42.0948, width=23.1079, height=12.4489, viewOffsetX=1.78113, 
    viewOffsetY=0.701853)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31.5458, 
    farPlane=42.2214, width=23.0156, height=12.3991, viewOffsetX=2.30154, 
    viewOffsetY=-1.44289)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.4954, 
    farPlane=41.2719, width=12.0035, height=6.46662, viewOffsetX=1.66846, 
    viewOffsetY=-2.29467)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
