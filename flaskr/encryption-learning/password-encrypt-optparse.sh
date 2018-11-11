#!/mnt/c/mydev/venvp3flask/bin/python

# -*- coding: utf-8 -*-

import sys
import optparse
import  encrypt_with_fernet_key as efk

parser = optparse.OptionParser()
parser.add_option('-k', '--keypath', 
                  action = "store", dest = "keyfilepath", 
                  help = "", default = "")
                  
parser.add_option('-c', '--confilepath', 
                  action = "store", dest = "confilepath", 
                  help = "", default = "")                 
                  
parser.add_option('-s', '--confsection', 
                  action = "store", dest = "confsection", 
                  help = "", default = "")
                  
parser.add_option('-o', '--confoption', 
                  action = "store", dest = "confoption", 
                  help = "", default = "")
                  
options, args = parser.parse_args()

def main():
   keyfilepath = options.keyfilepath
   confilepath = options.confilepath
   conf_section = options.confsection
   conf_option = options.confoption 
   
   efk.encrypt_txt_in_ini_file(keyfilepath, confilepath, conf_section, conf_option)
   #print (keyfilepath, confilepath, conf_section, conf_option)

if __name__ == '__main__':
	main()
	
'''
./password-encrypt.sh -k /mnt/c/mydev/flask-tutorial/flaskr/encry
ption-learning/bhujaykey/info-ops-secret-key  -c /mnt/c/mydev/flask-tutorial/flaskr/encryption-learning/mysettings.ini -s database -o password
'''
	
    
