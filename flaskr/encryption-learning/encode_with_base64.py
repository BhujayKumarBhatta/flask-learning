import random
import base64
 
text = 'supersecretpassword' 

bt = text.encode("utf-8")  #or  text = b'supersecretpassword' 
bt
# b'supersecretpassword'
base64.b64encode(bt)
#b'c3VwZXJzZWNyZXRwYXNzd29yZA=='
encoded_text = b64encode(bt)

decoded_text_bytes =base64.b64decode(encoded_text)
decoded_text_bytes
#b'supersecretpassword'
decoded_text_in_cleartext = bytes(decoded_text_bytes).decode("utf-8")
decoded_text_in_cleartext
#'supersecretpassword'

#chartracter to number
ord('a')
#number to character
chr(97)
#generating randon sing a prefixed key 
rand = random.Random(key).randrange
key = 'abcd'
rand(256)


###################Using bz2 #######################
import bz2 
password = "NoVa52:)" 
encrypted_password = bz2.compress(password) 
encrypted_password 
#'BZh91AY&SY\xae\x1d\x86!\x00\x00\x02\x1f\x00\x00 \x12\x10\x00\x01\x01\x00 \x00\xa0\x00"\x06\'\xa8C\x02\x12\xe6\xc0\xf1w$S\x85\t\n\xe1\xd8b\x10' 
print bz2.decompress(encrypted_password) 
#NoVa52:) 
import bz2
f=open("test.txt", "w")
f.write(bz2.compress("mypassword"))
f.close()
w = open("test.txt", "r")
password = bz2.decompress(w.read())
w.close()
print password  
  

