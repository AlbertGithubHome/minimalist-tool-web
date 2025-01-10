import base64

def encode_to_base64(text):
    encoded_text = base64.b64encode(text.encode()).decode()
    return encoded_text

def decode_from_base64(encoded_text):
    decoded_text = base64.b64decode(encoded_text).decode()
    return decoded_text

def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
             .decode('unicode-escape') # Perform the actual octal-escaping decode
             .encode('latin1')         # 1:1 mapping back to bytes
             .decode(encoding))        # Decode original encoding

def comm_string_escape(s, encoding='utf-8'):
    return (s.encode('utf-8')          # To bytes, required by 'unicode-escape'
             .decode('unicode-escape') # Perform the actual octal-escaping decode
             .encode('latin1')         # 1:1 mapping back to bytes
             .decode(encoding))        # Decode original encoding

def local_bytes_str_to_text(bytes_str):
    text_result = bytes_str.encode('latin1').decode('utf-8')
    return text_result

def text_to_bytes_str(text):
    bytes_result = text.encode('utf-8')
    return str(bytes_result)

#print(bytes_str_to_text(r'\xe5\xbe\x88\xe6\xa3\x92'))
#print(bytes_str_to_text(r'\346\240\274'))
#print(local_bytes_str_to_text('\346\240\274'))
def bytes_str_to_text(bytes_str):
    return comm_string_escape(bytes_str)

def hex_with_dash(string):
    hex_string = ''.join(hex(ord(c))[2:].zfill(2) for c in string)
    return '-'.join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))

def xor_text(text1, text2):
    bytes1 = text1.encode('utf-8').decode('unicode-escape').encode('latin1')
    bytes2 = text2.encode('utf-8').decode('unicode-escape').encode('latin1')

    length = min(len(bytes1), len(bytes2))

    xor_result = ''.join(chr(c1 ^ c2) for c1, c2 in zip(bytes1[:length], bytes2[:length]))
    bytes_str = str(xor_result.encode('latin1'))
    hex_str = hex_with_dash(xor_result)

    return xor_result + '\n\n' + bytes_str + '\n\n' + hex_str

def decimal_to_base36(num: int) -> str:
    """将 10 进制整数转换为 36 进制字符串"""
    if num < 0:
        raise ValueError("只支持非负整数的转换")

    # 定义 36 进制的字符集
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return "0"

    base36 = ""
    while num > 0:
        remainder = num % 36
        base36 = digits[remainder] + base36
        num //= 36
    return base36

def base36_to_decimal(base36: str) -> int:
    """将 35 进制字符串转换为 10 进制整数"""
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    base36 = base36.lower()  # 确保大小写一致
    decimal = 0
    for char in base36:
        if char not in digits:
            raise ValueError(f"非法字符: {char}")
        decimal = decimal * 36 + digits.index(char)
    return decimal

