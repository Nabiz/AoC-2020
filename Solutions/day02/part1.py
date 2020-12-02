import re


def main():
    input_file = open("input", "r")
    list_of_passwords = input_file.readlines()
    input_file.close()

    correct_passwords_count = 0

    password_parser = re.compile(r"(?P<MIN>\d+)-(?P<MAX>\d+)\s(?P<LETTER>.):\s(?P<PASSWORD>.*)")
    for password_string in list_of_passwords:
        result = re.match(password_parser, password_string)
        min_occurrences = int(result.group("MIN"))
        max_occurrences = int(result.group("MAX"))
        letter = result.group("LETTER")
        password = result.group("PASSWORD")
        if min_occurrences <= password.count(letter) <= max_occurrences:
            correct_passwords_count += 1
    return correct_passwords_count


if __name__ == '__main__':
    print(main())
