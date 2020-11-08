import numbers_generator
from cool_print import indent_print
from cool_print import ASCII_UCU_LOGO
import random
import time


def gen_field(ulam_numbers: list, lucky_numbers: list, even_numbers: list, height: int, length: int)-> list:
    """
    This function takes three lists of Ulam, lucky and even numbers and returns a game field as a list

    Precondition: height > 0 and length > 0
    Precondition: (height * length) % 3 == 0
    """
    num_elements = height * length

    field_set = set()

    counter = 0
    while len(field_set) < num_elements:
        if counter % 3 == 0:
            field_set.add(random.choice(ulam_numbers))
        elif counter % 3 == 1:
            field_set.add(random.choice(lucky_numbers))
        else:
            field_set.add(random.choice(even_numbers))
        counter += 1

    field = list(field_set)
    random.shuffle(field)

    return field


def gen_grid(field: list, height: int, width: int):
    """
    Precondition: len(field) == height*width
    Precondition height > 0 and width > 0

    Returns field as grid with specified height and width.
    Parameter field has to be a list of elements.
    """
    space_per_element = 6

    num_element = 0

    grid = ""

    grid += '\u2015'*(width*(space_per_element+1)+1) + '\n'
    for _ in range(height):
        for _ in range(width):
            grid += "|"

            grid += f"{field[num_element]:^{space_per_element}}"
            num_element += 1
        grid += '|\n'

        grid += '\u2015'*(width*(space_per_element+1)+1) + '\n'
    
    return grid


def intro():
    """
    Prints introduction to the game.
    """

    lines = ['*8 ранку, дзвонить будильник:\n\n',
            '"- dInG dOnG"',
            '*Я прокидаюся і розумію, що маю 10 іспитів із математичного аналізу. \nДо жодного з них я не готовий повністю... \n',
            'Закрити перший семестр мені допоможе тільки удача...\n',
            '*Підходячи до кабінету пана Степана, я зустрічаю одногрупника Богдана. Він уже все склав!!!',
            '*Він поділився секретом успіху: якщо я витягну білет за номером [even\\ulam\\lucky], мені попадеться найлегше завдання. Шанси успішно закрити сесію ще є!'
            ]

    indent_print(lines[0], 5, 0.08)
    time.sleep(1)
    indent_print(lines[1], 5, 0.05, prior_text=lines[0])
    time.sleep(2)

    indent_print(lines[2], 5, 0.08)
    time.sleep(1)
    indent_print(lines[3], 5, 0.08, lines[2])
    time.sleep(2)


def print_after_win(exams_left):
    """This function is used to print Fedynyak's words
    and gives info about how many exams are left to pass
    """

    lines = [
        '*Пан Фединяк\n\n',
        '"- угу:)"\n\n',
        'Кількість іспитів, які ще потрібно скласти: '
    ]

    indent_print(lines[0], 6, 0.1)
    time.sleep(1.5)
    indent_print(lines[1], 6, 0.07, lines[0])
    time.sleep(1.5)
    indent_print(lines[2] + str(exams_left), 6, 0.07, lines[0] + lines[1])
    time.sleep(2)


def print_after_loss(health):
    """This function is used to print Fedynyak's words
    and gives info about how many trials are left
    """

    lines = [
        '*Пан Фединяк\n\n',
        '"- не угу:( "\n\n',
        'Кількість спроб, що лишилися: '
    ]

    indent_print(lines[0], 6, 0.1)
    time.sleep(1.5)
    indent_print(lines[1], 6, 0.07, lines[0])
    time.sleep(1.5)
    indent_print(lines[2] + str(health), 6, 0.07, lines[0] + lines[1])
    time.sleep(2)


def check_answer() -> bool:
    """
    Checks if the user's guess is correct. Returns True if it is.
    Returns False if it isn't.
    """
    current_field = gen_field(ulam_nums, lucky_nums, even_nums, FIELD_HEIGHT, FIELD_WIDTH)

    # print grid
    print("\n"*25)
    indent_print("І С П И Т   П О Ч И Н А Є Т Ь С Я", 7, 0.1)
    time.sleep(2)
    print("\nМожливих перездач:", health)
    print("\nКількість іспитів, які ще потрібно скласти:", exams_left)
    print(gen_grid(current_field, FIELD_HEIGHT, FIELD_WIDTH), end='')
    time.sleep(2)

    # generate random task
    cur_task_num, cur_task_text = random.choice(TASKS)

    # print character's lines
    for char in '"Чорт, а їх багато."\n\r\r\r\r"Потрібно витягнути саме за номером ' + cur_task_text + '": ':
        print(char, end="", flush=True)
        time.sleep(0.09)

    user_guess = None
    try:
        user_guess = int(input())
    except ValueError:
        print("You should enter an integer!")

    if cur_task_num == 0:
        # check if user's number is lucky
        if user_guess in current_field and user_guess in lucky_nums:
            return True
    elif cur_task_num == 1:
        # check if user number is ulam
        if user_guess in current_field and user_guess in ulam_nums:
            return True
    else:
        # check if user number is even
        if user_guess in current_field and user_guess in even_nums:
            return True

    return False


lucky_nums = numbers_generator.gen_lucky(30)
ulam_nums = numbers_generator.gen_ulam(30)
even_nums = numbers_generator.gen_even(30)

FIELD_HEIGHT = 4
FIELD_WIDTH = 9
NUM_NUMBERS = FIELD_HEIGHT * FIELD_WIDTH

TASKS = [(0, "lucky"), (1, "Ulam"), (2, "even")]

intro()

exams_left = 10
health = 3
# game loop
while exams_left > 0 and health > 0:
    won = check_answer()

    if won:
        exams_left -= 1
        print_after_win(exams_left)
    else:
        health -= 1
        print_after_loss(health)

# print whether user won or failed
if exams_left == 0:
    indent_print('W I N !!!', 6, 0.1)
    time.sleep(1)
    indent_print('Я можу перейти на другий семестр! gg', 6, 0.07, 'W I N !!!\n\n')
else:
    indent_print('G A M E   O V E R', 6, 0.1)
    time.sleep(1)
    indent_print('PRESS "F" TO PAY RESPECT', 6, 0.07, 'G A M E   O V E R\n\n')

time.sleep(10)
