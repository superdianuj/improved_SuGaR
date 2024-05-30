import open3d as o3d
import numpy as np
import imageio
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True, help='Path to the Colmap project folder')
args = parser.parse_args()

# Load the mesh from a .ply file
mesh = o3d.io.read_triangle_mesh(args.path+"/dense/0/meshed-poisson.ply")

# Load the point cloud from a .ply file
pcd = o3d.io.read_point_cloud(args.path+"/dense/0/fused.ply")

# Create visualizers for mesh and point cloud
vis_mesh = o3d.visualization.Visualizer()
vis_mesh.create_window(visible=False)
vis_mesh.add_geometry(mesh)

vis_pcd = o3d.visualization.Visualizer()
vis_pcd.create_window(visible=False)
vis_pcd.add_geometry(pcd)

# Set the camera parameters for both visualizers
ctr_mesh = vis_mesh.get_view_control()
ctr_mesh.set_zoom(0.8)
ctr_mesh.set_lookat([0, 0, 0])
ctr_mesh.set_up([0, 1, 0])

ctr_pcd = vis_pcd.get_view_control()
ctr_pcd.set_zoom(0.8)
ctr_pcd.set_lookat([0, 0, 0])
ctr_pcd.set_up([0, 1, 0])

# Initialize the video writer
writer = imageio.get_writer(args.path+'_video.mp4', fps=30)

# Rotate and capture frames for mesh and point cloud
for i in range(360):
    ctr_mesh.rotate(10.0, 0.0)
    vis_mesh.poll_events()
    vis_mesh.update_renderer()
    image_mesh = vis_mesh.capture_screen_float_buffer(False)
    image_mesh = np.asarray(image_mesh) * 255
    image_mesh = image_mesh.astype(np.uint8)

    ctr_pcd.rotate(10.0, 0.0)
    vis_pcd.poll_events()
    vis_pcd.update_renderer()
    image_pcd = vis_pcd.capture_screen_float_buffer(False)
    image_pcd = np.asarray(image_pcd) * 255
    image_pcd = image_pcd.astype(np.uint8)

    # Add titles to the frames
    cv2.putText(image_pcd, "Point Cloud", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,9,0), 2)
    cv2.putText(image_mesh, "Mesh", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,9,0), 2)

    # Combine the mesh and point cloud views horizontally
    combined_image = cv2.hconcat([image_pcd, image_mesh])
    writer.append_data(combined_image)

# Close the video writer and windows
writer.close()
vis_mesh.destroy_window()
vis_pcd.destroy_window()