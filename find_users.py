from data_parser import parseData

users = {}
for i in range(1, 9):
    data = parseData(i)
    print(len(data))
    for key, items in data.items():
        if key in users:
            users[key] += 1
        else:
            users[key] = 1
    
print(len(users))
sortedUsers = sorted(users.keys(), key=lambda k: users[k], reverse=True)
sortedUsers = sortedUsers[:53979]
with open("users.txt", "a") as f:
    counter = 0
    for user in sortedUsers:
        f.write(str(user) + "\n")
        if(counter < 5):
            print(users[user])
        counter += 1
