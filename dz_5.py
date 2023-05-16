count = int(input("Please enter integer number: "))
suma = 0
for item in range(1, count+1):
    if item % 3 == 0:
        continue
    else: suma+=item**3
print(suma)


count = int(input("Please enter integer number: "))
suma = 0
i = 0
while i<count:
    i += 1
    if i % 3 == 0:
        continue
    else: suma+=i**3
print(suma)
