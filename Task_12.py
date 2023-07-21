n = int(input("Input sum  "))
m = int(input("Input multiply  "))
for i in range (1,1000):
    for j in range (1,1000):
        sum = i+j
        if sum == n:
            if i*j == m:
                print(i,j)



        
        



