import os
from yaml import load, dump
try:
    from yaml import Cloader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import json


ACTION_SAMPLE = {
    'actionType': '鍑哄簱',
    'mission': {
        'lane_driving_sweeping_mode': 1,
        'free_space_sweeping_mode': 7,
        'mission_order': 1,
        'goal': {
            'x': 232.756378174,
            'y': 108.402732849,
            'z': 0,
            'qx': 0,
            'qy': 0,
            'qz': -0.0765393613544,
            'qw': 0.997066560548
            }
        }
    }

YAML_SAMPLE = {
    'goal': {
        'position': {
            'x': 154.743881226,
            'y': -74.5904083252,
            'z': 0.0
        },
        'orientation': {
            'x': 0.0,
            'y': 0.0,
            'z': 0.997596635076,
            'w': 0.0692889145902
        }
    },
    'lane_driving_sweeping_mode': 4,
    'free_space_sweeping_mode': 7,
    'mission_order': 18
}


def read_sh_file(file_path: str):
    with open(file_path, "r+") as file_handle:
        text = file_handle.read()
        text_list = text.split('"')
    yaml_obj = load(text_list[1], Loader).copy()
    return yaml_obj


def read_json(file_path: str):
    with open(file_path, "r") as file_handle:
        text = file_handle.read()
    json_obj = json.loads(text)
    return json_obj


def construct_action_dict(mission_dict: dict, action_type: str = "default"):
    action_dict = ACTION_SAMPLE
    action_dict['actionType'] = action_type
    action_dict['mission']['lane_driving_sweeping_mode'] = mission_dict['lane_driving_sweeping_mode']
    action_dict['mission']['free_space_sweeping_mode'] = mission_dict['free_space_sweeping_mode']
    action_dict['mission']['mission_order'] = mission_dict['mission_order']
    action_dict['mission']['goal']['x'] = mission_dict['goal']['position']['x']
    action_dict['mission']['goal']['y'] = mission_dict['goal']['position']['y']
    action_dict['mission']['goal']['z'] = mission_dict['goal']['position']['z']
    action_dict['mission']['goal']['qx'] = mission_dict['goal']['orientation']['x']
    action_dict['mission']['goal']['qy'] = mission_dict['goal']['orientation']['y']
    action_dict['mission']['goal']['qz'] = mission_dict['goal']['orientation']['z']
    action_dict['mission']['goal']['qw'] = mission_dict['goal']['orientation']['w']
    return action_dict


def read_all_sh_file(dir_path: str):
    return


if __name__ == "__main__":
    yaml_dir_path = "./flm_sweeping_scripts-master"
    yaml_file_paths = os.listdir(yaml_dir_path)
    file_order = [int(x.split('_')[0]) for x in yaml_file_paths]

    json_missions_sample = read_json("file/mission_example.json")
    json_missions_sample['actionLists'] = []
    for i in range(len(yaml_file_paths)):
        try:
            action_dict_t = construct_action_dict(read_sh_file(
                yaml_dir_path + "/" + yaml_file_paths[file_order.index(i+1)]))
            action_txt = json.dumps(action_dict_t)
            json_missions_sample['actionLists'].append(json.loads(action_txt))
        except:
            pass
    with open('a.json', 'w') as file:
        json.dump(json_missions_sample, file)
