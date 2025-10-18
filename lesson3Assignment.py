# try:
#     a = 1 / 0
# except ZeroDivisionError as e:
#     print(e.args)

file = open("words.txt", "a")
file.write("ohad\n")
file.close()
file = open("words.txt", "r")
for line in file.readlines():
    print(line, end="")

file = open("words.txt", "a")
file.write("ohad\n")
file.write("reches\n")
file.close()

file = open("words.txt", "r")
for line in file.readlines():
    print(line, end="")

file.close()
file = open("words.txt", "w")
file.flush()
file.close()
