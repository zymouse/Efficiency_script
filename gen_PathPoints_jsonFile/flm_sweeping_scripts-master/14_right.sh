#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 394.263946533
    y: -118.056274414
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.9970586319
    w: 0.0766425766352
lane_driving_sweeping_mode: 3
free_space_sweeping_mode: 0
mission_order: 14"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 