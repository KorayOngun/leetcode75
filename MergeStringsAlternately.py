word1 = "abc"
word2 = "pqr"

i,j = 0,0
lenWord1, lenWord2 = len(word1),len(word2)
r=""

while i <= lenWord1 or j <= lenWord2:
    w1 =  word1[i] if i<lenWord1 else " "
    w2 =  word2[j] if j<lenWord2  else " "
    i+=1
    j+=1
    r=r+" "+w1+" "+w2




