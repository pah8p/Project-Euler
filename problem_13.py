
NAME_FILE = 'C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p013_numbers.txt'

with open (NAME_FILE, "r") as name_file:
    names = name_file.readlines()

names = [int(n) for n in names]

print(names)
print(sum(names))
print(str(sum(names))[:10])
print(len(str(sum(names))[:10]))
