"""
  dfa_simulator.py
  Daniel Pavenko

  This program simulates / computes our DFA using the data from our dfa_reader and the states of our
  dfa_state class.
"""
from dfa_reader import read_dfa
from dfa_state import dfa_state

# Constants
START_STATE = 0 # The start state num

# simulate_dfa
#
# Function that simulates / computes the given DFA
#
# param states: List of dfa_state objects representing the DFA's states
# param alphabet: The DFA's alphabet (list of characters)
# param input_string: The string to evaluate
def simulate_dfa(states, alphabet, input_string):
    # Starts the simulation at the start state by looking through the states list for the start state
    current_state = next(state.state_num for state in states if state.is_start)
    valid = True

    print(">>> Computation...")
    while len(input_string) > 0: 
        print(f"{current_state},{input_string} -> ", end="")

        # Get the next state
        next_state = states[current_state].get_next_state(input_string[0], alphabet)
        if next_state is None: # Check for valid input
            print("INVALID INPUT")
            valid = False
            break

        current_state = next_state
        # Essentially remove the first char since we've already processed it
        input_string = input_string[1:]

        # If there are still chars in our input string
        if input_string:
            print(f"{current_state},{input_string}")
        else:
            # Don't print a comma before the empty string transition
            print(f"{current_state},", end="")

    # If the input was invalid, print REJECTED
    if not valid:
        print("REJECTED")
    else:
        # After processing the entire input string, print the last state with {e} (empty string)
        print(f"{{e}}")

        # Final state check
        if states[current_state].is_accepting:
            print("ACCEPTED") 
        else:
            print("REJECTED")

# main()
#
# Main method to initialize the DFA, prompt user for input and simulate the DFA
def main():
    print(">>> Loading DFA.txt…")
    
    # Read DFA configuration from "DFA.txt"
    num_of_states, accepting_states, alphabet, transitions = read_dfa()

    # Create DFA states, marking the start and accepting states
    states = []
    for state_num in range(num_of_states):
        is_accepting = state_num in accepting_states # True if state is in our accepting states list
        is_start = (state_num == START_STATE)  # State 0 is always our start state
        # Create a state filled with relevant data gathered
        state = dfa_state(state_num, transitions[state_num], is_accepting, is_start)
        states.append(state) # Add the newly created state object to our list of state objects

    # Input loop
    while True:
        input_string = input(">>> Please enter a string to evaluate (or 'Quit' to exit): ")
        if input_string.lower() == "quit":
            print(">>> Goodbye!")
            break
        else:
          # Simulate the DFA for the given input string
          simulate_dfa(states, alphabet, input_string)

# Entry point, prevents main() from running automatically if imported
if __name__ == "__main__":
    main()
