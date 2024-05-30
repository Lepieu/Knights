# Knights
A Knights and Knaves game using propositional logic to have a computer determine queries given prior. This was submitted for the Harvard CS50 AI course.
logic.py contains all definitions for propositional logic, while puzzle.py contains the actual puzzles that are solved. If you wish to create and solve your own puzzle, you can wipe one of the knowledge sets and create your own puzzles inside it.

Puzzle 0 is the puzzle from the Background. It contains a single character, A.
    
    A says “I am both a knight and a knave.”

Puzzle 1 has two characters: A and B.
  
    A says “We are both knaves.”
    B says nothing.

Puzzle 2 has two characters: A and B.
    
    A says “We are the same kind.”
    B says “We are of different kinds.”
Puzzle 3 has three characters: A, B, and C.

    A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
    B says “A said ‘I am a knave.’”
    B then says “C is a knave.”
    C says “A is a knight.”
