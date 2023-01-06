#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -16.8370323181
    y: -18.6452789307
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.99125657076
    w: 0.131948516188
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 5
mission_order: 5"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 