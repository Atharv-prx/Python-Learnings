def fun():
    try:
        l = [1,5,6,9]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1

    except:
        print("Some error occured")
        return 0

    finally:
        print("Code in finally is always executed")

x = fun()
print(x)

# finally is always exected 
# I we use normally something instead of finally then it won't be executed cuz of "return" but finally is always executed