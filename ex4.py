while True:
    x = input("Enter a positive number")
    try:
        x = float(x)
    except ValueError:
        print(x,"Number cannot be converted")
        continue
    except:
        print("unexpected error")
        exit()
    if(x<=0):
        print(x,"not a positive number")
        continue
#what to do when given the correct input
    print(x)
    
