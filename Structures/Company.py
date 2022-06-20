from imports import *


class Shop:

    def __init__(self, brand_name):
        self.brand_name = brand_name
        self.url = ''

        # execution
        self.data_set = self.load_json_file("../Data/WebsitesFeatures.json", self.brand_name)
        self.get_url()

    def load_json_file(self, file_name: str, key_arg: str) -> dict:
        """
        Converting a json file to a dictionary
        :param file_name : str, file's name
        :param key_arg: str, key to save
        :return: data_dict
        """
        with open(file_name, "r") as json_data:
            data_dict = json.load(json_data)

        return data_dict[key_arg]

    def get_url(self):
        """
        Getting the url
        :param : None
        :return: None
        """
        url_brand = self.load_json_file('../Data/Websites.json', self.brand_name)
        self.url = url_brand

    def get_response(self) -> requests.models.Response:
        """
        Getting the response
        :param : None
        :return: requests.models.Response
        """
        return requests.get(self.url)

    def get_dict_keys(self, dict_to_slice, i, j) -> list:
        """
        Getting keys from index i to j
        :param dict_to_slice : list
        :param i : int
        :param j : int
        :return: list
        """
        return list(dict_to_slice.keys())[i:j+1]

    def is_connected(self) -> bool:
        """
        Verify whether the request succeeded or not
        :param : None
        :return: bool
        """
        return self.get_response().ok


Shop = Shop('boulanger')
kind_of_product = Shop.get_dict_keys(Shop.data_set, 0, 1)