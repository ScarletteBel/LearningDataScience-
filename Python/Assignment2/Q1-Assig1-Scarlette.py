#Scarlette Bello Barron     0860234
#Q1

ae1 = [] #Empty list
ae1 = [622, 2, 81, 4, 7, "Asia", "Africa", "America"] # five integers and three strings inserted
print(ae1)
removedInt = ae1.pop(4) #removing int 7 from the list
print(ae1)
removedStr = ae1.remove("America") #removing a string from the list
print(ae1)
insertedInt = ae1.insert(4,32) #Inserting int 32 in position 4 of the list
print(ae1)
print(len(ae1)) #printing list's lenght
twoStrsMore = "Europe", "Oceania"
ae1.extend(twoStrsMore) #Two strings added to the list
print(ae1)
subList = [45.1, 22.37, 14.11] #Definig a sublist
ae1.append(subList) #Sublist added to the list ae1
print(ae1)
print(ae1[-1])  #printing sublist by locating it in ae1
print(ae1[-1][0])  #Printing one specific float number from the Sublist in ae1 (the first one)
import random
print(random.choice(ae1))  #Printing one random value from ae1
print(random.sample(ae1[-1], len(ae1[-1]))) #Shuffle randomly the sublist in ae1




