#Write a function that takes a string as input and returns the number of the vowels...

# def many_vowels(s):
#     string_list = s
#     existing_vowels = []
#     vowels = [ "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
#     for c in string_list:
#         if c in vowels:
#             existing_vowels.append(c)
    
#     len_list = len(existing_vowels)
#     return len_list

# string = "Hello beautiful people!"
# print(many_vowels(string))




# def many_vowels(s):
#     vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#     for c in s.lower():
#         if c in vowels_dict:
#             vowels_dict[c] += 1

#     total_vowels = sum(vowels_dict.values())
#     return total_vowels

# string = "Hello beautiful people!"
# print(many_vowels(string))



# def many_vowels(s):
#     vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#     for c in s.lower():
#         if c in vowels_dict:
#             vowels_dict[c] += 1

#     max_vowel = max(vowels_dict, key=vowels_dict.get)
#     return max_vowel

# string = "Hello beautiful people!"
# print(many_vowels(string))



# def sum_pair(n):
#     pair_sum = 0
#     for c in range(n+1):
#         if c % 2 == 0:
#             pair_sum += c
        
#     return pair_sum 

# number = 100
# print(sum_pair(number))
            

def big_num(s):
    num_num = s.split(",")
    num_list = []
    for c in num_num:
        num_list.append(int(c))

    bigs_num = max(num_list)

    return bigs_num
    
num_str = input("Write different numbers devided by a comma (,): ")
print(big_num(num_str))





def big_num(s):
    num_list = [int(c) for c in s.split(",")]
    bigs_num = max(num_list)

    return bigs_num
    
num_str = input("Write different numbers devided by a comma (,): ")
print(big_num(num_str))