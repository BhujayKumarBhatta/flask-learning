#!/mnt/c/mydev/venvp3flask/bin/python

# -*- coding: utf-8 -*-

import sys
import  encrypt_with_fernet_key as efk

def main():
   keyfilepath = sys.argv[1]
   confilepath = sys.argv[2] 
   conf_section = sys.argv[3] 
   conf_option = sys.argv[4] 
   efk.encrypt_txt_in_ini_file(keyfilepath, confilepath, conf_section, conf_option)

if __name__ == '__main__':
	main()
    
