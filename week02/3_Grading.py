hw = int(input())
test_1st = int(input())
test_2nd = int(input())
test_3rd = int(input())

sum = hw + test_1st + test_2nd + test_3rd

if 80 <= sum <= 100:
    print("A")
elif 75 <= sum <= 79:
    print("B+")
elif 70 <= sum <= 74:
    print("B")
elif 65 <= sum <= 69:
    print("C+")
elif 60 <= sum <= 64:
    print("C")
elif 55 <= sum <= 59:
    print("D+")
elif 50 <= sum <= 54:
    print("D")
else:
    print("F")
