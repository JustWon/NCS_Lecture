# Removing outliers using a Conditional or RadiusOutlier removal
# http://pointclouds.org/documentation/tutorials/remove_outliers.php#remove-outliers

import pcl
import numpy as np
import random

import argparse

parser = argparse.ArgumentParser(
    description='PointCloudLibrary example: Remove outliers')
parser.add_argument('--Removal', '-r', choices=('Radius', 'Condition'), default='',
                    help='RadiusOutlier/Condition Removal')
args = parser.parse_args()


def main():
    cloud = pcl.load('../data/table_scene_lms400.pcd')
    cloud_filtered = pcl.PointCloud()

    if args.Removal == 'Radius':
        outrem = cloud.make_RadiusOutlierRemoval()
        outrem.set_radius_search(1.0)
        outrem.set_MinNeighborsInRadius(2)
        cloud_filtered = outrem.filter()
    elif args.Removal == 'Condition':
        range_cond = cloud.make_ConditionAnd()

        range_cond.add_Comparison2('z', pcl.CythonCompareOp_Type.GT, 0.0)
        range_cond.add_Comparison2('z', pcl.CythonCompareOp_Type.LT, 1.0)

        # build the filter
        condrem = cloud.make_ConditionalRemoval()
        condrem.set_KeepOrganized(True)
        # apply filter
        cloud_filtered = condrem.filter()

        # Test
        # cloud_filtered = cloud
    else:
        print("please specify command line arg paramter 'Radius' or 'Condition'")

    print('Cloud before filtering: ')
    print(cloud.size)

    print('Cloud after filtering: ')
    print(cloud_filtered.size)

if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()', sort='time')
    main()