#Scarlette Bello Barron     0860234
#Q3

#empty list...
student1 = []
student2 = []
student3 = []

#asking to the user for three student's data to insert it in the lists...
lastName1, grade1_1, grade2_1, grade3_1, grade4_1 = input("Please enter the first student's last name followed by your four grades: ").split()
lastName2, grade1_2, grade2_2, grade3_2, grade4_2 = input("Please enter the second student's last name followed by your four grades: ").split()
lastName3, grade1_3, grade2_3, grade3_3, grade4_3 = input("Please enter the thirth student's last name followed by your four grades: ").split()

#lists wuth data...
student1 = [lastName1, grade1_1, grade2_1, grade3_1, grade4_1]
student2 = [lastName2, grade1_2, grade2_2, grade3_2, grade4_2]
student3 = [lastName3, grade1_3, grade2_3, grade3_3, grade4_3]

#calculating grade averages...
average1 = (int(student1[1]) + int(student1[2]) + int(student1[3]) + int(student1[4]))/4
average2 = (int(student2[1]) + int(student2[2]) + int(student2[3]) + int(student2[4]))/4
average3 = (int(student3[1]) + int(student3[2]) + int(student3[3]) + int(student3[4]))/4

#adding averages into the lists...
student1.append(average1)
student2.append(average2)
student3.append(average3)

print(student1)
print(student2)
print(student3)







