#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 12:46:08 2018

Generate a pair of a key and a password in
binary format. The user can either invoke 
the method "passwd_encryption" to encrypt a 
given plain-text password and store the pair
of the key and the password, or can call
the "passwd_decryption" to read a pair of the
key and the password to decipher the encrypted
password

@author: Yousof Mardoukhi
"""

from cryptography.fernet import Fernet


class Passwd(object):
    
    def __init__(self, key_path, pass_path, password = '',
                 encoding = 'utf-8'):
        """
        ---------------------
        Initialise an object to generate a pair of a key
        and a ciphered password.
        It is highly suggested to use 'key_name'
        and 'pass_name', where 'name' is an arbitrary
        choice of name.
        ---------------------
        Parameters:
            arg1 : str
                The given path and the name to store
                the generated random key in binary format
            arg2 : str
                The given path and the name to store
                the ciphered password in binary format
            arg3 (optional) : str
                The given password to be ciphered
        ---------------------
        """
        self.encoding = encoding
        self.key_path = key_path
        self.pass_path = pass_path
        self.password = password

    def passwd_encryption(self):
        """
        ---------------------
        Generate a pair of a key and a ciphered password.
        ---------------------
        Parameters:
            NULL
        ---------------------
        Returns:
            NULL
        ---------------------
        """
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        bin_passwd = bytes(self.password, 'utf-8')
        ciphered_text = cipher_suite.encrypt(bin_passwd)
        with open(self.pass_path, 'wb') as pass_output:
            pass_output.write(ciphered_text)
        with open(self.key_path, 'wb') as key_output:
            key_output.write(key)


    def passwd_decryption(self):
        """
        ---------------------
        Decrypt the ciphered password with the given
        key
        ---------------------
        Parameters:
            NULL
        ---------------------
        Returns:
            plain_password : the decrypted password
        ---------------------
        """
        with open(self.key_path, 'rb') as input_key:
            for line in input_key:
                key = line
        with open(self.pass_path, 'rb') as input_password:
            for line in input_password:
                password = line
        cipher_suit = Fernet(key)
        plain_password = cipher_suit.decrypt(password)
        plain_password = bytes(plain_password).decode('utf-8')
    
        return plain_password

    def recover_encrypt_pass(self):
        """
        Generate the same encrypted string from the plain text
        :return:
            cipher_text: encrypted password in the binary format
        """
        with open(self.key_path) as input_file:
            key = input_file.readlines()
        cipher_suite = Fernet(key[0])
        bin_passwd = bytes(self.password, 'utf-8')
        ciphered_text = cipher_suite.encrypt(bin_passwd)
        return ciphered_text

