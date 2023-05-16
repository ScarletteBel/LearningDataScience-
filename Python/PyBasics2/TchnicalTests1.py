
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


# def deviding_range(k): 
#     k = int(k)
#     element_count = 2000000001//k
#     return element_count

# devisor = input("Write a devisor, you can choose within a range from 1 to 2000000000: ")
# print(deviding_range(devisor))


# def array_sum(A):
#     sum = 0
#     for c in A:
#         sum += c
#     return sum 

# print(array_sum([23, 56, 3, 98]))



# def summung_pair_cero(l):
#     elem_seen = set()
#     for c in l:
#         if -c in elem_seen:
#             return [-c, c]
#         elem_seen.add(c) 
#     return None 

# print(summung_pair_cero([2, 34, 17, 8, -17, 9]))


# def small_positive_missed(l):
#     positive_num = [c for c in l if c > 0]
#     if not positive_num:
#         return 1
    
#     positive_num.sort()
#     smallest_num = 1
#     for c in positive_num:
#         if c == smallest_num:
#             smallest_num += 1
#         elif c > smallest_num:
#             break
#     return smallest_num
  
# print(small_positive_missed([1, 6, 2, 3, 4, 11]))


# import re 

# def palindrome(s):
#     string = s.lower
#     clean_string = re.sub(r'[^\w\s]',"",string)
#     clean_string = clean_string.replace(" ","")
    
#     reversed_string = []
#     for c in clean_string:
#         reversed_string.insert(0,c)
#     separator = ""
#     new_string = separator.join(reversed_string)

#     if string == new_string:
#         return "True"
#     else: 
#         return "False"

# print(palindrome("Hola Canadades"))



# def solution(s, k):
#     week = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
#     index_day = week.index(s)

#     it_num = index_day + k

#     for c in range(index_day):
#         for day in week:
#             return day

#     return c

# print(solution("Mon", 2))


# def solution(s, k):
#     week = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
#     index_day = week.index(s)

#     index_day_k = index_day + k
#     it_num = index_day_k % len(week)

#     return week[it_num]

# print(solution("Sat", 23))


# def solution(S):
#     ban = 0
#     for c in S:
#         if c == "B" or "A" or "N":
#             ban += 1
#     return ban 

# print(solution("ABCDDKNBAA"))
        

# def solution(S):
#     ban_counts = {"B": 0, "A": 0, "N": 0}
#     for c in S:
#         if c in ban_counts:
#             ban_counts[c] += 1
#     total_ban = sum(ban_counts.values())
#     ban_inS = T
    

# print(solution("BAANNAABCDDKBAA"))

def solution(S):
    letter_counts = {"B": 0, "A": 0, "N": 0}
    for c in S:
        if c in letter_counts:
            letter_counts[c] += 1
    return min(letter_counts["B"], letter_counts["A"] // 2, letter_counts["N"] // 3)

print(solution("BAAANNTGRAAA"))