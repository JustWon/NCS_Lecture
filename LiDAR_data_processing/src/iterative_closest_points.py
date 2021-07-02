import open3d as o3d
import numpy as np
import copy

def save_registration_result(source, target, transformation, filename):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.io.write_point_cloud(filename, source_temp)


source = o3d.io.read_point_cloud("../data/cloud_bin_0.pcd")
target = o3d.io.read_point_cloud("../data/cloud_bin_1.pcd")
threshold = 0.02
trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5],
                         [-0.139, 0.967, -0.215, 0.7],
                         [0.487, 0.255, 0.835, -1.4], 
                         [0.0, 0.0, 0.0, 1.0]])

reg_p2p = o3d.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.registration.TransformationEstimationPointToPoint())
save_registration_result(source, target, reg_p2p.transformation, 'point2point.pcd')

reg_p2l = o3d.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.registration.TransformationEstimationPointToPlane())
save_registration_result(source, target, reg_p2l.transformation, 'point2plane.pcd')