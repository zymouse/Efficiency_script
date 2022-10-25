#!/bin/bash
rostopic pub -1 /planning/mission_planner/current_mission autoware_planning_msgs/Mission "goal:
  position: 
    x: 211.396807981
    y: 103.913256516
    z: -1.27059364319
  orientation: 
    x: 0.00642162132573
    y: -0.00248502800985
    z: 0.625718475124
    w: 0.780018574973
lane_driving_sweeping_mode: 1
free_space_sweeping_mode: 10
mission_order: 70"

rostopic pub -1 /autoware/engage std_msgs/Bool "data: true" 