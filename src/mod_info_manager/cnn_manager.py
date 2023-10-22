import json
from src.utils.sys_parameters import CONNECTION_PATH


class ConnectionManager:
    list_conn: list

    def __init__(self):
        self.load_conn_from_config()

    def load_conn_from_config(self):
        self.list_conn = json.load(open(CONNECTION_PATH, 'r'))

    def get_list_conn_name(self) -> list:
        """
        This function return list name of connections
        """
        list_name_cnn = [x.get('name') for x in self.list_conn]
        list_name_cnn.sort()
        return list_name_cnn

    def get_conn_by_name(self, name) -> dict:
        """
        This function return a connection by provide a name.
        Note: Not sensitive
        :param name: name of connection that you want to retrieve
        :type name: str
        """
        conns = [x for x in self.list_conn if x.get('name').lower() == name.lower()]
        if conns:
            return conns[0]
        else:
            return None

    def check_name_conn_exists(self, check_name) -> bool:
        """
        This function check a name connection is exists
        :param check_name: name need to check
        :type check_name: str
        """
        return False if self.get_conn_by_name(check_name) is None else True

    def save_config_file(self):
        """
        This function save list connections to config file
        """
        with open(CONNECTION_PATH, 'w') as file:
            file.seek(0)
            json.dump(self.list_conn, file, indent=4)
        # reload list conn if any changes happened with files config
        self.load_conn_from_config()

    def create_or_update_conn(self, new_conn):
        """
        This function add a new connection to list connections and write to config file that value
        :param new_conn: one object to add to list connections
        :type new_conn: dict
        """
        if self.check_name_conn_exists(new_conn.get('name')):
            # update conn
            self.list_conn = [x for x in self.list_conn if x.get('name').lower() != new_conn.get('name')]
            self.list_conn.append(new_conn)
        else:
            self.list_conn.append(new_conn)
        self.save_config_file()

    def delete_conn(self, conn_name):
        """
        This function remove a connection from list config
        :param conn_name: name of connections that you want to remove
        :type conn_name: str
        """
        if not self.check_name_conn_exists(conn_name):
            raise Exception('Connection does not exists !')
        else:
            self.list_conn = [x for x in self.list_conn if x.get('name').lower() != conn_name.lower()]
            self.save_config_file()


if __name__ == '__main__':
    conn = ConnectionManager()
    new_conn = {
        'name': 'tvl2',
        'host': '10.37.16.110',
        'pass': 'abcd'
    }
    # print(new_conn.get('name'))
    # print(conn.check_name_conn_exists('tvl2'))
    # conn.create_or_update_conn(new_conn)
    print(conn.get_list_conn_name())