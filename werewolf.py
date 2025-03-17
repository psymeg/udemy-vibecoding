import random
import time

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.alive = True
    
    def __str__(self):
        return f"{self.name} ({'Alive' if self.alive else 'Dead'}) - {self.role}"

def assign_roles(players):
    roles = ['Werewolf', 'Seer'] + ['Villager'] * (len(players) - 2)
    random.shuffle(roles)
    return [Player(name, role) for name, role in zip(players, roles)]

def night_phase(players):
    print("\nNight falls...")
    time.sleep(1)
    
    werewolf = next((p for p in players if p.role == 'Werewolf' and p.alive), None)
    if werewolf:
        victims = [p for p in players if p.alive and p.role != 'Werewolf']
        if victims:
            victim = random.choice(victims)
            victim.alive = False
            print(f"The werewolf attacks and kills {victim.name}!")
        else:
            print("No one left to attack!")
    else:
        print("No werewolf remains.")
    
    seer = next((p for p in players if p.role == 'Seer' and p.alive), None)
    if seer:
        suspect = random.choice([p for p in players if p.alive and p != seer])
        print(f"The Seer peers into the night and sees that {suspect.name} is a {suspect.role}.")
    
    time.sleep(1)

def day_phase(players):
    print("\nDay breaks...")
    time.sleep(1)
    print("The villagers gather to discuss and vote.")
    
    candidates = [p for p in players if p.alive]
    if not candidates:
        print("No one is left to vote.")
        return
    
    voted_out = random.choice(candidates)
    voted_out.alive = False
    print(f"The villagers have chosen to eliminate {voted_out.name}, who was a {voted_out.role}.")
    
    time.sleep(1)

def check_winner(players):
    werewolves = sum(1 for p in players if p.role == 'Werewolf' and p.alive)
    villagers = sum(1 for p in players if p.role != 'Werewolf' and p.alive)
    
    if werewolves == 0:
        print("The villagers have won! The werewolf threat is gone!")
        return True
    if werewolves >= villagers:
        print("The werewolves have overpowered the villagers. Evil prevails!")
        return True
    return False

def play_game(player_names):
    players = assign_roles(player_names)
    print("Players:")
    for player in players:
        print(player)
    
    while True:
        night_phase(players)
        if check_winner(players):
            break
        day_phase(players)
        if check_winner(players):
            break

if __name__ == "__main__":
    player_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    play_game(player_names)

