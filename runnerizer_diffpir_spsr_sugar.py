import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--dir',required=True,type=str)
parser.add_argument('--choice',default='Gaussian',type=str,help='Deblurring Gaussian blur or motion blur',choices=['Gaussian','motion'])
parser.add_argument('--sugar_choice',default="density",type=str,help='SuGaR regularization type',choices=["density","sdf"])

args=parser.parse_args()


os.system(f'cp -r {args.dir} Diff-PIR')
os.system(f'cd Diff-PIR')
os.system(f'chmod +x runner.sh')
os.system(f'./runner.sh {args.dir} {args.choice}')
os.system(f'cd ..')


if os.path.exists('SPSR/code/dataset'):
    os.system('rm -r SPSR/code/dataset')

os.system('mkdir SPSR/code/dataset')
os.system('mkdir SPSR/code/dataset/LR')
os.system('mkdir SPSR/code/dataset/HR')
os.system('cp -r Diff-PIR/deblurred_results/* SPSR/data/dataset/LR')
os.system('cp -r Diff-PIR/original_images/* SPSR/data/dataset/HR')
os.system('cd SPSR')
os.system('chmod +x runner.sh')
os.system('./runner.sh')
os.system('cd ..')


os.system('mkdir SuGaR/dataset')
os.system('cp -r SPSR/results/SPSR/processed_results SuGaR/dataset')
os.system('mv SuGaR/dataset/processed_results SuGaR/dataset/input')
os.system('cd SuGaR')   
if os.path.exists('output'):
    os.system('rm -r output')
os.system('python gaussian_splatting/convert.py -s dataset')
os.system('python gaussian_splatting/train.py -s dataset -m out_gaussian --iterations 8000')
os.system(f'python train.py -s dataset -c out_gaussian/ -r {args.sugar_choice}')
os.system('cd ..')


if os.path.exists('results'):
    os.system('rm -r results')
os.system('mkdir results')
os.system('mkdir results/Gaussian_render')
os.system('mkdir results/Gaussian_mesh')
os.system('cp -r SuGaR/out_gaussian/point_cloud/iteration_8000/point_cloud.ply results/Gaussian_render')
if os.path.exists('SuGaR/output/refined_mesh/dataset'):
    os.system('cp -r SuGaR/output/refined_mesh/dataset/* results/Gaussian_mesh')
else:
    print('\n\n******SuGaR mesh reconstruction failed!!************\n\n')


