from imports import *


def load_json_file(file_name: str) -> dict:
    """
    Converting a json file to a dictionary
    :param file_name : str, file's name
    :return: data_dict
    """
    with open(file_name, "r") as json_data:
        data_dict = json.load(json_data)
        return data_dict
