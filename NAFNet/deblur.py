import torch
import gdown
from basicsr.models import create_model
from basicsr.utils import img2tensor as _img2tensor, tensor2img, imwrite
from basicsr.utils.options import parse
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import argparse
import imageio


def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img



def img2tensor(img, bgr2rgb=False, float32=True):
    img = img.astype(np.float32) / 255.
    return _img2tensor(img, bgr2rgb=bgr2rgb, float32=float32)



def display(img1, img2):
  fig = plt.figure(figsize=(25, 10))
  ax1 = fig.add_subplot(1, 2, 1) 
  plt.title('Input image', fontsize=16)
  ax1.axis('off')
  ax2 = fig.add_subplot(1, 2, 2)
  plt.title('NAFNet output', fontsize=16)
  ax2.axis('off')
  ax1.imshow(img1)
  ax2.imshow(img2)



def single_image_inference(model, img, save_path):
      model.feed_data(data={'lq': img.unsqueeze(dim=0)})

      if model.opt['val'].get('grids', False):
          model.grids()

      model.test()

      if model.opt['val'].get('grids', False):
          model.grids_inverse()

      visuals = model.get_current_visuals()
      sr_img = tensor2img([visuals['result']])
      imwrite(sr_img, save_path)



def gifer(out_directory, gif_name, fps=2):
    if os.path.exists(gif_name+'.gif'):
        os.system("rm -rf "+gif_name+".gif")

    images = [img for img in os.listdir(out_directory) if img.endswith(".png") or img.endswith(".jpg") or img.endswith(".JPG") or img.endswith(".jpeg")]
    # Sort images by their integer values
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))

    # Get the full path of each image
    images = [os.path.join(out_directory, img) for img in images]

    gif = []
    for image in images:
        gif.append(imageio.imread(image))

    imageio.mimsave(gif_name, gif, fps=fps)

    print("\nGif is created successfully!\n")




def main(args):
    if not os.path.exists('./experiments/pretrained_models/NAFNet-REDS-width64.pth'):
        gdown.download('https://drive.google.com/uc?id=14D4V4raNYIOhETfcuuLI3bGLB-OYIv6X', "./experiments/pretrained_models/", quiet=False)
    opt_path = 'options/test/REDS/NAFNet-width64.yml'
    opt = parse(opt_path, is_train=False)
    opt['dist'] = False
    NAFNet = create_model(opt)
    dir = args.dir
    out_dir='output_deblur'
    ref_dir='input_blurry'
    IMG_SIZE = args.im_size
    file_names = sorted(os.listdir(dir), key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))

    # Full paths of the files
    images_path = [os.path.join(dir, file_name) for file_name in file_names if file_name.endswith(('.JPG', '.png', '.jpg'))]

    if os.path.exists(out_dir):
        os.system(f'rm -rf {out_dir}')
    os.makedirs(out_dir, exist_ok=True)

    if os.path.exists(ref_dir):
        os.system(f'rm -rf {ref_dir}')
    os.makedirs(ref_dir, exist_ok=True)
    counter=0

    for img_path in images_path:
        image = cv2.imread(img_path)
        if IMG_SIZE!=None:
            image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
        cv2.imwrite(os.path.join(ref_dir, str(counter)+'.jpg'), image)
        inp = img2tensor(image)
        output_path = os.path.join(out_dir, str(counter)+'.jpg')
        single_image_inference(NAFNet, inp, output_path)
        counter+=1


    file_names = sorted(os.listdir(out_dir), key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))

    # Full paths of the files
    images_path = [os.path.join(out_dir, file_name) for file_name in file_names if file_name.endswith(('.jpg'))]

    for path in images_path:
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(path, img)

    gifer(out_dir, 'deblurred_images.gif', fps=2)
    gifer(ref_dir, 'blurry_images.gif', fps=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deblur images')
    parser.add_argument('--dir', type=str, help='Path to the directory containing images')
    parser.add_argument('--im_size', type=int, default=None, help='Size of the image')
    args = parser.parse_args()
    main(args)


