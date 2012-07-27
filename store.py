#coding:utf-8

from durus.persistent import Persistent
from durus.btree import BTree
from durus.connection import Connection
from durus.client_storage import ClientStorage

class Store():
    def __init__(self,host="127.0.0.1",port=2972):
        self.address = host,port
        self.conn = Connection(ClientStorage(self.address))
        self.root = self.conn.get_root()

    def get_objects(self,key):
        return self.root.get(key)

    def new_objects(self,key):
        assert key and type(key) == str
        self.root[key] = BTree()

store = Store()


if __name__ == '__main__':
    store.get_objects("test")







