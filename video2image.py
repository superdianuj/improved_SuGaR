import os
import cv2
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--dir',required=True,type=str)
parser.add_argument('--save_freq',type=int, default=10)
args=parser.parse_args()

if os.path.exists('images'):
    os.system('rm -rf images')

os.system('mkdir images')

cap=cv2.VideoCapture(args.dir)

if not cap.isOpened():
    print("This stupid video file aint legit")
    exit()

total_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

save_freq=args.save_freq

frame_index=0
save_frame_count=0

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break

    if frame_index%save_freq==0:
        frame_filename='images/img_'+str(save_frame_count)+'.jpg'
        cv2.imwrite(frame_filename,frame)
        save_frame_count+=1

    frame_index+=1


cap.release()

print(f'Extracted {save_frame_count}/{frame_index} frames as images from video file')
