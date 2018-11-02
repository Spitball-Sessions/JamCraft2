import tdl
from render_func import clear_all, render_all
from handlers import handle_keys
from entities import Entity

def main():
    screen_width = 80
    screen_height = 50

    player = Entity(int(screen_width  /2), int(screen_height /2), '@', 0x0DE6F0)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", 0xFFFFFF)
    entities = [npc, player]


    tdl.set_font('terminal16x16_gs_ro.png', greyscale=True, altLayout=False)

    root_console = tdl.init(screen_width,screen_height, title = "E=Quality")
    con = tdl.Console(screen_width,screen_height)

    while not tdl.event.is_window_closed():
        render_all(con, entities, root_console, screen_width, screen_height)
        tdl.flush()

        clear_all(con, entities)

        for event in tdl.event.get():
            if event.type == "KEYDOWN":
                user_input = event
                break

        else:
            user_input = None

        if not user_input:
            continue

        action = handle_keys(user_input)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get("fullscreen")

        if move:
            dx, dy = move
            player.move(dx,dy)

        if exit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())




if __name__ == '__main__':
    print("Do you want to play easy or hard mode?")
    choice = input()
    if choice == "easy":
        print("easy")
    elif choice == "hard":
        print("hard")
    else:
        print("no input")

    main()