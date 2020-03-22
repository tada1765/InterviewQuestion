'''

Hi, here's your problem today. 
This problem was recently asked by Facebook:

Given a list of meetings that will happen during a day,
find the minimum number of meeting rooms that can fit 
all meetings.

Each meeting will be represented by a tuple of 
(start_time, end_time), where both start_time and 
end_time will be represented by an integer to indicate 
the time. start_time will be inclusive, and end_time 
will be exclusive, meaning a meeting of (0, 10) and 
(10, 20) will only require 1 meeting room.

Here's some examples and some starting code:

'''

'''
@brief  find the index of list by compare 1st value of the every tuple.
        compare and find the min value.
@param  meetings: is a list of tuple with 2 int in every tuple. 
@retval pos: the index of list 
'''
def findearliest(meetings):
    prev = meetings[0][0]
    pos = 0
    for i in range(len(meetings)):
        if meetings[i][0] > prev:
            prev = prev
        else:
            prev = meetings[i][0]
            pos = i          
    return pos

'''
@brief  find the number of room needed.
@param  meetings: is a list of tuple with 2 int in every tuple. 
@retval count: the number of room. 
'''
def meeting_rooms(meetings):
    if not meetings:
        return 0
    i = j = count = 0
    li = meetings.copy() # prevent origin list corrupted
    earliest = findearliest(meetings) # find min element
    start, end = meetings[earliest][0], meetings[earliest][1]
    li.remove(li[earliest]) # remove element
    while (not li == False):
        if not li:
            break
        # print(f"{i},{li}")
        if end <= li[j][0]:
            end = li[j][1]
            li.remove(li[j])
            j = 0   
        elif end >= li[j][0]:
            j+=1

        if j >= len(li):
            j = end = 0
            count+=1
        i+=1      
    return count  

# # print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# # 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# # 3 (all meetings overlap at time 20)

a = [(10,20),(20,30),(15,40),(35,40)]
a2 = [(10,20),(20,30),(21,25),(15,40),(35,40),(25,60)]
# possible1 a2:
# [(20,30),(15,40),(35,40)] = 1
# [(20,30)] = 2
# [] = 3
# possible2 a2:
# [(21,25),(15,40),(25,60)] = 1
# [(15,40)] = 2
# [] = 3
b = [(10,20),(9,35),(20,30),(35,40)]
c = [(7,10),(2,4)]

print(findearliest(a2))
print(f"{meeting_rooms(a2)} meeting room needed.")

# try chiness char
从 = [(10,20),(9,55),(20,30),(15,40)]
print(从)