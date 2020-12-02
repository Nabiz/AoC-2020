import re


def main():
    input_file = open("input", "r")
    list_of_passwords = input_file.readlines()
    input_file.close()

    correct_passwords_count = 0

    password_parser = re.compile(r"(?P<FIRST_POS>\d+)-(?P<SECOND_POS>\d+)\s(?P<LETTER>.):\s(?P<PASSWORD>.*)")
    for password_string in list_of_passwords:
        result = re.match(password_parser, password_string)
        first_pos = int(result.group("FIRST_POS"))
        second_pos = int(result.group("SECOND_POS"))
        letter = result.group("LETTER")
        password = result.group("PASSWORD")
        if (password[first_pos-1] == letter) ^ (password[second_pos-1] == letter):
            correct_passwords_count += 1
    return correct_passwords_count


if __name__ == '__main__':
    print(main())
