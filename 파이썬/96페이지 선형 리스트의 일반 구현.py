katok=[]
print(katok)
#[]

print(len(katok))
0
#0

katok.append(None)
print(len(katok))
#1

print(katok)
#None

katok[0] = "다현"
print(katok)
#['다현']

배열길이 = len(katok)
print(배열길이)
#1


katok[배열길이-1] = "다현"
print(katok)
#['다현']

katok.append(None)
배열길이 = len(katok)
katok[배열길이-1]='정연'
print(katok)
#['다현','정연']


