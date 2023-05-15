file = open("F:\code.txt", "r")
L = file.readlines()
for line in L:
    gtri = line.split(';')
    if int(gtri[1])>2000:
        print(line)
