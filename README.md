# bitcoin-script-disassembler
disassembler for bitcoin transactions. Does not support segwit. 

A science project after reading: 
https://github.com/bitcoinbook/bitcoinbook

Learn how to get raw bitcoin transactions in hex: https://www.reddit.com/r/Bitcoin/comments/7dtcpl/how_to_get_the_raw_transaction_in_hex_format/


Usage Example: 

```

python bitcoin-script-disassembler.py 0100000002d8c8df6a6fdd2addaf589a83d860f18b44872d13ee6ec3526b2b470d42a96d4d000000008b483045022100b31557e47191936cb14e013fb421b1860b5e4fd5d2bc5ec1938f4ffb1651dc8902202661c2920771fd29dd91cd4100cefb971269836da4914d970d333861819265ba014104c54f8ea9507f31a05ae325616e3024bd9878cb0a5dff780444002d731577be4e2e69c663ff2da922902a4454841aa1754c1b6292ad7d317150308d8cce0ad7abffffffff2ab3fa4f68a512266134085d3260b94d3b6cfd351450cff021c045a69ba120b2000000008b4830450220230110bc99ef311f1f8bda9d0d968bfe5dfa4af171adbef9ef71678d658823bf022100f956d4fcfa0995a578d84e7e913f9bb1cf5b5be1440bcede07bce9cd5b38115d014104c6ec27cffce0823c3fecb162dbd576c88dd7cda0b7b32b0961188a392b488c94ca174d833ee6a9b71c0996620ae71e799fc7c77901db147fa7d97732e49c8226ffffffff02c0175302000000001976a914a3d89c53bb956f08917b44d113c6b2bcbe0c29b788acc01c3d09000000001976a91408338e1d5e26db3fce21b011795b1c3c8a5a5d0788ac00000000

    0000:0007: 01000000: version (little endian)
    0008:0009: 02: num vins.
vin0: -------------------------
|   0010:0081: d8c8df6a6fdd2add
|              af589a83d860f18b
|              44872d13ee6ec352
|              6b2b470d42a96d4d
|              00000000: Previous output. 32 bytes oftxid, 4 of vin number
|   0082:0083: 8b: script size
||  0084:0361: 48: push next x bytes. In decimal:72
||  0084:0361: 3045022100b31557
||             e47191936cb14e01
||             3fb421b1860b5e4f
||             d5d2bc5ec1938f4f
||             fb1651dc89022026
||             61c2920771fd29dd
||             91cd4100cefb9712
||             69836da4914d970d
||             333861819265ba01: value
||  0084:0361: 41: push next x bytes. In decimal:65
||  0084:0361: 04c54f8ea9507f31
||             a05ae325616e3024
||             bd9878cb0a5dff78
||             0444002d731577be
||             4e2e69c663ff2da9
||             22902a4454841aa1
||             754c1b6292ad7d31
||             7150308d8cce0ad7
||             ab: value
|   0362:0369: ffffffff: sequence number... always FFFFFFFF
vin1: -------------------------
|   0370:0441: 2ab3fa4f68a51226
|              6134085d3260b94d
|              3b6cfd351450cff0
|              21c045a69ba120b2
|              00000000: Previous output. 32 bytes oftxid, 4 of vin number
|   0442:0443: 8b: script size
||  0444:0721: 48: push next x bytes. In decimal:72
||  0444:0721: 30450220230110bc
||             99ef311f1f8bda9d
||             0d968bfe5dfa4af1
||             71adbef9ef71678d
||             658823bf022100f9
||             56d4fcfa0995a578
||             d84e7e913f9bb1cf
||             5b5be1440bcede07
||             bce9cd5b38115d01: value
||  0444:0721: 41: push next x bytes. In decimal:65
||  0444:0721: 04c6ec27cffce082
||             3c3fecb162dbd576
||             c88dd7cda0b7b32b
||             0961188a392b488c
||             94ca174d833ee6a9
||             b71c0996620ae71e
||             799fc7c77901db14
||             7fa7d97732e49c82
||             26: value
|   0722:0729: ffffffff: sequence number... always FFFFFFFF
    0730:0731: 02: Number of vouts
vout0: ------------------------
|   0732:0747: c017530200000000: Satoshis in this output: 39,000,000
|   0748:0749: 19: pubkey script size. In Decimal: 25
||  0750:0799: Script is P2PKH: 76a914xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx88ac
19
76a914
b2bc
||  0750:0799: 76: opcode: OP_DUP
||  0750:0799: a9: opcode: OP_HASH160
||  0750:0799: 14: push next x bytes. In decimal:20
||  0750:0799: a3d89c53bb956f08
||             917b44d113c6b2bc
||             be0c29b7: value
||  0750:0799: 88: opcode: OP_EQUALVERIFY
||  0750:0799: ac: opcode: OP_CHECKSIG
vout1: ------------------------
|   0800:0815: c01c3d0900000000: Satoshis in this output: 155,000,000
|   0816:0817: 19: pubkey script size. In Decimal: 25
||  0818:0867: Script is P2PKH: 76a914xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx88ac
19
76a914
1c3c
||  0818:0867: 76: opcode: OP_DUP
||  0818:0867: a9: opcode: OP_HASH160
||  0818:0867: 14: push next x bytes. In decimal:20
||  0818:0867: 08338e1d5e26db3f
||             ce21b011795b1c3c
||             8a5a5d07: value
||  0818:0867: 88: opcode: OP_EQUALVERIFY
||  0818:0867: ac: opcode: OP_CHECKSIG
    0868:0875: 00000000: Locktime. Usually 00000000
```
