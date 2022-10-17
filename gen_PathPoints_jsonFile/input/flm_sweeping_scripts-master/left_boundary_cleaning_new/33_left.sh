#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 229.559265137
    y: 111.858978271
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0932724684103
    w: 0.995640621227
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 33"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 