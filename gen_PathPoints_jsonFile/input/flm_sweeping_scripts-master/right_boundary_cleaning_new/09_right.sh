#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 74.4080047607
    y: 258.190460205
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0597204136116
    w: 0.998215143242
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 9"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 