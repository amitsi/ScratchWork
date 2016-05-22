'''
### Code to break Vigenere Cipher

Step 0
======
Decrypt the file which is base64'd after being encrypted with repeating-key XOR.
'''

ciphertext = open("cipher.txt", "r").read().strip().decode("base64")
numOfKeysToTry = 3

'''
Step 1-4
========
1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
2. Write a function to compute the edit distance/Hamming distance between two
   strings.
3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
   KEYSIZE worth of bytes, and find the edit distance between them. Normalize
   this result by dividing by KEYSIZE.
4. The KEYSIZE with the smallest normalized edit distance is probably the key.
'''

# Hamming Distance is the number of differing bits
def hammingdist(s1, s2):
    res = "".join([bin(ord(s1[i]) ^ ord(s2[i])) for i in range(len(s1))])
    count = 0
    for i in res:
        if i == '1': count = count + 1
    return count

def leastHammingDistKeys():
    keyszdict = {}
    for keysz in range(2, 41):
        chunks = []
        for i in range(0, len(ciphertext), keysz):
            chunks.append(ciphertext[i:i+keysz])
        sum1, len1 = 0, 0
        for i in range(0, len(chunks)-1, 2):
            if (len(chunks[i]) == len(chunks[i+1])):
                sum1 = sum1 + hammingdist(chunks[i], chunks[i+1])/float(keysz)
                len1 = len1 + 1
        avghd = sum1/len1
        keyszdict[keysz] =  avghd
        keyszs = [x for x,y in sorted(keyszdict.items(), key = lambda x:x[1])]
    return keyszs[0:numOfKeysToTry]

keyszs = leastHammingDistKeys()

'''
Step 5-8
========
5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of
   KEYSIZE length.
6. Now transpose the blocks: make a block that is the first byte of every block,
   and a block that is the second byte of every block, and so on.
7. Solve each block as if it was single-character XOR. You already have code to
   do this.
8. For each block, the single-byte XOR key that produces the best looking
   histogram is the repeating-key XOR key byte for that block. Put them together
   and you have the key.
'''

def singlexorcipher(hexstr):
    charlist = {'$': 0.0561, '(': 0.2178, ',': 0.7384, '0': 0.5516, '4': 0.1348,
                '8': 0.1054, '<': 0.1225, '@': 0.0073, 'D': 0.3151, 'H': 0.2321,
                'L': 0.1884, 'P': 0.2614, 'T': 0.3322, 'X': 0.0343, '\\': 0.0016,
                '`': 0.0009, 'd': 2.5071, 'h': 2.7444, 'l': 3.175, 'p': 1.5482,
                't': 6.37, 'x': 0.195, '|': 0.0007, ' ': 17.1662, '#': 0.0179,
                "'": 0.2447, '+': 0.0215, '/': 0.1549, '3': 0.1847, '7': 0.103,
                ';': 0.1214, '?': 0.1474, 'C': 0.3906, 'G': 0.1876, 'K': 0.0687,
                'O': 0.1842, 'S': 0.4003, 'W': 0.2527, '[': 0.0086, '_': 0.1159,
                'c': 2.1129, 'g': 1.5597, 'k': 0.6753, 'o': 5.7701, 's': 4.3686,
                'w': 1.3034, '{': 0.0026, '"': 0.2442, '&': 0.0226, '*': 0.0628,
                '.': 1.5124, '2': 0.3322, '6': 0.1153, ':': 0.4354, '>': 0.1242,
                'B': 0.2163, 'F': 0.1416, 'J': 0.1726, 'N': 0.2085, 'R': 0.2519,
                'V': 0.0892, 'Z': 0.0076, '^': 0.0003, 'b': 1.0195, 'f': 1.3725,
                'j': 0.0867, 'n': 4.9701, 'r': 4.2586, 'v': 0.8462, 'z': 0.0596,
                '~': 0.0003, '!': 0.0072, '%': 0.016, ')': 0.2233, '-': 1.3734,
                '1': 0.4594, '5': 0.1663, '9': 0.1024, '=': 0.0227, 'A': 0.3132,
                'E': 0.2673, 'I': 0.3211, 'M': 0.3529, 'Q': 0.0316, 'U': 0.0814,
                'Y': 0.0304, ']': 0.0088, 'a': 5.188, 'e': 8.5771, 'i': 4.9019,
                'm': 1.6437, 'q': 0.0747, 'u': 2.0999, 'y': 1.133, '}': 0.0026}
    final = {}
    for a in charlist:
        out= "".join([chr(ord(x) ^ ord(y)) for x,y in zip(hexstr,a*len(hexstr))])
        res = 0
        for i in out.lower():
            res = res + charlist.get(i, -10)
        final[res] = (out, a)
    i = sorted(final.keys(),reverse=True)
    return final[i[0]]

blks = {}
for sz in keyszs:
    key = []
    blocks = [[] for i in range(sz)]
    for i in range(0, len(ciphertext)):
        blocks[i%sz].append(ciphertext[i])
    ret = [singlexorcipher("".join(i)) for i in blocks]
    blks[sz] = []
    for x,y in ret:
        blks[sz].append(x)
        key.append(y)
    vals = [len(i) for i in blks[sz]]
    blks[sz] = "".join([blks[sz][j][k] for k in range(max(vals)) \
                for j in range(sz) if (k < len(blks[sz][j]))])
    print blks[sz]
    print "="*(11+len(key))
    print "Key is : ", "".join(key)
    print "="*(11+len(key))
