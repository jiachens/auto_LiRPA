'''
Description: 
Autor: Jiachen Sun
Date: 2022-01-27 17:35:15
LastEditors: Jiachen Sun
LastEditTime: 2022-01-28 17:52:51
'''
import numpy as np
import sys
import os

MODEL = ['resnet18']
COR_H = ['gaussian_noise', 'shot_noise', 'impulse_noise', 'pixelate', 'jpeg_compression']
COR_M = [ 'defocus_blur', 'frosted_glass_blur', 'motion_blur', 'zoom_blur', 'elastic']
COR_L = ['contrast','fog','snow','frost','brightness']
SEV = ['1','2','3','4','5']

def calculate(corruptions,dir):
    total_error = 0
    for cor in corruptions:
        for sev in SEV:
            file_name = cor + '_' + sev + '.out'
            output = os.path.join(dir,file_name)
            f = open(output,'r')
            # print(f.readlines()[-1])
            error = f.readlines()[-1].split(' ')[-2].split('=')[-1].strip(',')
            # print(error)
            error = float(error)
            total_error += error
    return total_error / (len(corruptions) * len(SEV))
            
        

def process(data_dir='./output'):
    for model in MODEL:
        print("evaluating " + model + " ......")
        _dir = os.path.join(data_dir, model)
        print("High Frequency Error :" )
        print(calculate(COR_H,_dir))
        print("Mid Frequency Error :" )
        print(calculate(COR_M,_dir))
        print("Low Frequency Error :" )
        print(calculate(COR_L,_dir))

    

if __name__ == '__main__':
    process()