from abaqus import *
from abaqusConstants import *
import __main__
import numpy as np
# import read_odb_utils
import os
import subprocess
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
import sys
import time
import os

csv_name = sys.argv[-3]
out_dir = sys.argv[-2]
job = sys.argv[-1]
# print >> sys.__stdout__, os.getcwd()
os.chdir(out_dir)


def string_map(a_list):
    return map(lambda x: str(x), a_list)


def extract_cap_data():
    o = session.openOdb(name=job + '.odb', readOnly=False)
    step = o.steps.keys()[0]
    force = np.array(o.steps[step].historyRegions['NodeSet . Z000002'].historyOutputs[
        'CFT2     ASSEMBLY_CAP-1_TRANSITION-AND-PUMP-CONTACT/ASSEMBLY_TRANSITION-PIECE-1_END-CONTACT'].data)
    t = force[:, 0]
    force = force[:, 1]
    pd = np.array(o.steps[step].historyRegions['Assembly ASSEMBLY'].historyOutputs['ALLPD'].data)[:, 1]
    xt = np.array(o.steps[step].historyRegions['Node CAP-1.7'].historyOutputs['U2'].data)[:, 1]

    data = 'time (s),force (N),x_t (mm),plastic dissipation (mJ)\n'
    data += '\n'.join(string_map(np.array([t, force, xt, pd]).T.tolist())).replace('[', '').replace(']', '')
    open(csv_name, 'w+').write(data)
    # print >> sys.__stdout__, data


extract_cap_data()

# o = session.openOdb(name=job + '.odb', readOnly=False)
# step = o.steps.keys()[0]
# print >> sys.__stdout__, 'Force'
# print >> sys.__stdout__, o.steps[step].historyRegions['NodeSet . Z000002'].historyOutputs['CFT2     ASSEMBLY_CAP-1_TRANSITION-AND-PUMP-CONTACT/ASSEMBLY_TRANSITION-PIECE-1_END-CONTACT'].data
# print >> sys.__stdout__, 'x_t'
# print >> sys.__stdout__, o.steps[step].historyRegions['Node CAP-1.7'].historyOutputs['U2'].data
# print >> sys.__stdout__, 'PD'
# pd = np.array(o.steps[step].historyRegions['Assembly ASSEMBLY'].historyOutputs['ALLPD'].data)[:, 1]
# # print >> sys.__stdout__, o.steps[step].historyRegions['Assembly ASSEMBLY'].historyOutputs['ALLPD'].data
# print >> sys.__stdout__, pd


