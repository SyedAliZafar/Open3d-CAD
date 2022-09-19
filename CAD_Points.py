
import open3d as o3d
import numpy as np
import open3d


def draw_geometries_pick_points(geometries):
    vis = open3d.visualization.VisualizerWithEditing()
    vis.create_window()
    for geometry in geometries:
        vis.add_geometry(geometry)
        vis.run()
    vis.destroy_window()
    
    
    
    
mesh = o3d.io.read_triangle_mesh("FW75735_jt.ply")
mesh.compute_vertex_normals()
draw_geometries_pick_points(mesh)