# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def make_model():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=81.0483, 
        farPlane=107.514, width=141.215, height=62.8799, cameraPosition=(
        28.1633, 17.5932, 94.2809), cameraTarget=(28.1633, 17.5932, 0))
    s.rectangle(point1=(0.0, 0.0), point2=(20.0, 20.0))
    p = mdb.models['Model-1'].Part(name='piston', dimensionality=AXISYMMETRIC, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['piston']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['piston']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(viewStyle=AXISYM)
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s1.FixedConstraint(entity=g[2])
    s1.Line(point1=(20.0, 0.0), point2=(20.0, 20.0))
    s1.VerticalConstraint(entity=g[3], addUndoState=False)
    s1.Line(point1=(20.0, 20.0), point2=(10.0, 40.0))
    s1.Line(point1=(10.0, 40.0), point2=(0.0, 40.0))
    s1.HorizontalConstraint(entity=g[5], addUndoState=False)
    s1.Line(point1=(0.0, 40.0), point2=(0.0, 5.0))
    s1.VerticalConstraint(entity=g[6], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s1.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=82.5589, 
        farPlane=106.003, width=125.095, height=55.7017, cameraPosition=(
        23.5712, 21.8848, 94.2809), cameraTarget=(23.5712, 21.8848, 0))
    s1.Line(point1=(0.0, 40.0), point2=(0.0, 45.0))
    s1.VerticalConstraint(entity=g[6], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s1.Line(point1=(0.0, 45.0), point2=(13.75, 45.0))
    s1.HorizontalConstraint(entity=g[7], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s1.Line(point1=(13.75, 45.0), point2=(25.0, 22.5))
    s1.Line(point1=(25.0, 22.5), point2=(25.0, 0.0))
    s1.VerticalConstraint(entity=g[9], addUndoState=False)
    s1.Line(point1=(25.0, 0.0), point2=(20.0, 0.0))
    s1.HorizontalConstraint(entity=g[10], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    p = mdb.models['Model-1'].Part(name='tube', dimensionality=AXISYMMETRIC, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['tube']
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['tube']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
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
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), 
        point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
    p = mdb.models['Model-1'].parts['piston']
    a.Instance(name='piston-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['tube']
    a.Instance(name='tube-1', part=p, dependent=ON)


def make_tube():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=62.6837, 
        farPlane=125.878, width=337.198, height=150.146, cameraPosition=(
        46.7744, 5.38679, 94.2809), cameraTarget=(46.7744, 5.38679, 0))
    s.Line(point1=(0.0, -40.0), point2=(20.0, -40.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    s.Line(point1=(20.0, -40.0), point2=(20.0, 20.0))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(20.0, 20.0), point2=(10.0, 50.0))
    s.Line(point1=(10.0, 50.0), point2=(0.0, 50.0))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=77.4504, 
        farPlane=111.111, width=149.617, height=66.6207, cameraPosition=(
        20.7422, 32.8131, 94.2809), cameraTarget=(20.7422, 32.8131, 0))
    s.Line(point1=(0.0, 50.0), point2=(0.0, 55.0))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(0.0, 55.0), point2=(13.75, 55.0))
    s.HorizontalConstraint(entity=g[8], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s.Line(point1=(13.75, 55.0), point2=(25.0, 22.5))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=62.0254, 
        farPlane=126.536, width=330.592, height=147.205, cameraPosition=(
        18.6778, 16.9507, 94.2809), cameraTarget=(18.6778, 16.9507, 0))
    s.Line(point1=(25.0, 22.5), point2=(25.0, -45.0))
    s.VerticalConstraint(entity=g[10], addUndoState=False)
    s.Line(point1=(25.0, -45.0), point2=(0.0, -45.0))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    s.CoincidentConstraint(entity1=v[9], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, -45.0), point2=(0.0, -40.0))
    s.VerticalConstraint(entity=g[12], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
    p = mdb.models['Model-1'].Part(name='tube', dimensionality=AXISYMMETRIC, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['tube']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['tube']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


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
        previous='Initial', maxNumInc=10000, nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='taper-slide')


def create_surfaces():
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
    s1 = a.instances['tube-1'].edges
    side1Edges1 = s1.findAt(((7.5, 50.0, 0.0), ), ((17.5, 27.5, 0.0), ), ((20.0, 
        -25.0, 0.0), ), ((5.0, -40.0, 0.0), ))
    a.Surface(side1Edges=side1Edges1, name='inner-tube')


def make_piston_surfaces():
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
    side1Edges1 = s1.findAt(((15.0, 0.0, 0.0), ), ((20.0, 15.0, 0.0), ), ((5.0, 
        20.0, 0.0), ))
    a.Surface(side1Edges=side1Edges1, name='outer-piston')


def make_interaction():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=95.8412, 
        farPlane=142.184, width=276.584, height=118.01, viewOffsetX=50.6546, 
        viewOffsetY=-8.44681)
    mdb.models['Model-1'].ContactProperty('sliding')
    mdb.models['Model-1'].interactionProperties['sliding'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.05, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['sliding'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.surfaces['inner-tube']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.surfaces['outer-piston']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='piston-tube-contact', 
        createStepName='taper-slide', master=region1, slave=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='sliding', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)


def make_amplitudes():
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
    mdb.models['Model-1'].TabularAmplitude(name='piston-back', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
    mdb.models['Model-1'].TabularAmplitude(name='piston-front', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))


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
    pass


def make_tube_bcs():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['tube-1'].edges
    edges1 = e1.findAt(((18.75, -45.0, 0.0), ), ((3.4375, 55.0, 0.0), ))
    region = a.Set(edges=edges1, name='tube-ends')
    mdb.models['Model-1'].DisplacementBC(name='fix-tube-ends', 
        createStepName='Initial', region=region, u1=UNSET, u2=SET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['tube-1'].edges
    edges1 = e1.findAt(((0.0, -43.75, 0.0), ), ((0.0, 51.25, 0.0), ))
    region = a.Set(edges=edges1, name='tube-centre')
    mdb.models['Model-1'].DisplacementBC(name='fix-tube-centre', 
        createStepName='Initial', region=region, u1=SET, u2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)


def make_piston_bcs():
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
    e1 = a.instances['piston-1'].edges
    edges1 = e1.findAt(((0.0, 5.0, 0.0), ))
    region = a.Set(edges=edges1, name='piston-centre')
    mdb.models['Model-1'].DisplacementBC(name='fix-piston-centre', 
        createStepName='Initial', region=region, u1=SET, u2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='taper-slide')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['piston-1'].edges
    side1Edges1 = s1.findAt(((15.0, 0.0, 0.0), ))
    region = a.Surface(side1Edges=side1Edges1, name='piston-back')
    mdb.models['Model-1'].Pressure(name='piston-back-pressure', 
        createStepName='taper-slide', region=region, distributionType=UNIFORM, 
        field='', magnitude=0.2, amplitude='piston-back')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['piston-1'].edges
    side1Edges1 = s1.findAt(((5.0, 20.0, 0.0), ))
    region = a.Surface(side1Edges=side1Edges1, name='piston-front')
    mdb.models['Model-1'].Pressure(name='piston-front-pressure', 
        createStepName='taper-slide', region=region, distributionType=UNIFORM, 
        field='', magnitude=0.1, amplitude='piston-front')


def make_piston_initial_v():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['piston-1'].faces
    faces1 = f1.findAt(((6.666667, 6.666667, 0.0), ))
    region = a.Set(faces=faces1, name='piston')
    mdb.models['Model-1'].Velocity(name='piston-initial-velocity', region=region, 
        field='', distributionType=MAGNITUDE, velocity1=0.0, velocity2=3000.0, 
        omega=0.0)


def mesh_piston():
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
    p = mdb.models['Model-1'].parts['piston']
    f = p.faces
    pickedRegions = f.findAt(((6.666667, 6.666667, 0.0), ))
    p.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
    p = mdb.models['Model-1'].parts['piston']
    e = p.edges
    pickedEdges1 = e.findAt(((20.0, 15.0, 0.0), ))
    pickedEdges2 = e.findAt(((5.0, 20.0, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, minSize=0.4, maxSize=2.0, constraint=FINER)
    p = mdb.models['Model-1'].parts['piston']
    p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['piston']
    p.generateMesh()


def mesh_piston_2():
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
    p = mdb.models['Model-1'].parts['piston']
    e = p.edges
    pickedEdges1 = e.findAt(((15.0, 0.0, 0.0), ))
    pickedEdges2 = e.findAt(((0.0, 5.0, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, minSize=0.4, maxSize=2.0, constraint=FINER)
    p = mdb.models['Model-1'].parts['piston']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['piston']
    f = p.faces
    faces = f.findAt(((6.666667, 6.666667, 0.0), ))
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))


def mesh_tube():
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
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    pickedRegions = f.findAt(((6.666667, -41.666667, 0.0), ))
    p.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges1 = e.findAt(((17.5, 27.5, 0.0), ), ((25.0, 5.625, 0.0), ))
    pickedEdges2 = e.findAt(((20.0, -25.0, 0.0), ), ((16.5625, 46.875, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, minSize=0.4, maxSize=2.0, constraint=FINER)
    p = mdb.models['Model-1'].parts['tube']
    p.seedPart(size=4.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['tube']
    p.generateMesh()


def mesh_tube_2():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=221.291, 
        farPlane=269.015, width=288.494, height=123.419, viewOffsetX=19.4474, 
        viewOffsetY=-2.58198)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges = e.findAt(((0.0, -43.75, 0.0), ), ((0.0, 51.25, 0.0), ))
    p.seedEdgeBySize(edges=pickedEdges, size=0.5, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    p = mdb.models['Model-1'].parts['tube']
    p.generateMesh()


def mesh_tube_3():
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
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges = e.findAt(((0.0, -43.75, 0.0), ), ((18.75, -45.0, 0.0), ), ((
        3.4375, 55.0, 0.0), ), ((0.0, 51.25, 0.0), ), ((7.5, 50.0, 0.0), ), ((
        5.0, -40.0, 0.0), ))
    p.seedEdgeBySize(edges=pickedEdges, size=1.0, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges = e.findAt(((0.0, -43.75, 0.0), ), ((18.75, -45.0, 0.0), ), ((
        3.4375, 55.0, 0.0), ), ((0.0, 51.25, 0.0), ), ((7.5, 50.0, 0.0), ), ((
        5.0, -40.0, 0.0), ))
    p.seedEdgeBySize(edges=pickedEdges, size=2.0, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    p = mdb.models['Model-1'].parts['tube']
    p.generateMesh()


def mesh_tube_4():
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
    p = mdb.models['Model-1'].parts['tube']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(6.666667, 
        -41.666667, 0.0), normal=(0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
        origin=(17.783958, 2.137002, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=206.15, gridSpacing=5.15, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['tube']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=192.308, 
        farPlane=220.002, width=123.094, height=54.8107, cameraPosition=(
        16.317, -18.8961, 206.155), cameraTarget=(16.317, -18.8961, 0))
    s1.Line(point1=(2.216042, -42.137002), point2=(2.216042, -47.1370019999434))
    s1.VerticalConstraint(entity=g.findAt((2.216042, -44.637002)), 
        addUndoState=False)
    s1.ParallelConstraint(entity1=g.findAt((2.216042, -12.137002)), 
        entity2=g.findAt((2.216042, -44.637002)), addUndoState=False)
    s1.CoincidentConstraint(entity1=v.findAt((2.216042, -47.137002)), 
        entity2=g.findAt((-5.283958, -47.137002)), addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=189.865, 
        farPlane=222.446, width=144.816, height=64.4831, cameraPosition=(
        22.9521, 31.1373, 206.155), cameraTarget=(22.9521, 31.1373, 0))
    s1.Line(point1=(-7.783958, 47.862998), point2=(-4.033958, 52.862998))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.629, 
        farPlane=232.682, width=326.379, height=145.329, cameraPosition=(
        40.3776, 17.7049, 206.155), cameraTarget=(40.3776, 17.7049, 0))
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    pickedFaces = f.findAt(((6.666667, -41.666667, 0.0), ))
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    pickedRegions = f.findAt(((7.916667, 53.333333, 0.0), ), ((13.333333, 
        -41.666667, 0.0), ), ((21.666667, -43.333333, 0.0), ))
    p.setMeshControls(regions=pickedRegions, technique=STRUCTURED)
    p = mdb.models['Model-1'].parts['tube']
    p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    pickedRegions = f.findAt(((21.666667, -43.333333, 0.0), ))
    p.setMeshControls(regions=pickedRegions, technique=FREE)
    p = mdb.models['Model-1'].parts['tube']
    p.generateMesh()


def mesh_tube_5():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=220.364, 
        farPlane=269.942, width=254.034, height=108.677, viewOffsetX=19.9301, 
        viewOffsetY=-4.67083)
    p = mdb.models['Model-1'].parts['tube']
    f1, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f1.findAt(coordinates=(6.666667, 
        -41.666667, 0.0), normal=(0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
        origin=(17.783958, 2.137002, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=206.15, gridSpacing=5.15, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['tube']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.Line(point1=(-7.783958, 47.862998), point2=(-4.033958, 52.862998))
    s.Line(point1=(2.216042, 17.862998), point2=(7.216042, 20.362998))
    s.Line(point1=(2.216042, -42.137002), point2=(2.216042, -47.1370019999434))
    s.VerticalConstraint(entity=g.findAt((2.216042, -44.637002)), 
        addUndoState=False)
    s.ParallelConstraint(entity1=g.findAt((2.216042, -12.137002)), 
        entity2=g.findAt((2.216042, -44.637002)), addUndoState=False)
    s.CoincidentConstraint(entity1=v.findAt((2.216042, -47.137002)), 
        entity2=g.findAt((-5.283958, -47.137002)), addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=231.092, height=102.9, 
        cameraPosition=(13.095, 4.30104, 206.155), cameraTarget=(13.095, 
        4.30104, 0))
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    pickedFaces = f.findAt(((6.666667, -41.666667, 0.0), ))
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges1 = e.findAt(((21.25, 20.625, 0.0), ), ((10.9375, 51.25, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=0.4, 
        maxSize=2.0, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=233.781, 
        farPlane=256.525, width=101.642, height=43.4829, viewOffsetX=13.8627, 
        viewOffsetY=8.97882)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges1 = e.findAt(((21.25, 20.625, 0.0), ), ((10.9375, 51.25, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=0.4, 
        maxSize=1.0, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=227.727, 
        farPlane=262.579, width=185.212, height=79.2346, viewOffsetX=20.374, 
        viewOffsetY=5.82631)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges = e.findAt(((17.5, 27.5, 0.0), ))
    p.seedEdgeBySize(edges=pickedEdges, size=0.4, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=226.072, 
        farPlane=264.234, width=195.355, height=83.5738, viewOffsetX=25.8987, 
        viewOffsetY=-5.38858)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges2 = e.findAt(((20.0, -25.0, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end2Edges=pickedEdges2, minSize=0.4, 
        maxSize=4.0, constraint=FINER)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges1 = e.findAt(((20.0, -41.25, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=1.0, 
        maxSize=4.0, constraint=FINER)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges1 = e.findAt(((25.0, 5.625, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=0.4, 
        maxSize=1.0, constraint=FINER)
    p = mdb.models['Model-1'].parts['tube']
    e = p.edges
    pickedEdges1 = e.findAt(((25.0, 5.625, 0.0), ))
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=0.4, 
        maxSize=4.0, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=222.958, 
        farPlane=267.348, width=235.799, height=100.876, viewOffsetX=26.4704, 
        viewOffsetY=-1.12872)
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    pickedRegions = f.findAt(((13.333333, -41.666667, 0.0), ), ((7.916667, 
        53.333333, 0.0), ), ((21.666667, 0.833333, 0.0), ), ((18.333333, 
        30.833333, 0.0), ))
    p.setMeshControls(regions=pickedRegions, technique=SWEEP)
    p = mdb.models['Model-1'].parts['tube']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['tube']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    pickedRegions = f.findAt(((13.333333, -41.666667, 0.0), ), ((7.916667, 
        53.333333, 0.0), ), ((21.666667, 0.833333, 0.0), ), ((18.333333, 
        30.833333, 0.0), ))
    p.setMeshControls(regions=pickedRegions, technique=FREE)
    p = mdb.models['Model-1'].parts['tube']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    faces = f.findAt(((13.333333, -41.666667, 0.0), ), ((7.916667, 53.333333, 0.0), 
        ), ((21.666667, 0.833333, 0.0), ), ((18.333333, 30.833333, 0.0), ))
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))


def make_abs_material():
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
    mdb.models['Model-1'].Material(name='ABS')
    mdb.models['Model-1'].materials['ABS'].Elastic(table=((2200.0, 0.35), ))
    mdb.models['Model-1'].materials['ABS'].Plastic(table=((48.2633, 0.0), (48.2633, 
        1.0)))
    mdb.models['Model-1'].materials['ABS'].Density(table=((1.05e-09, ), ))


def make_steel():
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
    mdb.models['Model-1'].Material(name='steel')
    mdb.models['Model-1'].materials['steel'].Elastic(table=((200000.0, 0.3), ))
    mdb.models['Model-1'].materials['steel'].Density(table=((8e-09, ), ))


def assign_tube_material():
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
    mdb.models['Model-1'].HomogeneousSolidSection(name='tube', material='steel', 
        thickness=None)
    p = mdb.models['Model-1'].parts['tube']
    f = p.faces
    faces = f.findAt(((13.333333, -41.666667, 0.0), ), ((7.916667, 53.333333, 0.0), 
        ), ((21.666667, 0.833333, 0.0), ), ((18.333333, 30.833333, 0.0), ))
    region = p.Set(faces=faces, name='tube')
    p = mdb.models['Model-1'].parts['tube']
    p.SectionAssignment(region=region, sectionName='tube', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def assign_piston_material():
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
    p = mdb.models['Model-1'].parts['piston']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models['Model-1'].HomogeneousSolidSection(name='piston', material='ABS', 
        thickness=None)
    p = mdb.models['Model-1'].parts['piston']
    f = p.faces
    faces = f.findAt(((6.666667, 6.666667, 0.0), ))
    region = p.Set(faces=faces, name='piston')
    p = mdb.models['Model-1'].parts['piston']
    p.SectionAssignment(region=region, sectionName='piston', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


