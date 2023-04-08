#Write a function that takes a string as input and returns the number of the vowels...

def many_vowels(s):
    existing_vowels = []
    vowels = [ "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for c in s:
        if c in vowels:
            existing_vowels = existing_vowels + c
    
    len_list = len(existing_vowels)
    return len_list

string = "Hello beautiful people!"
print(many_vowels(string))

