import random

# Function to simulate a match
def play_match(my_team, opponent):
    my_score = 0
    opponent_score = 0
    for _ in range(90):  # Simulate 90 minutes of gameplay
        if random.random() < 0.45:  # 45% chance for your team to score each minute
            my_score += 1
        if random.random() < 0.45:  # 45% chance for the opponent to score each minute
            opponent_score += 1
    return my_score, opponent_score

# Main game function
def main():
    print("Welcome to the Python Football Game!")
    my_team_name = input("Enter your team name: ")
    opponent_team_names = ['Ice Slayers', 'Crazy Cats', 'Red Devils', 'Blue Walls']
    opponent_team_name = random.choice(opponent_team_names)
    print(f"Your match is against {opponent_team_name}.")

    # Play the match
    my_score, opponent_score = play_match(my_team_name, opponent_team_name)
    print(f"Match Result: {my_team_name} {my_score} - {opponent_team_name} {opponent_score}")

    # Determine the winner
    if my_score > opponent_score:
        print("Congratulations! You won the match!")
    elif my_score < opponent_score:
        print("You lost the match. Better luck next time!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
