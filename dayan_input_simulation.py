"""Original layout-- hardcoded features and values."""
# from SATDRL_model import *

# num_simulations = 1

# simulation_parameters = {
#     "alpha_sd":0.5,
#     "tau":12,
#     "init_val":0,
#     "init_unc":50,
#     "num_trials":15,
#     "num_feats":6
#     }

# # features --- 0: orange, 1: blue, 2: shorthat, 3: tallhat, 4: bowtie, 5: glasses
# input_features = [[[0,3],[1,2]],
#                   [[1,3],[0,2]],
#                   [[0,2],[0,3]],
#                   [[1,2],[1,3]],
#                   [[0,2],[1,2]], #end of phase 1
#                   [[0,2,4],[1,3,5]],
#                   [[1,2,5],[1,3,5]],
#                   [[1,2,5],[0,3,4]],
#                   [[0,2,4],[0,2,5]],
#                   [[1,3,5],[0,3,5]], #end of phase 2
#                   [[0,2,4],[0,3,4]],
#                   [[0,2,5],[1,3,4]],
#                   [[1,2,4],[0,3,5]],
#                   [[1,3,4],[1,3,5]],
#                   [[1,3,5],[0,3,5]]] #end of phase 3

# input_rewards = [[-5,5],
#                  [-25,25],
#                  [25,-5],
#                  [5,-25],
#                  [25,5], #end phase 1 -- add variation.. somehow
#                  [25,-25],
#                  [5,-25],
#                  [5,-5],
#                  [25,25],
#                  [-25,-5], #end phase 2
#                  [30,0],
#                  [20,-20],
#                  [10,-10],
#                  [-20,-30],
#                  [-30,-10]] #end phase 3

# # run simulation(s)
# for simulation in range(num_simulations):
#     print("************** Starting Simulation **************\n")
#     simulate_satdrl(input_features, input_rewards, simulation_parameters)

########################################################
"""Functions to integrate: generate_icons + evaluate_icon --> randomize icons and evaluate the point values."""
# import random
# import os

# # Path to the phase folders
# PHASE_FOLDER_PATHS = {
#     "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
#     "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
# }

# # Function to generate two different icons from the current phase folder
# def generate_icons(phase):
#     phase_folder = PHASE_FOLDER_PATHS[phase]
#     icons = os.listdir(phase_folder)
    
#     if icons:
#         while True:
#             icon1_filename = random.choice(icons)
#             icon2_filename = random.choice(icons)
            
#             if icon1_filename != icon2_filename:
#                 icon1_path = os.path.join(phase_folder, icon1_filename)
#                 icon2_path = os.path.join(phase_folder, icon2_filename)
#                 return icon1_path, icon2_path
#     else:
#         return None, None
    
# # Function to evaluate the icon and return a score based on its features
# def evaluate_icon(icon_path, current_phase):
#     # Extract features from icon_path assuming a naming convention like "orange_short_hat_bowtie.png"
#     icon_filename = os.path.basename(icon_path)
#     icon_filename = icon_filename.replace('.png', "")
#     features = icon_filename.split('_')

#     # Define feature values
#     feature_values = {
#         "color": {"orange": 10, "blue": -10},
#         "hat": {"tall": -15, "short": 15},
#         "accessories": {"bow": 5, "glass": -5}
#     }

#     total_value = 0
#     if current_phase == 1:
#         for feature in features:
#             if feature in feature_values["color"]:
#                 total_value += feature_values["color"][feature]
#             elif feature in feature_values["hat"]:
#                 total_value += feature_values["hat"][feature]
#     else:
#         for feature in features:
#             if feature in feature_values["color"]:
#                 total_value += feature_values["color"][feature]
#             elif feature in feature_values["hat"]:
#                 total_value += feature_values["hat"][feature]
#             elif feature in feature_values["accessories"]:
#                 total_value += feature_values["accessories"][feature]

#     # Add random variation between -2 and 2
#     variation = random.randint(-2, 2)
#     # print(total_value)
#     return total_value + variation

####################################################################
"""Integrated functions with working SA-TDRL simulations."""
# import random
# import os
# from SATDRL_model import *

# # Path to the phase folders
# PHASE_FOLDER_PATHS = {
#     "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
#     "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
# }

# # Feature mapping
# FEATURE_MAPPING = {
#     "orange": 0,
#     "blue": 1,
#     "short": 2,
#     "tall": 3,
#     "bow": 4,
#     "glass": 5
# }

# def generate_icons(phase):
#     # print(phase)
#     phase_folder = PHASE_FOLDER_PATHS[phase]
#     icons = os.listdir(phase_folder)
    
#     if icons:
#         while True:
#             icon1_filename = random.choice(icons)
#             icon2_filename = random.choice(icons)
            
#             if icon1_filename != icon2_filename:
#                 icon1_path = os.path.join(phase_folder, icon1_filename)
#                 icon2_path = os.path.join(phase_folder, icon2_filename)
#                 return icon1_path, icon2_path
#     else:
#         return None, None

# def extract_features(icon_path):
#     icon_filename = os.path.basename(icon_path)
#     icon_filename = icon_filename.replace('.png', "")
#     features = icon_filename.split('_')
#     return [FEATURE_MAPPING.get(feature, -1) for feature in features] #***

# def evaluate_icon(icon_path, current_phase):
#     features = extract_features(icon_path)
#     # print(current_phase)

#     # Define feature values for evaluation -- 0: orange, 1: blue, 2: shorthat, 3: tallhat, 4: bowtie, 5: glasses
#     feature_values = {
#         "color": {0: 10, 1: -10},
#         "hat": {2: -15, 3: 15},
#         "accessories": {4: 5, 5: -5}
#     }

#     total_value = 0
#     if 5 < current_phase < 11:
#         for feature in features:
#             if feature in feature_values["color"]:
#                 total_value += feature_values["color"][feature]
#             elif feature in feature_values["hat"]:
#                 total_value += feature_values["hat"][feature]
#     else:
#         for feature in features:
#             if feature in feature_values["color"]:
#                 total_value += feature_values["color"][feature]
#             elif feature in feature_values["hat"]:
#                 total_value += feature_values["hat"][feature]
#             elif feature in feature_values["accessories"]:
#                 total_value += feature_values["accessories"][feature]

#     # Add random variation between -2 and 2
#     variation = random.randint(-2, 2)
#     return total_value + variation

# def generate_trial_data(num_trials):
#     input_features = []
#     input_rewards = []
    
#     for trial in range(num_trials):
#         if trial < 5:
#             phase = "phase1"
#         else:
#             phase = "phases2_3"
        
#         icon1_path, icon2_path = generate_icons(phase)
        
#         if icon1_path and icon2_path:
#             features1 = extract_features(icon1_path)
#             features2 = extract_features(icon2_path)
            
#             # Collect features as pairs
#             features_pair = [features1, features2]
            
#             rewards = [evaluate_icon(icon1_path, trial + 1), evaluate_icon(icon2_path, trial + 1)]
            
#             input_features.append(features_pair)
#             input_rewards.append(rewards)
#         else:
#             # Fallback if no icons are found
#             input_features.append([[], []])
#             input_rewards.append([0, 0])
    
#     return input_features, input_rewards

# num_simulations = 1
# simulation_parameters = {
#     "alpha_sd": 0.5,
#     "tau": 12,
#     "init_val": 0,
#     "init_unc": 50,
#     "num_trials": 15,
#     "num_feats": 6
# }

# for simulation in range(num_simulations):
#     print("************** Starting Simulation **************\n")
    
#     input_features, input_rewards = generate_trial_data(simulation_parameters["num_trials"])
    
#     simulate_satdrl(input_features, input_rewards, simulation_parameters)
################################################################################
"""Saving simulation data as txt files to run through Stan code. Trials were also changes to be 150 total"""

# import random
# import os
# from SATDRL_model import *

# # Path to the phase folders
# PHASE_FOLDER_PATHS = {
#     "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
#     "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
# }

# # Feature mapping
# FEATURE_MAPPING = {
#     "orange": 0,
#     "blue": 1,
#     "short": 2,
#     "tall": 3,
#     "bow": 4,
#     "glass": 5
# }

# def generate_icons(phase):
#     phase_folder = PHASE_FOLDER_PATHS.get(phase)
#     if not phase_folder or not os.path.isdir(phase_folder):
#         raise ValueError(f"Invalid phase folder path: {phase_folder}")

#     icons = os.listdir(phase_folder)
#     if not icons:
#         return None, None

#     while True:
#         icon1_filename = random.choice(icons)
#         icon2_filename = random.choice(icons)

#         if icon1_filename != icon2_filename:
#             icon1_path = os.path.join(phase_folder, icon1_filename)
#             icon2_path = os.path.join(phase_folder, icon2_filename)
#             return icon1_path, icon2_path

# def extract_features(icon_path):
#     icon_filename = os.path.basename(icon_path)
#     icon_filename = icon_filename.replace('.png', "")
#     features = icon_filename.split('_')
#     return [FEATURE_MAPPING.get(feature, -1) for feature in features] #***

# def evaluate_icon(icon_path, current_phase):
#     features = extract_features(icon_path)
    
#     feature_values = {
#         "color": {0: 10, 1: -10},
#         "hat": {2: -15, 3: 15},
#         "accessories": {4: 5, 5: -5}
#     }

#     total_value = 0
#     if 25 < current_phase < 76:
#         for feature in features:
#             if feature in feature_values["color"]:
#                 total_value += feature_values["color"][feature]
#             elif feature in feature_values["hat"]:
#                 total_value += feature_values["hat"][feature]
#     else:
#         for feature in features:
#             if feature in feature_values["color"]:
#                 total_value += feature_values["color"][feature]
#             elif feature in feature_values["hat"]:
#                 total_value += feature_values["hat"][feature]
#             elif feature in feature_values["accessories"]:
#                 total_value += feature_values["accessories"][feature]

#     variation = random.randint(-2, 2)
#     return total_value + variation

# def generate_trial_data(num_trials):
#     input_features = []
#     input_rewards = []
    
#     for trial in range(num_trials):
#         phase = "phase1" if trial < 25 else "phases2_3"
        
#         icon1_path, icon2_path = generate_icons(phase)
        
#         if icon1_path and icon2_path:
#             features1 = extract_features(icon1_path)
#             features2 = extract_features(icon2_path)
            
#             features_pair = [features1, features2]
#             rewards = [evaluate_icon(icon1_path, trial + 1), evaluate_icon(icon2_path, trial + 1)]
            
#             input_features.append(features_pair)
#             input_rewards.append(rewards)
#         else:
#             input_features.append([[], []])
#             input_rewards.append([0, 0])
    
#     return input_features, input_rewards

# def log_simulation(num_simulations, log_dir="logs"):
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)

#     for simulation in range(num_simulations):
#         log_file = os.path.join(log_dir, f"simulation_{simulation + 1}.txt")
#         with open(log_file, 'w') as f:
#             f.write("************** Starting Simulation **************\n")
            
#             input_features, input_rewards = generate_trial_data(simulation_parameters["num_trials"])
            
#             # Write trial data to the log file
#             f.write(f"Simulation {simulation + 1} Data:\n")
#             f.write(f"Input Features: {input_features}\n")
#             f.write(f"Input Rewards: {input_rewards}\n")
            
#             # Call simulation function
#             simulate_satdrl(input_features, input_rewards, simulation_parameters)
            
#             f.write("Simulation completed.\n\n")

# # Define simulation parameters
# simulation_parameters = {
#     "alpha_sd": 0.5,
#     "tau": 12,
#     "init_val": 0,
#     "init_unc": 50,
#     "num_trials": 150,
#     "num_feats": 6
# }

# num_simulations = 100  # Set to 10 or 100 based on your requirement

# log_simulation(num_simulations)
#####################
import random
import os
from SATDRL_model import simulate_satdrl

# Path to the phase folders
PHASE_FOLDER_PATHS = {
    "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
    "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
}

# Feature mapping
FEATURE_MAPPING = {
    "orange": 0,
    "blue": 1,
    "short": 2,
    "tall": 3,
    "bow": 4,
    "glass": 5
}

def generate_icons(phase):
    phase_folder = PHASE_FOLDER_PATHS.get(phase)
    if not phase_folder or not os.path.isdir(phase_folder):
        raise ValueError(f"Invalid phase folder path: {phase_folder}")

    icons = os.listdir(phase_folder)
    if not icons:
        return None, None

    while True:
        icon1_filename = random.choice(icons)
        icon2_filename = random.choice(icons)

        if icon1_filename != icon2_filename:
            icon1_path = os.path.join(phase_folder, icon1_filename)
            icon2_path = os.path.join(phase_folder, icon2_filename)
            return icon1_path, icon2_path

def extract_features(icon_path):
    icon_filename = os.path.basename(icon_path)
    icon_filename = icon_filename.replace('.png', "")
    features = icon_filename.split('_')
    return [FEATURE_MAPPING.get(feature, -1) for feature in features]

def evaluate_icon(icon_path, current_phase):
    features = extract_features(icon_path)
    
    feature_values = {
        "color": {0: 10, 1: -10},
        "hat": {2: -15, 3: 15},
        "accessories": {4: 5, 5: -5}
    }

    total_value = 0
    if 25 < current_phase < 76:
        for feature in features:
            if feature in feature_values["color"]:
                total_value += feature_values["color"][feature]
            elif feature in feature_values["hat"]:
                total_value += feature_values["hat"][feature]
    else:
        for feature in features:
            if feature in feature_values["color"]:
                total_value += feature_values["color"][feature]
            elif feature in feature_values["hat"]:
                total_value += feature_values["hat"][feature]
            elif feature in feature_values["accessories"]:
                total_value += feature_values["accessories"][feature]

    variation = random.randint(-2, 2)
    return total_value + variation

def generate_trial_data(num_trials):
    input_features = []
    input_rewards = []
    
    for trial in range(num_trials):
        phase = "phase1" if trial < 25 else "phases2_3"
        
        icon1_path, icon2_path = generate_icons(phase)
        
        if icon1_path and icon2_path:
            features1 = extract_features(icon1_path)
            features2 = extract_features(icon2_path)
            
            features_pair = [features1, features2]
            rewards = [evaluate_icon(icon1_path, trial + 1), evaluate_icon(icon2_path, trial + 1)]
            
            input_features.append(features_pair)
            input_rewards.append(rewards)
        else:
            input_features.append([[], []])
            input_rewards.append([0, 0])
    
    return input_features, input_rewards

def log_simulation(num_simulations, log_file="simulation_data.txt"):
    with open(log_file, 'w') as f:
        f.write("************** Starting Simulations **************\n")
        
        for simulation in range(num_simulations):
            f.write(f"\n************** Simulation {simulation + 1} **************\n")
            
            input_features, input_rewards = generate_trial_data(simulation_parameters["num_trials"])
            
            # Write trial data to the log file
            f.write(f"Input Features: {input_features}\n")
            f.write(f"Input Rewards: {input_rewards}\n")
            
            # Call simulation function
            simulate_satdrl(input_features, input_rewards, simulation_parameters)
            
            f.write("Simulation completed.\n")
        
        f.write("\nAll simulations completed.\n")

# Define simulation parameters
simulation_parameters = {
    "alpha_sd": 0.5,
    "tau": 12,
    "init_val": 0,
    "init_unc": 50,
    "num_trials": 150,
    "num_feats": 6
}

num_simulations = 100  # Set to 10 or 100 based on your requirement

log_simulation(num_simulations)
