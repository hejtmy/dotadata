import dota2api
import loader
import pandas as pd
%load_ext autoreload
%autoreload 2

api = dota2api.Initialise()
#might consider raw_mode
player_id = 126212866
pd_history = loader.load_history(api, player_id)
pd_matches = loader.fill_matches_data(api, pd_history)

pd_matches.to_csv('matches.csv', sep=";", index=False)