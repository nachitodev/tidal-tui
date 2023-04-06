import os, json

def select():
    from main import session, settings
    settings_data = json.load(settings)
    
    if settings_data["autoplay"] == True:
        settings_str = '✅'
    else:
        settings_str = '❌'
    i=-1
    playlists = session.user.playlists()
    for name in playlists:
        i = i+1
        print(f"{i+1} - {playlists[i].name}")
    print(f"\n[{settings_str}] - Autoplay \n")
    playlist_id = int(input("What playlist you wanna hear: "))
    select_track(playlists, playlist_id, settings_str)
    
    # -- Track --
def select_track(playlists, playlist_id, settings_str):
    os.system("clear")
    tracks = playlists[playlist_id-1].tracks(limit=25)
    x=-1
    for name in tracks:
        x = x+1 
        print(f"{x+1} - {tracks[x].name}")
    print("0 - Return to Playlist Select")
    print(f"\n[{settings_str}] - Autoplay \n")
    
    track= int(input("Select Track: "))
    
    if track == 0:
        from funcs.menu import main_menu
        print(track)
        select()
    else:
        from funcs.music import music 
        music(tracks, track-1)