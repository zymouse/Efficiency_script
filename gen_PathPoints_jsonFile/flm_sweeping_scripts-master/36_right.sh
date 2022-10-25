#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 350.792205811
    y: 84.0567474365
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.993576264466
    w: 0.113164511621
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 36"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 