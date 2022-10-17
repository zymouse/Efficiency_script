#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: -5.54243755341
    y: -11.7647018433
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.646137319888
    w: 0.763221176231
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 20"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 
