import base64

def encode_to_base64(text):
    encoded_text = base64.b64encode(text.encode()).decode()
    return encoded_text

def decode_from_base64(encoded_text):
    decoded_text = base64.b64decode(encoded_text).decode()
    return decoded_text
