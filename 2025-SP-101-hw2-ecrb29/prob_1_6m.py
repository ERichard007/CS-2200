from automata.fa.dfa import DFA

prob_1_6m = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1', ''},
    transitions={
        'q0': {'': 'q2', '0': 'q1', '1': 'q1'},
	'q1': {'': 'q1', '0': 'q1', '1': 'q1'},
	'q2': {'': 'q2', '0': 'q1', '1': 'q1'} 
    },
    initial_state='q0',
    final_states={'q2'}
)

