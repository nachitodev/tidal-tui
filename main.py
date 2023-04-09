global session
import tidalapi, json, warnings, subprocess, os, sys
from json.decoder import JSONDecodeError

home = os.environ["HOME"]
settings = open(f'{home}/.tidal-tui/settings.json', 'r')

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
session = tidalapi.Session()
 
try:
    f = open(f'{home}/.tidal-tui/credentials.json', 'r')
    data = json.load(f)
    
    from funcs.menu import main_menu 
    session.load_oauth_session(data["token_type"], data["access_token"], data["refresh_token"])
    
    f.close()
    main_menu()
    
except FileNotFoundError:
    from funcs.login import login
    pass
    login()

except JSONDecodeError:
    #settings_data = {"autoplay": False}
    #
    #with open(f'{home}/.tidal-tui/settings.json', 'w',) as w:
    #    json.dump(settings_data, w)
    #w.close()
    pass