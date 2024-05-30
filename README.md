# Improved SuGaR
This project is intended to improve results of SuGaR (both rendering and mesh reconstruction) from the perspective of improving quality of images that is fed into COLMAP, and then GS.
In this course, I employ deblurring, followed by super resolution to improve quality of images that are fodder to a rather complicated scheme. 
The great thing about this is that it leads to obvious rooms for novelties, but I am not here for publications, am I? But only I can exploit the most fruitful novelties.

# Strategy-1: Deblurring (DiffPIR) + Super Resolution (SPSR):
```bash
git clone --recursive https://github.com/superdianuj/improved_SuGaR.git
cd improved_SuGaR
# drop a folder of images in current directory
python runnerizer_diffpir_spsr_sugar.py --dir <name of the folder of images> --choice <'Gaussian' or 'motion'> --sugar_choice <"density or "sdf">
```

# Strategy-2: Deblurring (NAFNet) + Super Resolution (SPSR):
```bash
git clone --recursive https://github.com/superdianuj/improved_SuGaR.git
cd improved_SuGaR
# drop a folder of images in current directory
python runnerizer_nafnet_spsr_sugar.py --dir <name of the folder of images> --resize_imgs <resize images to some dimensions (a x a)> --sugar_choice <"density or "sdf">
```

**Visualize Gaussian Splat**: https://playcanvas.com/supersplat/editor/

**Visualize Mesh**: https://poly.cam/tools/gaussian-splatting or Meshlab


# Observation: Preprocessing on already good enough images leads to bad results

![Untitled](https://github.com/superdianuj/improved_SuGaR/assets/47445756/9bd9198d-952f-4043-a214-a02bfff85137)

Another thing to note is that NAFNet works much better than Diffusion based approach for faithful debluring.


# Observation: Preprocessing on bad images lead to good results

## Gaussian Rendering


![Preprocessing Gaussian Splatting_show5 (1)](https://github.com/superdianuj/improved_SuGaR/assets/47445756/a7303b39-29c1-497d-a350-a631985e4f62)


## Mesh Reconstruction

![Preprocessing Gaussian Splatting_show5](https://github.com/superdianuj/improved_SuGaR/assets/47445756/6cc6e7dd-b12f-4c6c-827f-3c6ab617e688)



# References
https://github.com/Anttwo/SuGaR?tab=readme-ov-file

https://github.com/megvii-research/NAFNet

https://github.com/yuanzhi-zhu/DiffPIR

https://github.com/Maclory/SPSR




