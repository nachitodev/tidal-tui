import os, subprocess

def music(tracks, track):
    from funcs.menu import main_menu
    os.system("clear")
    try:
        p = subprocess.Popen(f"mpv '{tracks[track].get_url()}'", shell=True)
        while p.poll() is None:
            pass
        else:
            from funcs.select import settings_data
            if settings_data["autoplay"] == True:
                music(tracks, track+1)
            else:
                main_menu()
    except KeyboardInterrupt:
        p.kill()
        os.system("clear")
        main_menu()