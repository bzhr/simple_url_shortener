import base64


def shorten_id(id):
    str_id = str(id)
    encoded_bytes = base64.urlsafe_b64encode(str_id.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    return encoded_str


def find_index(code):
    decoded_bytes = base64.urlsafe_b64decode(code)
    int_index = int(decoded_bytes)
    return int_index
