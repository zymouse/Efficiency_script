#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -7.29678821564
    y: -12.5655603409
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.648336781068
    w: 0.76135367492
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 19"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 
