
# def deviding_range(k): 
#     k = int(k)
#     numbers_range = range(2000000001)
#     element_count = 0
#     for c in numbers_range:
#         if c % k == 0:
#             element_count += 1
#     return element_count


# devisor = input("Write a devisor, you can choose within a range from 1 to 2000000000: ")
# print(deviding_range(devisor))


def deviding_range(k): 
    k = int(k)
    element_count = 2000000001//k
    return element_count

devisor = input("Write a devisor, you can choose within a range from 1 to 2000000000: ")
print(deviding_range(devisor))


