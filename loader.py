import dota2api
import pandas as pd

api = dota2api.Initialise()
#might consider raw_mode
player_id = 126212866

#only first 100
hist = api.get_match_history(account_id=player_id)

pd_matches = pd.DataFrame.from_dict(hist['matches'])

pd_raw_players = pd_matches.players.apply(pd.Series)
pd_raw_players = pd_raw_players.rename(columns = lambda x : 'player_' + str(x))

for i_player in range(0,10):
	colname = "player_" + str(i_player)
	default = {'account_id': 0, 'hero_id': 999, 'player_slot': 999}
	## replaces nulls in bot matches
	dict_players = [default if pd.isnull(player) else player for player in pd_raw_players[colname]]
	pd_player = pd.DataFrame.from_records(dict_players, columns=['account_id', 'player_slot', 'hero_id'])
	pd_player.columns = [str(col) + '_' + str(i_player) for col in pd_player.columns]
	if(i_player == 0):
		pd_players = pd_player
	else: 
		pd_players = pd.concat([pd_players, pd_player], axis=1)

pd_raw_players = None
pd_matches = pd.concat([pd_matches, pd_players], axis=1)