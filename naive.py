from data_parser import parseData
import csv

# naive approach, find top 5 entries of id3, treat them as predictions for all
counter = {}
for i in range(1, 9):
    data = parseData(i)
    print(len(data))
    for key, items in data.items():
        if(items[0][3] in counter):
            counter[items[0][3]] += 1
        else:
            counter[items[0][3]] = 1

counter = sorted(counter.keys(), key=lambda k: counter[k], reverse=True)
# data = parseData(3)
# print(len(data))
# with open('output.csv', 'w', newline='') as out:
#     w = csv.writer(out, delimiter=',')
#     w.writerow(["user_id", "id3_1", "id3_2", "id3_3", "id3_4", "id3_5"])
#     count = 0
#     for key, items in data.items():
#         w.writerow([key, counter[0], counter[1], counter[2], counter[3], counter[4]])
#         count += 1
#         if(count == 53979):
#             break

with open('output_from_file_all.csv', 'w', newline='') as out:
    w = csv.writer(out, delimiter=',')
    w.writerow(["user_id", "id3_1", "id3_2", "id3_3", "id3_4", "id3_5"])
    lines = [line.rstrip('\n') for line in open('users.txt')]
    for line in lines:
        w.writerow([line, counter[0], counter[1], counter[2], counter[3], counter[4]])