def byRef(myList): #[10, 20, 30]
    print('\nThe received list2 is: ',myList) #[10, 20, 30]
    myList.append([1, 2, 3]) #[10, 20, 30, 1, 2, 3]
    print('in byRef the list2 is : ', myList)#[10, 20, 30, 1, 2, 3]


def callingF():
    myList = [10, 20, 30]
    print('The list in the calling function is: ', myList)
    byRef(myList)
    print('\nIn the calling function the list is:', myList)# ?? [10, 20, 30] OR [10, 20, 30, 1, 2, 3]

def main():
    callingF()
main()