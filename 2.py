with open('input/2.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

opp_choices = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
scores = {'rock': 1, 'paper': 2, 'scissors': 3, 'win': 6, 'draw': 3, 'lose': 0}


def what_to_choose():
    my_choices = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    results = {'rock': {'rock': 'draw', 'paper': 'win', 'scissors': 'lose'},
               'paper': {'rock': 'lose', 'paper': 'draw', 'scissors': 'win'},
               'scissors': {'rock': 'win', 'paper': 'lose', 'scissors': 'draw'}}
    return calculate_score(my_choices, results)


def what_to_achieve():
    my_choices = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    results = {'rock': {'win': 'paper', 'draw': 'rock', 'lose': 'scissors'},
               'paper': {'win': 'scissors', 'draw': 'paper', 'lose': 'rock'},
               'scissors': {'win': 'rock', 'draw': 'scissors', 'lose': 'paper'}}
    return calculate_score(my_choices, results)


def calculate_score(my_choices, results):
    score = 0
    for line in lines:
        opp_choice, my_choice = opp_choices[line[0]], my_choices[line[2]]
        score += scores[my_choice] + scores[results[opp_choice][my_choice]]
    return score


print(what_to_choose())
print(what_to_achieve())
