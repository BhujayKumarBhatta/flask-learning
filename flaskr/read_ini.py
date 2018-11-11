import os
import sys
sys.path.append('../')

def convert_settings_ini_to_dict(filename):
    '''
    ini file with '=' delimeter will be converted to  dict
    '''
    settings_dict = {}
    with open(filename, "r") as f:     
        for l in f:                
             list = l.split('=')
             k = list[0].strip()
             v = list[1].strip()        
             settings_dict[k] = v             
        return settings_dict


        
def get_value_from_settings_ini_file(key):
    '''
    search the lines of setting ini file by key 
    and return it's values'
    '''
    filename = "../settings.ini"
    settings_dict = convert_settings_ini_to_dict(filename)
    return settings_dict[key]
    
    
    
    
    

if __name__ == '__main__':
    lines = convert_to_dict_from_settings_ini_file('settings.ini')
    print (lines)
    