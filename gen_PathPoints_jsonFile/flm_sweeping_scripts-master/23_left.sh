#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 523.49206543
    y: 150.057800293
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.774156467821
    w: 0.632994283805
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 23"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 