#Seek the square root of x
x = 2
#
rnew = x
#
diff = rnew - x/rnew
if (diff < 0):
    diff = -diff
#
while True:
    r1 = rnew
    r2 = x/rnew
    rnew = (r1 + r2)/2
    print(r1,rnew,r2)
    diff = r1 - r2
    if(diff < 0):
        diff = -diff
    if(diff <= 1.0E-6):
        break
        
