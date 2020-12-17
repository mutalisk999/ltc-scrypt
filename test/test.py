#!/usr/bin/env python
# encoding: utf-8

from ltc_scrypt import getPoWHash

# block header
# "01000000f615f7ce3b4fc6b8f61e8f89aedb1d0852507650533a9e3b10b9bbcc30639f279fcaa86746e1ef52d3edb3c4ad8259920d509bd073605c9bf1d59983752a6b06b817bb4ea78e011d012d59d4"
# double sha256
# "adf6e2e56df692822f5e064a8b6404a05d67cccd64bc90f57f65b46805e9a54b"
# scrypt
# 0000000110c8357966576df46f3b802ca897deb7ad18b12f1c24ecff6386ebd9

# "0000000110c8357966576df46f3b802ca897deb7ad18b12f1c24ecff6386ebd9"
s = "01000000f615f7ce3b4fc6b8f61e8f89aedb1d0852507650533a9e3b10b9bbcc30639f279fcaa86746e1ef52d3edb3c4ad8259920d509bd073605c9bf1d59983752a6b06b817bb4ea78e011d012d59d4"
print getPoWHash(s.decode("hex"))[::-1].encode("hex")