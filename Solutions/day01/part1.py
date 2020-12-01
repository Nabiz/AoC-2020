def main():
    input_file = open("input", "r")
    expense_report = [int(x) for x in input_file.readlines()]
    input_file.close()
    target = 2020

    for i in range(len(expense_report)-1):
        for j in range(i+1, len(expense_report)):
            if expense_report[i] + expense_report[j] == target:
                return expense_report[i] * expense_report[j]


if __name__ == "__main__":
    print(main())
