'''Zambies: Spawn levels
Created Fall 2018
@author: Duncan Van Keulen (djv78)
'''


level_1 = '''\
if loops == 5*FPS:
    print('Level 1')
    add_zombies(1, zombie_speed, 1)
if loops == 13*FPS:
    add_zombies(2, zombie_speed, 1)
if loops == 25*FPS:
    add_zombies(3, zombie_speed, 1)
if loops == 30*FPS:
    add_zombies(4, zombie_speed, 2)'''

level_2 = '''\
if loops == 5*FPS:
    print('Level 2')
    add_zombies(2, zombie_speed, 1)
if loops == 10*FPS:
    add_zombies(4, zombie_speed, 2)
if loops == 15*FPS:
    add_zombies(6, zombie_speed, 2)
if loops == 25*FPS:
    add_zombies(6, zombie_speed, 2)'''

level_3 = '''\
if loops == 3*FPS:
    print('Level 3')
    add_zombies(3, zombie_speed, 1)
if loops == 10*FPS:
    add_zombies(6, zombie_speed, 2)
if loops == 20*FPS:
    add_zombies(9, zombie_speed, 3)
    add_zombies(1, zombie_speed, 4)'''

levels = [level_1, level_2, level_3]

