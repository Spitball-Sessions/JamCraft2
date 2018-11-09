import random

class BasicMonster:
    def take_turn(self, target, game_map, entities):
        monster = self.owner
        d = getattr(monster.fighter, 'defense')
        confuse = random.randint(1,4)
        if game_map.fov[monster.x, monster.y]:
            if monster.distance_to(target) >= 1 and monster.distance_to(target) <= 6:
                if d == 10:
                    if confuse < 2:
                        monster.move_away(target.x, target.y, game_map, entities)
                    if confuse == 4:
                        monster.move_towards(target.x, target.y, game_map, entities)
                elif d > target.fighter.power:
                    if confuse > 2:
                        monster.move_towards(target.x, target.y, game_map, entities)
                elif confuse == 1:
                    monster.move_away(target.x, target.y, game_map, entities)


            elif target.fighter.hp > 0:
                print("The {0} insults you!  Your ego is damaged!".format(monster.name))
                2
            '''  
            if monster.distance_to(target) > 10:
                if d <= 4:
                    monster.move_towards(target.x, target.y, game_map, entities)
            '''
