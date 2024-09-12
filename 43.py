from pwn import *
address = 0x0000000000400751
address_bytes = p64(address)
print(address_bytes)
