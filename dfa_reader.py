"""
  dfa_reader.py
  Daniel Pavenko
  This program reads in "DFA.txt", which should be in the projects directory, and sets the files data as
  vars
"""

# read_dfa(file_path)
# This function reads through the DFA.txt file and sets the correct vars with the files read data.
def read_dfa():
    file_path = 'DFA.txt'
    with open(file_path, 'r') as file:
        num_states = int(file.readline().strip())  # Line 1: number of states
        accepting_states = list(map(int, file.readline().strip().split()))  # Line 2: accepting states
        alphabet = file.readline().strip().split()  # Line 3: alphabet
        transitions = []  # Lines 4+: transitions

        # Fill our transition table with the transitions
        for _ in range(num_states):
            transitions.append(list(map(int, file.readline().strip().split())))

    return num_states, accepting_states, alphabet, transitions

# Testing
#num_states, accepting_states, alphabet, transitions = read_dfa()
#print(f"Number of states: {num_states}")
#print(f"Accepting states: {accepting_states}")
#print(f"Alphabet: {alphabet}")
#print(f"Transitions: {transitions}")
