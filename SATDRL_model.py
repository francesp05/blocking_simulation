"""Original SATDRL model code."""

from selection_functions import *
import numpy as np

def simulate_satdrl(input_features, input_rewards, simulation_parameters):
    ## input_features - [[left_features(f1,f2),right_features(f1,f2)]...trials]
    ## input_rewards - [[left_reward,right_reward]...trials]
    ## simulation_parameters - dictionary of simulation parameters

    # extract simulation parameters
    alpha_sd = simulation_parameters["alpha_sd"]
    tau = simulation_parameters["tau"]
    initial_value = simulation_parameters["init_val"]
    initial_uncert = simulation_parameters["init_unc"]
    num_trials = simulation_parameters["num_trials"]
    num_features = simulation_parameters["num_feats"]

    # initialize value and uncertainty for all features
    memory = [[initial_value,initial_uncert] for x in range(num_features)]

    # loop through trials
    for trial in range(num_trials):
        print("--------------------TRIAL:",trial,"--------------------")
        # get trial features
        trial_features = [input_features[trial][0],input_features[trial][1]]
        left_features = trial_features[0]
        right_features = trial_features[1]

        # get trial potential rewards
        potential_rewards = [input_rewards[trial][0], input_rewards[trial][1]]

        # calculate total feature uncertainty for left/right
        left_total_uncert = 0
        for feature in left_features:
            temp_feature_uncertainty = memory[feature][1]
            left_total_uncert += temp_feature_uncertainty
        right_total_uncert = 0
        for feature in right_features:
            temp_feature_uncertainty = memory[feature][1]
            right_total_uncert += temp_feature_uncertainty

        # calculate left/right feature expected value & uncertainty
        left_expected_value = 0
        right_expected_value = 0
        left_weighted_expected_value = 0
        right_weighted_expected_value = 0

        left_alphas = []
        right_alphas = []

        for feature in left_features:
            temp_feature_value = memory[feature][0]
            temp_feature_uncertainty = memory[feature][1]
            if left_total_uncert == 0:
                temp_feature_alpha = 1/ len(left_features)
            else:
                temp_feature_alpha = temp_feature_uncertainty/left_total_uncert
            left_alphas.append(temp_feature_alpha)
            # temp_feature_precision = (1/temp_feature_alpha)
            temp_feature_precision = (1-temp_feature_alpha) #<----- testing 1- instead of inverse *doesn't work, should be value 1 for f0, not 0.5
            left_weighted_expected_value += (temp_feature_value * temp_feature_precision)
            left_expected_value += temp_feature_value

        for feature in right_features:
            temp_feature_value = memory[feature][0]
            temp_feature_uncertainty = memory[feature][1]
            if right_total_uncert == 0:
                temp_feature_alpha = 1/ len(right_features)
            else:
                temp_feature_alpha = temp_feature_uncertainty/right_total_uncert
            right_alphas.append(temp_feature_alpha)
            # temp_feature_precision = (1/temp_feature_alpha)
            temp_feature_precision = (1-temp_feature_alpha) #<----- testing 1- instead of inverse **doesn't work, should be value 1 for f0, not 0.5
            right_weighted_expected_value += (temp_feature_value * temp_feature_precision)
            right_expected_value += temp_feature_value

        weighted_expected_values = [left_weighted_expected_value,right_weighted_expected_value] #uncertainty-weighted value
        expected_values = [left_expected_value,right_expected_value] #unweighted, value only
        expected_uncertainty = [left_total_uncert,right_total_uncert] #uncertainty only
        alphas = [left_alphas,right_alphas]

        choice = makeSelection(weighted_expected_values,"softmax",optional_parameter=tau) #choice returns 0/1 for left/right
        choice_alphas = alphas[choice]

        actual_reward = potential_rewards[choice]

        print("> left features:",left_features," - right features:",right_features)
        print("> left value:",left_weighted_expected_value," - right value:",right_weighted_expected_value)
        print("> choice:",choice," - reward:",actual_reward)

        rpe = actual_reward - expected_values[choice] #<--------------------------------------------------------------- simple and does not include gamma yet!!!!

        upe = abs(rpe) - expected_uncertainty[choice]

        # value update
        for idx,feature in enumerate(trial_features[choice]):
            memory[feature][0] += rpe*choice_alphas[idx]
            if (memory[feature][1] + upe) < 0:
                memory[feature][1] = 0
            else:
                memory[feature][1] += upe*alpha_sd

        print("> memory:\n",memory,"\n-------------------------------------------------\n")

#############################################################
"""Saving print lines to .txt file. -- nvm not needed ;p"""
# import io
# import sys
# import numpy as np
# from selection_functions import makeSelection

# def simulate_satdrl(input_features, input_rewards, simulation_parameters, log_file="simulation_log.txt"):
#     # Redirect print statements to capture them in a string
#     original_stdout = sys.stdout  # Save a reference to the original standard output
#     log_output = io.StringIO()    # Create a StringIO object to capture print statements
#     sys.stdout = log_output       # Redirect stdout to the StringIO object

#     # extract simulation parameters
#     alpha_sd = simulation_parameters["alpha_sd"]
#     tau = simulation_parameters["tau"]
#     initial_value = simulation_parameters["init_val"]
#     initial_uncert = simulation_parameters["init_unc"]
#     num_trials = simulation_parameters["num_trials"]
#     num_features = simulation_parameters["num_feats"]

#     # initialize value and uncertainty for all features
#     memory = [[initial_value, initial_uncert] for _ in range(num_features)]

#     # loop through trials
#     for trial in range(num_trials):
#         print("--------------------TRIAL:", trial, "--------------------")
#         # get trial features
#         trial_features = [input_features[trial][0], input_features[trial][1]]
#         left_features = trial_features[0]
#         right_features = trial_features[1]

#         # get trial potential rewards
#         potential_rewards = [input_rewards[trial][0], input_rewards[trial][1]]

#         # calculate total feature uncertainty for left/right
#         left_total_uncert = sum(memory[feature][1] for feature in left_features)
#         right_total_uncert = sum(memory[feature][1] for feature in right_features)

#         # calculate left/right feature expected value & uncertainty
#         left_expected_value = 0
#         right_expected_value = 0
#         left_weighted_expected_value = 0
#         right_weighted_expected_value = 0

#         left_alphas = []
#         right_alphas = []

#         for feature in left_features:
#             temp_feature_value = memory[feature][0]
#             temp_feature_uncertainty = memory[feature][1]
#             temp_feature_alpha = 1 / len(left_features) if left_total_uncert == 0 else temp_feature_uncertainty / left_total_uncert
#             left_alphas.append(temp_feature_alpha)
#             temp_feature_precision = 1 - temp_feature_alpha
#             left_weighted_expected_value += temp_feature_value * temp_feature_precision
#             left_expected_value += temp_feature_value

#         for feature in right_features:
#             temp_feature_value = memory[feature][0]
#             temp_feature_uncertainty = memory[feature][1]
#             temp_feature_alpha = 1 / len(right_features) if right_total_uncert == 0 else temp_feature_uncertainty / right_total_uncert
#             right_alphas.append(temp_feature_alpha)
#             temp_feature_precision = 1 - temp_feature_alpha
#             right_weighted_expected_value += temp_feature_value * temp_feature_precision
#             right_expected_value += temp_feature_value

#         weighted_expected_values = [left_weighted_expected_value, right_weighted_expected_value]
#         expected_values = [left_expected_value, right_expected_value]
#         expected_uncertainty = [left_total_uncert, right_total_uncert]
#         alphas = [left_alphas, right_alphas]

#         choice = makeSelection(weighted_expected_values, "softmax", optional_parameter=tau)
#         choice_alphas = alphas[choice]

#         actual_reward = potential_rewards[choice]

#         print("> left features:", left_features, " - right features:", right_features)
#         print("> left value:", left_weighted_expected_value, " - right value:", right_weighted_expected_value)
#         print("> choice:", choice, " - reward:", actual_reward)

#         rpe = actual_reward - expected_values[choice]
#         upe = abs(rpe) - expected_uncertainty[choice]

#         # value update
#         for idx, feature in enumerate(trial_features[choice]):
#             memory[feature][0] += rpe * choice_alphas[idx]
#             memory[feature][1] = max(0, memory[feature][1] + upe * alpha_sd)

#         print("> memory:\n", memory, "\n-------------------------------------------------\n")

#     # Restore the original stdout and write the captured output to the log file
#     sys.stdout = original_stdout
#     with open(log_file, 'w') as f:
#         f.write(log_output.getvalue())
    
#     # Close the StringIO object
#     log_output.close()
