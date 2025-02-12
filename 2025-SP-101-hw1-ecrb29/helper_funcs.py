"""
Contains code_to_jff() and jff_to_code()
"""
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def code_to_jff(dfa: DFA = None, nfa: NFA = None, file_name: str = "out.jff") -> None:
    """
    Takes a DFA or NFA and prints it to a .jff file in XML.
    """
    if (dfa is not None) and (nfa is not None):
        export_str = "BOTH A DFA AND AN NFA WERE PASSED IN"
    elif dfa is not None:
        # Get 5-tuple in mutable form
        states = list(dfa.states)
        input_symbols = list(dfa.input_symbols)
        transitions = dict(dfa.transitions)
        for i in transitions.keys():
            transitions[i] = dict(transitions[i])
        initial_state = str(dfa.initial_state)
        final_states = list(dfa.final_states)

        # Initialize XML String
        export_str = '<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 7.1.--><structure>&#13;\n'
        export_str += "\t<type>fa</type>&#13;\n"
        export_str += "\t\t<automaton>&#13;\n"

        # States
        export_str += "\t\t<!--The list of states.-->&#13;\n"
        x = 100.0
        y = 100.0
        for i in range(len(states)):
            export_str += (
                '\t\t<state id="' + str(i) + '" name="' + str(states[i]) + '">&#13;\n'
            )
            export_str += "\t\t\t<x>" + str(x) + "</x>&#13;\n"
            export_str += "\t\t\t<y>" + str(y) + "</y>&#13;\n"
            if str(states[i]) == initial_state:
                export_str += "\t\t\t<initial/>&#13;\n"
            if states[i] in final_states:
                export_str += "\t\t\t<final/>&#13;\n"
            if (i % 5) != 4:
                x += 100.0
            if (i % 5) == 4:
                y += 100.0
                x -= 400.0
            export_str += "\t\t</state>&#13;\n"

        # Transitions
        export_str += "\t\t<!--The list of transitions.-->&#13;\n"
        for start in transitions.keys():
            for trans in transitions[start].keys():
                export_str += "\t\t<transition>&#13;\n"
                export_str += (
                    "\t\t\t<from>" + str(states.index(start)) + "</from>&#13;\n"
                )
                export_str += (
                    "\t\t\t<to>"
                    + str(states.index(transitions[start][trans]))
                    + "</to>&#13;\n"
                )
                if trans == "":
                    export_str += "\t\t\t<read/>&#13;\n"
                else:
                    export_str += "\t\t\t<read>" + str(trans) + "</read>&#13;\n"
                export_str += "\t\t</transition>&#13;\n"

        # Ending Lines
        export_str += "\t</automaton>&#13;\n"
        export_str += "</structure>"
    elif nfa is not None:
        # Get 5-tuple in mutable form
        states = list(nfa.states)
        input_symbols = list(nfa.input_symbols)
        transitions = dict(nfa.transitions)
        for i in transitions.keys():
            transitions[i] = dict(transitions[i])
            for j in transitions[i].keys():
                transitions[i][j] = list(transitions[i][j])
        initial_state = str(nfa.initial_state)
        final_states = list(nfa.final_states)

        # Initialize XML String
        export_str = '<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 7.1.--><structure>&#13;\n'
        export_str += "\t<type>fa</type>&#13;\n"
        export_str += "\t\t<automaton>&#13;\n"

        # States
        export_str += "\t\t<!--The list of states.-->&#13;\n"
        x = 100.0
        y = 100.0
        for i in range(len(states)):
            export_str += (
                '\t\t<state id="' + str(i) + '" name="' + str(states[i]) + '">&#13;\n'
            )
            export_str += "\t\t\t<x>" + str(x) + "</x>&#13;\n"
            export_str += "\t\t\t<y>" + str(y) + "</y>&#13;\n"
            if str(states[i]) == initial_state:
                export_str += "\t\t\t<initial/>&#13;\n"
            if states[i] in final_states:
                export_str += "\t\t\t<final/>&#13;\n"
            if (i % 5) != 4:
                x += 100.0
            if (i % 5) == 4:
                y += 100.0
                x -= 400.0
            export_str += "\t\t</state>&#13;\n"

        # Transitions
        export_str += "\t\t<!--The list of transitions.-->&#13;\n"
        for start in transitions.keys():
            for trans in transitions[start].keys():
                for end in transitions[start][trans]:
                    export_str += "\t\t<transition>&#13;\n"
                    export_str += (
                        "\t\t\t<from>" + str(states.index(start)) + "</from>&#13;\n"
                    )
                    export_str += "\t\t\t<to>" + str(states.index(end)) + "</to>&#13;\n"
                    if trans == "":
                        export_str += "\t\t\t<read/>&#13;\n"
                    else:
                        export_str += "\t\t\t<read>" + str(trans) + "</read>&#13;\n"
                    export_str += "\t\t</transition>&#13;\n"

        # Ending Lines
        export_str += "\t</automaton>&#13;\n"
        export_str += "</structure>"
    else:
        export_str = "NO DFA OR NFA WAS PASSED IN"

    f_out = open(file_name, "w")
    f_out.write(export_str)
    f_out.close()
    return None


def jff_to_code(file_name: str) -> NFA:
    """
    Takes a .jff file and returns an NFA.
    """
    # Get file contents
    f_in = open(file_name, "r")
    lines = f_in.readlines()
    f_in.close()

    # init params
    states = []
    input_symbols = []
    trans = {}
    initial_state = ""
    final_states = []

    states_list_start = lines.index("\t\t<!--The list of states.-->&#13;\n")
    trans_list_start = lines.index("\t\t<!--The list of transitions.-->&#13;\n")
    trans_list_end = lines.index("\t</automaton>&#13;\n")

    # Get initial state
    for i in range(states_list_start + 1, trans_list_start):
        if lines[i][:11] == "\t\t\t<initial":
            initial_state = lines[i - 3].split('"')[3]

    # Get final state
    for i in range(states_list_start + 1, trans_list_start):
        if lines[i][:9] == "\t\t\t<final":
            final_states.append(lines[i - 3].split('"')[3])

    # Get states
    for i in range(states_list_start + 1, trans_list_start):
        if lines[i][:8] == "\t\t<state":
            states.append(lines[i].split('"')[3])

    # Get transitions and input symbols
    to_ind = []
    from_ind = []
    trans_symbol = []
    for i in range(trans_list_start + 1, trans_list_end):
        if lines[i][:8] == "\t\t\t<from":
            from_ind.append(int(lines[i].split("<from>")[1].split("</from>")[0]))
            to_ind.append(int(lines[i + 1].split("<to>")[1].split("</to>")[0]))
            tmp = (
                lines[i + 2]
                .strip()
                .split("<read/>")[0]
                .split("</read>")[0]
                .split("<read>")
            )
            tmp.reverse()
            trans_symbol.append(tmp[0])

    input_symbols = set(trans_symbol)
    for i in states:
        temp_dict = {}
        for j in input_symbols:
            temp_list = []
            for n in range(len(from_ind)):
                if (states.index(i) == from_ind[n]) and (j == trans_symbol[n]):
                    # print(f"{i} --{j}--> {states[to_ind[n]]}")
                    temp_list.append(states[to_ind[n]])
            temp_dict[j] = set(temp_list)
        trans[i] = temp_dict
    input_symbols.discard("")

    # Make the NFA
    return_nfa = NFA(
        states=set(states),
        input_symbols=input_symbols,
        transitions=trans,
        initial_state=initial_state,
        final_states=set(final_states),
    )
    return return_nfa
