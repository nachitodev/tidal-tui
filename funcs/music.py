import os, subprocess

def music(tracks, track):
    from funcs.menu import main_menu
    os.system("clear")
    try:
        p = subprocess.Popen(f"mpv '{tracks[track].get_url()}'", shell=True)
        while p.poll() is None:
            pass
        else:
            from funcs.select import autoplay
            if autoplay == True:
                playall(tracks, track+1)
            else:
                main_menu()
    except KeyboardInterrupt:
        p.kill()
        os.system("clear")
        main_menu()
def playall(tracks, track):
    p = subprocess.Popen(f"mpv '{tracks[track].get_url()}'", shell=True)
    while p.poll() is None:
        pass
    else:
        track = track+1
        playall(tracks, track)
    
        