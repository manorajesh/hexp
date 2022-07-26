from random import randint

data = []
for i in range(1000000):
    data.append(randint(0, 255))

with open("bintest.bin", "wb") as f:
    f.write(bytes(data))