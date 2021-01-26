from src.player import Player
from src.trueskill_helpers import check_fair, report_match
import numpy as np
from src.spreadsheet_helpers import players_to_spreadsheet, spreadsheet_to_players

players = []
num_players = 10
num_matches = 1000

for i in range(num_players):
    players.append(Player(str(i), "hi"))

for match in range(num_matches):
    participants = np.random.choice(players, 2, replace=False)
    if int(participants[1].discord_id) < int(participants[0].discord_id):
        report_match(participants[1], participants[0])
        continue
    report_match(participants[0], participants[1])

for player in players:
    player.skill_report()

players_to_spreadsheet("backups/backup.csv", players)
new_players = spreadsheet_to_players('backups/backup.csv')

