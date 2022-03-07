import requests
import hmac
import hashlib
import time
import sys
import struct
import base64
import json
timestep = 30
T0 = 0

'''def HOTP(K, C, digits=10):
    """HTOP:
    K is the shared key
    C is the counter value
    digits control the response length
    """
    K_bytes = K.encode()
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    """truncate sha512 value"""
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def TOTP(K, digits=10, timeref = 0, timestep = 30):
    """TOTP, time-based variant of HOTP
    digits control the response length
    the C in HOTP is replaced by ( (currentTime - timeref) / timestep )
    """
    C = int ( 1395069651 - timeref ) // timestep
    return HOTP(K, C, digits = digits)'''

def hotp(key, counter, digits=6, digest='sha1'):
    key = base64.b32decode(key.upper() + '=' * ((8 - len(key)) % 8))
    counter = struct.pack('>Q', counter)
    mac = hmac.new(key, counter, digest).digest()
    offset = mac[-1] & 0x0f
    binary = struct.unpack('>L', mac[offset:offset+4])[0] & 0x7fffffff
    return str(binary)[-digits:].zfill(digits)


def totp(key, time_step=30, digits=6, digest='sha1'):
    return hotp(key, int(time.time() / time_step), digits, digest)


def main():
    args = [int(x) if x.isdigit() else x for x in sys.argv[1:]]
    for key in sys.stdin:
        print(totp(key.strip(), *args))


def main():
    url = 'https://api.challenge.hennge.com/challenges/003'
    python_json = {
        "github_url": "https://gist.github.com/klaus8363/8b80c857994e9e9197bb400dbeb9b829",
        "contact_email": "eric_torres@live.com",
        "solution_language": "python"
    }
    secret = 'eric_torres@live.comHENNGECHALLENGE003'
    secret = base64.b64encode(secret.encode("utf8"))
    #secret = base64.b64encode(bytes(secret, 'utf-8'))
    secret = "MVZGSY27ORXXE4TFONAGY2LWMUXGG33NJBCU4TSHIVBUQQKMJRCU4R2FGAYDG==="
    # secret = "ZXJpY190b3JyZXNAbGl2ZS5jb21IRU5OR0VDSEFMTEVOR0UwMDM="
    headers={
        'Content-Type': 'application/json',
    }

    print(secret)
    passwd = totp(secret, digits=10, digest='sha512')
    print(passwd)

    r = requests.post(url, headers=headers, auth=('eric_torres@live.com', passwd), data=json.dumps(python_json))
    print(r.json())

    #print(get_totp_token(secret))


if __name__ == "__main__":
    main()
