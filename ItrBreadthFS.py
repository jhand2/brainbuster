""" ItrBradthFS.py
Jordan Hand, CSE 415, Spring 2015, University of Washington
Instructor: S. Tanimoto

Solves the Towers of Hanoi problem formulation using breadth
first search.

This program is actually slightly different that if I had just
modified the one line from ItrDFS. This program takes slightly
more observations but is gaurunteed to find the solution with the
fewest moves.
"""

import TowersOfHanoi as Problem

COUNT = None
BACKLINKS = {}


def runBFS():
    """
    Creates the inital state of the problem, initializes global variables and
    runs a breadth first search to find the shortest solution to the given
    problem. Prints solution when one is found as well as the number of nodes
    visited in the graph.
    """
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(Problem.DESCRIBE_STATE(initial_state))
    global COUNT, BACKLINKS
    COUNT = 0
    BACKLINKS = {}
    bfs(initial_state)
    print(str(COUNT) + " states examined.")


def bfs(initial_state):
    """
    Finds the shortest solution to Problem with the given initial
    state. Prints the solution when it is found.
    """
    global COUNT, BACKLINKS

    OPEN = [initial_state]
    CLOSED = []
    BACKLINKS[Problem.HASHCODE(initial_state)] = -1

    while OPEN != []:
        temp = OPEN[0]
        del OPEN[0]
        CLOSED.append(temp)

        if Problem.GOAL_TEST(temp):
            print(Problem.GOAL_MESSAGE_FUNCTION(temp))
            backtrace(temp)
            return

        COUNT += 1

        children = []
        for op in Problem.OPERATORS:
            # Optionally uncomment the following when debugging
            # a new problem formulation.
            # print("Trying operator: " + op.name)
            if op.precond(temp):
                new_state = op.state_transf(temp)
                if not (occurs_in(new_state, CLOSED) or
                        occurs_in(new_state, OPEN)):
                    children.append(new_state)
                    BACKLINKS[Problem.HASHCODE(new_state)] = temp
                    # Uncomment for debugging:
                    # print(Problem.DESCRIBE_STATE(new_state))

        OPEN = OPEN + children


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
    runBFS()
