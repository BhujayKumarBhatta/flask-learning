#!/mnt/c/mydev/venvp3flask/bin/python

# -*- coding: utf-8 -*-

import sys
import argparse
import  encrypt_with_fernet_key as efk

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keypath', 
                  action = "store", dest = "keyfilepath",
                  required = True,
                  help = "key file name along with full path e.g. /home/user1/keyfile.txt",
                  default = "")
                  
parser.add_argument('-c', '--confilepath', 
                  action = "store", dest = "confilepath",
                  required = True,
                  help = "Configuration file name with full path",
                  default = "/opt/mypackage/settings.ini")                 
                  
parser.add_argument('-s', '--confsection', 
                  action = "store", dest = "confsection",
                  required = True,
                  help = "Section name in the configuration file e.g. [database] ",
                  default = "")
                  
parser.add_argument('-o', '--confoption', 
                  action = "store", dest = "confoption",
                  required = True,
                  help = "",
                  default = "Option name in the ini file e.g. password")               

try:                  
    options = parser.parse_args()    
except:
    #print usage help when no argument is provided
    parser.print_help(sys.stderr)
    sys.exit(1)

def main():
   keyfilepath = options.keyfilepath
   confilepath = options.confilepath
   conf_section = options.confsection
   conf_option = options.confoption 
   
   efk.encrypt_txt_in_ini_file(keyfilepath, confilepath, conf_section, conf_option)
#    print (keyfilepath, confilepath, conf_section, conf_option)
#    print (options)

if __name__ == '__main__':
	main()
	
'''
./password-encrypt.sh -k /mnt/c/mydev/flask-tutorial/flaskr/encry
ption-learning/bhujaykey/info-ops-secret-key  -c /mnt/c/mydev/flask-tutorial/flaskr/encryption-learning/mysettings.ini -s database -o password
'''
	
    
