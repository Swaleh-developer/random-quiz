import random

answer_1 = "Yes"
answer_2 = "Not a chance"
answer_3 = "Only skys knows"
answer_4 = "Without a doubt"
answer_5 = "Ask again later"

def answer_one_question():
    answer_number = random.randint(1, 5)
    if answer_number == 1:
        print(answer_1)
    if answer_number == 2:
        print(answer_2)
    if answer_number == 3:
        print(answer_3)
    if answer_number == 4:
        print(answer_4)
    if answer_number == 5:
        print(answer_5)


def main():
    question = input("Ask a yes or no question: ")
    while question != "":
        answer_one_question()
        question = input("Ask a yes or no question: ")

if __name__ == "__main__":
    main()




