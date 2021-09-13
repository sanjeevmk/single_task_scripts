from Escher.tools import apply_decimation_filter
from Escher.Geometry import Mesh
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("high_res_mesh_path",help="Path to High resolutiom mesh")
parser.add_argument("low_res_mesh_path",help="Path to Corrsponding Low resolutiom mesh")
parser.add_argument("dfaust_directory",help="Directory where the subject ids subfolders are stored")
parser.add_argument("output_directory",help="Output root directory where the new subfolders will be created with low-res outputs")

args = parser.parse_args()

_dfaust_subdirs = [d for d in os.listdir(args.dfaust_directory) if d.startswith("500")]

for subdir_index,dfaust_subdir in enumerate(_dfaust_subdirs):
    print(subdir_index,len(_dfaust_subdirs))
    obj_names = [x for x in os.listdir(os.path.join(args.dfaust_directory,dfaust_subdir)) if x.endswith('.obj')]
    sequence_paths = [os.path.join(args.dfaust_directory,dfaust_subdir,obj_name) for obj_name in obj_names]

    high_res_mesh = Mesh(mesh_path=args.high_res_mesh_path)
    high_res_mesh.load()
    low_res_mesh = Mesh(mesh_path=args.low_res_mesh_path)
    low_res_mesh.load()

    target_high_res_meshes = []
    for path in sequence_paths:
        _mesh = Mesh(mesh_path=path)
        _mesh.load()
        target_high_res_meshes.append(_mesh)

    low_res_meshes = apply_decimation_filter(high_res_mesh=high_res_mesh,low_res_mesh=low_res_mesh,
                                                target_high_res_meshes=target_high_res_meshes)

    if low_res_meshes:
        if not os.path.exists(os.path.join(args.output_directory,dfaust_subdir)):
            os.makedirs(os.path.join(args.output_directory,dfaust_subdir))

    for i,_low_mesh in enumerate(low_res_meshes):
        output_path = os.path.join(args.output_directory,dfaust_subdir,obj_names[i])
        _low_mesh.export(output_path)