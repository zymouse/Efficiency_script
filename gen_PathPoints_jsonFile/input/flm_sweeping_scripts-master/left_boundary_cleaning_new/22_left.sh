#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 239.981185913
    y: 231.344924927
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0923691873756
    w: 0.995724828064
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 22"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 