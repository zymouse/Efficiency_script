#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 9.22239112854
    y: 33.051197052
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.640143411458
    w: 0.768255434583
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 8"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 