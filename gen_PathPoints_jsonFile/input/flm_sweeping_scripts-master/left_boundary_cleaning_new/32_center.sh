#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 50.3857078552
    y: 146.441085815
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0932764148392
    w: 0.995640251514
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 32"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 