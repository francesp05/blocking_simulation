"""Adding data folders and subjective value test, removing phase change screens, made window fullscreen."""
import pygame
import random
import os
import datetime

# Initialize pygame
pygame.init()

# Set up the screen in fullscreen mode
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Pooble Task")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font size for all text
font_size = 48

# Path to the phase folders
PHASE_FOLDER_PATHS = {
    "phase1": os.path.join(os.path.dirname(__file__), 'phase1'),
    "phases2_3": os.path.join(os.path.dirname(__file__), 'phases2_3')
}

# Initialize user choices array to store each choice
user_choices = []

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

# Function to display icons
def display_icons(icon1_path, icon2_path, selected_icon, score, points, color):
    screen.fill(WHITE)
    font = pygame.font.Font(None, font_size)
    # Display "CHOOSE ONE:" in the top left corner
    choose_text = font.render("CHOOSE ONE:", True, BLACK)
    choose_rect = choose_text.get_rect(topleft=(10, 10))
    screen.blit(choose_text, choose_rect)

    # Load and display icon 1 on the left side
    icon1 = pygame.image.load(icon1_path).convert_alpha()
    icon1_rect = icon1.get_rect(midright=(WIDTH // 2 - 100, HEIGHT // 2))
    screen.blit(icon1, icon1_rect)

    # Display "or" text between the icons
    or_text = font.render("or", True, BLACK)
    or_text_rect = or_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(or_text, or_text_rect)

    # Load and display icon 2 on the right side
    icon2 = pygame.image.load(icon2_path).convert_alpha()
    icon2_rect = icon2.get_rect(midleft=(WIDTH // 2 + 100, HEIGHT // 2))
    screen.blit(icon2, icon2_rect)

    # Display chosen icon with black rectangle outline
    if selected_icon == icon1_path:
        pygame.draw.rect(screen, BLACK, icon1_rect, 3)
    elif selected_icon == icon2_path:
        pygame.draw.rect(screen, BLACK, icon2_rect, 3)

    # Display score in the upper right corner
    score_text = font.render(f"Score: {score}", True, BLACK)
    score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(score_text, score_rect)

    # Display points gained or lost under "or" text
    points_text = font.render("Points: " + points, True, color)
    points_rect = points_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(points_text, points_rect)

    pygame.display.flip()

# Main game loop
def main():
    running = True
    current_phase = 0
    score = 0  # Initialize the score
    phase_scores = []

    # Display start screen
    display_start_screen()
    pygame.time.wait(500)  # Wait for a short moment

    while current_phase < len(phases) and running:
        phase = phases[current_phase]
        num_choices = phase["num_choices"]

        for _ in range(num_choices):
            # Generate two different icons
            icon1_path, icon2_path = generate_icons(phase["folder"])

            # Display the two icons and the score
            display_icons(icon1_path, icon2_path, None, score, "", BLACK)

            # Get user input (left or right arrow key)
            selected_icon = None
            while selected_icon is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            selected_icon = icon1_path
                        elif event.key == pygame.K_RIGHT:
                            selected_icon = icon2_path

            # Evaluate the selected icon and update the score
            points = evaluate_icon(selected_icon, current_phase)
            if points >= 0:
                display_icons(icon1_path, icon2_path, selected_icon, score, "+" + str(points), GREEN)
            else:
                display_icons(icon1_path, icon2_path, selected_icon, score, str(points), RED)
            score += points

            # Log user choice
            log_choice(icon1_path, icon2_path, selected_icon, points, score)

            # Wait for space key to continue
            space_pressed = False
            while not space_pressed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            space_pressed = True

        # Add the score for the current phase to the list of phase scores
        phase_scores.append(score)

        # Move to the next phase
        current_phase += 1
        # Reset the score for the next phase
        score = 0

    # Display final scores for each phase
    display_final_score(phase_scores)

    # Save user choices to a text file
    save_user_choices()

    pygame.quit()

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
    if current_phase == 1:
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
    return total_value + variation

# Function to log user choice
def log_choice(icon1_path, icon2_path, selected_icon, points, total_score):
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

# Function to display the start screen
def display_start_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, font_size)
    title_text = font.render("Pooble Task", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_text, title_rect)
    start_text = font.render("Press SPACE to start", True, BLACK)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(start_text, start_rect)
    pygame.display.flip()

    # Wait for SPACE key to start the game
    space_pressed = False
    while not space_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space_pressed = True

# Function to display final scores for each phase
def display_final_score(phase_scores):
    screen.fill(WHITE)
    font = pygame.font.Font(None, font_size)
    text_y = HEIGHT // 2 - 50

    for phase_num, score in enumerate(phase_scores, start=1):
        text = font.render(f"Phase {phase_num} Score: {score}", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, text_y))
        screen.blit(text, text_rect)
        text_y += 50

    # Add "Press ESC to exit" text at the bottom
    exit_text = font.render("Press ESC to exit", True, BLACK)
    exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(exit_text, exit_rect)

    pygame.display.flip()

    # Wait for ESC key to quit the game
    esc_pressed = False
    while not esc_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = True

# Function to save user choices to a text file
def save_user_choices():
    # Determine the directory of the script
    script_dir = os.path.dirname(__file__)
    
    # Create the 'data' folder if it doesn't exist
    data_folder = os.path.join(script_dir, 'pooble_data')
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Generate a timestamp for the current session
    timestamp = datetime.datetime.now().strftime("%Y.%m.%d_%H%M")

    # Define the file path with a unique filename
    file_name = f"{timestamp}.txt"
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

if __name__ == "__main__":
    phases = [
        {"folder": "phase1", "num_choices": 5},
        {"folder": "phases2_3", "num_choices": 5},
        {"folder": "phases2_3", "num_choices": 5} #25,50,75
    ]
    main()