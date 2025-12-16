from rich import print

def tu():

    lis = [

    ["✓ Which bracket is used for a list in Python?",
    "1. ()", "2. {}", "3. []", "4. <>", 3],

    ["✓ List in Python is?",
    "1. Mutable", "2. Immutable", "3. Both", "4. None", 1],

    ["✓ Which function is used to add an element at the end of a list?",
    "1. add()", "2. append()", "3. insert()", "4. extend()", 2],

    ["✓ What is the index of the first element in a list?",
    "1. 0", "2. 1", "3. -1", "4. None", 1],

    ["✓ Which method removes the last element of a list?",
    "1. remove()", "2. pop()", "3. delete()", "4. clear()", 2],

    ["✓ Which keyword is used to delete a list?",
    "1. remove", "2. del", "3. clear", "4. pop", 2],

    ["✓ What does len(list) return?",
    "1. Size of list", "2. Last element", "3. Index", "4. Data type", 1],

    ["✓ Which method removes all elements from a list?",
    "1. pop()", "2. del()", "3. clear()", "4. remove()", 3],

    ["✓ Which of these is a valid list?",
    "1. [1,2,3]", "2. (1,2,3)", "3. {1,2,3}", "4. <1,2,3>", 1],

    ["✓ What does list[1] return?",
    "1. First element", "2. Second element", "3. Last element", "4. Error", 2],

    ["✓ Which method adds multiple elements to a list?",
    "1. append()", "2. add()", "3. extend()", "4. insert()", 3],

    ["✓ Which method removes a specific element?",
    "1. pop()", "2. del()", "3. remove()", "4. clear()", 3],

    ["✓ What is output of [1,2]*2 ?",
    "1. [1,2,1,2]", "2. [2,4]", "3. Error", "4. None", 1],

    ["✓ Which function sorts the list?",
    "1. sort()", "2. order()", "3. arrange()", "4. set()", 1],

    ["✓ Which method returns index of element?",
    "1. find()", "2. index()", "3. search()", "4. locate()", 2],

    ["✓ Which slicing gets all elements?",
    "1. list[:]", "2. list[0]", "3. list[-1]", "4. list[1:]", 1],

    ["✓ What does list[-1] return?",
    "1. First element", "2. Second element", "3. Last element", "4. Error", 3],

    ["✓ Which operator repeats a list?",
    "1. +", "2. *", "3. /", "4. %", 2],

    ["✓ Which operator joins two lists?",
    "1. *", "2. +", "3. -", "4. /", 2],

    ["✓ Which method reverses the list?",
    "1. sort()", "2. reverse()", "3. swap()", "4. change()", 2]

    ]

    i = 1

    
    for question in lis:
        print(question[0])
        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])

        s = int(input("Enter a option (1,2,3,4): "))
        if s == question[5]:
            v = "Correct Answer.."
            print("{:^70}".format(v))
            print(f"Your Score is {i}")
        else:
            print(f"Wrong Answer.. Answer={question[5]} ")
            continue
        i +=1

