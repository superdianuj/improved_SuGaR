# Improved SuGaR
This project is intended to improve results of SuGaR (both rendering and mesh reconstruction) from the perspective of improving quality of images that is fed into COLMAP, and then GS.
In this course, I employ deblurring, followed by super resolution to improve quality of images that are fodder to a rather complicated scheme. 
The great thing about this is that it leads to obvious rooms for novelties, but I am not here for publications, am I? But only I can exploit the most fruitful novelties.

# Strategy-1: Deblurring (DiffPIR) + Super Resolution (SPSR):
```bash
git clone --recurse-submodules https://github.com/superdianuj/improved_SuGaR.git
cd improved_SuGaR
# drop a folder of images in current directory
python runnerizer_diffpir_spsr_sugar.py --dir <name of the folder of images> --choice <'Gaussian' or 'motion'> --sugar_choice <"density or "sdf">

# SuGaR results are in 'results' folder
```

# Strategy-2: Deblurring (NAFNet) + Super Resolution (SPSR):
```bash
git clone --recurse-submodules https://github.com/superdianuj/improved_SuGaR.git
cd improved_SuGaR
# drop a folder of images in current directory
python runnerizer_nafnet_spsr_sugar.py --dir <name of the folder of images> --resize_imgs <resize images to some dimensions (a x a)> --sugar_choice <"density or "sdf">

# SuGaR results are in 'results' folder
```

**Visualize Gaussian Splat**: https://playcanvas.com/supersplat/editor/

**Visualize Mesh**: https://poly.cam/tools/gaussian-splatting or Meshlab


# Observation-1: Preprocessing on already good enough images leads to bad results

![Untitled](https://github.com/superdianuj/improved_SuGaR/assets/47445756/150cbe12-344f-4fc3-8b00-38f6a9b4d667)


Another thing to note is that NAFNet works much better than Diffusion based approach for faithful debluring.


# Observation-2: Preprocessing on bad images lead to good results

## Gaussian Rendering
![Preprocessing Gaussian Splatting_show5 (1)](https://github.com/superdianuj/improved_SuGaR/assets/47445756/6f7ed96a-4745-4fc0-b619-1faeded2ce4b)




## Mesh Reconstruction
![Preprocessing Gaussian Splatting_show5](https://github.com/superdianuj/improved_SuGaR/assets/47445756/b565da27-70c3-4b59-ac88-79842c9695fe)



# References
https://github.com/Anttwo/SuGaR?tab=readme-ov-file

https://github.com/megvii-research/NAFNet

https://github.com/yuanzhi-zhu/DiffPIR

https://github.com/Maclory/SPSR




