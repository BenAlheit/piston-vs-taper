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


def extract_uniaxial_data():
    o = session.openOdb(name=job + '.odb', readOnly=False)
    step = o.steps.keys()[0]
    n_frames = len(o.steps[step].frames)
    s = np.zeros(n_frames)
    eps = np.zeros(n_frames)
    t = np.zeros(n_frames)
    for i_frame in range(n_frames):
        s[i_frame] = o.steps[step].frames[i_frame].fieldOutputs['S'].bulkDataBlocks[0].data.transpose()[0,:].mean()
        # eps[i_frame] = np.exp(o.steps[step].frames[i_frame].fieldOutputs['LE'].bulkDataBlocks[0].material_data.transpose()[0,:].mean())-1
        eps[i_frame] = o.steps[step].frames[i_frame].fieldOutputs['LE'].bulkDataBlocks[0].data.transpose()[0,:].mean()
        t[i_frame] = o.steps[step].frames[i_frame].frameValue

    data = 'time (s),strain (mm/mm),stress (MPa)\n'
    data += '\n'.join(string_map(np.array([t, eps, s]).T.tolist())).replace('[', '').replace(']', '')
    open(csv_name, 'w+').write(data)
    # print >> sys.__stdout__, material_data


extract_uniaxial_data()

