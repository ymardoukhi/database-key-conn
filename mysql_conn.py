#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:37:13 2018

A Class to make a connection to the MySQL database
provided that the username, the path to the pair of 
the key and the password and the ip-address of the 
server are given

@author: yousof
"""

from password_encryption import Passwd
import sqlalchemy as alsql

class AlSQLConn(object):
    
    def __init__(self, ip_address, db_name, user,
                 key_path, pass_path):
        """
        ---------------------
        Initialise an object to make a connection
        to a MySQL database given the pair of the key
        and the password associated to it
        ---------------------
        Parameters:
            arg1 : str
                IP-Address of the MySQL server
            arg2 : str
                The name of the database
            arg3 : str
                The MySQL username
            arg4 : str
                The filepath to the binary key file
            arg5 : str
                The filepath to the binary password file
        ---------------------
        Returns:
            NULL
        ---------------------
        """
        self.ip_address = ip_address
        self.db_name = db_name
        self.user = user
        self.key_path = key_path
        self.pass_path = pass_path
        self.passwd = ''
    
    
    
    def db_conn(self):
        """
        ---------------------
        Make a MySQL connection to the provided
        MySQL database
        ---------------------
        Parameters:
            NULL
        ---------------------
        Returns:
            db_conn : A alsql connection to the MySQL database
        ---------------------
        """
        passwd = Passwd(self.key_path, self.pass_path)
        password = passwd.passwd_decryption()
        db_engine = alsql.create_engine('mysql+mysqlconnector://{}:{}@{}/{}\
                                        '.format(self.user, password,
                                        self.ip_address, self.db_name))
        db_conn = db_engine.connect()
        return (db_conn, db_engine)
