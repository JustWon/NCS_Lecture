import pcl

cloud = pcl.load('../data/table_scene_lms400.pcd')

sor = cloud.make_statistical_outlier_filter()
sor.set_mean_k(50)
sor.set_std_dev_mul_thresh(1.0)
cloud_inlier = sor.filter()

pcl.save(cloud_inlier, "table_scene_lms400_inliers.pcd")

sor.set_negative(True)
cloud_outlier = sor.filter()
pcl.save(cloud_outlier, "table_scene_lms400_outliers.pcd")

