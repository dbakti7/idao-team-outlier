import csv
# format: id3,user_id,id2,date,id1
# sample:
# 714,464300,34,1,4
# 714,915655,34,1,4
# 316,262696,42,1,2
# 52,354280,4,1,10

id3 = 0
user_id = 1
id2 = 2
date = 3
id1 = 4

weekLabel = "week"
csvExtension = ".csv"

def split_file():
    # splitting the csv into 8 different files, based on the week
    fileName = weekLabel + "1" + csvExtension
    weekCount = 1
    with open('train.csv', newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        heading = True
        writeFile = open(fileName, 'a', newline='')
        w = csv.writer(writeFile, delimiter=',')
        for row in r:
            if(heading):
                heading = False
                continue
            currentWeek = ((int(row[date]) - 1) // 7) + 1
            if(currentWeek != weekCount):
                weekCount = currentWeek
                fileName = weekLabel + str(weekCount) + csvExtension
                writeFile.close()
                writeFile = open(fileName, 'a', newline='')
                w = csv.writer(writeFile, delimiter=',')
            w.writerow(row)
        writeFile.close()

def parseData(weekNumber, data_size = -1):
    # parse the file for the corresponding weekNumber 
    # into the following dictionary format:
    # {user_id: [[date, id1, id2, id3], ...]}
    # return the dictionary

    data = {}
    fileName = weekLabel + str(weekNumber) + csvExtension
    with open(fileName, newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        heading = True
        for row in r:
            if(heading):
                heading = False
                continue
            if(row[user_id] in data):
                data[row[user_id]].append([row[date], row[id1], row[id2], row[id3]])
            else:
                data[row[user_id]] = [[row[date], row[id1], row[id2], row[id3]]]
            data_size -= 1
            if(data_size == 0):
                break
    return data


# data = parseData(1)
# print(len(data))