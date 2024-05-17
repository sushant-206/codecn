data = [0] * 10
datarec = [0] * 10
print("Enter a 4 redundant bits\n")
data[7] = int(input())
data[6] = int(input())
data[5] = int(input())
data[3] = int(input())

data[4] = data[5] ^ data[6] ^ data[7]
data[2] = data[3] ^ data[6] ^ data[7]
data[1] = data[3] ^ data[5] ^ data[7]

print("Encoded data is")
for idx in range(1, 8):
    print(data[idx], end='')
print("\nEnter received data bits one by one")
for idx in range(1, 8):
    datarec[idx] = int(input())

c1 = datarec[1] ^ datarec[3] ^ datarec[5] ^ datarec[7]
c2 = datarec[2] ^ datarec[3] ^ datarec[6] ^ datarec[7]
c3 = datarec[4] ^ datarec[5] ^ datarec[6] ^ datarec[7]
c = c3 * 4 + c2 * 2 + c1
if c == 0:
    print("Congratulations! There is no error.")
else:
    print("Error on the position:", c)
    print("Correct message is:")
    if datarec[c] == 0:
        datarec[c] = 1
    else:
        datarec[c] = 0
    for idx in range(1, 8):
        print(datarec[idx], end='')
