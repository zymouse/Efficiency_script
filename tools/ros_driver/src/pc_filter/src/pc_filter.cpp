#include "ros/ros.h"
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/filters/passthrough.h>
#include <pcl_ros/transforms.h>
#include <tf/transform_listener.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl/io/pcd_io.h>
#include <iostream>
#include <memory>

ros::Publisher filtered_pc_pub;
tf::TransformListener *tf_listener;
ros::NodeHandle* n;

float x_clip_min_;
float x_clip_max_;
float y_clip_min_;
float y_clip_max_;
float z_clip_min_;
float z_clip_max_;

float downsample_;

std::string filtered_frame_id;
std::string observed_frame_id;
std::string input_pc_topic;
std::string output_pc_topic;

void filterCallback(const sensor_msgs::PointCloud2ConstPtr& sensor_message_pc)
{
  ROS_DEBUG("Filtering PointCloud Callback");
  pcl::PCLPointCloud2 original_pc2;
  pcl_conversions::toPCL(*sensor_message_pc, original_pc2);

  pcl::PointCloud<pcl::PointXYZRGB>::Ptr original_pc(new pcl::PointCloud<pcl::PointXYZRGB>());
  pcl::fromPCLPointCloud2(original_pc2, *original_pc);

  tf::StampedTransform transform;
  ros::Time now = ros::Time::now();
    try{
        ROS_DEBUG("Waiting for world Transform");
        tf_listener->waitForTransform (observed_frame_id, filtered_frame_id, now, ros::Duration(10.0));
        ROS_DEBUG("Looking up Transform");
        tf_listener->lookupTransform (observed_frame_id, filtered_frame_id, now, transform);
        ROS_DEBUG("Finished Look up Transform");
    }
    catch (tf::TransformException ex){
        ROS_ERROR("%s",ex.what());
        return;
    }


  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_transformed(new pcl::PointCloud<pcl::PointXYZRGB>());
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filtered_x(new pcl::PointCloud<pcl::PointXYZRGB>());
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filtered_xy(new pcl::PointCloud<pcl::PointXYZRGB>());
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filtered_xyz(new pcl::PointCloud<pcl::PointXYZRGB>());
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_downsampled(new pcl::PointCloud<pcl::PointXYZRGB>());
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_transformed_back(new pcl::PointCloud<pcl::PointXYZRGB>());

  original_pc->header.frame_id = observed_frame_id;
  pcl_ros::transformPointCloud(filtered_frame_id,
          *original_pc,
          *cloud_transformed,
          *tf_listener);

  pcl::PassThrough<pcl::PointXYZRGB > pass;

  ROS_DEBUG_STREAM("filtercloudsize before x: " << cloud_transformed->size());

  pass.setInputCloud(cloud_transformed);
  pass.setFilterFieldName ("x");
  pass.setFilterLimits (x_clip_min_, x_clip_max_);
  pass.filter(*cloud_filtered_x);

  ROS_DEBUG_STREAM("filtercloudsize before y: " << cloud_filtered_x->size());

  pass.setInputCloud(cloud_filtered_x);
  pass.setFilterFieldName ("y");
  pass.setFilterLimits (y_clip_min_, y_clip_max_);
  pass.filter(*cloud_filtered_xy);

  ROS_DEBUG_STREAM("filtercloudsize before z: " << cloud_filtered_xy->size());

  pass.setInputCloud(cloud_filtered_xy);
  pass.setFilterFieldName ("z");
  pass.setFilterLimits (z_clip_min_, z_clip_max_);
  pass.filter(*cloud_filtered_xyz);

  cloud_filtered_xyz->header.frame_id = filtered_frame_id;
  pcl_ros::transformPointCloud(observed_frame_id,
		      *cloud_filtered_xyz,
		      *cloud_transformed_back,
		      *tf_listener);

  cloud_transformed_back->header.frame_id = observed_frame_id;

  pcl::PCLPointCloud2Ptr cloud_transformed_back_pc2(new pcl::PCLPointCloud2());
  pcl::toPCLPointCloud2(*cloud_transformed_back, *cloud_transformed_back_pc2);

  ROS_DEBUG_STREAM("filtercloudsize before downsample: " << cloud_transformed_back_pc2->data.size());

  pcl::PCLPointCloud2 cloud_filtered_downsampled;
  if(downsample_) {
    pcl::VoxelGrid<pcl::PCLPointCloud2> sor;
    sor.setInputCloud (cloud_transformed_back_pc2);
    sor.setLeafSize (downsample_, downsample_, downsample_);
    sor.filter (cloud_filtered_downsampled);
  } else {
    cloud_filtered_downsampled = *cloud_transformed_back_pc2;
  }

  sensor_msgs::PointCloud2 cloud_transformed_back_msg;
  cloud_transformed_back_msg.header.frame_id = observed_frame_id;
  pcl_conversions::fromPCL(cloud_filtered_downsampled, cloud_transformed_back_msg);
  ROS_DEBUG_STREAM("filtercloudsize: " << cloud_transformed_back->size());
  filtered_pc_pub.publish(cloud_transformed_back_msg);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "filteredpcserver");
  ros::NodeHandle n_;
  tf::TransformListener tfl;
  tf_listener = &tfl;
  n = &n_;

  n_.getParam("xpassthrough/filter_limit_min", x_clip_min_);
  n_.getParam("xpassthrough/filter_limit_max", x_clip_max_);
  n_.getParam("ypassthrough/filter_limit_min", y_clip_min_);
  n_.getParam("ypassthrough/filter_limit_max", y_clip_max_);
  n_.getParam("zpassthrough/filter_limit_min", z_clip_min_);
  n_.getParam("zpassthrough/filter_limit_max", z_clip_max_);

  n_.getParam("downsample", downsample_);

  n_.getParam("observed_frame_id", observed_frame_id);
  n_.getParam("filtered_frame_id", filtered_frame_id);
  n_.getParam("input_pc_topic", input_pc_topic);
  n_.getParam("output_pc_topic", output_pc_topic);

  ROS_INFO_STREAM("Listening on this input pc topic " << input_pc_topic);
  ROS_INFO_STREAM("Listening on this output pc topic " << output_pc_topic);
  ROS_INFO_STREAM("Listening on this observed_frame_id " << observed_frame_id);
  ROS_INFO_STREAM("Listening on this filtered_frame_id " << filtered_frame_id);
  ROS_INFO_STREAM("Dimensions for filtered scene are: (" << x_clip_min_ << ", " << x_clip_max_ << ") (" << y_clip_min_ << ", " << y_clip_max_ << ") (" << z_clip_min_ << ", " << z_clip_max_ << ")");

  ros::Time now = ros::Time::now();

  tf_listener->waitForTransform (observed_frame_id, filtered_frame_id, now, ros::Duration(10.0));

  ros::Subscriber original_pc_sub = n_.subscribe(input_pc_topic, 1, filterCallback);
  filtered_pc_pub = n_.advertise<sensor_msgs::PointCloud2>(output_pc_topic, 1);

  ros::spin();
  return 0;
}

