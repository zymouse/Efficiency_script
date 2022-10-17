#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 379.087585449
    y: -118.624824524
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.995404123573
    w: 0.0957634104143
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 27"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 