tests = int(input(""))
while(tests>0):
    tests-=1
    length = int(input(""))
    string = input("")
    window = 2
    output = set()
    slides = length - window + 1
    for j in range(slides):
        output.add(string[j:window])
        window += 1
    print(len(output))