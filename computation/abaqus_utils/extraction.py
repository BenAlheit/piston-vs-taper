import pandas as pd
import os


def extract_uniaxial(directory, job, csv_name='uniaxial-tension-data.csv', clean=True):
    os.system(f'abaqus cae noGUI=extract_uniaxial_data_macro.py -- {csv_name} {directory} {job}')
    aba_data = pd.read_csv(f'{directory}/{csv_name}')
    if clean:
        os.system(f'rm {directory}/{csv_name}')
    return aba_data

