students=[
    {"name":"mina","note1":19,"note2":13,"note3":16},
    {"name":"david","note1":6,"note2":17,"note3":12},
    {"name":"john","note1":16,"note2":8,"note3":20},
    {"name":"mohamed","note1":18,"note2":9,"note3":11},
    {"name":"sara","note1":14,"note2":10,"note3":18}
]
moyene={}
for i in range(len(students)):
    moyene[students[i]["name"]]=((students[i]["note1"]+students[i]["note2"]+students[i]["note3"])/3)

names = list(moyene.keys())

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if moyene[names[i]] < moyene[names[j]]:
            names[i], names[j] = names[j], names[i]

for name in names:
    print(name)

print(f"the first student is named {names[0]}")
print(f"the last student is named {names[-1]}")

