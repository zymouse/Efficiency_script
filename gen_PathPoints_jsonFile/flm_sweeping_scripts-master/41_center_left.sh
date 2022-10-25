#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 27.1376838684
    y: 132.716583252
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.620604556074
    w: 0.784123705151
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 41"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 