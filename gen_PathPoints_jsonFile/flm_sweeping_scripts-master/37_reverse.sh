#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 255.306915283
    y: 78.3472900391
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.76296792432
    w: 0.646436343702
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 37"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 