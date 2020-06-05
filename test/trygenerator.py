import random
from time import process_time
import timeit

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


#  func people_list:
t1 = process_time()
people = people_list(10000)
t2 = process_time()

print('people_list Took {} Seconds'.format(t2-t1))
# print(people)


#  func people_generator:
t1 = process_time()
people = people_generator(10000)
t2 = process_time()

print('people_generator Took {} Seconds'.format(t2-t1))
# print(people)


# TRY timeit:
def func(num):
    pass

list_time = timeit.timeit(func(1),number=10)
print(list_time)


# generator_time = timeit.timeit(people_generator(), number=100)

