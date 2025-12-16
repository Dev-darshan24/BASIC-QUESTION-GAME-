from rich import print

def cl():

    lis = [

["✓ What is a class in Python?",
 "1. Collection of functions", "2. Blueprint of object",
 "3. Data type", "4. Module", 2],

["✓ Which keyword is used to define a class?",
 "1. define", "2. function", "3. class", "4. struct", 3],

["✓ What is an object?",
 "1. Blueprint", "2. Instance of class",
 "3. Function", "4. Variable", 2],

["✓ Which function is called automatically when object is created?",
 "1. init()", "2. constructor()", "3. __init__()", "4. create()", 3],

["✓ What does self refer to?",
 "1. Class", "2. Object",
 "3. Module", "4. Function", 2],

["✓ Which keyword is used to create object?",
 "1. new", "2. create",
 "3. class", "4. No keyword needed", 4],

["✓ Can a class have multiple objects?",
 "1. Yes", "2. No",
 "3. Sometimes", "4. Error", 1],

["✓ Which method represents constructor?",
 "1. __start__()", "2. __create__()",
 "3. __init__()", "4. __self__()", 3],

["✓ Which access specifier is default in Python?",
 "1. Public", "2. Private",
 "3. Protected", "4. None", 1],

["✓ How do you access variable of class?",
 "1. class.variable", "2. object.variable",
 "3. Both", "4. None", 3],

["✓ What is inheritance?",
 "1. Creating object", "2. One class acquiring properties of another",
 "3. Deleting class", "4. Copying object", 2],

["✓ Which keyword is used for inheritance?",
 "1. extends", "2. inherit",
 "3. super", "4. No keyword", 4],

["✓ Which function returns class name of object?",
 "1. type()", "2. class()",
 "3. name()", "4. isinstance()", 1],

["✓ What does isinstance(obj, Class) return?",
 "1. Object", "2. True/False",
 "3. Class name", "4. Error", 2],

["✓ Which concept allows method with same name?",
 "1. Inheritance", "2. Polymorphism",
 "3. Encapsulation", "4. Abstraction", 2],

["✓ Which concept hides data?",
 "1. Inheritance", "2. Polymorphism",
 "3. Encapsulation", "4. Abstraction", 3],

["✓ What is method overriding?",
 "1. Same method in same class",
 "2. Same method in child class",
 "3. Different method name",
 "4. Error", 2],

["✓ Which symbol is used for protected members?",
 "1. __", "2. _",
 "3. #", "4. &", 2],

["✓ Which symbol is used for private members?",
 "1. _", "2. __",
 "3. #", "4. &", 2],

["✓ Can Python class have multiple constructors?",
 "1. Yes", "2. No",
 "3. Sometimes", "4. Error", 2]

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

