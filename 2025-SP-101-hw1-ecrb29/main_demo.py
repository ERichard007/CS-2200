"""
This file contains examples of the syntax we will be using for state machines
and examples of how to use the helper functions.
"""
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from helper_funcs import code_to_jff, jff_to_code

# example DFA syntax
example_dfa = DFA(
    states={'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'0', '1'},
    transitions={
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q1', '1': 'q3'},
        'q3': {'0': 'q2', '1': 'q4'},
        'q4': {'0': 'q3', '1': 'q5'},
        'q5': {'0': 'q4', '1': 'q5'}
    },
    initial_state='q3',
    final_states={'q3'}
)

# example NFA syntax
example_nfa = NFA(
    states={"q0", "q1", "q2"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"": {"q1", "q2"}},
        "q1": {"0": {"q1"}, "1": {"q2"}},
        "q2": {"0": {"q1"}, "1": {"q2"}},
    },
    initial_state="q0",
    final_states={"q1"},
)

# example regular expression syntax
example_regex = "(a*ba*(a|b)*)|()"


########################################
"""code_to_jff() and jff_to_code()"""
########################################


"""
code_to_jff() takes a DFA or an NFA and writes it to a file that JFLAP can open
"""
# code_to_jff(nfa=example_nfa, file_name="example_nfa.jff")
# code_to_jff(dfa=example_dfa, file_name="example_dfa.jff")

"""
jff_to_code() takes a JFLAP file and reutrns an NFA
"""
# new_example_nfa = jff_to_code(file_name="example_nfa.jff")

