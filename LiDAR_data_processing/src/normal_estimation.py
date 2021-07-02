import pcl
import pcl.pcl_visualization

cloud = pcl.load('../data/table_scene_lms400.pcd')

feature = cloud.make_NormalEstimation()

feature.set_KSearch(3)
normals = feature.compute()

viewer = pcl.pcl_visualization.PCLVisualizering()
viewer.SetBackgroundColor(0.0, 0.0, 0.5)
viewer.AddPointCloud(cloud)
viewer.AddPointCloudNormals(cloud, normals, 10, 0.05, b'normals')

flag = True
while (flag):
    flag = not(viewer.WasStopped())
    viewer.SpinOnce()
