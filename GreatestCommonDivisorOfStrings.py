


str1 = "ABCABCABCABC" #12
str2 = "ABCABC"  #6     

def gcdofString(str1: str,str2: str):
    if str1+str2 != str2 + str1:
        return ""
    gcdBase = str1 if len(str1) < len(str2) else str2
    # gcdBase = "ABCABC"
    i = len(gcdBase)
    # i = 6
    commonDivisors = []
    while i>0:
        if len(str1) % i == 0 and len(str2) % i == 0:
            commonDivisors.append(i)
        i-=1
    # commonDivisors = [6,3,2,1]
    for j in commonDivisors:
        if str1.replace(gcdBase[0:j],"") == str2.replace(gcdBase[0:j],""):
            return gcdBase[0:j]
            


r = gcdofString(str1,str2)
print(r)
