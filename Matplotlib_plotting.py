#!/usr/bin/env python
# coding: utf-8

# In[5]:


import open3d
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# In[2]:


import open3d as o3d

if __name__ == "__main__":
    knot_data = o3d.data.KnotMesh()
    #print(f"Reading mesh from file: knot.ply stored at {knot_data.path}")
    mesh = o3d.io.read_triangle_mesh("KnotMesh.ply")
    print(mesh)
    print("Saving mesh to file: copy_of_knot.ply")
    #o3d.io.write_triangle_mesh("copy_of_knot.ply", mesh)
    vis = open3d.visualization.VisualizerWithEditing()
    vis.create_window()
    vis.add_geometry(mesh)
    vis.run()
    vis.destroy_window()
    print(vis.get_picked_points()) #[84, 119, 69]


# In[3]:


# 
import open3d
import open3d as o3d 
import numpy as np 

xyz = o3d.io.read_point_cloud("FW75735_jt.ply")

vis = open3d.visualization.VisualizerWithEditing()
vis.create_window()
vis.add_geometry(xyz,reset_bounding_box=True)
vis.run()
# Picked point #84 (-0.00, 0.01, 0.01) to add in queue.
# Picked point #119 (0.00, 0.00, -0.00) to add in queue.
# Picked point #69 (-0.01, 0.02, 0.01) to add in queue.
vis.destroy_window()
print(vis.get_picked_points()) #[84, 119, 69]


# In[4]:


cloud=xyz


# In[6]:


mesh = o3d.io.read_triangle_mesh("FW75735_jt.ply")
if mesh.is_empty(): exit()


# In[7]:


if not mesh.has_vertex_normals(): mesh.compute_vertex_normals()
if not mesh.has_triangle_normals(): mesh.compute_triangle_normals()


# In[8]:


triangles = np.asarray(mesh.triangles)
vertices = np.asarray(mesh.vertices)
colors = None
if mesh.has_triangle_normals():
    colors = (0.5, 0.5, 0.5) + np.asarray(mesh.triangle_normals) * 0.5
    colors = tuple(map(tuple, colors))
else:
    colors = (1.0, 0.0, 0.0)


# In[9]:


import plotly.graph_objects as go


# In[10]:


fig = go.Figure(
    data=[
        go.Mesh3d(
            x=vertices[:,0],
            y=vertices[:,1],
            z=vertices[:,2],
            i=triangles[:,0],
            j=triangles[:,1],
            k=triangles[:,2],
            facecolor=colors,
            opacity=0.50)
    ],
    layout=dict(
        scene=dict(
            xaxis=dict(visible=True),
            yaxis=dict(visible=True),
            zaxis=dict(visible=True)
        )
    )
)
fig.show()


# In[ ]:




