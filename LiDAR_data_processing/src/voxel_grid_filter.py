import pcl

cloud = pcl.load('../data/table_scene_lms400.pcd')
sor = cloud.make_voxel_grid_filter()
sor.set_leaf_size(0.01, 0.01, 0.01)
cloud_filtered = sor.filter()

pcl.save(cloud_filtered, 'table_scene_lms400_voxelgridfilter.pcd')