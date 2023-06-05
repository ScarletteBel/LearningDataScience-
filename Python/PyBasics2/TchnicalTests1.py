
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
    

# # print(solution("BAANNAABCDDKBAA"))

# def solution(S):
#     letter_counts = {"B": 0, "A": 0, "N": 0}
#     for c in S:
#         if c in letter_counts:
#             letter_counts[c] += 1
#     total_ban = min(letter_counts["B"], letter_counts["A"] // 2, letter_counts["N"] // 3)
#     return total_ban

# print(solution("BAAANNTGRAAA"))


# def solution(S):
#     baannnserie_counts = {"B": 0, "A": 0, "N": 0}
#     for c in S:
#         if c in baannnserie_counts:
#             baannnserie_counts[c] += 1
#     total_ban = min(baannnserie_counts["B"], baannnserie_counts["A"] // 2, baannnserie_counts["N"] // 3)
#     return total_ban



# def multiply_by_two(list):
#     new_list = [c*2 for c in list]
#     return new_list

# print(multiply_by_two([2, 7, -1, 14, 118, 0]))
    

# def even_numbers(list):
#     new_list = [c for c in list if c%2 == 0]
#     return new_list

# print(even_numbers([2, 7, -1, 14, 118]))



# def find_pairs(l, t):
#     seen = {}
#     for i, num in enumerate(l):
#         diff = t - num
#         if diff in seen:
#             return [seen[diff], num]
#         seen[num] = num
#     return None

# print(find_pairs([5, 19, 22, 11, 24, 2], 7))


# def creating_dic(l):
#     dic = {}
#     for c in l:
#         dic[c] = c**2
#     return dic 

# print(creating_dic([1, 2, 7, 14]))

# def unique_elements(l):
#     my_set = set()
#     unique_list = []
#     for c in l:
#             if c not in my_set:
#                 my_set.add(c)
#                 unique_list.append(c)
#     return unique_list

# print(unique_elements([13, 200, 200, 14, 21, 2, 21, 7, 7, 7, 13]))







# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_nums(l):
#     prime_list = []
#     for num in l:
#         if is_prime(num):
#             prime_list.append(num)
#     return prime_list

# print(prime_nums([2, 7, 14, 10, -1]))


# def revere_string(s):
#     inversed_list = []
#     for c in s:
#         inversed_list.insert(0,c)
#         inversed_string =  ''.join(inversed_list)
#     return inversed_string

# print(revere_string("Hello there!"))

# def revere_string(s):
#     inversed_string = s[::-1]
#     return inversed_string

# print(revere_string("Hello there!"))


# def word_counts(l):
#     str_list = [c.lower() for c in l]
#     dict_count = {}
#     for c in str_list:
#         if c not in dict_count:
#             dict_count[c] = 1
#         else:
#             dict_count[c] += 1
#     return dict_count

# print(word_counts(["Hello", "Hallo", "Hola", "Bonjour", "Hola", "Hola", "Bonjour"]))


# def unique_pairs(nums):
#     pairs = set()
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == 10:
#                 pair = tuple(sorted((nums[i], nums[j])))
#                 pairs.add(pair)
#     return pairs

# nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 5, -1, 11]
# print(unique_pairs(nums)) 


# def unique_fruits(f):
#     only_fruits = {}
#     for c in f:
#         if c['fruit'] not in only_fruits:
#             only_fruits[c['fruit']] = c['quantity']
#         else:
#             only_fruits[c['fruit']] += c['quantity']
#     return only_fruits 
    

# fruits = [
#     {'fruit': 'apple', 'quantity': 10}, 
#     {'fruit': 'banana', 'quantity': 5}, 
#     {'fruit': 'orange', 'quantity': 3},
#     {'fruit': 'pear', 'quantity': 6},
#     {'fruit': 'apple', 'quantity': 2},
#     {'fruit': 'banana', 'quantity': 5},
#     {'fruit': 'apple', 'quantity': 1},
# ]

# print(unique_fruits(fruits))



# def avg_grades(l):
#     dic_grades = {}
#     for c in l:
#         dic_grades[c["name"]] = sum(c["grades"]) / len(c["grades"])
#     return dic_grades

# students = [
#     {"name": "Alice", "grades": [80, 85, 90]},
#     {"name": "Bob", "grades": [70, 75, 80]},
#     {"name": "Charlie", "grades": [60, 65, 70]}
# ]

# print(avg_grades(students))


# def books_clasifier(books):
#     by_author = {}
#     for book in books:
#         author = book["author"]
#         if author in by_author:
#             by_author[author].append(book)
#         else:
#             by_author[author] = [book]

#     return by_author

# books = [    {"title": "Book 1", "author": "Author A", "year": 2001},
#              {"title": "Book 2", "author": "Author B", "year": 2002},    
#              {"title": "Book 3", "author": "Author A", "year": 2003},    
#              {"title": "Book 4", "author": "Author C", "year": 2004},    
#              {"title": "Book 5", "author": "Author B", "year": 2005},
#         ]

# print(books_clasifier(books))


# def update_grades(grades, opr, sub, grd=None):
#     if opr == "add" or opr == "update":
#         grades[sub] = int(grd)
#     elif opr == "remove":
#         if sub in grades:
#             del grades[sub]
#     return grades


# grades = {"Math": 85, "English": 90, "History": 88}

# print(update_grades(grades, "add", "Physics", 92))
# print(update_grades(grades, "update", "English", 93))
# print(update_grades(grades, "remove", "Science"))
# print(update_grades(grades, "remove", "History"))


# def get_value(dic, key):
#     if key in dic:
#         return  dic[key]
#     else:
#         return "not in this dictionary"

# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# print(get_value(person, "nationality"))
# print(get_value(person, "age"))


# def count_words(l):
#     str_dict = {}
#     for c in l:
#         if c not in str_dict:
#             str_dict.update({c:1})
#         else:
#             str_dict[c] += 1
#     return str_dict

# fruits = ["apple", "orange", "banana", "apple", "orange", "apple"]
# print(count_words(fruits))


# def product_prices(l):
#     new_dic = {}
#     for c in l:
#         product_name = c["product"]
#         product_price = c["price"]
#         if product_name not in new_dic:
#             new_dic[product_name] = product_price
#         else:
#             if product_price < new_dic[product_name]:
#                 new_dic[product_name] = product_price
#     return new_dic

# products = [
#     {"product": "apple", "price": 1.0},
#     {"product": "banana", "price": 0.5},
#     {"product": "orange", "price": 0.8},
#     {"product": "apple", "price": 0.9},
#     {"product": "banana", "price": 0.4},
# ]
# print(product_prices(products))

# def add_avrg(l):
#     for c in l:
#         grades = c["grades"]
#         avrg = sum(grades)/len(grades)
#         grade_avrg = round(avrg, 1)
#         c["average"] = grade_avrg
#     return l

# students = [
#     {"name": "Alice", "grades": [80, 85, 90]},
#     {"name": "Bob", "grades": [70, 75, 80]},
#     {"name": "Charlie", "grades": [60, 65, 70]}
# ]

# print(add_avrg(students))




# def get_all_paths(tree, path=[]):
#     for key in tree:
#         new_path = path + [key]
#         print(new_path)
#         if isinstance(tree[key], dict):
#             get_all_paths(tree[key], new_path)

# tree = {
#     "dir1": {
#         "dir2": {
#             "dir3": {}
#         },
#         "file1": {}
#     },
#     "file2": {},
#     "dir3": {
#         "file3": {},
#         "dir4": {}
#     }
# }

# print(get_all_paths(tree))

# def filter_cities(cities, min_populat, max_area):
#     clasified_cities = {}
#     for city, attributes in cities.items():
#         if attributes["population"] > min_populat and attributes["area"] < max_area:
#             clasified_cities[city] = attributes
#     return clasified_cities

# cities = {
#     "Los Angeles": {"population": 3977686, "area": 1302, "timezone": "Pacific"},
#     "New York": {"population": 8419600, "area": 783.8, "timezone": "Eastern"},
#     "Chicago": {"population": 2701423, "area": 588, "timezone": "Central"},
# }

# print(filter_cities(cities, 3000000, 800))


# def highest_grade(students):
#     max_grade = 0
#     top_student = ''

#     for student in students:
#         if max(student['grades']) > max_grade:
#             max_grade = max(student['grades'])
#             top_student = student['name']

#     return top_student, max_grade
    

# students = {
#     "Alice": {"Math": 85, "English": 78, "Science": 92},
#     "Bob": {"Math": 91, "History": 82, "Science": 79},
#     "Charlie": {"Math": 79, "English": 88, "Art": 92},
# }

# print(highest_grade(students))


# def student_report(students):
#     for c in students:
#         student_name = c["name"]
#         print(student_name)
#         average = sum(c["grades"])/len(c["grades"])
#         print("Average Grade: ", average)
#         attendance = c["attendance"]
#         print("attendance: ", attendance)

#         if average > 90:
#             print("Note: High distinction")
#         if attendance < 0.90:
#             print("Note: Low Atendance")
#         print()
    

# students = [
#     {"name": "Alice", "grades": [85, 86, 92, 78], "attendance": 0.95},
#     {"name": "Bob", "grades": [79, 85, 88, 91], "attendance": 0.87},
#     {"name": "Charlie", "grades": [90, 92, 91, 92], "attendance": 0.99},
# ]

# print(student_report(students))



# def student_report(students):
#     for student in students:
#         try:
#             student_name = student["name"]
#             grades = student["grades"]
#             attendance = student["attendance"]
#         except KeyError as e:
#             print(f"Missing required information in student data: {e}")
#             continue

#         # calculate average grade
#         try:
#             average = sum(grades) / len(grades)
#         except ZeroDivisionError:
#             print(f"No grades found for student {student_name}.")
#             continue
#         print(f"Student Name: {student_name}")
#         print(f"Average Grade: {average:.2f}")
#         print(f"Attendance: {attendance}%")

#         if average > 90:
#             print("Note: High distinction")
#         if attendance < 90:
#             print("Note: Low attendance")
#         print("\n")  # adding a newline for better readability between students report

# students = [
#     {"name": "Alice", "grades": [80, 85, 90], "attendance": 95},
#     {"name": "Bob", "grades": [70, 75, 80], "attendance": 85},
#     {"name": "Charlie", "grades": [60, 65, 70], "attendance": 90}
#     ]

# print(student_report(students))
    
