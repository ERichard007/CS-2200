from automata.fa.dfa import DFA

prob_1_6a = DFA(
    states={'q0','q1','q2','q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q2'},
	'q1': {'0': 'q1', '1': 'q1'},
	'q2': {'0': 'q3', '1': 'q2'},
	'q3': {'0': 'q3', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q3'}
)

