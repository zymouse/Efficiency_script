#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 502.045562744
    y: 40.8036270142
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.777337469241
    w: 0.629083825029
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 24"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 