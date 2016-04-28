"""AStar.py
Jordan Hand, CSE 415, Spring 2015, University of Washington
Instructor: S. Tanimoto

Solves a given puzzle with a given initial state using a give
heuristic function. Finds the solution using A* search.

Uses python 3.X, tested with python 3.5

Usage:
    python3 AStar.py EightPuzzleWithHeuristics h_euclidean puzzle2a.py
"""

import sys
import importlib

if len(sys.argv) < 2:
    import EightPuzzle as Problem
else:
    Problem = importlib.import_module(sys.argv[1])

puzzle = sys.argv[3].split(".")[0]
STATE = importlib.import_module(puzzle).CREATE_INITIAL_STATE()
H_FUNCTION = Problem.HEURISTICS[sys.argv[2]]
FVALUE = {}


print("\nWelcome to A* search")
BACKLINKS = {}


def runAStar():
    """
    Starts A* search with the given initial state to find a solution to
    Problem. The solution is gaurunteed to be the shortest path if
    H_FUNCTION is admissable.
    """
    aStar(STATE)
    print(str(COUNT) + " states examined")


def aStar(initial_state):
    """
    Conducts an A* search using H_FUNCTION as a heuristic to find a solution
    to Problem.
    """
    global COUNT, BACKLINKS, STATE, H_FUNCTION, FVALUE

    GVALUE = {}
    FVALUE = {}

    OPEN = [initial_state]
    CLOSED = []
    BACKLINKS[Problem.HASHCODE(initial_state)] = -1
    GVALUE[Problem.HASHCODE(initial_state)] = 0
    FVALUE[Problem.HASHCODE(initial_state)] = f(initial_state, GVALUE)
    COUNT = 1

    arc_length = 1

    while OPEN != []:
        temp = delete_min(OPEN)
        CLOSED.append(temp)
        COUNT += 1
        if Problem.GOAL_TEST(temp):
            return backtrace(temp)

        for op in Problem.OPERATORS:
            if op.precond(temp):
                new_state = op.state_transf(temp)
                hc_new = Problem.HASHCODE(new_state)
                hc_temp = Problem.HASHCODE(temp)
                if not (occurs_in(new_state, CLOSED) or
                        occurs_in(new_state, OPEN)):
                    GVALUE[hc_new] = GVALUE[hc_temp] + arc_length
                    FVALUE[hc_new] = f(new_state, GVALUE)
                    OPEN.append(new_state)
                    BACKLINKS[hc_new] = temp
                else:
                    z = BACKLINKS[hc_new]
                    if z != -1:
                        new_f = FVALUE[hc_new] -\
                                GVALUE[Problem.HASHCODE(z)] +\
                                GVALUE[hc_temp]
                    else:
                        new_f = FVALUE[hc_new]

                    if new_f < FVALUE[hc_new]:
                        GVALUE[hc_new] = GVALUE[hc_temp] + arc_length
                        FVALUE[hc_new] = new_f
                        if new_state in OPEN:
                            deep_delete(new_state, OPEN)
                            OPEN.append(new_state)
                        if new_state in CLOSED:
                            OPEN.append(new_state)
                            deep_delete(new_state, CLOSED)


def delete_min(lst):
    """
    Finds the value in lst with the minumum F value, removes it from
    lst and returns it. If no value is found returns None.
    """
    index = -1
    min_val = 99999
    for i in range(len(lst)):
        hc_item = Problem.HASHCODE(lst[i])
        if FVALUE[hc_item] < min_val:
            min_val = FVALUE[hc_item]
            index = i
    if index >= 0:
        temp = lst[index]
        del lst[index]
        return temp
    return None


def f(state, gvals):
    """
    Computes the F value from the initial state to the goal that
    passes through the given state 'state'
    """
    return gvals[Problem.HASHCODE(state)] + H_FUNCTION(state)


def deep_delete(item, lst):
    """
    Deletes the first occurance of item in lst
    """
    for i in range(len(lst)):
        if Problem.DEEP_EQUALS(lst[i], item):
            del lst[i]
            return


def backtrace(S):
    """
    Prints the path found from the initial state to the given state S
    """
    global BACKLINKS

    path = []
    while not S == -1:
        path.append(S)
        S = BACKLINKS[Problem.HASHCODE(S)]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(Problem.DESCRIBE_STATE(s))
    return path


def occurs_in(s1, lst):
    """
    Determines if s1 is in the list lst

    returns:
        - True if s1 is in lst
        - False if s2 is not in lst
    """
    for s2 in lst:
        if Problem.DEEP_EQUALS(s1, s2):
            return True
    return False


if __name__ == '__main__':
    runAStar()
