import tdl
from render_func import clear_all, render_all
from map_utils import make_map, GameMap
from handlers import handle_keys
from entities import Entity

def main():
    screen_width = 80
    screen_height = 50

    map_width = 65
    map_height = 50

    room_max_size = 15
    room_min_size = 8
    max_rooms = 30

    fov_algorithm = "BASIC"
    fov_light_walls = True
    fov_radius = 6

    colors = {
        "d_wall": 0x666666,
        "d_ground": 0x1C1C1C,
        "l_wall": 0xA7A26E,
        "l_ground": 0xFBF084,

    }

    player = Entity(int(screen_width  /2), int(screen_height /2), '@', 0x0DE6F0)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", 0xFFFFFF)
    entities = [npc, player]


    tdl.set_font('terminal16x16_gs_ro.png', greyscale=True, altLayout=False)

    root_console = tdl.init(screen_width,screen_height, title = "E=Quality")
    con = tdl.Console(screen_width,screen_height)

    game_map = GameMap(map_width, map_height)
    make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, player)

    fov_recompute = True

    while not tdl.event.is_window_closed():
        if fov_recompute:
            game_map.compute_fov(player.x, player.y, fov=fov_algorithm, radius=fov_radius, light_walls=fov_light_walls)
        render_all(con, entities, game_map, fov_recompute, root_console, screen_width, screen_height, colors)
        tdl.flush()

        clear_all(con, entities)

        fov_recompute = False

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
            if game_map.walkable[player.x + dx, player.y + dy]:
               player.move(dx,dy)

            fov_recompute = True

        if exit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())




if __name__ == '__main__':
    '''
    print("Do you want to play easy or hard mode?")
    choice = input()
    if choice == "easy":
        print("easy")
    elif choice == "hard":
        print("hard")
    else:
        print("no input")
    '''
    main()