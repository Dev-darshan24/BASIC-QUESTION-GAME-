from rich import print

def li():

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

    ["✓ Which list allows duplicate values?",
    "1. List", "2. Set", "3. Tuple", "4. Dictionary", 1],

    ["✓ Which function converts tuple to list?",
    "1. tuple()", "2. list()", "3. set()", "4. dict()", 2],

    ["✓ What is output of len([])?",
    "1. 0", "2. 1", "3. Error", "4. None", 1],

    ["✓ Which slicing gets all elements?",
    "1. list[:]", "2. list[0]", "3. list[-1]", "4. list[1:]", 1],

    ["✓ What does list[-1] return?",
    "1. First element", "2. Second element", "3. Last element", "4. Error", 3],

    ["✓ Which operator repeats a list?",
    "1. +", "2. *", "3. /", "4. %", 2],

    ["✓ Which operator joins two lists?",
    "1. *", "2. +", "3. -", "4. /", 2],

    ["✓ Which method reverses the list?",
    "1. sort()", "2. reverse()", "3. swap()", "4. change()", 2],

    ["✓ What is output of type([])?",
    "1. tuple", "2. set", "3. list", "4. dict", 3],

    ["✓ Which list index gives last element?",
    "1. 0", "2. 1", "3. -1", "4. -2", 3],

    ["✓ Which function gives maximum value?",
    "1. max()", "2. high()", "3. big()", "4. large()", 1],

    ["✓ Which function gives minimum value?",
    "1. min()", "2. small()", "3. low()", "4. tiny()", 1],

    ["✓ Can list store different data types?",
    "1. Yes", "2. No", "3. Sometimes", "4. Error", 1],

    ["✓ Which keyword checks element existence?",
    "1. in", "2. has", "3. exist", "4. check", 1],

    ["✓ What does list.pop(0) do?",
    "1. Removes last element", "2. Removes first element", "3. Clears list", "4. Error", 2],

    ["✓ Which method copies a list?",
    "1. copy()", "2. duplicate()", "3. clone()", "4. repeat()", 1],

    ["✓ What is output of [] == [] ?",
    "1. True", "2. False", "3. Error", "4. None", 1],

    ["✓ Which loop is commonly used with lists?",
    "1. for", "2. while", "3. do-while", "4. switch", 1],

    ["✓ What does sum([1,2,3]) return?",
    "1. 6", "2. 123", "3. Error", "4. None", 1],

    ["✓ Which list method counts elements?",
    "1. count()", "2. len()", "3. size()", "4. total()", 1],

    ["✓ What does list.insert(1,10) do?",
    "1. Add at end", "2. Add at index 1", "3. Remove element", "4. Replace list", 2],

    ["✓ Which method removes element by index?",
    "1. remove()", "2. pop()", "3. delete()", "4. clear()", 2],

    ["✓ What is output of list(range(3))?",
    "1. [1,2,3]", "2. [0,1,2]", "3. [0,1,2,3]", "4. Error", 2],

    ["✓ Which keyword creates empty list?",
    "1. list()", "2. []", "3. Both", "4. None", 3],

    ["✓ Which list method modifies original list?",
    "1. sort()", "2. sorted()", "3. order()", "4. arrange()", 1],

    ["✓ What does list.clear() return?",
    "1. Empty list", "2. None", "3. 0", "4. Error", 2],

    ["✓ Which operation is faster for lists?",
    "1. Append", "2. Insert", "3. Delete middle", "4. Sort", 1],

    ["✓ Which method removes first matching value?",
    "1. pop()", "2. remove()", "3. clear()", "4. del()", 2],

    ["✓ Which list is a nested list?",
    "1. [1,2,3]", "2. [[1,2],[3,4]]", "3. (1,2)", "4. {1,2}", 2],

    ["✓ Which function converts string to list?",
    "1. list()", "2. split()", "3. str()", "4. tuple()", 1],

    ["✓ What is output of [1,2,3][::-1]?",
    "1. [1,2,3]", "2. [3,2,1]", "3. Error", "4. None", 2]

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

