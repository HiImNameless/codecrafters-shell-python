import sys
import os
import platform
import subprocess

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
                tested_command = user_input.split()[1]

                type(tested_command)
            case _:
                if type_return(command) == "external":
                    file_path = path_exec_lookup(command)

                    run(user_input, file_path)
                else:
                    error(1, command)

        

def error(code, command):
    match code:
        case 1:
            print(f"{command}: not found")

def echo(command):
    print(f"{command[5:]}")  # Print everything after "echo "

def path_exec_lookup(file_name):     # Searches through the PATH directories for the first .exe file with execute permissions
    path_env = os.environ.get("PATH", "")   # Stores the PATH directory
    directories = path_env.split(os.pathsep)    # 
    user_platform = platform.system()   # Stores the user's operating system

    for directory in directories:
        if not directory or not os.path.isdir(directory):   # Skips invalid directories
            continue
        
        try:
            if user_platform == "Windows":
                for filename in os.listdir(directory):      # Looks through every file inside the current directory and looks for a .exe file name that matches
                    if filename.lower() == f"{file_name}.exe":
                        full_path = os.path.join(directory, filename)

                        if os.path.isfile(full_path) and os.access(full_path, os.X_OK): # Checks whether the .exe has execute permissions
                            return full_path
            else:
                for filename in os.listdir(directory):      # Looks through every file inside the current directory and looks for a .exe file name that matches
                    if filename.lower() == f"{file_name}":
                        full_path = os.path.join(directory, filename)

                        if os.path.isfile(full_path) and os.access(full_path, os.X_OK): # Checks whether the .exe has execute permissions
                            return full_path
                
        except PermissionError:
            continue
    return None

def type(command):   # Determines and tells the user how a command would be interpreted if it were used

    built_in_commands = ["echo", "exit", "type"]    # List of commands categorized as built-ins
    file_path = path_exec_lookup(command)   # Stores the file path to the executable file

    if command in built_in_commands:    # Checks whether the command is a builtin
        print(f"{command} is a shell builtin")
    elif file_path != None:     # Checks whether a file path was found
        print(f"{command} is {file_path}")
    else:
        error(1, command) 

def type_return(command):   # Determines the command's type and returns the value
    built_in_commands = ["echo", "exit", "type"]    # List of commands categorized as built-ins
    file_path = path_exec_lookup(command)   # Stores the file path to the executable file
        
    if command in built_in_commands:    # Checks whether the command is a builtin
        return "builtin"
    elif file_path != None:     # Checks whether a file path was found
        return "external"
    else:
        return None

def run(user_input, executable_path):
    arguments = user_input.split()[1:]

    process = subprocess.run([executable_path] + arguments)
    sys.exit(0)


if __name__ == "__main__":
    main()