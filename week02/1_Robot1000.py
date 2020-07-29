def Robot1000(walk) :
    x = 0
    y = 0
    i = 0
    while (i< len(walk)):
        if (walk[i] == "Z"):
            x = 0
            y = 0
        elif (walk[i] == "N"):
            y += 1
        elif (walk[i] == "S"):
            y -= 1
        elif (walk[i] == "E"):
            x += 1
        elif (walk[i] == "W"):
            x -= 1
        i += 1
    print (str(x), str(y))

n = input()
Robot1000(n)
