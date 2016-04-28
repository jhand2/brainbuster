""" BrainBuster.py
Jordan Hand and Kevin Fong

Brain Buster Problem Formulation

Uses on python 3.X
"""

import random as r
import math

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
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def DESCRIBE_STATE(state):
    st = ""
    for eq in state:
        st += str(eq) + '\n'
    return st


def HASHCODE(state):
    return DESCRIBE_STATE(state)


def copy_state(state):
    """
    Creates a deep copy of state
    """
    cp = []
    for eq in state:
        cp.append(eq[:])
    return cp


def can_move(s, disk_num, direction):
    return True


def move(s, disk_num, direction):
    new_state = copy_state(s)
    if direction == 1:
        prev = new_state[-1][disk_num]
        for eq in new_state:
            temp = eq[disk_num]
            eq[disk_num] = prev
            prev = temp
    else:
        nxt = new_state[1][disk_num]
        for eq in new_state:
            temp = eq[disk_num]
            eq[disk_num] = nxt
            nxt = temp
        new_state[0][disk_num] = nxt

    return new_state


def goal_test(s):
    """
    Returns True if s is the goal state, else returns False
    """
    for eq in s:
        if not is_valid(eq):
            return False
    return True


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


def calculate(eq):
    curr_eq = eq[:]
    while len(curr_eq) > 1:
        new_operand = operations[curr_eq[1]](curr_eq[0], curr_eq[2])
        curr_eq = curr_eq[3:]
        curr_eq.insert(0, new_operand)
    return curr_eq[0]


def is_valid(eq):
    ans = calculate(eq[:-2])
    return equality_test[eq[-2]](ans, eq[-1])

# </COMMON_CODE>

# <COMMON_DATA>
num_disks = 5
num_sides = 8
max_num = 100
max_right = math.pow(max_num, (num_disks - 2) // 2)

operators = ['+', '-', '*', '/', '%']
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
    '%': lambda x, y: x % y
}
equalities = ['=', '<=', '>=', '<', '>']
answers = {
    '=': lambda x: x,
    '<=': lambda x: r.choice(range(0, x + 1)),
    '<': lambda x: r.choice(range(0, x)),
    '>': lambda x: r.choice(range(x + 1, max_right + 1)),
    '>=': lambda x: r.choice(range(x, max_right + 1))
}
equality_test = {
    '=': lambda x, y: x == y,
    '<=': lambda x, y: x <= y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '>=': lambda x, y: x >= y
}
# </COMMON_DATA>


# <INITIAL_STATE>


def CREATE_INITIAL_STATE():
    left_disk_num = num_disks - 2
    state = []
    for i in range(num_disks):
        side = []
        for j in range(left_disk_num):
            if j % 2 == 0:
                side.append(r.choice(range(max_num)))
            else:
                side.append(r.choice(operators))
        print(side)
        equality = r.choice(equalities)
        ans = calculate(side)
        side += [equality, ans]

        state.append(side)
    print(DESCRIBE_STATE(state))
    return state

# </INITIAL_STATE>

# <OPERATORS>
dir_names = ['up', 'down']
move_combos = []
for i in range(num_disks):
    move_combos.append((i, 0))
    move_combos.append((i, 1))

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
