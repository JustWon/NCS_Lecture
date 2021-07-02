import open3d as o3d

cloud = o3d.io.read_point_cloud("../data/cloud_bin_2.pcd")
voxel_down_pcd = cloud.voxel_down_sample(voxel_size=0.02)
cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=16, radius=0.05)

inlier_cloud = voxel_down_pcd.select_by_index(ind)
o3d.io.write_point_cloud('radius_removal_inliers.pcd', inlier_cloud)

outlier_cloud = voxel_down_pcd.select_by_index(ind, invert=True)
o3d.io.write_point_cloud('radius_removal_outliers.pcd', outlier_cloud)
