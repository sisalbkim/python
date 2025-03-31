katok = [] #빈 배열

def add_data(friend) :
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

count = 0
while True:
    name = input("카톡친구 입력==>")
    add_data(name)
    print(katok)

    count = count + 1
    if count > 4:
        break
