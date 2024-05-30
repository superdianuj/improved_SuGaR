import imageio.v2 as imageio
import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='2d_g/results', help='directory of images')
args=parser.parse_args()

# The directory containing your .jpg files
dir = args.dir

try:
    file_names = sorted(os.listdir(dir), key=lambda x: int(x.split('_')[-2]) if '_' in x else int(x.split('.')[0]))
except:
    file_names = sorted(os.listdir(dir), key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))

# Full paths of the files
images_path = [os.path.join(dir, file_name) for file_name in file_names if file_name.endswith('.JPG') or file_name.endswith('.png') or file_name.endswith('.jpg')]

# Create a GIF
with imageio.get_writer(args.dir+'.gif', mode='I', duration=0.5) as writer:
    for filename in images_path:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF created successfully!")
