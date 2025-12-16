from rich import print

def se():

    lis = [

["✓ Which bracket is used to create a set in Python?",
 "1. []", "2. ()", "3. {}", "4. <>", 3],

["✓ Which of the following creates an empty set?",
 "1. {}", "2. []", "3. set()", "4. ()", 3],

["✓ Set in Python is?",
 "1. Ordered", "2. Unordered", "3. Indexed", "4. Sorted", 2],

["✓ Which data type does not allow duplicate values?",
 "1. List", "2. Tuple", "3. Set", "4. Dictionary", 3],

["✓ How do you add an element to a set?",
 "1. add()", "2. append()", "3. insert()", "4. extend()", 1],

["✓ Which method adds multiple elements to a set?",
 "1. add()", "2. append()", "3. update()", "4. extend()", 3],

["✓ Which method removes a specific element from a set?",
 "1. pop()", "2. remove()", "3. delete()", "4. clear()", 2],

["✓ Which method removes an element without error if not found?",
 "1. remove()", "2. pop()", "3. discard()", "4. clear()", 3],

["✓ Which method removes all elements from a set?",
 "1. clear()", "2. pop()", "3. remove()", "4. del()", 1],

["✓ What does set.pop() do?",
 "1. Removes first element", "2. Removes last element",
 "3. Removes a random element", "4. Clears set", 3],

["✓ Which operator performs union of sets?",
 "1. &", "2. |", "3. -", "4. ^", 2],

["✓ Which operator performs intersection of sets?",
 "1. |", "2. -", "3. &", "4. ^", 3],

["✓ Which operator performs difference of sets?",
 "1. |", "2. &", "3. -", "4. ^", 3],

["✓ Which operator performs symmetric difference?",
 "1. |", "2. &", "3. -", "4. ^", 4],

["✓ What does len(set) return?",
 "1. Number of elements", "2. Size in bytes",
 "3. Index", "4. Data type", 1],

["✓ Can a set contain mutable elements like list?",
 "1. Yes", "2. No", "3. Sometimes", "4. Error", 2],

["✓ Which method checks if one set is subset of another?",
 "1. subset()", "2. issubset()", "3. contains()", "4. in()", 2],

["✓ Which method checks if two sets have no common elements?",
 "1. isdisjoint()", "2. issubset()", "3. union()", "4. intersect()", 1],

["✓ What is output of type(set())?",
 "1. list", "2. tuple", "3. set", "4. dict", 3],

["✓ Which function converts list to set?",
 "1. list()", "2. tuple()", "3. dict()", "4. set()", 4]

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

