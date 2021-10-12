# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def make_piston():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(viewStyle=AXISYM)
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=80.1919, 
        farPlane=108.37, width=113.315, height=66.9493, cameraPosition=(
        25.4093, 26.919, 94.2809), cameraTarget=(25.4093, 26.919, 0))
    s.Line(point1=(25.0, 125.0), point2=(12.0, 125.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2751, 
        farPlane=129.287, width=281.545, height=166.344, cameraPosition=(
        57.7464, 55.372, 94.2809), cameraTarget=(57.7464, 55.372, 0))
    s.Line(point1=(12.0, 125.0), point2=(12.0, 100.0))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(12.0, 100.0), point2=(0.0, 100.0))
    s.HorizontalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(0.0, 100.0), point2=(0.0, 35.0))
    s.VerticalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(0.0, 35.0), point2=(5.0, 35.0))
    s.HorizontalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(5.0, 35.0), point2=(5.0, 0.0))
    s.VerticalConstraint(entity=g[8], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s.Line(point1=(5.0, 0.0), point2=(20.0, 0.0))
    s.HorizontalConstraint(entity=g[9], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
    s.Line(point1=(20.0, 0.0), point2=(20.0, 50.0))
    s.VerticalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=275.914, height=163.017, 
        cameraPosition=(57.0196, 55.2876, 94.2809), cameraTarget=(57.0196, 
        55.2876, 0))
    s.Line(point1=(20.0, 50.0), point2=(25.0, 55.0))
    s.Line(point1=(25.0, 55.0), point2=(25.0, 125.0))
    s.VerticalConstraint(entity=g[12], addUndoState=False)
    p = mdb.models['Model-1'].Part(name='piston', dimensionality=AXISYMMETRIC, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['piston']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['piston']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def make_cap():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(viewStyle=AXISYM)
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s1.FixedConstraint(entity=g[2])
    s1.Line(point1=(0.0, 0.0), point2=(12.0, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    s1.Line(point1=(12.0, 0.0), point2=(12.0, 25.0))
    s1.VerticalConstraint(entity=g[4], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s1.Line(point1=(12.0, 25.0), point2=(25.0, 25.0))
    s1.HorizontalConstraint(entity=g[5], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s1.Line(point1=(25.0, 25.0), point2=(25.0, 75.0))
    s1.VerticalConstraint(entity=g[6], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=74.8402, 
        farPlane=113.722, width=159.615, height=94.3047, cameraPosition=(
        7.32501, 37.8997, 94.2809), cameraTarget=(7.32501, 37.8997, 0))
    s1.Line(point1=(25.0, 75.0), point2=(0.0, 75.0))
    s1.HorizontalConstraint(entity=g[7], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s1.Line(point1=(0.0, 75.0), point2=(0.0, 0.0))
    s1.VerticalConstraint(entity=g[8], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s1.CircleByCenterPerimeter(center=(23.0, 73.0), point1=(25.0, 73.0))
    s1.autoTrimCurve(curve1=g[9], point1=(22.4427509307861, 71.1175231933594))
    s1.autoTrimCurve(curve1=g[6], point1=(25.8178806304932, 74.3548431396484))
    s1.autoTrimCurve(curve1=g[7], point1=(24.5522022247314, 74.9178619384766))
    p = mdb.models['Model-1'].Part(name='cap', dimensionality=AXISYMMETRIC, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['cap']
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['cap']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['cap']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
        11.234559, 42.724308, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=158.11, gridSpacing=3.95, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['cap']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=140.506, 
        farPlane=175.722, width=141.617, height=83.6706, cameraPosition=(
        12.3066, 37.7338, 158.114), cameraTarget=(12.3066, 37.7338, 0))
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['cap']
    f1, e1, d2 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
        11.234559, 42.724308, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=158.11, gridSpacing=3.95, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['cap']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=150.728, 
        farPlane=165.5, width=57.0542, height=33.709, cameraPosition=(18.1291, 
        30.5086, 158.114), cameraTarget=(18.1291, 30.5086, 0))
    s1.Line(point1=(11.765441, 32.275692), point2=(11.765441, -17.7243079999731))
    s1.VerticalConstraint(entity=g[10], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[7], entity2=g[10], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[8], entity2=g[5], addUndoState=False)
    p = mdb.models['Model-1'].parts['cap']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e, d1 = p.edges, p.datums
    p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['cap']
    f, e1, d2 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
        10.362069, 42.241379, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=158.11, gridSpacing=3.95, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['cap']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.Line(point1=(14.637931, 30.758621), point2=(-10.3620690000122, 30.758621))
    s.HorizontalConstraint(entity=g[13], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[10], entity2=g[13], addUndoState=False)
    s.CoincidentConstraint(entity1=v[9], entity2=g[4], addUndoState=False)
    p = mdb.models['Model-1'].parts['cap']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#3 ]', ), )
    e, d1 = p.edges, p.datums
    p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']


def make_pump_tube():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=2000.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(viewStyle=AXISYM)
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -1000.0), point2=(0.0, 1000.0))
    s1.FixedConstraint(entity=g[2])
    s1.rectangle(point1=(25.0, 0.0), point2=(35.0, 800.0))
    p = mdb.models['Model-1'].Part(name='pump-tube', dimensionality=AXISYMMETRIC, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['pump-tube']
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['pump-tube']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def make_transition_piece():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=300.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(viewStyle=AXISYM)
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -150.0), point2=(0.0, 150.0))
    s1.FixedConstraint(entity=g[2])
    s1.Line(point1=(40.0, 0.0), point2=(40.0, 120.0))
    s1.VerticalConstraint(entity=g[3], addUndoState=False)
    s1.Line(point1=(40.0, 120.0), point2=(6.0, 120.0))
    s1.HorizontalConstraint(entity=g[4], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s1.Line(point1=(6.0, 120.0), point2=(6.0, 107.0))
    s1.VerticalConstraint(entity=g[5], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s1.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=106.387, 
        farPlane=176.456, width=281.773, height=166.479, cameraPosition=(
        69.8422, 61.6261, 141.421), cameraTarget=(69.8422, 61.6261, 0))
    s1.Line(point1=(6.0, 120.0), point2=(6.0, 102.0))
    s1.VerticalConstraint(entity=g[5], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s1.Line(point1=(6.0, 102.0), point2=(25.0, 50.0))
    s1.Line(point1=(25.0, 50.0), point2=(35.0, 50.0))
    s1.HorizontalConstraint(entity=g[7], addUndoState=False)
    s1.Line(point1=(35.0, 50.0), point2=(35.0, 0.0))
    s1.VerticalConstraint(entity=g[8], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s1.Line(point1=(35.0, 0.0), point2=(40.0, 0.0))
    s1.HorizontalConstraint(entity=g[9], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
    p = mdb.models['Model-1'].Part(name='transition-piece', 
        dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['transition-piece']
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['transition-piece']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['transition-piece']
    f1, e1, d2 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
        27.164014, 82.063358, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=252.98, gridSpacing=6.32, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['transition-piece']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.Line(point1=(7.835986, -32.063358), point2=(12.83598600001, -32.063358))
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    s.ParallelConstraint(entity1=g[7], entity2=g[10], addUndoState=False)
    s.CoincidentConstraint(entity1=v[7], entity2=g[3], addUndoState=False)
    s.Line(point1=(-21.164014, 19.936642), point2=(12.83598600001, 19.936642))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[11], addUndoState=False)
    s.CoincidentConstraint(entity1=v[8], entity2=g[3], addUndoState=False)
    p = mdb.models['Model-1'].parts['transition-piece']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e, d1 = p.edges, p.datums
    p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']


def assemble():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a1 = mdb.models['Model-1'].rootAssembly
    a1.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), 
        point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
    p = mdb.models['Model-1'].parts['pump-tube']
    a1.Instance(name='pump-tube-1', part=p, dependent=ON)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate_x(instanceList=('pump-tube-1',), vector=(0.0, -800.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['transition-piece']
    a1.Instance(name='transition-piece-1', part=p, dependent=ON)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate_x(instanceList=('transition-piece-1',), vector=(0.0, -50.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['cap']
    a1.Instance(name='cap-1', part=p, dependent=ON)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate_x(instanceList=('cap-1',), vector=(0.0, -75.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['piston']
    a1.Instance(name='piston-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2031.43, 
        farPlane=2147.63, width=467.009, height=264.389, viewOffsetX=11.6364, 
        viewOffsetY=362.785)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate_x(instanceList=('piston-1',), vector=(0.0, -175.0, 0.0))


def make_step():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.models['Model-1'].ImplicitDynamicsStep(name='taper-slide', 
        previous='Initial', timePeriod=0.001, maxNumInc=1000000, 
        initialInc=1e-07, minInc=1e-08, nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='taper-slide')


def partition_tube():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1871.95, 
        farPlane=1970.61, width=381.243, height=215.834, viewOffsetX=0.602808, 
        viewOffsetY=311.199)
    p = mdb.models['Model-1'].parts['pump-tube']
    f, e1, d2 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
        30.0, 400.0, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=1601.53, gridSpacing=40.03, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['pump-tube']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1565.01, 
        farPlane=1635.24, width=271.244, height=160.258, cameraPosition=(
        34.2952, 721.386, 1600.12), cameraTarget=(34.2952, 721.386, 0))
    s1.Line(point1=(-5.0, 320.24), point2=(5.0, 320.24))
    s1.HorizontalConstraint(entity=g[7], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[5], entity2=g[7], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[4], entity2=g[5], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[5], entity2=g[3], addUndoState=False)
    s1.VerticalDimension(vertex1=v[4], vertex2=v[3], textPoint=(-59.8712577819824, 
        353.198486328125), value=50.0)
    p = mdb.models['Model-1'].parts['pump-tube']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e, d1 = p.edges, p.datums
    p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']


def make_surfaces():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].view.setValues(nearPlane=279.637, 
        farPlane=318.172, width=130.428, height=73.8396, viewOffsetX=6.78705, 
        viewOffsetY=-13.4806)
    p = mdb.models['Model-1'].parts['transition-piece']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#420 ]', ), )
    p.Surface(side1Edges=side1Edges, name='tube-tie')
    p = mdb.models['Model-1'].parts['transition-piece']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#200 ]', ), )
    p.Surface(side1Edges=side1Edges, name='end-contact')
    p = mdb.models['Model-1'].parts['piston']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['piston']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#e ]', ), )
    p.Surface(side1Edges=side1Edges, name='end-contact')
    p = mdb.models['Model-1'].parts['piston']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Surface(side1Edges=side1Edges, name='pump-contact')
    p = mdb.models['Model-1'].parts['cap']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['cap']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#e04 ]', ), )
    p.Surface(side1Edges=side1Edges, name='piston-contact')
    p = mdb.models['Model-1'].parts['cap']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#1048 ]', ), )
    p.Surface(side1Edges=side1Edges, name='transition-and-pump-contact')


def make_interactions():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2050.02, 
        farPlane=2129.04, width=317.679, height=179.849, viewOffsetX=15.5557, 
        viewOffsetY=329.352)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['pump-tube-1'].surfaces['transition-tie']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['transition-piece-1'].surfaces['tube-tie']
    mdb.models['Model-1'].Tie(name='transition-fitting', master=region1, 
        slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, 
        tieRotations=ON, thickness=ON)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['piston-1'].surfaces['end-contact']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['cap-1'].surfaces['piston-contact']
    mdb.models['Model-1'].Tie(name='cap-to-piston', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
        thickness=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2026.1, 
        farPlane=2152.97, width=509.877, height=288.658, viewOffsetX=29.1893, 
        viewOffsetY=298.75)
    mdb.models['Model-1'].ContactProperty('HDPE-on-steel')
    mdb.models['Model-1'].interactionProperties['HDPE-on-steel'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.02, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['HDPE-on-steel'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    mdb.models['Model-1'].ContactProperty('aluminium-on-steel')
    mdb.models['Model-1'].interactionProperties['aluminium-on-steel'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.01, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['aluminium-on-steel'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='taper-slide')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2069.87, 
        farPlane=2109.19, width=151.894, height=85.9921, viewOffsetX=13.369, 
        viewOffsetY=344.882)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['transition-piece-1'].surfaces['end-contact']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['cap-1'].surfaces['transition-and-pump-contact']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='cap-transition', 
        createStepName='taper-slide', master=region1, slave=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='HDPE-on-steel', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2059.62, 
        farPlane=2119.45, width=240.538, height=136.176, viewOffsetX=54.2315, 
        viewOffsetY=344.131)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['pump-tube-1'].surfaces['piston-contact']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['cap-1'].surfaces['transition-and-pump-contact']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='cap-on-tube', 
        createStepName='taper-slide', master=region1, slave=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='HDPE-on-steel', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2033.15, 
        farPlane=2145.92, width=453.243, height=256.596, viewOffsetX=42.0318, 
        viewOffsetY=337.996)
    a = mdb.models['Model-1'].rootAssembly
    a.features['cap-1'].suppress()
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['pump-tube-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#42 ]', ), )
    region1=a.Surface(side1Edges=side1Edges1, name='tube-inner')
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['piston-1'].surfaces['pump-contact']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='piston-on-tube', 
        createStepName='taper-slide', master=region1, slave=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='aluminium-on-steel', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    a.features['cap-1'].resume()


def make_bcs():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2010.64, 
        farPlane=2168.42, width=634.026, height=358.943, viewOffsetX=-41.9365, 
        viewOffsetY=248.613)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2030.49, 
        farPlane=2148.58, width=456.338, height=258.348, viewOffsetX=-12.887, 
        viewOffsetY=-354.166)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['transition-piece-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#6 ]', ), )
    e2 = a.instances['pump-tube-1'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#4 ]', ), )
    region = a.Set(edges=edges1+edges2, name='fixed')
    mdb.models['Model-1'].DisplacementBC(name='fix', createStepName='Initial', 
        region=region, u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2082.02, 
        farPlane=2097.04, width=50.3439, height=28.5014, viewOffsetX=-16.7963, 
        viewOffsetY=363.741)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['piston-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#10 ]', ), )
    e2 = a.instances['cap-1'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#180 ]', ), )
    region = a.Set(edges=edges1+edges2, name='piston-centre')
    mdb.models['Model-1'].DisplacementBC(name='piston-centre', 
        createStepName='Initial', region=region, u1=SET, u2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2074.35, 
        farPlane=2104.72, width=122.112, height=69.1316, viewOffsetX=-8.97403, 
        viewOffsetY=360.107)
    del mdb.models['Model-1'].boundaryConditions['piston-centre']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2037.28, 
        farPlane=2141.78, width=420.023, height=237.789, viewOffsetX=38.3335, 
        viewOffsetY=320.31)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['cap-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#180 ]', ), )
    e2 = a.instances['piston-1'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#10 ]', ), )
    region = a.Set(edges=edges1+edges2, name='piston-centre-actual')
    mdb.models['Model-1'].DisplacementBC(name='piston-centre', 
        createStepName='Initial', region=region, u1=SET, u2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2073.72, 
        farPlane=2105.35, width=122.177, height=69.1686, viewOffsetX=9.73257, 
        viewOffsetY=343.441)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['piston-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
    f2 = a.instances['cap-1'].faces
    faces2 = f2.getSequenceFromMask(mask=('[#f ]', ), )
    region = a.Set(faces=faces1+faces2, name='piston-and-cap')
    mdb.models['Model-1'].Velocity(name='contact-velocity', region=region, 
        field='', distributionType=MAGNITUDE, velocity1=0.0, velocity2=5000.0, 
        omega=0.0)


def make_bcs_cont():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['piston-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#3e0 ]', ), )
    region = a.Surface(side1Edges=side1Edges1, name='piston-back')
    mdb.models['Model-1'].Pressure(name='back-pressure', 
        createStepName='taper-slide', region=region, distributionType=UNIFORM, 
        field='', magnitude=1.0, amplitude=UNSET)


def make_amp():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.models['Model-1'].TabularAmplitude(name='pressure', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 1.0), (1.0, 1.0)))
    mdb.models['Model-1'].loads['back-pressure'].setValues(amplitude='pressure')
    mdb.models['Model-1'].TabularAmplitude(name='front-pressure', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 1.0), (1.0, 1.0)))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2061.25, 
        farPlane=2117.82, width=218.544, height=123.725, viewOffsetX=-1.55261, 
        viewOffsetY=323.809)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['cap-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1040 ]', ), )
    region = a.Surface(side1Edges=side1Edges1, name='cap-front')
    mdb.models['Model-1'].Pressure(name='front-pressure', 
        createStepName='taper-slide', region=region, distributionType=UNIFORM, 
        field='', magnitude=0.01, amplitude='front-pressure')


def mesh_cap():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].view.setValues(nearPlane=175.74, 
        farPlane=197.891, width=85.3532, height=48.4922, viewOffsetX=4.79585, 
        viewOffsetY=16.8762)
    p = mdb.models['Model-1'].parts['cap']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1021 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.31, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['cap']
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=('[#52 ]', ), )
    pickedEdges2 = e.getSequenceFromMask(mask=('[#8 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, minSize=0.062, maxSize=0.31, constraint=FINER)
    p = mdb.models['Model-1'].parts['cap']
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=('[#52 ]', ), )
    pickedEdges2 = e.getSequenceFromMask(mask=('[#8 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, minSize=0.31, maxSize=1.0, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.954, 
        farPlane=202.677, width=126.906, height=72.0996, viewOffsetX=-3.61743, 
        viewOffsetY=8.41788)
    p = mdb.models['Model-1'].parts['cap']
    p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['cap']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['cap']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#f ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['cap']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#f ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TRI)
    p = mdb.models['Model-1'].parts['cap']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    p = mdb.models['Model-1'].parts['cap']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#f ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))


def make_materials():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.models['Model-1'].Material(name='mild-steel')
    mdb.models['Model-1'].materials['mild-steel'].Elastic(table=((200000.0, 0.33), 
        ))
    mdb.models['Model-1'].materials['mild-steel'].Density(table=((8e-09, ), ))
    mdb.models['Model-1'].Material(name='aluminium')
    mdb.models['Model-1'].materials['aluminium'].Elastic(table=((68000.0, 0.32), ))
    mdb.models['Model-1'].materials['aluminium'].Density(table=((2.7e-09, ), ))
    mdb.models['Model-1'].Material(name='HDPE')
    mdb.models['Model-1'].materials['HDPE'].Elastic(table=((1000.0, 0.46), ))
    mdb.models['Model-1'].materials['HDPE'].Density(table=((9.5e-10, ), ))
    mdb.models['Model-1'].materials['HDPE'].Plastic(table=((12.5, 0.0), ))


def assign_materials():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.models['Model-1'].HomogeneousSolidSection(name='steel', 
        material='mild-steel', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='aluminium', 
        material='aluminium', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='hdpe', material='HDPE', 
        thickness=None)
    p = mdb.models['Model-1'].parts['piston']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='piston')
    p = mdb.models['Model-1'].parts['piston']
    p.SectionAssignment(region=region, sectionName='aluminium', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['cap']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['cap']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#f ]', ), )
    region = p.Set(faces=faces, name='cap')
    p = mdb.models['Model-1'].parts['cap']
    p.SectionAssignment(region=region, sectionName='hdpe', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['pump-tube']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['pump-tube']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
    region = p.Set(faces=faces, name='tube')
    p = mdb.models['Model-1'].parts['pump-tube']
    p.SectionAssignment(region=region, sectionName='steel', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['transition-piece']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['transition-piece']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    region = p.Set(faces=faces, name='transition-piece')
    p = mdb.models['Model-1'].parts['transition-piece']
    p.SectionAssignment(region=region, sectionName='steel', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


