from random import randint
from brain_games.brain_engine.brain_games_engine import brain_engine


def progression_game():
    task = 'Find the greatest common divisor of given numbers.'
    def get_expression():
        progression = [(randint(1, 21)), ]
        progression_length = randint(5, 11)
        common_difference = randint(1, 10)

        while len(progression) < progression_length:
            next_term = progression[-1] + common_difference
            progression.append(next_term)

        hide_index = randint(0, len(progression) - 1)
        progression[hide_index] = '..'
        return (str(progression).replace('[', '').replace(']', '').replace(',', '')
                .replace('\'', ''))


    def correct_answer(hidden_progression):
        progression_list = []
        common_difference = 0
        for term in hidden_progression.split():
            progression_list.append(term)
        for i in progression_list[:-1]:
            next_i = progression_list[progression_list.index(i) + 1]
            if i != '..' and next_i != '..':
                common_difference = int(next_i) - int(i)
                break
        for i in progression_list:
            if i == '..' and progression_list.index(i) != 0:
                previous_i = progression_list[progression_list.index(i) - 1]
                return int(previous_i) + int(common_difference)
            elif i == '..' and progression_list.index(i) < len(progression_list) - 1:
                next_i = progression_list[progression_list.index(i) + 1]
                return int(next_i) - int(common_difference)
    brain_engine(task, get_expression, correct_answer)



def main():
    progression_game()


if __name__ == '__main__':
    main()