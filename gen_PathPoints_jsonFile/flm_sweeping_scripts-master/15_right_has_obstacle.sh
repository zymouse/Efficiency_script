#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 237.1512146
    y: -84.0999908447
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.996322672821
    w: 0.085680403966
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 15"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 