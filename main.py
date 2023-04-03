import tidalapi, json, warnings, subprocess, os, sys

def clear():
    os.system("clear")
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
session = tidalapi.Session()

def login(session):
    clear() 
    session.login_oauth_simple()
    if session.check_login() == True:
        data = {
            "token_type": session.token_type,
            "access_token": session.access_token,
            "refresh_token": session.refresh_token
        }
        with open('credentials.json', 'w',) as f:
            json.dump(data, f)
        f.close()
        menu(session)
    else:
        print("Thats was a error in the login section.")
def music(tracks, track):
    clear()
    try:
        p = subprocess.Popen(f"mpv '{tracks[track].get_url()}'", shell=True)
        while p.poll() is None:
            pass
        else:
            menu(session)
    except KeyboardInterrupt:
        p.kill()
        os.system("clear")
        menu(session)

def playlist_select(session):
    i=-1
    playlists = session.user.playlists()
    for name in playlists:
        i = i+1
        print(f"{i} - {playlists[i].name}")
    playlist_id = int(input("What playlist you wanna hear: "))
    select_track(session, playlists, playlist_id)
def select_track(session, playlists, playlist_id):
    clear()
    tracks = playlists[playlist_id].tracks(limit=25)
    x=-1
    for name in tracks:
        x = x+1 
        print(f"{x} - {tracks[x].name}")
    print("25 - Return to Playlist Select")
    track= int(input("Select Track: "))
    if track == 25:
        menu(session)
    else: 
        music(tracks, track)


def menu(session):
    clear()
    try:
        playlist_select(session)
    except IndexError:
        pass
    except KeyboardInterrupt:
        sys.exit()
try:
    f = open('credentials.json', 'r')
    data = json.load(f)
    session.load_oauth_session(data["token_type"], data["access_token"], data["refresh_token"])
    f.close()
    menu(session)
except FileNotFoundError:
    pass
    login(session)
