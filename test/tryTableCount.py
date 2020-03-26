
# count no. letter in str:
def table(data):
    temp = {}
    for i in range(0,len(data)):
        temp[data[i]] = 0 # init { count is 0 } for +=1 error
        for j in range(0,len(data)):
            
            if data[i] == data[j]:
                temp[data[i]] += 1
    return temp

data = "hdhasddfgsg"

# print(table(data))
# {'h': 2, 'd': 3, 'a': 1, 's': 2, 'f': 1, 'g': 2}


def _putBackToStr(table):
    return "re"

def compareTable(table1,table2):
    
    return "a"

data1 = "youtube"
data2 = "google"
table1 = table(data1)
table2 = table(data2)

print(table1.get("y")) # 1
print(table2.get("o")) # 2
print(table1.pop("u")) # 2
print(table1.items())
print(table1.keys()) # dict_keys(['y', 'o', 't', 'b', 'e'])
result = table1.keys()
print(result)
print(list(table1)) # ['y', 'o', 't', 'b', 'e']

print(compareTable(table1,table2))

