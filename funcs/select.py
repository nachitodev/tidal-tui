import os, json

def select():
    global autoplay
    from main import session, settings
    settings_data = json.load(settings)
    autoplay = settings_data["autoplay"]
    
    if autoplay == True:
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
    global ROWS
    ROWS = [
        ("Duration", "Name", "Artist name")
    ]
    os.system("clear")
    tracks = playlists[playlist_id-1].tracks()
    x=-1
    for name in tracks:
        from funcs.ui import app
        from funcs.utils import convert_duration
        
        duration = convert_duration(tracks[x].duration)
        name = tracks[x].name
        artist_name = tracks[x].artist.name
        x = x+1 
        
        rows_data = (duration, name, artist_name)
        ROWS.append(rows_data)
        #print(f"{x+1} - {tracks[x].name}")
    app.run()
        
    #print("0 - Return to Playlist Select")
    #print(f"\n[{settings_str}] - Autoplay \n")
    
    #track= int(input("Select Track: "))
    
    #if track == 0:
        #from funcs.menu import main_menu
        #print(track)
        #select()
    #else:
        #from funcs.music import music 
        #music(tracks, track-1)