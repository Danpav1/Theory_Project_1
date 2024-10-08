"""
  dfa_state.py
  Daniel Pavenko
  This program is a class that houses our dfa_state object, it is used when we simulate and compute or DFA
"""
class dfa_state:
  
    # __init__
    # This is our constructor, it initializes a dfa_state with the params as instance variables
    # param state_num: The integer representing our state number (0 being start)
    # param transitions: A list where each index corresponds to a symbol from the alphabet and contains
    #                    the state to transition to for that symbol
    # param is_accepting: Boolean showing whether this state is an accepting state
    # param is_start: Boolean showing whether this state is the start state (state num = 0) 
    def __init__(self, state_num, transitions, is_accepting=False, is_start=False):
        self.state_num = state_num  # State number of this node (state)
        self.transitions = transitions  # List of transitions for each symbol in the alphabet
        self.is_accepting = is_accepting  # True if this state is an accepting state
        self.is_start = is_start # True if this is the start Node (state)

    # get_next_state
    # Function that gets the next state on a given input symbol
    # param symbol: The input symbol (a character from the alphabet)
    # param alphabet: The DFA's alphabet (a list of characters)
    # return: The next state number, or None if the symbol is not in the alphabet
    def get_next_state(self, symbol, alphabet):
        if symbol in alphabet:
            # Find the index of the symbol in the alphabet
            symbol_index = alphabet.index(symbol)
            # Return the state the current node transitions to on this symbol
            return self.transitions[symbol_index]
        else:
            # Return None if the symbol is not part of the alphabet (invalid input)
            return None