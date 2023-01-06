#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 478.222290039
    y: 63.5535125732
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: -0.0932731434575
    w: 0.995640557987
lane_driving_sweeping_mode: 4
free_space_sweeping_mode: 0
mission_order: 34"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 