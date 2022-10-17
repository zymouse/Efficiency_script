#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -5.57836818695
    y: -30.4673347473
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.680138996116
    w: 0.733083178065
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 8
mission_order: 6"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 