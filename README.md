# DFA Simulator

This project is a DFA simulator for Theoretical Foundations of Computer Science & Automata. The program reads a file (DFA.txt), prompts the user for a string to evaluate, and simulates whether the string is accepted or rejected by the DFA.

## How It Works

- **Input**: A file called DFA.txt that describes the DFA:
  - The number of states.
  - The accepting states.
  - The alphabet (set of valid symbols).
  - The transition table (defining state transitions for each symbol).
  
- **Simulation**: The user enters a string to evaluate, and the program simulates how the DFA processes the string.
  
- **Output**: The program prints a step-by-step transition of the DFA and whether the input string is ACCEPTED or REJECTED.

## Files

1. **dfa_simulator.py**: The main program that runs the DFA simulation.
2. **dfa_reader.py**: Reads the DFA from DFA.txt.
3. **dfa_state.py**: Defines the dfa_state class representing each DFA state.

## Running the Program

1. Make sure that you have a file called DFA.txt in the src folder. The file should follow this format:
   - Line 1: Number of states (integer).
   - Line 2: Space-separated list of accepting state numbers.
   - Line 3: Space-separated list of alphabet symbols.
   - Lines 4+: Transition table, one line per state, listing next states for each symbol.

2. cd into the projects src folder:
   ##### cd <path>

3. Run the dfa_simulator.py script:
   ##### python3 dfa_simulator.py

4. Enter a string to evaluate when prompted, or type Quit to exit.

