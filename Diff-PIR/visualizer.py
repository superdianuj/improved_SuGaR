import imageio
import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='2d_g/results', help='directory of images')
args=parser.parse_args()

# The directory containing your .jpg files
directory = args.dir
# Sort files by numeric order

file_names = os.listdir(directory)


# Full paths of the files
images_path = [os.path.join(directory, file_name) for file_name in file_names if file_name.endswith('.png')]

# Create a GIF
with imageio.get_writer(args.dir+'_gif.gif', mode='I', duration=0.5) as writer:
    for filename in images_path:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF created successfully!")
