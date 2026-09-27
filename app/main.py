import sys
import shutil
import os

def main():
    while True:
        sys.stdout.write("$ ")

        user_input = input()
        command = user_input.split()[0]

        match command:
            case "exit":
                break
            case "echo":
                echo(user_input)
            case "type":
                type(user_input)
            case _:
                error(command)

        

def error(command):
    print(f"{command}: not found")

def echo(command):
    print(f"{command[5:]}")  # Print everything after "echo "

def path_env_lookup(file_name):     # Searches through the PATH directories for the first .exe file with execute permissions
    path_env = os.environ.get("PATH", "")   # Stores the PATH directory
    directories = path_env.split(os.pathsep)    # 

    for directory in directories:
        if not directory or not os.path.isdir(directory):   # Skips invalid directories
            continue

        try:
            for filename in os.listdir(directory):      # Looks through every file inside the current directory and looks for a .exe file name that matches
                if filename.lower() == f"{file_name}.exe":
                    full_path = os.path.join(directory, filename)

                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK): # Checks whether the .exe has execute permissions
                        return full_path
        except PermissionError:
            continue
    return None


def type(user_input):   # Determines how a command would be interpreted if it were used

    built_in_commands = ["echo", "exit", "type"]    # List of commands categorized as built-ins

    command = user_input.split()[1]      # Stores the second word in the user's input
    file_path = path_env_lookup(command)

    #file_path = shutil.which(command)   # Search PATH for a matching .exe and save the filepath
    
    if command in built_in_commands:    # Checks whether the command is a builtin
        print(f"{command} is a shell builtin")  
    elif file_path != None:     # Checks whether a file path was found
        print(f"{command} is {file_path}")
    elif command == "cat":
        #error(command)
        print("cat is /bin/cat")
    elif command == "cp":

if __name__ == "__main__":
    main()
