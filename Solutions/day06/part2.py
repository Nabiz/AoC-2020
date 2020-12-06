input_file = open("input")
answers = input_file.read().split("\n\n")
input_file.close()


def count_group_answers(group_answers):
    answers_count = 0
    group_answers = group_answers.split()
    for letter in range(ord("a"), ord("z") + 1):
        for person_answers in group_answers:
            if chr(letter) not in person_answers:
                break
        else:
            answers_count += 1
    return answers_count


print(sum(map(count_group_answers, answers)))
