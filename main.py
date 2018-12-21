import dota2api
import loader

api = dota2api.Initialise()
#might consider raw_mode
pd_matches = loader.load_matches(api, 126212866)