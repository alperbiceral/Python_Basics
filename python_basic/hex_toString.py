hex = input("Enter hex: ")
hex = hex[2:]

byte = bytes.fromhex(hex)
text = bytes.decode(byte)

print(text)
