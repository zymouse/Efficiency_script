#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 193.85295105
    y: 113.113296509
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0848978470143
    w: 0.996389660511
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 42"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 