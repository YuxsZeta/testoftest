#
import math
#
while True:
#Seek the square root of x
     x = input("Number of square roots of x")
     if(x == "end"):
         exit()
     try:
        x = float(x)
     except ValueError:
        print(x,"Number cannot be converted")
        continue
     except:
        print(x,"unexpected error")
        exit()
     if(x <= 0):
        print(x,"not a positive number")
        continue  
     rnew = x
     diff = abs(rnew - x/rnew)
     while True:
        r1 = rnew
        r2 = x/rnew
        rnew = (r1+r2)/2
        print(r1, rnew, r2)
        diff = abs(r1 - r2)
        if(diff <= math.sqrt(x)*1.0E-6):
            break
        

        


