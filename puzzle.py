from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

baseRules = And(
    Biconditional(AKnight, Not(AKnave)), #if A is a truthsayer, A must also not be a liar
    Biconditional(BKnight, Not(BKnave)), #if B is a truthsayer, B must also not be a liar
    Or(AKnight, AKnave),
    Or(BKnight, BKnave)
)
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    baseRules,
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    baseRules,
    Implication(AKnight, And(AKnave, BKnave)), #If A is truthful, they are both knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    baseRules,
    Implication(AKnight, BKnight), #If A is truthful, B is a knight because they are the same type
    Implication(BKnight, AKnave), #If B is truthful, A is a knave because they are not the same type
    Implication(AKnave, BKnight), #If A is lying, they are not the same type
    Implication(BKnave, AKnave) #If B is lying, A is the same type
)   
    



baseRulesForThree = And(
    #If someone is a knight, they are not a knave
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    baseRulesForThree,
    Implication(AKnight, Or(
        AKnight,
        AKnave
    )),
    Implication(AKnave, Or(
        AKnave,
        AKnight
    )),

    Implication(BKnight, And(
        Implication(AKnight, AKnave),
        Implication(AKnave, AKnight),
        CKnave)),
    Implication(BKnave, Not(CKnave)),
    
    Implication(CKnight, AKnight)
    # TODO
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
