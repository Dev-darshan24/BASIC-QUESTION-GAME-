from rich import print

def ie():

    lis = [

["✓ Which keyword is used for decision making in Python?",
 "1. for", "2. while", "3. if", "4. switch", 3],

["✓ Which keyword is used when condition is false?",
 "1. elif", "2. else", "3. except", "4. finally", 2],

["✓ Which keyword is used for multiple conditions?",
 "1. if", "2. else", "3. elif", "4. case", 3],

["✓ Which operator is used to compare values?",
 "1. =", "2. ==", "3. !=", "4. Both 2 and 3", 4],

["✓ What is the output of: if 5 > 3?",
 "1. True", "2. False", "3. Error", "4. None", 1],

["✓ Which statement has no condition?",
 "1. if", "2. elif", "3. else", "4. All", 3],

["✓ Which indentation is correct in Python?",
 "1. Tabs or spaces", "2. Curly brackets",
 "3. Semicolon", "4. Parentheses", 1],

["✓ Which symbol is used to end if condition?",
 "1. ;", "2. :", "3. {}", "4. None", 2],

["✓ What does nested if mean?",
 "1. if inside if", "2. if inside else",
 "3. else inside if", "4. All", 4],

["✓ Which logical operator is used for AND condition?",
 "1. &&", "2. &", "3. and", "4. AND", 3],

["✓ Which logical operator is used for OR condition?",
 "1. ||", "2. |", "3. or", "4. OR", 3],

["✓ Which logical operator is used for NOT condition?",
 "1. !", "2. not", "3. != ", "4. none", 2],

["✓ What is output of: if 0?",
 "1. True", "2. False", "3. Error", "4. None", 2],

["✓ Which condition always returns False?",
 "1. 0", "2. None",
 "3. False", "4. All", 4],

["✓ Which statement is correct?",
 "1. if (a>b)", "2. if a>b:",
 "3. if a>b then", "4. if {a>b}", 2],

["✓ Which keyword is used for exception condition?",
 "1. else", "2. finally",
 "3. except", "4. catch", 3],

["✓ Can if be used without else?",
 "1. Yes", "2. No",
 "3. Sometimes", "4. Error", 1],

["✓ Which data type can be used in condition?",
 "1. int", "2. bool",
 "3. expressions", "4. All", 4],

["✓ Which block executes when condition is True?",
 "1. if", "2. else",
 "3. elif", "4. None", 1],

["✓ Which keyword is used to pass empty if block?",
 "1. break", "2. continue",
 "3. pass", "4. skip", 3]

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

