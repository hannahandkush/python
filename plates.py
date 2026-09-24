def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:                              # Check minimum and maximum length
        return False

    if not s[0].isalpha() or not s[1].isalpha():          # Check first two characters are letters
        return False

    if not s.isalnum():                                   # Check for punctuation, spaces, etc. using isalnum (is alphanumeric)
        return False

    i = 0                                                 # introduces the variable (i) as a tempory counter, it will be equal to the position of the first character that is a number
    while i < len(s):                                     # if there are no numbers present this line will be false and the following checks will be skipped
        if s[i].isdigit():
            break
        i += 1                                            # adds one to i to check the next character in the sequence for the next cycle of the loop

    if i < len(s):                                        # checks the first number is not a 0
        if s[i] == '0':
            return False

        for j in range(i + 1, len(s)):                    # The for loop is used to test each character in the string that follows the first number, to see if it is a number
            if not s[j].isdigit():                        # the range function is used to generate the position of characters to be checked, held in the variable counter (j)
                return False

    return True


if __name__ == "__main__":
    main()
