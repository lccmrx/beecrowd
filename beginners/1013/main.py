a, b, c = input().split(" ")
a, b, c = int(a), int(b), int(c)

aux = a
if a < b:
    aux = b
if aux < c:
    aux = c
    
print(f"{aux} eh o maior")
