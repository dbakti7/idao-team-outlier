from data_parser import parseData
import csv

# naive approach, find top 5 entries of id3, treat them as predictions for all

data = parseData(2)
print(len(data))
counter = {}
for key, items in data.items():
    if(items[0][3] in counter):
        counter[items[0][3]] += 1
    else:
        counter[items[0][3]] = 1

counter = sorted(counter.keys(), key=lambda k: counter[k], reverse=True)
data = parseData(3)
print(len(data))
with open('output.csv', 'w', newline='') as out:
    w = csv.writer(out, delimiter=',')
    w.writerow(["user_id", "id3_1", "id3_2", "id3_3", "id3_4", "id3_5"])
    count = 0
    for key, items in data.items():
        w.writerow([key, counter[0], counter[1], counter[2], counter[3], counter[4]])
        count += 1
        if(count == 53979):
            break

