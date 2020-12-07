import re


def parse_rule(rule):
    container_bag_regex = re.compile(r"(?P<CONTAINER_BAG>[\w\s]*) bags contain")
    inside_bags_regex = re.compile(r"(?P<NUMBER>\d+) (?P<INSIDE_BAG>[\w\s]*) bags?[,.]")

    container_bag = re.match(container_bag_regex, rule).group("CONTAINER_BAG")
    inside_bags = [(int(number), inside_bag) for number, inside_bag in re.findall(inside_bags_regex, rule)]
    return container_bag, inside_bags


input_data = open("input", "r")
rules = {key: value for key, value in map(parse_rule, input_data.readlines())}
input_data.close()

#PART1

possible_bag_colors = []


def search_bag_color(searched_bag_color):
    for key_bag in rules:
        for bag in rules[key_bag]:
            if searched_bag_color in bag and key_bag not in possible_bag_colors:
                possible_bag_colors.append(key_bag)
                search_bag_color(key_bag)


my_bag = "shiny gold"
search_bag_color(my_bag)

print(len(possible_bag_colors))

#PART2

my_bag = "shiny gold"


def calculate_inside_bags_number(bag_color):
    inside_bags_number = 1
    for number, inside_bag_color in rules[bag_color]:
        inside_bags_number += number * calculate_inside_bags_number(inside_bag_color)
    return inside_bags_number

# NEED TO -1, bc of its count top level bag itself ;(
print(calculate_inside_bags_number(my_bag)-1)
