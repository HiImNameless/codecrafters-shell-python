import sys


def main():
    while True:
        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        command = input()

        if command == "exit":
            break
        elif command.startswith("echo"):
            echo(command)
        else:
            error(command)

def error(command):
    print(f"{command}: command not found")

def echo(command):
    print

if __name__ == "__main__":
    main()
