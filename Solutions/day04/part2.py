input_file = open("input", "r")
passports = input_file.read().split("\n\n")
input_file.close()
passports = [passport.replace("\n", " ").split(" ") for passport in passports]


def convert_passport_to_dict(passport):
    result = []
    for field in passport:
        result.append(field.split(':'))
    return dict(result)


passports = list(map(convert_passport_to_dict, passports))


def remove_not_completed_passports(passports):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    completed_passports = []
    for passport in passports:
        for field in required_fields:
            if field not in passport.keys():
                break
        else:
            completed_passports.append(passport)
    return completed_passports


passports = remove_not_completed_passports(passports)


def validate_passport(passport):
    if not (1920 <= int(passport["byr"]) <= 2002):
        return False
    if not (2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not (2020 <= int(passport["eyr"]) <= 2030):
        return False

    if "cm" in passport["hgt"]:
        if not (150 <= int(passport["hgt"].replace("cm", "")) <= 193):
            return False
    elif "in" in passport["hgt"]:
        if not (59 <= int(passport["hgt"].replace("in", "")) <= 76):
            return False
    else:
        return False

    if passport["hcl"][0] != "#" or len(passport["hcl"]) != 7:
        return False

    if not passport['hcl'][1:6].isalnum():
        return False

    if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False

    if len(passport["pid"]) != 9:
        return False
    if not passport["pid"].isnumeric():
        return False

    return True


second_part_valid_passwords = 0

for passport in passports:
    if validate_passport(passport):
        second_part_valid_passwords += 1

print(second_part_valid_passwords)
