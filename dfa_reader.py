"""
  dfa_reader.py
  Daniel Pavenko
  
  This program reads in "DFA.txt" which should be in the projects directory, sets the files data to their
  respective method variables and returns said variables (to be used by dfa_state & dfa_simulator)
"""

# read_dfa()
#
# This function reads through the "DFA.txt" file, sets method vars with the files read data and returns 
#   said data
def read_dfa():
    file_path = "DFA.txt" # Hardcoded input file, change this to whatever formatted dfa file you'd like
    with open(file_path, 'r') as file:
        num_of_states = int(file.readline().strip())  # Line 1: number of states
        accepting_states = list(map(int, file.readline().strip().split()))  # Line 2: accepting states
        alphabet = file.readline().strip().split()  # Line 3: alphabet
        transitions = []  # Lines 4+: transitions

        # Fill our transition table with the transitions
        for _ in range(num_of_states):
            transitions.append(list(map(int, file.readline().strip().split())))

    return num_of_states, accepting_states, alphabet, transitions
