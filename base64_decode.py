import base64
import console

s = str.encode(input('Base64 Encoded string:'))

decoded_s = base64.b64decode(s)

print(decoded_s.decode("utf-8"))
