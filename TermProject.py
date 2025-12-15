import random

mlbteam_city = {
    "Diamondbacks": "Phoenix, AZ",
    "Braves": "Atlanta, GA",
    "Orioles": "Baltimore, MD",
    "Red Sox": "Boston, MA",
    "Cubs": "Chicago, IL",
    "White Sox": "Chicago, IL",
    "Reds": "Cincinnati, OH",
    "Guardians": "Cleveland, OH",
    "Rockies": "Denver, CO",
    "Tigers": "Detroit, MI",
    "Astros": "Houston, TX",
    "Royals": "Kansas City, MO",
    "Angels": "Anaheim, CA",
    "Dodgers": "Los Angeles, CA",
    "Marlins": "Miami, FL",
    "Brewers": "Milwaukee, WI",
    "Twins": "Minneapolis, MN",
    "Mets": "New York, NY",
    "Yankees": "New York, NY",
    "Athletics": "West Sacramento, CA",
    "Phillies": "Philadelphia, PA",
    "Pirates": "Pittsburgh, PA",
    "Padres": "San Diego, CA",
    "Giants": "San Francisco, CA",
    "Mariners": "Seattle, WA",
    "Cardinals": "St. Louis, MO",
    "Rays": "St. Petersburg, FL",
    "Rangers": "Arlington, TX",
    "Blue Jays": "Toronto, ON",
    "Nationals": "Washington, DC"
}
def questions_count(questions):
    while True:
        try:
            num = int(input(f"How many questions would you like (1–{questions})? "))
            if 1 <= num <= questions:
                return num
            print("Please enter a valid number.")
        except ValueError:
            print("Enter a number.")
def ask_question(team, correct_city, all_cities):
    wrong_choices = random.sample(
        [city for city in all_cities if city != correct_city],
        3
    )
    options = wrong_choices + [correct_city]
    random.shuffle(options)
    print(f"\nWhere are the {team} located?")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Your choice (1–4): "))
            if 1 <= choice <= 4:
                return options[choice - 1] == correct_city
            print("Choose a number between 1 and 4.")
        except ValueError:
            print("Enter a number.")
def quiz(teams, cities, team_city_map, num_questions):
    score = 0
    missed = []
    random.shuffle(teams)
    for i in range(num_questions):
        team = teams[i]
        correct_city = team_city_map[team]

        if ask_question(team, correct_city, cities):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {correct_city}")
            missed.append(team)
    return score, missed
def show_results(score, num_questions, missed, team_city_map):
    print(f"Final Score: {score} / {num_questions}")
    print(f"Accuracy: {(score / num_questions) * 100:.1f}%")

    if missed:
        print("\nTeams you missed:")
        for team in missed:
            print(f"{team}: {team_city_map[team]}")
print("\nMLB Teams & Cities Quiz")
print("-" * 25)
teams = list(mlbteam_city.keys())
cities = list(set(mlbteam_city.values()))
num_questions = questions_count(len(teams))
score, missed_teams = quiz(teams, cities, mlbteam_city, num_questions)
show_results(score, num_questions, missed_teams, mlbteam_city)