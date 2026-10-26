# coding: utf-8
import hashlib
import time

"""
难以破解，不可逆算法

md5("your_string_here")
sha1("your_string_here")
sha256("your_string_here")
sha512("your_string_here")
 """

hashobj = hashlib.md5(b"hello world")
print(hashobj.hexdigest())

print('--------------------')

def custom():
    base_sign = '1qaz'
    a_timestamp = int(time.time())

    _token = '%s%s' % (base_sign, a_timestamp)
    print(_token)

    hashobj = hashlib.sha1(_token.encode('utf-8'))
    a_token = hashobj.hexdigest() # 16进制加密串
    print(a_token)
    return a_token, a_timestamp


def b_service_check(token, timestamp):
    base_sign = '1qaz'
    _token = '%s%s' % (base_sign, timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest() # 16进制加密串
    if (token == b_token):
        return True
    return False

if __name__ == "__main__":
    a_token, a_timestamp = custom()
    print(b_service_check(a_token, a_timestamp))