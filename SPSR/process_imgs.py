import os
import cv2

dir='results/SPSR/pred'

file_names = os.listdir(dir)

# Full paths of the files
images_path = [os.path.join(dir, file_name) for file_name in file_names if file_name.endswith('.JPG') or file_name.endswith('.png') or file_name.endswith('.jpg')]

if os.path.exists('processed_results'):
    os.system('rm -r processed_results')

os.mkdir('processed_results')

counter=0

for filename in images_path:
    img=cv2.imread(filename)
    cv2.imwrite('processed_results/processed_'+str(counter)+'.jpg',img)
    counter+=1

