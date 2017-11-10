# -*- coding:utf-8 -*-
import socks
import socket
from app.proxy.Connection import Connection
from app.util.logger import logger

class Server(Connection):
    """Establish connection to destination server."""

    def __init__(self, host, port):
        super(Server, self).__init__(b'server')
        self.addr = (host, int(port))

    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.addr[0], self.addr[1]))
        self.conn.connect((str(self.addr[0], encoding='utf-8'), self.addr[1]))
