#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 464.601226807
    y: -26.6359958649
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.996197362738
    w: 0.0871252803389
lane_driving_sweeping_mode: 2
free_space_sweeping_mode: 0
mission_order: 35"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 