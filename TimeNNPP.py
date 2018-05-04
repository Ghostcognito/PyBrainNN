'''Time normer'''

index = []

file = open("TimeFormated.txt", "a")

with open('Time.txt') as data:
    prev = 0
    for line in data:
        value = int(line)
        x = value - prev
        x = str(x)
        file.write(x + "\n")
        prev = value
file.close()
    
