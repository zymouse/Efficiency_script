#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 503.630310059
    y: 175.871139526
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.10115274473
    w: 0.994870907321
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 11"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 