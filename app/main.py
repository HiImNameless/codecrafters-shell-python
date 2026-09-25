import sys


def main():
    while True:
        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        command = input()
        if command == "exit":
            break
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
