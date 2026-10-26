# coding: utf-8
import base64
""" Base64 编码与解码示例
通用型，可解密
常用函数：
    encodestring(b'string')
    decodestring(b'string')
    推荐使用
    encodebytes(b'string')
    decodebytes(b'string')
示例:
    encoded = base64.b64encode(b"hello world")
    print(encoded)
    decoded = base64.b64decode(encoded)
    print(decoded)
"""

base_sign = '1qaz'
replace_one = '%'
replace_two = '$'

def encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError("Input must be a string or bytes")
    _data = base64.encodebytes(data).decode('utf-8')
    _data = _data.replace('b', replace_one).replace('2', replace_two)
    return _data

def decode(data):
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    replace_one_b  = replace_one.encode('utf-8')
    replace_two_b  = replace_two.encode('utf-8')
    data = data.replace(replace_one_b, b'b').replace(replace_two_b, b'2')
    return base64.decodebytes(data).decode('utf-8')

if __name__ == "__main__":
    test_string = "hello world"
    encoded = encode(test_string)
    print(encoded)
    decoded = decode(encoded.encode('utf-8'))
    print(decoded)