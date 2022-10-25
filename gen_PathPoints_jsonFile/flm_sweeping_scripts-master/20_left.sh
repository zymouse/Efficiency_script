#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 42.4204292297
    y: 242.290435791
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.629102299334
    w: 0.777322517989
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 20"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 