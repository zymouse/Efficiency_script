# LIO-SAM-6AXIS建图话题录制所用

```
# t@t-Default-string:~/Efficiency_script/tools/bag_record_tools/sensor_driversource 
$ ../setup.bash

# t@t-Default-string:~/Efficiency_script/tools/bag_record_tools/sensor_driver
$ roslaunch sensing_fusion.launch 

$ rosrun rs_to_velodyne rs_to_velodyne XIRT XYZIRT
$ rosrun tf static_transform_publisher 0 0 0  0 0 0 /rs16 /velodyne 10
$ rosrun tf tf_echo velodyne zed2i_imu_link
At time 1663726852.835
- Translation: [0.663, -0.049, -0.501]
- Rotation: in Quaternion [0.006, -0.038, -0.004, 0.999]
            in RPY (radian) [0.013, -0.076, -0.008]
            in RPY (degree) [0.755, -4.329, -0.434]
```
