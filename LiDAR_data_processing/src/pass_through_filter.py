import pcl

cloud = pcl.load('../data/table_scene_lms400.pcd')

passthrough = cloud.make_passthrough_filter()
passthrough.set_filter_field_name("y")
passthrough.set_filter_limits(0.0, 1.0)
cloud_filtered = passthrough.filter()

pcl.save(cloud_filtered, "table_scene_lms400_passthroughfilter.pcd")
