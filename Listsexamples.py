def run():
    running = True
    lines = []
    while running:
        # Get user input and start processing it
        command = input("> ")

        if command == "q":
            running = False
        elif command == "h":
            print("i - input new line")
            print("p - print current lines")
            print("d - delete last line")
            print("r - reverse the order of the lines")
            print("s - shift the lines")
        elif command == "i":
            # Input
            # Prompt the user to add a new line
            # at the end of the input.
            new_val = input("+ ")
            lines.append(new_val)
        elif command == "p":
            # Print
            # Print out each line with line numbers.
            # Note that these line numbers start at 1,
            # but the actual indexes are 0-based.
            for i in range(len(lines)):
                print(str(i + 1) + " " + lines[i])
        elif command == "d":
            # Delete (not disemvowel)
            # Delete the last line of the text.
            if len(lines) > 0:
                lines.pop(len(lines) - 1)
        elif command == "r":
            # Reverse the order of the lines
            lines.reverse()
        elif command == "s":
            # Shift the lines by one
            if len(lines) > 1:
                lines = lines[1:] + lines[:1]
        else:
            print("Sorry.")

if __name__ == "__main__":
    run()
