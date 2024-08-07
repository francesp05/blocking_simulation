from choice_policy import *
import numpy as np

def makeSelection(choices,choice_type,optional_parameter=""):
    ## choices - [left_weighted_value, right_weighted_value]
    ## choice_type - "softmax", "random", or "greedy"
    ## optional_parameter - tau, if "softmax" is selected for type

    # SOFTMAX - choose based on tau exploration parameter using softmax
    if choice_type == "softmax":
        probability_distribution = softmax(choices,optional_parameter)
        random_number = np.random.uniform(0,1)
        if random_number <= probability_distribution[0]:
            choice = 0
        else:
            choice = 1

    # RANDOM - simple random choice
    if choice_type == "random":
        choice = np.random.randint(0, 2)  # simple random choice
        probability_distribution = [0.5,0.5]

    # GREEDY - choose value which is bigger
    if choice_type == "greedy":
        if choices[0] >= choices[1]: # if first choice is higher or equal, make simple greedy choice
            choice = 0
            probability_distribution = [1,0]
        else: # otherwise, choose the second choice
            choice = 1
            probability_distribution = [0,1]

    return choice