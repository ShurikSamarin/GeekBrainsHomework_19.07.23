n = int(input("Input N  "))
print()
sum_up = 0
sum_down = 0
for i in range (0, n):
    coin = input("Input side of coin u/d  ")
    if coin == "u":
        sum_up = sum_up + 1
    elif coin == "d":
        sum_down = sum_down + 1
else: 
    print()
if sum_up > sum_down:
    print("Turn", sum_down, "coins")
else:
    print("Turn", sum_up, "coins")
