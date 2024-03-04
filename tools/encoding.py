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

def local_bytes_str_to_text(bytes_str):
    text_result = bytes_str.encode('latin1').decode('utf-8')
    return text_result

def text_to_bytes_str(text):
    bytes_result = text.encode('utf-8')
    return str(bytes_result)

#print(bytes_str_to_text('\xe5\xbe\x88\xe6\xa3\x92'))
#print(bytes_str_to_text('\346\240\274'))
def bytes_str_to_text(bytes_str):
    return string_escape(bytes_str)

def hex_with_dash(string):
    hex_string = ''.join(hex(ord(c))[2:].zfill(2) for c in string)
    return '-'.join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))

def xor_text(text1, text2):
    bytes1 = text1.encode('latin1').decode('unicode-escape').encode('latin1')
    bytes2 = text2.encode('latin1').decode('unicode-escape').encode('latin1')

    length = min(len(bytes1), len(bytes2))

    xor_result = ''.join(chr(c1 ^ c2) for c1, c2 in zip(bytes1[:length], bytes2[:length]))
    bytes_str = str(xor_result.encode('latin1'))
    hex_str = hex_with_dash(xor_result)

    return xor_result + '\n\n' + bytes_str + '\n\n' + hex_str



