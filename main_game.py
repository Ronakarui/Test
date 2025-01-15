import random
import time
from data import *
from helpers import *

current_enemy = 0
name = input("Как звать вас?")
player["name"] = name

print(f"В один ужасный день маленький парк был заколдован. Теперь {player['name']} Должен победить всех там, так как это его работа. Парк настолько был маленький, что там было всего 4 существа.")


while True:
    action = input("Выберите действие: 1 - в бой\n 2 - тренировка\n 3 - Статы игрока\n 4 - Статы противника\n 5 - Инвентарь\n 6 - Магазин\n 7 - Заработать деньги\n 8 - Лечение")

    if action == "1":
        current_enemy = fight(current_enemy)
        if current_enemy == len(enemies):
            print(f"Вы победили и разколдовали этот парк снова. {player['name']} думает, что пора менять работу.Он хочет пойди на завод. Надеюсь, ему повезёт и он не пойдёт на завод.")
            break

    elif action == '2':
        training_type = input('''1 - Тренировать атаку
2 - Тренировать оборону
3 - Тренировка скорости
''')
        training(training_type)
    
    elif action == "3":
        display_player()
        print()

    elif action == "4":
        display_enemy(current_enemy)
        print()
    
    elif action == "5":
        display_inventory()
        print()

    elif action == "6":
        shop()
        print()
    
    elif action == "7":
        earn()
        print()

    elif action == "8":
        Healing()
        print()