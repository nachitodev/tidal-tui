import os, sys

def main_menu():
    try:
        from funcs.select import select
        select()
    except IndexError:
        pass
    except KeyboardInterrupt:
        sys.exit()