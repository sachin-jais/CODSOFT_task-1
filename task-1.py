import random

# Emoji mapping for fun
emoji_map = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}

def get_computer_move():
    return random.choice(['rock', 'paper', 'scissors'])

def get_full_move(shortcut):
    mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    return mapping.get(shortcut, shortcut)

def decide_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

print("==== Rock, Paper, Scissors ====")
print("Instructions:")
print("Type 'r' for Rock, 'p' for Paper, 's' for Scissors")
print("Or type full words: rock, paper, scissors")

user_score = 0
computer_score = 0
rounds = 0
history = []  # To store result of each round

while True:
    user_input = input("\nYour move (r/p/s or full word): ").lower().strip()
    user_move = get_full_move(user_input)

    if user_move not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        continue

    computer_move = get_computer_move()
    print(f"Computer chose: {computer_move}")
    print(f"You chose: {user_move}")

    result = decide_winner(user_move, computer_move)
    rounds += 1

    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        user_score += 1
        print("You win this round! 🎉")
    else:
        computer_score += 1
        print("Computer wins this round.")

    # Save round history
    history.append({
        'round': rounds,
        'user': user_move,
        'computer': computer_move,
        'result': result
    })

    print(f"Score -> You: {user_score} | Computer: {computer_score} | Rounds: {rounds}")

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again not in ['yes', 'y']:
        break

# Final Scores
print("\n==== Game Over! ====")
print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
if user_score > computer_score:
    print("🏆 You are the overall winner!")
elif user_score < computer_score:
    print("💻 Computer won overall.")
else:
    print("🤝 It's an overall tie.")

# Game result chart
print("\n🎮 Game Result Chart:")
print(f"{'Round':<7} {'You':<12} {'Computer':<12} {'Result':<10}")
print("-" * 43)

for entry in history:
    user_icon = emoji_map[entry['user']]
    comp_icon = emoji_map[entry['computer']]
    result = entry['result'].capitalize()
    if result == 'User':
        result = "Win"
    elif result == 'Computer':
        result = "Lose"
    else:
        result = "Tie"
    
    print(f"{entry['round']:<7} {entry['user'].capitalize()} {user_icon:<6} {entry['computer'].capitalize()} {comp_icon:<6} {result:<10}")
