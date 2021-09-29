import pandas as pd
import os

file_path = os.path.realpath(__file__)
if '/' in file_path:
    utils_dir = '/'.join(file_path.split('/')[:-1])
else:
    utils_dir = '\\'.join(file_path.split(r'\\')[:-1])


def extract_uniaxial(directory, job, csv_name='uniaxial-tension-data.csv', clean=True):
    os.system(f'abaqus cae noGUI={utils_dir}/extract_uniaxial_data_macro.py -- {csv_name} {directory} {job}')
    aba_data = pd.read_csv(f'{directory}/{csv_name}')
    if clean:
        os.system(f'rm {directory}/{csv_name}')
    return aba_data

