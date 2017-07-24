from base64 import b64encode
from base64 import b64decode
import hashlib
import zlib

from .swapper import swap


def _urlify(text):
    return text.replace('=', '#').replace('/', '.').replace('+', '-')

def _deurlify(text):
    return text.replace('#', '=').replace('.', '/').replace('-', '+')


def encode_data(dataLst):
    secret = b"9m6WDiXc4X"
    salt = b"f3bulEiIpR"
    separator = "#"

    translateA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"
    translateB = "n1yA5267CuDktv0YJl4Ng/ImQTMjsePBSVxZOfHhi9LcXzrEbdqKaR+Ww3F8GoUp"

    data = str.encode(separator.join([str(i).strip() for i in dataLst]))
    first = b64encode(data)
    second = salt + first
    third = b64encode(second)
    translated = swap(third.decode(), translateA, translateB)
    compressed = zlib.compress(translated.encode())
    text = b64encode(compressed)
    ourHash = hashlib.md5(secret + text).hexdigest()[:12]
    return ourHash, _urlify(text.decode())


def decode_data(ourHash, enc):
    secret = b"9m6WDiXc4X"
    salt = b"f3bulEiIpR"
    separator = "#"

    enc = _deurlify(enc).encode()

    translateA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"
    translateB = "n1yA5267CuDktv0YJl4Ng/ImQTMjsePBSVxZOfHhi9LcXzrEbdqKaR+Ww3F8GoUp"

    if hashlib.md5(secret + enc).hexdigest()[:12] != ourHash:
        raise Exception("Bad Hash!")

    compressed = b64decode(enc)
    translated = zlib.decompress(compressed)
    third = swap(translated.decode(), translateB, translateA)
    second = b64decode(third.encode())
    first = second[len(salt):]
    data = b64decode(first).decode()
    return data.split(separator)