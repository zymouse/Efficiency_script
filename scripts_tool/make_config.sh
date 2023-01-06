#!/bin/bash
control="control"
control_1="mpc_follower"
control_2="pedal_calibration"
control_3="pure_pursit"
control_4="vehicle_cmd_gate"
control_5="vehicle_controller"

localization="localization"

perception="perception"

planning="planning"
planning_1="scenario_planning"
planning_1_1="common"
planning_1_1_1="motion_velocity_optimizer"

planning_1_2="lane_driving"
planning_1_2_1="motion_planning"
planning_1_2_1_1="obstacle_avoidance_planner"
planning_1_2_1_2="surround_obstacle_checker"

sensing="sensing"

vehicle="vehicle"
vehicle_1="default"
vehicle_1_1="sweeper_sensor_kit"
vehicle_2="sweeper"


control_1_path=$control/$control_1
control_2_path=$control/$control_2
control_3_path=$control/$control_3
control_4_path=$control/$control_4
control_5_path=$control/$control_5

localization_path=$localization
perception_path=$perception

planning_1_1_1_path=$planning/$planning_1/$planning_1_1/$planning_1_1_1
planning_1_2_1_1_path=$planning/$planning_1/$planning_1_2/$planning_1_2_1/$planning_1_2_1_1
planning_1_2_1_2_path=$planning/$planning_1/$planning_1_2/$planning_1_2_1/$planning_1_2_1_2

sensing_path=$sensing

vehicle_1_1_path=$vehicle/$vehicle_1/$vehicle_1_1
vehicle_2_path=$vehicle/$vehicle_2

function mkdir_folder()
{
    mkdir -p  $control_1_path
    mkdir -p  $control_2_path
    mkdir -p  $control_3_path
    mkdir -p  $control_4_path
    mkdir -p  $control_5_path

    mkdir -p  $localization_path
    mkdir -p  $perception_path

    mkdir -p  $planning_1_1_1_path
    mkdir -p  $planning_1_2_1_1_path
    mkdir -p  $planning_1_2_1_2_path

    mkdir -p  $sensing_path

    mkdir -p  $vehicle_1_1_path
    mkdir -p  $vehicle_2_path
}

function roscp_yaml_files()
{
    roscp mpc_follower mpc_follower_param.yaml                  $control_1_path
    roscp raw_vehicle_cmd_converter accel_map.csv               $control_2_path
    roscp raw_vehicle_cmd_converter brake_map.csv               $control_2_path
    roscp pure_pursuit pure_pursuit_param.yaml                  $control_3_path
    roscp vehicle_cmd_gate vehicle_cmd_gate.yaml                $control_4_path
    roscp velocity_controller velocity_controller_param.yaml    $control_5_path
    roscp localization_launch ndt_scan_matcher.yaml             $localization_path

    roscp planning_launch adaptive_cruise_control.yaml          $planning
    roscp planning_launch obstacle_stop_planner.yaml            $planning
    roscp planning_launch motion_velocity_optimizer.yaml        $planning_1_1_1_path  
    roscp planning_launch obstacle_avoidance_planner.yaml       $planning_1_2_1_1_path
    roscp planning_launch surround_obstacle_checker.yaml        $planning_1_2_1_2_path

    roscp vehicle_launch sensors_calibration.yaml               $vehicle_1_1_path
    roscp vehicle_launch sensor_kit_calibration.yaml            $vehicle_1_1_path
    roscp  vehicle_launch sensors_calibration_copy.yaml         $vehicle_1_1_path

    roscp sweeper_description vehicle_info.yaml                 $vehicle_2_path
}

function main()
{
    mkdir_folder
    roscp_yaml_files
}

source ~/pix-citybot-v2/install/setup.bash 
mkdir -p pix-citybot && cd pix-citybot
main
