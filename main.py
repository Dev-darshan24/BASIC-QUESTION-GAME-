from list2 import li
from dict2 import dc
from sets2 import se
from tuple2 import tu
from class2 import cl
from ifelse import ie
from rich import print


while True:
    try:
        greet = "[bold blue]Welcome to Question Game[/bold blue]"
        print("{:^70}".format(greet))
        print("[green]Topics :\n1. class \n2. List\n3. Tuple\n4. Set\n5. Dictionary\n6. If-else\n7. Exit[/green]")
        a= int(input("Select topic: "))
        try:
            if a == 1:
                cl()
            elif a == 2:
                li()
            elif a == 3:
                tu()
            elif a == 4:
                se()
            elif a == 5:
                dc()
            elif a == 6:
                ie()
            elif a == 7:
                break
            else:
                print("Invalid Input..")
        except Exception as e:
            print("Give proper value...")

    except Exception as f:
        print("Choose proper number...")