from rich import print

def dc():

    lis = [

["✓ Which bracket is used to create a dictionary?",
 "1. []", "2. ()", "3. {}", "4. <>", 3],

["✓ Dictionary in Python stores data in the form of?",
 "1. Values only", "2. Keys only", "3. Key–Value pairs", "4. Indexes", 3],

["✓ Which of the following creates an empty dictionary?",
 "1. {}", "2. dict()", "3. Both", "4. None", 3],

["✓ Are dictionary keys allowed to be duplicate?",
 "1. Yes", "2. No", "3. Sometimes", "4. Error", 2],

["✓ Are dictionary values allowed to be duplicate?",
 "1. Yes", "2. No", "3. Sometimes", "4. Error", 1],

["✓ Which method is used to get value of a key safely?",
 "1. value()", "2. get()", "3. fetch()", "4. find()", 2],

["✓ How do you access value of key 'a'?",
 "1. dict(a)", "2. dict['a']", "3. dict{'a'}", "4. dict.a", 2],

["✓ Which method returns all keys of dictionary?",
 "1. keys()", "2. values()", "3. items()", "4. get()", 1],

["✓ Which method returns all values of dictionary?",
 "1. keys()", "2. values()", "3. items()", "4. get()", 2],

["✓ Which method returns key-value pairs?",
 "1. keys()", "2. values()", "3. items()", "4. pairs()", 3],

["✓ Which method removes a specific key?",
 "1. remove()", "2. pop()", "3. delete()", "4. clear()", 2],

["✓ Which method removes the last inserted item?",
 "1. pop()", "2. popitem()", "3. remove()", "4. del()", 2],

["✓ Which method removes all items from dictionary?",
 "1. pop()", "2. popitem()", "3. clear()", "4. del()", 3],

["✓ Which function returns number of key-value pairs?",
 "1. size()", "2. count()", "3. len()", "4. total()", 3],

["✓ Which operator checks key existence in dictionary?",
 "1. has", "2. exist", "3. in", "4. check", 3],

["✓ Can dictionary contain mutable values like list?",
 "1. Yes", "2. No", "3. Sometimes", "4. Error", 1],

["✓ Which method copies a dictionary?",
 "1. copy()", "2. duplicate()", "3. clone()", "4. repeat()", 1],

["✓ Which method updates dictionary with another dictionary?",
 "1. add()", "2. merge()", "3. update()", "4. extend()", 3],

["✓ What is output of type({})?",
 "1. list", "2. tuple", "3. set", "4. dict", 4],

["✓ Which function converts list of tuples to dictionary?",
 "1. list()", "2. tuple()", "3. dict()", "4. set()", 3]

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

