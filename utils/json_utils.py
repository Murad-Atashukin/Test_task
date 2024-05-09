import json
import os
from typing import TypeVar
from models.configuration_model import ConfigurationModel

T = TypeVar("T")


def get_data_json(file_path: str, model: T) -> T:
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_path)
    with open(file_path) as file:
        data = model.from_dict(json.load(file))
    return data


config = get_data_json(file_path="resources/config.json", model=ConfigurationModel)
