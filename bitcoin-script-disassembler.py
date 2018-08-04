# Based on https://bitcoin.org/en/developer-reference#raw-transaction-format
import sys #I'll need this to read args
import struct #This is for little endian stuff
import codecs #This is to parse hexc

prefix = "    "

def pb():
    return prefix + '{:04d}'.format(loc) + ":" + '{:04d}'.format(loc+size*2-1) + ": "

def bu(s):
    val = "\033[94m"
    while (len(s) > 16):
        val = val + s[0:16] + "\n" + prefix + "           "
        s=s[16:]
    val = val + s + '\033[37m'
    return val



OPCODE_LIST = [
      ("OP_0", 0),
      ("OP_PUSHDATA1", 76),
      ("OP_PUSHDATA2", 77),
      ("OP_PUSHDATA4", 78),
      ("OP_1NEGATE", 79),
      ("OP_RESERVED", 80),
      ("OP_1", 81),
      ("OP_2", 82),
      ("OP_3", 83),
      ("OP_4", 84),
      ("OP_5", 85),
      ("OP_6", 86),
      ("OP_7", 87),
      ("OP_8", 88),
      ("OP_9", 89),
      ("OP_10", 90),
      ("OP_11", 91),
      ("OP_12", 92),
      ("OP_13", 93),
      ("OP_14", 94),
      ("OP_15", 95),
      ("OP_16", 96),
      ("OP_NOP", 97),
      ("OP_VER", 98),
      ("OP_IF", 99),
      ("OP_NOTIF", 100),
      ("OP_VERIF", 101),
      ("OP_VERNOTIF", 102),
      ("OP_ELSE", 103),
      ("OP_ENDIF", 104),
      ("OP_VERIFY", 105),
      ("OP_RETURN", 106),
      ("OP_TOALTSTACK", 107),
      ("OP_FROMALTSTACK", 108),
      ("OP_2DROP", 109),
      ("OP_2DUP", 110),
      ("OP_3DUP", 111),
      ("OP_2OVER", 112),
      ("OP_2ROT", 113),
      ("OP_2SWAP", 114),
      ("OP_IFDUP", 115),
      ("OP_DEPTH", 116),
      ("OP_DROP", 117),
      ("OP_DUP", 118),
      ("OP_NIP", 119),
      ("OP_OVER", 120),
      ("OP_PICK", 121),
      ("OP_ROLL", 122),
      ("OP_ROT", 123),
      ("OP_SWAP", 124),
      ("OP_TUCK", 125),
      ("OP_CAT", 126),
      ("OP_SUBSTR", 127),
      ("OP_LEFT", 128),
      ("OP_RIGHT", 129),
      ("OP_SIZE", 130),
      ("OP_INVERT", 131),
      ("OP_AND", 132),
      ("OP_OR", 133),
      ("OP_XOR", 134),
      ("OP_EQUAL", 135),
      ("OP_EQUALVERIFY", 136),
      ("OP_RESERVED1", 137),
      ("OP_RESERVED2", 138),
      ("OP_1ADD", 139),
      ("OP_1SUB", 140),
      ("OP_2MUL", 141),
      ("OP_2DIV", 142),
      ("OP_NEGATE", 143),
      ("OP_ABS", 144),
      ("OP_NOT", 145),
      ("OP_0NOTEQUAL", 146),
      ("OP_ADD", 147),
      ("OP_SUB", 148),
      ("OP_MUL", 149),
      ("OP_DIV", 150),
      ("OP_MOD", 151),
      ("OP_LSHIFT", 152),
      ("OP_RSHIFT", 153),
      ("OP_BOOLAND", 154),
      ("OP_BOOLOR", 155),
      ("OP_NUMEQUAL", 156),
      ("OP_NUMEQUALVERIFY", 157),
      ("OP_NUMNOTEQUAL", 158),
      ("OP_LESSTHAN", 159),
      ("OP_GREATERTHAN", 160),
      ("OP_LESSTHANOREQUAL", 161),
      ("OP_GREATERTHANOREQUAL", 162),
      ("OP_MIN", 163),
      ("OP_MAX", 164),
      ("OP_WITHIN", 165),
      ("OP_RIPEMD160", 166),
      ("OP_SHA1", 167),
      ("OP_SHA256", 168),
      ("OP_HASH160", 169),
      ("OP_HASH256", 170),
      ("OP_CODESEPARATOR", 171),
      ("OP_CHECKSIG", 172),
      ("OP_CHECKSIGVERIFY", 173),
      ("OP_CHECKMULTISIG", 174),
      ("OP_CHECKMULTISIGVERIFY", 175),
      ("OP_NOP1", 176),
      ("OP_NOP2", 177),
      ("OP_CHECKLOCKTIMEVERIFY", 177),
      ("OP_NOP3", 178),
      ("OP_CHECKSEQUENCEVERIFY", 178),
      ("OP_NOP4", 179),
      ("OP_NOP5", 180),
      ("OP_NOP6", 181),
      ("OP_NOP7", 182),
      ("OP_NOP8", 183),
      ("OP_NOP9", 184),
      ("OP_NOP10", 185),
      ("OP_NULLDATA", 252),
      ("OP_PUBKEYHASH", 253),
      ("OP_PUBKEY", 254),
      ("OP_INVALIDOPCODE", 255),
    ]

oti = dict(o for o in OPCODE_LIST)

ito = dict(reversed(i) for i in OPCODE_LIST)

def ps(s):
    lloc=0
    while (lloc < len(s)):
        size=1
        opcode=s[lloc:lloc+size*2]
        i_opcode = int (opcode, 16)
        if (i_opcode>0 and i_opcode<76):
            print pb() + bu(opcode) + ": push next x bytes. In decimal:" + str(i_opcode)
            value = s[lloc+size*2:lloc + size*2 + i_opcode*2]
            print pb() + bu(value) + ": value"
            lloc+=size*2 + i_opcode*2
        elif (i_opcode == 76):
            print pb() + bu(opcode) + ": push next x bytes specified in next byte"

            next_opcode = s[lloc+size*2:lloc+size*2+size*2]
            i_next_opcode = int(next_opcode, 16)
            print pb() + bu(next_opcode) + ". In decimal:" + str(i_next_opcode)

            value = s[lloc+size*2+size*2:lloc + size*2 +size*2+ i_next_opcode*2]
            print pb() + bu(value) + ": value. This is likely to be a script... Bitcoin has 1 level of lambda function."

#            oldprefix=prefix
            prefix = "||| "
            print pb() + "\033[95mBeginning double decompiled raw script-----\033[37m"
            ps(value)
            print pb() + "\033[95mEnd double decompiled raw script-----------\033[37m"
            prefix = "||  "
            #            prefix=oldprefix


            lloc+=size*2 + size*2 + i_next_opcode*2
        elif (i_opcode == 77):
            exit();
        elif (i_opcode == 78):
            exit();
        else:
            print pb() + bu(opcode) + ": opcode: " + ito[i_opcode]
            lloc+=size*2

        
script = sys.argv[1]
loc = 0
size = 0

print "\033[37m"

size=4
version=script[loc:loc+size*2]
print pb() + bu(version) + ": version (little endian)"
loc+=size*2


size=1
count_vins = script[loc:loc+size*2]
n_count_vins = int (count_vins, 16)
print pb() + bu(count_vins) + ": num vins."
loc+=size*2



x=0
while (x<n_count_vins):

    print "vin" + str(x) + ": -------------------------"
    prefix = "|   "
    
    size=36
    output = script[loc:loc+size*2]
    print pb() + bu(output) + ": Previous output. 32 bytes oftxid, 4 of vin number"
    loc+=size*2


    size=1
    script_size= script[loc:loc+size*2]
    print pb() + bu(script_size) + ": script size"
    loc+=size*2

    size=int(script_size, 16)
    scriptline=script[loc:loc+size*2]
    # print pb() + bu(scriptline) + ": scriptsig"
    prefix="||  "
    ps (scriptline)
    prefix="|   "
    loc+=size*2

    size=4
    sequence=script[loc:loc+size*2]
    print pb() + bu(sequence) + ": sequence number... always FFFFFFFF"
    loc+=size*2
        
    x+=1

prefix = "    "

#VOUTs

size=1
count_vouts = script[loc:loc+size*2]
n_count_vouts = int (count_vouts, 16)
print pb() + bu(count_vouts) + ": Number of vouts"
loc+=size*2

x=0
while (x<n_count_vouts):
    print "vout" + str(x) + ": ------------------------"
    prefix = "|   "

    size=8
    satoshis=script[loc:loc+size*2]
    print pb() + bu(satoshis) + ": Satoshis in this output: " + "{:,}".format(struct.unpack("<Q",codecs.decode(satoshis, "hex"))[0])
    loc+=size*2

    size=1
    pubkeyscript_size = script[loc:loc+size*2]
    n_pubkeyscript_size = int (pubkeyscript_size, 16)
    print pb() + bu(pubkeyscript_size) + ": pubkey script size. In Decimal: " + str(n_pubkeyscript_size)
    loc+=size*2

    size=n_pubkeyscript_size
    pubkeyscriptline=script[loc:loc+size*2]
    #    print pb() + bu(pubkeyscriptline) + ": pubkeyscript to unlock this vin"
    prefix="||  "
    if ("19" == pubkeyscript_size and "76a914" == script[loc:loc+6] and "88ac" == script[loc+46:loc+50]):
        print pb() + "Script is P2PKH: 76a914xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx88ac"
        

    print pubkeyscript_size
    print script[loc:loc+6]
    print script[loc+34:loc+38]
    

    if ("17" == pubkeyscript_size and "a914" == script[loc:loc+4] and "87" == script[loc+44:loc+46]):
        print pb() + "Script is P2SH:  a914xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx87"
        

    ps(pubkeyscriptline)
    prefix="|   "
    
    loc+=size*2

    x+=1

prefix = "    "

size=4
locktime = script[loc:loc+size*2]
print pb() + bu(locktime) + ": Locktime. Usually 00000000"
loc+=size*2

print "\033[0m"
        
        
