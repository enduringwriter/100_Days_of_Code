# .format and f string, numbers and scientific notation

rank = 1
team = 'USA'

print(team, 'will always be #' + str(rank))  # concatenation
print('{} will always be #{}'.format(team, rank))  # .format
print(f'{team} will always be #{rank}', end='\n'*2)  # f string

team = 'USA'
team_USA_wins = 5.9722*10**24
all_teams_all_wins = 9.303*10**24
fans = 3_752_910_390

print('{} wins about {:.2} games ({:.3%} of all wins by all teams worldwide). {} is home to {:,} fans.'
      .format(team,team_USA_wins,team_USA_wins/all_teams_all_wins,team,fans))
print(f'{team} wins about {team_USA_wins:.2} games ({team_USA_wins/all_teams_all_wins:.3%} of all wins by all teams worldwide). {team} is home to {fans:,} fans.', end='\n'*2)

print('{:.2} means two decimal places')
print('{:.3%} means three decimal places; format as percent')
print('{:,} means separate number with commas')
print("Underscores help make variables more readable: 'fans = 3_752_910_390'")
