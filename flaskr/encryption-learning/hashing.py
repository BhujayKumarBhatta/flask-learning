import hashlib

text1 = 'secret'

encrypted1 = hashlib.sha256(text1).hexdigest()

text2 = 'secret'

encrypted2 = hashlib.sha256(text1).hexdigest()

if encrypted1 == encrypted2:
    return True





