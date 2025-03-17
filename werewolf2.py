import random
import time
import matplotlib.pyplot as plt

def assign_roles(num_villagers, num_werewolves):
    players = [f"Player {i+1}" for i in range(num_villagers + num_werewolves + 1)]
    roles = ['Seer'] + ['Werewolf'] * num_werewolves + ['Villager'] * num_villagers
    random.shuffle(roles)
    return {name: {'role': role, 'alive': True} for name, role in zip(players, roles)}

def night_phase(players):
    werewolves = [p for p in players if players[p]['role'] == 'Werewolf' and players[p]['alive']]
    if werewolves:
        victims = [p for p in players if players[p]['alive'] and players[p]['role'] != 'Werewolf']
        if victims:
            victim = random.choice(victims)
            players[victim]['alive'] = False

def day_phase(players):
    candidates = [p for p in players if players[p]['alive']]
    if candidates:
        voted_out = random.choice(candidates)
        players[voted_out]['alive'] = False

def check_winner(players):
    werewolves = sum(1 for p in players if players[p]['role'] == 'Werewolf' and players[p]['alive'])
    villagers = sum(1 for p in players if players[p]['role'] != 'Werewolf' and players[p]['alive'])
    
    if werewolves == 0:
        return "Villagers"
    if werewolves >= villagers:
        return "Werewolves"
    return None

def play_game(num_villagers, num_werewolves):
    players = assign_roles(num_villagers, num_werewolves)
    while True:
        night_phase(players)
        winner = check_winner(players)
        if winner:
            return winner
        day_phase(players)
        winner = check_winner(players)
        if winner:
            return winner

def run_simulation(num_games, num_villagers, num_werewolves):
    results = {"Villagers": 0, "Werewolves": 0}
    for _ in range(num_games):
        winner = play_game(num_villagers, num_werewolves)
        results[winner] += 1
    
    plt.bar(results.keys(), results.values(), color=['blue', 'red'])
    plt.xlabel("Winners")
    plt.ylabel("Number of Wins")
    plt.title("Werewolf Game Simulation Results")
    plt.show()

def main():
    num_villagers = int(input("Enter the number of villagers: "))
    num_werewolves = int(input("Enter the number of werewolves: "))
    num_games = int(input("Enter the number of simulations: "))
    run_simulation(num_games, num_villagers, num_werewolves)

if __name__ == "__main__":
    main()

