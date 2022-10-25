#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 22.5093154907
    y: 131.621505737
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.607540208407
    w: 0.794288924239
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 30"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 