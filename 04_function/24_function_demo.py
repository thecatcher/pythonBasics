def multiplication_table():
    i = 1
    while i<10:
        j=1
        while j<=i:
            print("%d*%d=%d "%(j,i,i*j),end="\t")
            j= j+1
        print("")
        i=i+1


multiplication_table()