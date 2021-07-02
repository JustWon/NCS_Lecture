import numpy as np
import pcl

cloud = pcl.load('../data/table_scene_lms400.pcd')

vg = cloud.make_voxel_grid_filter()
vg.set_leaf_size(0.01, 0.01, 0.01)
cloud_filtered = vg.filter()

tree = cloud_filtered.make_kdtree()

ec = cloud_filtered.make_EuclideanClusterExtraction()
ec.set_ClusterTolerance(0.01)
ec.set_MinClusterSize(100)
ec.set_MaxClusterSize(250000)
ec.set_SearchMethod(tree)
cluster_indices = ec.Extract()

print('cluster_indices : ' + str(cluster_indices.count) + " count.")

cloud_cluster = pcl.PointCloud()

for j, indices in enumerate(cluster_indices):
    print('indices = ' + str(len(indices)))
    points = np.zeros((len(indices), 3), dtype=np.float32)

    for i, indice in enumerate(indices):
        points[i][0] = cloud_filtered[indice][0]
        points[i][1] = cloud_filtered[indice][1]
        points[i][2] = cloud_filtered[indice][2]

    cloud_cluster.from_array(points)
    ss = "cloud_cluster_" + str(j) + ".pcd"
    pcl.save(cloud_cluster, ss)