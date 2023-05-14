tokens = open("tokens.txt", "r")
format = open("reformatted.txt", "w")
for line in tokens:
    format.write(line.split(":")[-1])
