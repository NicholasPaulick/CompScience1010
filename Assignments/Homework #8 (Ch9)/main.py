useractions = ["add", "remove", "count", "display", "quit"]

teams = {}

action = ""
while action != useractions[4]:
    action = ""
    while action not in useractions:
        action = input("What operation would you like to do: quit, add, remove, count, or display: ")
        if action not in useractions:
            print("This is not a valid option, please try again")
        # add teams
        elif action == useractions[0]:
            team_name = input("Please enter a team name: ")
            try:
                teams[team_name]
                team_year = input(f"What additional year did the {team_name} win the NBA championship: ")
                listholder = teams[team_name]
                listholder.append(team_year)
                print(f"{team_name} was added to the dictionary")
            except KeyError:
                team_year = input(f"What year did the {team_name} win the NBA championship: ")
                teams[team_name] = [team_year]
                print(f"{team_name} was added to the dictionary")
        # remove teams
        elif action == useractions[1]:
            team_name = input("Please enter a team name: ")
            try:
                teams.pop(team_name)
                print(f"{team_name} was removed from the dictionary")
            except KeyError:
                print("This team is not valid, please try again")
        # display teams
        elif action == useractions[3]:
            print(teams)
        # count teams
        elif action == useractions[2]:
            print(f"{len(teams)} teams have won the NBA championship")
