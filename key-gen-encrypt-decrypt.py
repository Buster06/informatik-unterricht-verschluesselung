import math


p = int(input("was ist p? "))
q = int(input("was ist q? "))
e = int(input("was ist e? "))
N = q*p

if (e < (p-1) * (q-1)):
    a = (p-1)*(q-1)
    b = e
else:
    b = (p-1)*(q-1)
    a = e

(u1,u2, u3) = (1, 0, a)
(v1,v2, v3) = (0, 1, b)

while (v3 != 0):
    r = math.floor(u3/v3)
    (t1, t2, t3) = (u1-(r*v1), u2-(r*v2), u3-(r*v3))
    (u1, u2, u3) = (v1, v2, v3)
    (v1, v2, v3) = (t1, t2, t3)

if ((p-1)*(q-1) > u2) and (u2 > 0):
    k = 0
elif ((p-1)*(q-1) > u2) and (u2 < 0):
    k = 1
elif ((p-1)*(q-1) < u2) and (u2 > 0):
    k = math.floor(u2 / ((p-1)*(q-1))) * -1
elif ((p-1)*(q-1) < u2) and (u2 < 0):
    k = math.ceil((u2 / ((p-1)*(q-1))) * -1)
# else:
#    d = "error"

d = u2 + k*(p-1)*(q-1)





RawText = "DU"




Blocklaenge = len(str(N)) - 1



AsciiRawTextList = list(RawText.encode('ascii'))
AsciiRawText = ''.join(map(str, AsciiRawTextList))



print("AsciiRawList:",AsciiRawTextList)
print("AsciiRawText",AsciiRawText)
print("Blocklaenge:",Blocklaenge)


textTab = {}

if len(AsciiRawText) > len(str(N)):
    print(" ho lee sheet ")


AsciiBlocks = {}


# Ascii in blöcke einteilen 

x = 0

for i in range(0, len(AsciiRawText), Blocklaenge): # string slicing, danke chatgpt :D
    
#    print(i, AsciiRawText[i:i+Blocklaenge])
    AsciiBlocks[x] = AsciiRawText[i:i+Blocklaenge]
    x += 1

print("Blocks",AsciiBlocks)



EncodedAsciiBlocks = {}

for i in AsciiBlocks:
    EncodedAsciiBlocks[i] = (int(AsciiBlocks[i])**e)%N


print("encoded:",EncodedAsciiBlocks)




DecodedEncodedAsciiBlocks = {}

for i in EncodedAsciiBlocks:
    DecodedEncodedAsciiBlocks[i] = (EncodedAsciiBlocks[i]**d)%N


print("DecodedEncoded",DecodedEncodedAsciiBlocks)




## Ascii zu text geht nicht in diesem fall

DecodedTextList = {}

for i in DecodedEncodedAsciiBlocks:
    DecodedTextList[i] = chr(int(DecodedEncodedAsciiBlocks[i]))


DecodedText = ''.join(map(str, DecodedTextList))

print("Decoded",DecodedText)

#Hallo fiete wie gehts# 