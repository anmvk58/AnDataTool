import json
from src.utils.sys_parameters import CONNECTION_PATH


class ConnectionManager:
    list_cnn = []

    def __init__(self):
        self.list_cnn = json.load(open(CONNECTION_PATH, 'r'))

    def get_list_cnn_name(self) -> list:
        """
        This function return list name of connections
        """
        return [x.get('name') for x in self.list_cnn]

    def get_cnn_by_name(self, name) -> dict:
        """
        This function return a cnn by provide a name.
        Note: Not sensitive case
        """
        conns = [x for x in self.list_cnn if x.get('name').lower() == name.lower()]
        if conns:
            return conns[0]
        else:
            return None

    def check_name_cnn_exists(self, check_name) -> bool:
        """
        This function check a name connection is exists ?
        """
        return False if self.get_cnn_by_name(check_name) is None else True

if __name__ == '__main__':
    cnn = ConnectionManager()
    print(cnn.check_name_cnn_exists('EficaZ'))