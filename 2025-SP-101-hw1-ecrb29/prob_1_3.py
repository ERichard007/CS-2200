from automata.fa.dfa import DFA

prob_1_3 = DFA(
    states={'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'u', 'd'},
    transitions={
        'q1': {'u': 'q1', 'd': 'q2'},
        'q2': {'u': 'q1', 'd': 'q3'},
        'q3': {'u': 'q2', 'd': 'q4'},
        'q4': {'u': 'q3', 'd': 'q5'},
        'q5': {'u': 'q4', 'd': 'q5'}
    },
    initial_state='q3',
    final_states={'q3'}
)

