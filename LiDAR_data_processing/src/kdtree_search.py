import numpy as np
import pcl

cloud = pcl.load('../data/table_scene_lms400.pcd')

kdtree = cloud.make_kdtree_flann()

searchPoint = pcl.PointCloud()
searchPoints = np.array([[0.0, 2.0, 0.0]], dtype=np.float32)
searchPoint.from_array(searchPoints)

K = 10000
[indices, sqdist] = kdtree.nearest_k_search_for_cloud(searchPoint, K)

points = np.zeros((len(indices[0]), 3), dtype=np.float32)
for i, indice in enumerate(indices[0]):
    points[i] = cloud[indice]

cloud_cluster = pcl.PointCloud()
cloud_cluster.from_array(points)
pcl.save(cloud_cluster, 'k_nearest_neighbor.pcd')
