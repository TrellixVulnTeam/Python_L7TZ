import base64

frase = "Python para hackers"
print(frase.count("a"))

encrypt = frase.encode("base64")
decrypt = encrypt.decode("base64")
print(encrypt)
print(decrypt)
