#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 17.7547645569
    y: -44.4848442078
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.99494073732
    w: 0.100463571611
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 39"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 