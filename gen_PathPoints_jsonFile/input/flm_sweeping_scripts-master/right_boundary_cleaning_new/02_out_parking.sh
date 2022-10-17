#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 228.807998657
    y: 108.261291504
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.107284212442
    w: 0.994228393158
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 8
mission_order: 2"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 