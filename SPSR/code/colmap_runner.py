import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--path', required=True, help='Path to the folder containing the images')
parser.add_argument('--project_name', required=True, help='Name of Project folder')
args=parser.parse_args()

if os.path.exists(args.project_name):
    os.system('rm -rf '+args.project_name)


os.system('mkdir '+args.project_name)
os.system('mkdir '+args.project_name+'/images')

os.system('cp -r ' + args.path + '/* ' + args.project_name + '/images')


# sdcs
os.system('colmap automatic_reconstructor --workspace_path '+args.project_name +' --image_path '+args.project_name+'/images')

