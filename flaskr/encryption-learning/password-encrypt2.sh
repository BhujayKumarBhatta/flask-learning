#!/mnt/c/mydev/venvp3flask/bin/python

# -*- coding: utf-8 -*-
import re
import sys
import os

import  encrypt_with_fernet_key as efk
from encrypt_with_fernet_key import encrypt_txt_in_ini_file

def main():
   keyfilepath = sys.argv[1]`
   confilepath = sys.argv[2]` 
   conf_section = sys.argv[3]` 
   conf_option = sys.argv[4]` 
   get_txt_from_ini_n_decrypt(keyfilepath, confilepath, conf_section, conf_option)

if __name__ == '__main__':
	main()
    
