import os
import cv2

main_dir='results'
sub_dir=os.listdir(main_dir)[0]
dirr=os.path.join(main_dir,sub_dir)

new_dir='deblurred_results'

if os.path.exists(new_dir):
    os.system(f'rm -rf {new_dir}')

os.system(f'mkdir {new_dir}')

img_paths=[img for img in os.listdir(dirr) if img.endswith('_diffusion_ffhq_10m.png')]

corr_img_paths=[os.path.join(dirr,img_path) for img_path in img_paths]
counter=0
for pth in corr_img_paths:
    img=cv2.imread(pth)
    new_pth=os.path.join(new_dir,str(counter)+'.png')  
    cv2.imwrite(new_pth,img)
    counter+=1


