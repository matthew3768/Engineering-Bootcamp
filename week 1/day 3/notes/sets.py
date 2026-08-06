team_a = {"Alice", "Bob", "Charlie"}
team_b = {"Charlie", "David", "Eve"}

players_in_both_teams = team_a.intersection(team_b) 
print(players_in_both_teams) 

different_players_a = team_a.difference(team_b)
print(different_players_a)

different_players_b = team_b.difference(team_a)
print(different_players_b)

