import json
f = open("file.json", "r")
x=json.load(f)
f.close()

sum_ages = 0
lst_ages = []
for i in x:
    temp = i ["What is your age?"]
    if temp.isnumeric():
        age = int(i["What is your age?"])
        sum_ages += sum_ages
        lst_ages.append(age)
avg = sum_ages/ len(x)
print(avg)
print(lst_ages)
