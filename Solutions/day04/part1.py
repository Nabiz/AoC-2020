def main():
    input_file = open("input", "r")
    passports = input_file.read().split("\n\n")
    input_file.close()

    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]

    valid_passports_count = 0

    for passport in passports:
        for field in required_fields:
            if field+":" not in passport:
                break
        else:
            valid_passports_count += 1

    return valid_passports_count


if __name__ == '__main__':
    print(main())
