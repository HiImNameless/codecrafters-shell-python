import sys
import os
import platform
import subprocess
from pathlib import Path

def main():
    while True:
        cwd = os.getcwd()
        sys.stdout.write("$ ")

        user_input = input()
        try:
            command = user_input.split()[0]
        except:
            continue

        match command:
            case "exit":
                break
            case "echo":
                echo(user_input)
            case "type":
                tested_command = user_input.split()[1]

                type(tested_command)
            case "pwd":
                pwd()
            case "cd":
                cd(user_input)
            case _:
                if type(command, "return") == "external":
                    file_path = path_exec_lookup(command)

                    run(user_input, file_path)
                else:
                    error(1, command)

def error(code, command):
    match code:
        case 1:
            print(f"{command}: not found")
        case 2:
            print(f"cd: {command}: No such file or directory")

def echo(command):
    print(f"{command[5:]}")  # Print everything after "echo "

def path_exec_lookup(file_name):     # Searches through the PATH directories for the first .exe file with execute permissions
    path_env = os.environ.get("PATH", "")   # Stores the PATH directory
    directories = path_env.split(os.pathsep) 
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

def type(command, mode = None):   # Determines and tells the user how a command would be interpreted if it were used

    built_in_commands = ["echo", "exit", "type", "pwd", "cd"]    # List of commands categorized as built-ins
    file_path = path_exec_lookup(command)   # Stores the file path to the executable file

    if mode == None:
        if command in built_in_commands:    # Checks whether the command is a builtin
            print(f"{command} is a shell builtin")
        elif file_path != None:     # Checks whether a file path was found
            print(f"{command} is {file_path}")
        else:
            error(1, command) 
    elif mode.lower() == "return":
        if command in built_in_commands:    # Checks whether the command is a builtin
            return "builtin"
        elif file_path != None:     # Checks whether a file path was found
            return "external"
        else:
            return None

def split_path_tail(path):  # Splits the a file path into a list at each / or \ depending on os and returns the final word in the list
    user_platform = platform.system()

    if user_platform == "Windows":
        list = path.split("\\")
    else:
        list = path.split("/")

    path_tail = list[len(list) - 1]

    return path_tail

def run(user_input, executable_path):
    arguments = user_input.split()[1:]

    process = subprocess.run([split_path_tail(executable_path)] + arguments, executable = executable_path)

def pwd():
    cwd = os.getcwd()
    print(cwd)
    return cwd

def cd(user_input):
    user_platform = platform.system()
    directory_path = user_input.split()[1]
    home_dir = Path.home()

    if os.path.isdir(directory_path):
        os.chdir(directory_path)
    elif directory_path == "~":
        if user_platform == "Linux":
            os.chdir(home_dir)
    else:
        error(2, directory_path)
    
if __name__ == "__main__":
    main()