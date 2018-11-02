from random import randint


class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.x2 = x + w
        self.y1 = y
        self.y2 = y + h

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return (center_x, center_y)

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

def create_room(game_map, room):
    # check tiles to make passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            game_map.walkable[x,y] = True
            game_map.transparent[x,y] = True

def create_h_tunnel(game_map, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
            game_map.walkable[x, y] = True
            game_map.transparent[x,y] = True

def create_v_tunnel(game_map, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        game_map.walkable[x, y] = True
        game_map.transparent[x,y] = True


def make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
    rooms = []
    num_rooms = 0

    for r in range(max_rooms):
        # random width & height
        w = randint(room_min_size, room_max_size)
        h = randint(room_min_size, room_max_size)
        # random position
        x = randint(0, map_width - w - 1)
        y = randint(0, map_height - h - 1)

        new_room = Rect(x, y, w, h)

        for other_room in rooms:
            overlap = 0
            if new_room.intersect(other_room):
                # this makes the map more roomy. return to "break" to make a classic nethack-style map
                if overlap == 1:
                    break
                else:
                    continue
                    overlap += 1

        else:
            # this would be the valid rooms
            create_room(game_map, new_room)
            (new_x, new_y) = new_room.center()

            if num_rooms == 0:
                player.x = new_x
                player.y = new_y

            else:
                (prev_x, prev_y) = rooms[num_rooms - 1].center()

                # flip a coin (random number that is either 0 or 1)
                # the y & x + 1's make the tunnels wider.
                if randint(0, 1) == 1:
                    # first move horizontally, then vertically
                    create_h_tunnel(game_map, prev_x, new_x, prev_y)
                    create_h_tunnel(game_map, prev_x, new_x, prev_y+1)
                    create_v_tunnel(game_map, prev_y, new_y, new_x)
                    create_v_tunnel(game_map, prev_y, new_y, new_x+1)
                else:
                    # first move vertically, then horizontally
                    create_v_tunnel(game_map, prev_y, new_y, prev_x)
                    create_v_tunnel(game_map, prev_y, new_y, prev_x+1)
                    create_h_tunnel(game_map, prev_x, new_x, new_y)
                    create_h_tunnel(game_map, prev_x, new_x, new_y+1)


            rooms.append(new_room)
            num_rooms += 1