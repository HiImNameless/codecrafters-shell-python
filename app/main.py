import sys


def main():
    while True:
        sys.stdout.write("$ ")

        input = input()
        command = input.split()[0]

        match command:
            case "exit":
                break
            case "echo":
                echo(input)
            case "type":
                type(input)
            case _:
                error(command)

        

def error(command):
    print(f"{command}: not found")

def echo(command):
    print(f"{command[5:]}")  # Print everything after "echo "

#Determines how a command would be interpreted if it were used
def type(input):
    #List of commands categorized as built-ins
    built_in_commands = ["echo", "exit", "type"]

    #Stores the second word in the user's input
    argument = input.split()[1]  # Get the second word of the command

    #If the argument exists inside a list it prints the type otherwise it throws an error
    if argument in built_in_commands:
        print(f"{argument} is a shell builtin")
    else:
        error(argument)

if __name__ == "__main__":
    main()
