""" BrainBuster.py
Jordan Hand and Kevin Fong

Brain Buster Problem Formulation

Uses on python 3.X
"""

# <METADATA>
QUIET_VERSION = "0.1"
PROBLEM_NAME = "Brain Buster"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['J. Hand', 'K. Fong']
PROBLEM_CREATION_DATE = "27-APR-2016"
PROBLEM_DESC = \
    '''
    This formulation of the Brain Buster problem uses generic
    Python 3 constructs and has been tested with Python 3.5.
    It is designed to work according to the QUIET tools interface.
    '''
# </METADATA>

# <COMMON_CODE>


def DEEP_EQUALS(s1, s2):
    return False


def DESCRIBE_STATE(state):
    return 0


def HASHCODE(state):
    return ""


def copy_state(state):
    """
    Creates a deep copy of state
    """
    return state[:]


def can_move(s, disk_num, direction):
    return False


def move(s, disk_num, direction):
    return s


def goal_test(s):
    """
    Returns True if s is the goal state, else returns False
    """
    return s == []


def goal_message(s):
    """
    Retuns a message associated with reaching the goal state.
    """
    return "Good mathing mathlete"


class Operator:
    """
    Represents an operator that moves a piece to another index.
    Includes a move name, precondition function, and state transfer
    function.
    """
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)
# </COMMON_CODE>

# <COMMON_DATA>
num_disks = 5

num_sides = 8
# </COMMON_DATA>


# <INITIAL_STATE>
INITIAL_STATE = INITIAL_STATE = []


def CREATE_INITIAL_STATE(): return INITIAL_STATE

DUMMY_STATE = []
# </INITIAL_STATE>

# <OPERATORS>
dir_names = ['up', 'down']
move_combos = []
for i in range(num_disks):
    move_combos.append(i, 0)
    move_combos.append(i, 1)

OPERATORS = [Operator("Move disk " + str(disk) + " " + dir_names[direction],
                      lambda s, dsk=disk, d=direction: can_move(s, dsk, d),
                      lambda s, dsk=disk, d=direction: move(s, dsk, d))
             for (disk, direction) in move_combos]
# </OPERATORS>

# <GOAL_TEST> (optional)


def GOAL_TEST(s): return goal_test(s)
# </GOAL_TEST>


# <GOAL_MESSAGE_FUNCTION> (optional)


def GOAL_MESSAGE_FUNCTION(s): return goal_message(s)
# </GOAL_MESSAGE_FUNCTION>
