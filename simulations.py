from pooblesim import *
# import time
print("hi")

simulations = 5

for x in range(simulations):
    print("Running simulation:", x)
    phases = [
        {"folder": "phase1", "num_choices": 5},
        {"folder": "phases2_3", "num_choices": 5},
        {"folder": "phases2_3", "num_choices": 5} #25,50,75
    ]
    main_game(phases)

    # time.sleep(5)