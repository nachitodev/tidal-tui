import os, json, shutil

def login():
    from main import home, session
    
    os.system("clear")
    
    shutil.rmtree(f"{home}/.tidal-tui")
    os.makedirs(f"{home}/.tidal-tui")
    
    session.login_oauth_simple()
    if session.check_login() == True:
        data = {
            "token_type": session.token_type,
            "access_token": session.access_token,
            "refresh_token": session.refresh_token
        }
        
        settings_data = {
            "autoplay": False
        }
        from funcs.menu import main_menu
        print(home)
        with open(f'{home}/.tidal-tui/credentials.json', 'w',) as f:
            json.dump(data, f)
        f.close()
        
        
        with open(f'{home}/.tidal-tui/settings.json', 'w',) as w:
            json.dump(settings_data, w)
        w.close()
        
        main_menu()
        
    else:
        print("Thats was a error in the login section.")