#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 195.807693481
    y: 113.951972961
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0762619326686
    w: 0.997087818412
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 11
mission_order: 44"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 