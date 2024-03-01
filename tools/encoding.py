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



