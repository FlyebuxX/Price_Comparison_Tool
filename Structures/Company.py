# ======================================================================== #
# IMPORTS                                                                  #
# ======================================================================== #


from imports import *
# ======================================================================== #
# CLASS                                                                    #
# ======================================================================== #


class Shop:
    """
    Class which defines a new shop
    """

    def __init__(self, brand_name: str, product_base: str) -> None:
        self.brand_name = brand_name
        self.url = ''
        self.current_url = ''
        self.kind_of_product = product_base

        # execution
        self.data_set = self.load_json_file("../Data/WebsitesFeatures.json", self.brand_name)
        self.get_url()

    @staticmethod
    def load_json_file(file_name: str, key_arg: str) -> dict:
        """
        Converting a json file to a dictionary
        :param file_name : str, file's name
        :param key_arg: str, key to save
        :return: data_dict
        """
        with open(file_name, "r") as json_data:
            data_dict = json.load(json_data)

        return data_dict[key_arg]

    def get_url(self) -> None:
        """
        Getting the url
        :param : None
        :return: None
        """
        url_brand = self.load_json_file('../Data/Websites.json', self.brand_name)
        self.url = url_brand

    @staticmethod
    def get_response(url: str) -> requests.models.Response:
        """
        Getting the response
        :param url: str
        :return: requests.models.Response
        """
        return requests.get(url)

    @staticmethod
    def get_dict_keys(dict_to_slice: dict, i: int, j: int) -> list:
        """
        Getting keys from index i to j
        :param dict_to_slice : list
        :param i : int
        :param j : int
        :return: list
        """
        return list(dict_to_slice.keys())[i:j+1]

    @staticmethod
    def get_dict_values(dict_to_slice, i, j) -> list:
        """
        Getting values from index i to j
        :param dict_to_slice : list
        :param i : int
        :param j : int
        :return: list
        """
        return list(dict_to_slice.values())[i:j+1]

    def is_connected(self, url: str) -> bool:
        """
        Verify whether the request succeeded or not
        :param url : str
        :return: bool
        """
        return self.get_response(url).ok

    def get_page_content(self, url: str) -> str:
        """
        Display the content of a page
        :param url : str
        :return: str
        """
        return self.get_response(url).text

    @staticmethod
    def get_filters(**kwargs):
        return kwargs

    def add_features(self, features_dict: dict) -> str:
        """
        Adding features to the url
        :param features_dict: dict
        :return self.current_url : str
        """
        self.current_url = self.url + self.kind_of_product + "?"
        for key, value in features_dict.items():
            domain = self.data_set[self.kind_of_product][key]
            for feature in value:
                if len(feature) > 0:
                    self.current_url += domain + feature + "|"

        self.current_url = self.current_url[:-1]  # removing "|"
        return self.current_url


# ======================================================================== #
# MAIN                                                                     #
# ======================================================================== #


Shop = Shop('boulanger', '/c/nav-filtre/tous-les-ordinateurs-portables')

features = Shop.get_filters(
    ssd=[""],
    cpu=["intel20core20i5", "amd20ryzen205"],
    ram=["820go"],
    brand=[""],
    hdd=[""],
    os=["windows2011"]
)

link = Shop.add_features(features)
print(link)