"""Pooble simulations."""
# import random
# import os
# import datetime
# import uuid

# # Path to the phase folders
# PHASE_FOLDER_PATHS = {
#     "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
#     "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
# }

# # Initialize user choices array to store each choice
# user_choices = []

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

# # Main game loop
# def main_game(phases):
#     current_phase = 0
#     score = 0  # Initialize the score
#     phase_scores = []

#     while current_phase < len(phases):
#         phase = phases[current_phase]
#         num_choices = phase["num_choices"]

#         for _ in range(num_choices):
#             # Generate two different icons
#             icon1_path, icon2_path = generate_icons(phase["folder"])

#             # Simulate random choice between icon1 and icon2
#             if random.choice([True, False]):
#                 selected_icon = icon1_path
#             else:
#                 selected_icon = icon2_path

#             # Evaluate the selected icon and update the score
#             points = evaluate_icon(selected_icon, current_phase)
#             score += points

#             # Log user choice
#             log_choice(icon1_path, icon2_path, selected_icon, points, score)

#         # Add the score for the current phase to the list of phase scores
#         phase_scores.append(score)

#         # Move to the next phase
#         current_phase += 1
#         # Reset the score for the next phase
#         score = 0

#     # Display final scores for each phase
#     display_final_score(phase_scores)

#     # Save user choices to a text file
#     save_user_choices()

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
#     return total_value + variation

# # Function to log user choice
# def log_choice(icon1_path, icon2_path, selected_icon, points, total_score):
#     icon1_data = get_icon_data(icon1_path)
#     icon2_data = get_icon_data(icon2_path)
    
#     if selected_icon == icon1_path:
#         chosen_icon = "left"
#     elif selected_icon == icon2_path:
#         chosen_icon = "right"
    
#     choice_data = {
#         "right_icon": icon1_data,
#         "left_icon": icon2_data,
#         "chosen_icon": chosen_icon,
#         "points_gained": points,
#         "total_score": total_score
#     }
    
#     user_choices.append(choice_data)

# # Function to extract icon data from its path
# def get_icon_data(icon_path):
#     icon_filename = os.path.basename(icon_path)
#     icon_filename = icon_filename.replace('.png', "")
#     features = icon_filename.split('_')
    
#     return "-".join(features)

# # Function to display final scores for each phase (simulated)
# def display_final_score(phase_scores):
#     print("Final Scores:")
#     for phase_num, score in enumerate(phase_scores, start=1):
#         print(f"Phase {phase_num} Score: {score}")

# # Function to save user choices to a text file
# def save_user_choices():
#     # Determine the directory of the script
#     script_dir = os.path.dirname(__file__)
    
#     # Create the 'data' folder if it doesn't exist
#     data_folder = os.path.join(script_dir, 'pooble_data')
#     if not os.path.exists(data_folder):
#         os.makedirs(data_folder)

#     # Generate a timestamp for the current session
#     timestamp = datetime.datetime.now().strftime("%Y.%m.%d_%H%M")

#     # Define the file path with a unique filename
#     file_name = f"{timestamp}.txt"
#     file_path = os.path.join(data_folder, file_name)

#     # Save user choices to the text file
#     with open(file_path, 'w') as f:
#         for index, choice in enumerate(user_choices, start=1):
#             right_icon = choice["right_icon"]
#             left_icon = choice["left_icon"]
#             chosen_icon = choice["chosen_icon"]
#             points_gained = choice["points_gained"]
#             total_score = choice["total_score"]
#             # Format the choice number string
#             choice_number = f"choice: {index}"
#             # Write formatted data to the file
#             f.write(f"{choice_number} || right_icon: {right_icon} || left_icon: {left_icon} || chosen_icon: {chosen_icon} || points_gained: {points_gained} || total_score: {total_score}\n")


# """# Function to save user choices to a text file (simulated)
# def save_user_choices():
#     # Determine the directory of the script
#     script_dir = os.path.dirname(__file__)
    
#     # Create the 'data' folder if it doesn't exist
#     data_folder = os.path.join(script_dir, 'pooble_data')
#     if not os.path.exists(data_folder):
#         os.makedirs(data_folder)

#     # Generate a unique identifier (UUID)
#     unique_id = uuid.uuid4().hex  # Generate a random UUID and convert to hexadecimal string

#     # Define the file path with a unique filename
#     file_name = f"{unique_id}.txt"
#     file_path = os.path.join(data_folder, file_name)

#     # Save user choices to the text file
#     with open(file_path, 'w') as f:
#         for index, choice in enumerate(user_choices, start=1):
#             right_icon = choice["right_icon"]
#             left_icon = choice["left_icon"]
#             chosen_icon = choice["chosen_icon"]
#             points_gained = choice["points_gained"]
#             total_score = choice["total_score"]
#             # Format the choice number string
#             choice_number = f"choice: {index}"
#             # Write formatted data to the file
#             f.write(f"{choice_number} || right_icon: {right_icon} || left_icon: {left_icon} || chosen_icon: {chosen_icon} || points_gained: {points_gained} || total_score: {total_score}\n")
# """
# # if __name__ == "__main__":
# #     phases = [
# #         {"folder": "phase1", "num_choices": 5},
# #         {"folder": "phases2_3", "num_choices": 5},
# #         {"folder": "phases2_3", "num_choices": 5}
# #     ]
# #     main()

# print("abc")

######################################
"""Fixin file naming."""
# import random
# import os
# import datetime

# # Path to the phase folders
# PHASE_FOLDER_PATHS = {
#     "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
#     "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
# }

# # Counter to track number of simulations
# simulation_counter = 0

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

# # Main game loop
# def main_game(phases):
#     global simulation_counter
#     current_phase = 0
#     score = 0  # Initialize the score
#     phase_scores = []
#     user_choices = []  # Initialize user choices array for the current simulation run

#     while current_phase < len(phases):
#         phase = phases[current_phase]
#         num_choices = phase["num_choices"]

#         for _ in range(num_choices):
#             # Generate two different icons
#             icon1_path, icon2_path = generate_icons(phase["folder"])

#             # Simulate random choice between icon1 and icon2
#             if random.choice([True, False]):
#                 selected_icon = icon1_path
#             else:
#                 selected_icon = icon2_path

#             # Evaluate the selected icon and update the score
#             points = evaluate_icon(selected_icon, current_phase)
#             score += points

#             # Log user choice
#             log_choice(user_choices, icon1_path, icon2_path, selected_icon, points, score)

#         # Add the score for the current phase to the list of phase scores
#         phase_scores.append(score)

#         # Move to the next phase
#         current_phase += 1
#         # Reset the score for the next phase
#         score = 0

#     # Display final scores for each phase
#     display_final_score(phase_scores)

#     # Save user choices to a text file
#     save_user_choices(user_choices)

#     # Increment simulation counter
#     simulation_counter += 1

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

# # Function to log user choice
# def log_choice(user_choices, icon1_path, icon2_path, selected_icon, points, total_score):
#     icon1_data = get_icon_data(icon1_path)
#     icon2_data = get_icon_data(icon2_path)
    
#     if selected_icon == icon1_path:
#         chosen_icon = "left"
#     elif selected_icon == icon2_path:
#         chosen_icon = "right"
    
#     choice_data = {
#         "right_icon": icon1_data,
#         "left_icon": icon2_data,
#         "chosen_icon": chosen_icon,
#         "points_gained": points,
#         "total_score": total_score
#     }
    
#     user_choices.append(choice_data)

# # Function to extract icon data from its path
# def get_icon_data(icon_path):
#     icon_filename = os.path.basename(icon_path)
#     icon_filename = icon_filename.replace('.png', "")
#     features = icon_filename.split('_')
    
#     return "-".join(features)

# # Function to display final scores for each phase (simulated)
# def display_final_score(phase_scores):
#     print("Final Scores:")
#     for phase_num, score in enumerate(phase_scores, start=1):
#         print(f"Phase {phase_num} Score: {score}")

# # Function to save user choices to a text file
# def save_user_choices(user_choices):
#     global simulation_counter
    
#     # Determine the directory of the script
#     script_dir = os.path.dirname(__file__)
    
#     # Create the 'data' folder if it doesn't exist
#     data_folder = os.path.join(script_dir, 'pooble_data')
#     if not os.path.exists(data_folder):
#         os.makedirs(data_folder)

#     # Generate a timestamp for the current session
#     timestamp = datetime.datetime.now().strftime("%Y.%m.%d_%H%M")

#     # Define the file path with a unique filename
#     file_name = f"sim{simulation_counter}.{timestamp}.txt"
#     file_path = os.path.join(data_folder, file_name)

#     # Save user choices to the text file
#     with open(file_path, 'w') as f:
#         for index, choice in enumerate(user_choices, start=1):
#             right_icon = choice["right_icon"]
#             left_icon = choice["left_icon"]
#             chosen_icon = choice["chosen_icon"]
#             points_gained = choice["points_gained"]
#             total_score = choice["total_score"]
#             # Format the choice number string
#             choice_number = f"choice: {index}"
#             # Write formatted data to the file
#             f.write(f"{choice_number} || right_icon: {right_icon} || left_icon: {left_icon} || chosen_icon: {chosen_icon} || points_gained: {points_gained} || total_score: {total_score}\n")

# # if __name__ == "__main__":
# #     phases = [
# #         {"folder": "phase1", "num_choices": 5},
# #         {"folder": "phases2_3", "num_choices": 5},
# #         {"folder": "phases2_3", "num_choices": 5}
# #     ]
# #     main_game(phases)

###############################################
"""Implementing tdrl and stuff."""
import random
import os
import datetime

# Variables
alpha_SD = 0.5
tau = 12
## gamma = 0
numfeats = 6
initval = 0
inituncert = 50
mem = ([0, 50] for f in range (numfeats))
# intialStddev = 
# total_mean = []

# Path to the phase folders
PHASE_FOLDER_PATHS = {
    "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
    "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
}

# Counter to track number of simulations
simulation_counter = 0

# Function to generate two different icons from the current phase folder
def generate_icons(phase):
    phase_folder = PHASE_FOLDER_PATHS[phase]
    icons = os.listdir(phase_folder)
    
    if icons:
        while True:
            icon1_filename = random.choice(icons)
            icon2_filename = random.choice(icons)
            
            if icon1_filename != icon2_filename:
                icon1_path = os.path.join(phase_folder, icon1_filename)
                icon2_path = os.path.join(phase_folder, icon2_filename)
                return icon1_path, icon2_path
    else:
        return None, None

# Main game loop
def main_game(phases):
    global simulation_counter
    current_phase = 0
    score = 0  # Initialize the score
    phase_scores = []
    user_choices = []  # Initialize user choices array for the current simulation run

    while current_phase < len(phases):
        phase = phases[current_phase]
        num_choices = phase["num_choices"]

        for _ in range(num_choices):
            # Generate two different icons
            icon1_path, icon2_path = generate_icons(phase["folder"])

            ## fill in for softmax later -- simulating choice!!!!
            # if random.choice([True, False]):
            #     selected_icon = icon1_path
            # else:
            #     selected_icon = icon2_path
            selectIcon()

            # Evaluate the selected icon and update the score
            points = evaluate_icon(selection, current_phase)
            score += points
            # generate RPE here!!!
            # update value in memory

            # Log user choice
            log_choice(user_choices, icon1_path, icon2_path, selection, points, score)

        # Add the score for the current phase to the list of phase scores
        phase_scores.append(score)

        # Move to the next phase
        current_phase += 1
        # Reset the score for the next phase
        score = 0

    # Display final scores for each phase
    display_final_score(phase_scores)

    # Save user choices to a text file
    save_user_choices(user_choices)

    # Increment simulation counter
    simulation_counter += 1

# Function to evaluate the icon and return a score based on its features
def evaluate_icon(icon_path, current_phase):
    # Extract features from icon_path assuming a naming convention like "orange_short_hat_bowtie.png"
    icon_filename = os.path.basename(icon_path)
    icon_filename = icon_filename.replace('.png', "")
    features = icon_filename.split('_')

    # Define feature values
    feature_values = {
        "color": {"orange": 10, "blue": -10},
        "hat": {"tall": -15, "short": 15},
        "accessories": {"bow": 5, "glass": -5}
    }

    total_value = 0
    if current_phase == 1: #append to total_memory (copy.deepcoppy(mem)) ?
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

    # Add random variation between -2 and 2
    variation = random.randint(-2, 2)
    # print(total_value)
    return total_value + variation

def selectIcon(tempLStorage,tempRStorage,stateMemory,tau): #<<<<------ need to update so values passed to makeSelection are summations of first/second option feature's values
                leftChoiceValue = 0
                rightChoiceValue = 0
                #feature numbers: 1: orange, 2: blue, 3: shorthat, 4: tallhat, 5: bowtie, 6:glasses
                for featureIdx,featureValue in (tempLStorage): #sum value of all features present in left icon *** weighted value
                    Lval = mem[feat][0]
                    uncert = mem[feat][0]
                    totalLval += Lval
                        #...uncertLval += unc
                    leftChoiceValue += (stateMemory[featureIdx][0] * featureValue)
                for featureIdx, featureValue in (tempRStorage): #sum value of all features present in right icon *** weighted value!!!!!! <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    Rval = mem[feat][0]
                    uncert = mem[feat][0]
                    totalRval += Rval
                        #...uncertRval += unc
                    rightChoiceValue += (stateMemory[featureIdx][0] * featureValue)
                choiceValues = [leftChoiceValue, rightChoiceValue]
                #make choice based on desired choiceType ("softmax","random", or "greedy")
                probDist, selection = makeSelection(choiceValues,"softmax",tau)
                # print("      left:    estimated value  ->", choiceValues[0])
                # print("            choice probability  ->", probDist[0])
                # print("     right:    estimated value  ->", choiceValues[1])
                # print("            choice probability  ->", probDist[1])
                return selection

# Function to log user choice
def log_choice(user_choices, icon1_path, icon2_path, selected_icon, points, total_score):
    icon1_data = get_icon_data(icon1_path)
    icon2_data = get_icon_data(icon2_path)
    
    if selected_icon == icon1_path:
        chosen_icon = "left"
    elif selected_icon == icon2_path:
        chosen_icon = "right"
    
    choice_data = {
        "right_icon": icon1_data,
        "left_icon": icon2_data,
        "chosen_icon": chosen_icon,
        "points_gained": points,
        "total_score": total_score
    }
    
    user_choices.append(choice_data)

# Function to extract icon data from its path
def get_icon_data(icon_path):
    icon_filename = os.path.basename(icon_path)
    icon_filename = icon_filename.replace('.png', "")
    features = icon_filename.split('_')
    
    return "-".join(features)

# Function to display final scores for each phase (simulated)
def display_final_score(phase_scores):
    print("Final Scores:")
    for phase_num, score in enumerate(phase_scores, start=1):
        print(f"Phase {phase_num} Score: {score}")

# Function to save user choices to a text file
def save_user_choices(user_choices):
    global simulation_counter
    
    # Determine the directory of the script
    script_dir = os.path.dirname(__file__)
    
    # Create the 'data' folder if it doesn't exist
    data_folder = os.path.join(script_dir, 'pooble_data')
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Generate a timestamp for the current session
    timestamp = datetime.datetime.now().strftime("%Y.%m.%d_%H%M")

    # Define the file path with a unique filename
    file_name = f"sim{simulation_counter}.{timestamp}.txt"
    file_path = os.path.join(data_folder, file_name)

    # Save user choices to the text file
    with open(file_path, 'w') as f:
        for index, choice in enumerate(user_choices, start=1):
            right_icon = choice["right_icon"]
            left_icon = choice["left_icon"]
            chosen_icon = choice["chosen_icon"]
            points_gained = choice["points_gained"]
            total_score = choice["total_score"]
            # Format the choice number string
            choice_number = f"choice: {index}"
            # Write formatted data to the file
            f.write(f"{choice_number} || right_icon: {right_icon} || left_icon: {left_icon} || chosen_icon: {chosen_icon} || points_gained: {points_gained} || total_score: {total_score}\n")

# if __name__ == "__main__":
#     phases = [
#         {"folder": "phase1", "num_choices": 5},
#         {"folder": "phases2_3", "num_choices": 5},
#         {"folder": "phases2_3", "num_choices": 5}
#     ]
#     main_game(phases)
# print("abc")