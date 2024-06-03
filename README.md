# Improved SuGaR
This project is intended to improve results of SuGaR (both rendering and mesh reconstruction) from the perspective of improving quality of images that is fed into COLMAP, and then GS.
In this course, I employ deblurring, followed by super resolution to improve quality of images that are fodder to a rather complicated scheme. 
The great thing about this is that it leads to obvious rooms for novelties, but I am not here for publications, am I? But only I can exploit the most fruitful novelties.

# Strategy-1: Deblurring (DiffPIR) + Super Resolution (SPSR):
```bash
git clone --recurse-submodules https://github.com/superdianuj/improved_SuGaR.git
cd improved_SuGaR

# install requirements within each individual folders by visting them and checking out respective README.md

# drop a folder of images in current directory

python runnerizer_diffpir_spsr_sugar.py --dir <name of the folder of images> --choice <'Gaussian' or 'motion'> --sugar_choice <"density or "sdf">

# SuGaR results are in 'results' folder
```

# Strategy-2: Deblurring (NAFNet) + Super Resolution (SPSR):
```bash
git clone --recurse-submodules https://github.com/superdianuj/improved_SuGaR.git
cd improved_SuGaR

# install requirements within each individual folders by visting them and checking out respective README.md

# drop a folder of images in current directory

python runnerizer_nafnet_spsr_sugar.py --dir <name of the folder of images> --resize_imgs <resize images to some dimensions (a x a)> --sugar_choice <"density or "sdf">

# SuGaR results are in 'results' folder
```

**Visualize Gaussian Splat**: https://playcanvas.com/supersplat/editor/

**Visualize Mesh**: https://poly.cam/tools/gaussian-splatting or Meshlab


# Observations
## Observation-1: Preprocessing on already good enough images leads to bad results

![Untitled](https://github.com/superdianuj/improved_SuGaR/assets/47445756/150cbe12-344f-4fc3-8b00-38f6a9b4d667)


Another thing to note is that NAFNet works much better than Diffusion based approach for faithful debluring.


## Observation-2: Preprocessing on bad images lead to good results

### Gaussian Rendering
![Preprocessing Gaussian Splatting_show5 (1)](https://github.com/superdianuj/improved_SuGaR/assets/47445756/6f7ed96a-4745-4fc0-b619-1faeded2ce4b)




### Mesh Reconstruction
![Preprocessing Gaussian Splatting_show5](https://github.com/superdianuj/improved_SuGaR/assets/47445756/b565da27-70c3-4b59-ac88-79842c9695fe)


## Observation-3: Decreasing resolution of blurry training images significantly negatively impacts the performance of gaussian splatting


![image](https://github.com/superdianuj/improved_SuGaR/assets/47445756/dfd09030-18e2-4068-beb3-839b0a14451a)


## Observation-4: Decreasing resolution of clean training images (with blurriness artifacts) negatively impacts the performance of gaussian splatting

![image](https://github.com/superdianuj/improved_SuGaR/assets/47445756/328fa673-1540-489f-87ac-3a6b2df56e2e)


## Observation-5: Taking Compliment of Observation-3 and 4 via SR and Deblurring Models leads to Improved Splatting Reconstruction

![image](https://github.com/superdianuj/improved_SuGaR/assets/47445756/61453c4d-1b90-46ca-8d9b-e284fee31289)

![image](https://github.com/superdianuj/improved_SuGaR/assets/47445756/02a9537c-18ab-4064-b75b-1b1b4a4aad1f)





# References
https://github.com/Anttwo/SuGaR?tab=readme-ov-file

https://github.com/megvii-research/NAFNet

https://github.com/yuanzhi-zhu/DiffPIR

https://github.com/Maclory/SPSR




