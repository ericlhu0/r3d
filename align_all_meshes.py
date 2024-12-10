import numpy as np
import trimesh
import os
import align_meshes

# read in the reference mesh of the mug
ref_mesh_path = "/Users/eric/Music/r3d/robosuite/robosuite/models/assets/objects/meshes/mug"

gen_folder_path = "/Users/eric/Music/r3d/robosuite/robosuite/models/assets/objects/meshes/demo_objects/"
output_folder_path = "/Users/eric/Music/r3d/robosuite/robosuite/models/assets/objects/meshes/aligned_demo_objects/"

obj_file_paths = []

obj_files_no_ext = [
    os.path.splitext(f)[0]
    for f in os.listdir(gen_folder_path)
    if f.lower().endswith('.obj')
]

for file in obj_files_no_ext:
  file_path = os.path.join(gen_folder_path, file)
  output_path = os.path.join(output_folder_path, file)
  obj_file_paths.append((file_path, output_path))

aligned_meshes = []

for file, output_path in obj_file_paths:
  align_meshes.rotate_meshes(ref_mesh_path, file, output_path)
