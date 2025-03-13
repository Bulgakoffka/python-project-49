from random import randint

from brain_games.scripts.brain_games_engine import brain_engine


def progression_game():
    task = 'What number is missing in the progression?'
    
    def get_expression():
        global progression
        progression = [(randint(1, 21)), ]
        progression_length = randint(5, 11)
        common_difference = randint(1, 10)

        while len(progression) < progression_length:
            next_term = progression[-1] + common_difference
            progression.append(next_term)

        hidden_progression = progression.copy()
        hide_index = randint(0, len(progression) - 1)
        hidden_progression[hide_index] = '..'
        return (str(hidden_progression).replace('[', '').replace(']', '')
                .replace(',', '').replace('\'', ''))

    def correct_answer(hidden_progression):
        hidden_progression_list = hidden_progression.split()
        str_progression = []

        for i in progression:
            str_progression.append(str(i))

        symmetric_difference = list((set(str_progression)
                                ^ set(hidden_progression_list)))[1]
        return symmetric_difference

    brain_engine(task, get_expression, correct_answer)


def main():
    progression_game()


if __name__ == '__main__':
    main()