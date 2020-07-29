def SwapBits(x) :
	even = x & 0b10101010
	odd = x & 0b01010101

	even >>= 1
	odd <<= 1

	return (even | odd)

x = int(input())
if (1 <= x and x <= 255):
    print(SwapBits(x))
else:
    print("please input again !!!")
