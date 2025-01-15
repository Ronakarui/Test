from data import *
import random
import time

def fight(current_enemy):
    enemy = enemies[current_enemy]

    if player["speed"] >= enemy["speed"]:
            round = 1
            print(f"Бой начинает {player['name']}")
    else:
            round = 2
            print(f"Бой начинает {enemy['name']}")

    enemy_hp = enemies[current_enemy]["hp"]

    print(f"Враг {enemy['name']}: {enemy['script']}")
    input("Нажмите Enter, чтобы продолжить")
    print()
    

    while player["hp"] > 0 and enemy_hp > 0:
        if "Частица бога" in player["inventory"]:
                print("Вы уничтожили врага")
                current_enemy += 1
                return current_enemy
                break
        
        if round % 2 == 1:
            if "Амулет удачи" in player["inventory"]:
                Choice = input("Вы хотите использовать Амулет удачи сейчас? 1 - да 2 - нет")

                if Choice == "1":
                    crit = random.randint(1,100)

                    if crit < player["luck"] + 50:
                        enemy_hp -= player["attack"] * 2
                    else:
                        enemy_hp -= player["attack"]
                    
                    if enemy_hp <= 0:
                        enemy_hp = 0

                        print(f"Враг - {enemy['name']} - {enemy['win']}")
                        current_enemy += 1

                        player["inventory"].remove("Амулет удачи")
                        
                        return current_enemy
                        break
                    player["inventory"].remove("Амулет удачи")
            elif "Малая аптечка" in player["inventory"] and player["hp"] < player["maxhp"]: 
                Choice = input("Вы хотите использовать малую аптечку? 1 - да 2 - нет")

                if Choice == "1":
                    player["hp"] += 25

                    if player["hp"] > player["maxhp"]:
                        player["hp"] = player["maxhp"]

                    player["inventory"].remove("Малая аптечка")
            elif "Большая аптечка" in player["inventory"] and player["hp"] < player["maxhp"]:
                Choice = input("Вы хотите использовать Большую аптечку? 1 - да 2 - нет")

                if Choice == "1":
                    player["hp"] = player["maxhp"]

                    player["inventory"].remove("Большая аптечка")
            elif "Круг лечения" in player["inventory"] and player["hp"] < player["maxhp"]:
                print("Ваши ранны немного зажили")
                player["hp"] += 5
                
                if player["hp"] > player["maxhp"]:
                    player["hp"] = player["maxhp"]

            print(f"{player['name']} атакует {enemy['name']}")

            additional_damage = random.randint(1, 10)
            crit = random.randint(1,100)

            if crit < player["luck"]:
                enemy_hp -= player["attack"] * 2 + additional_damage
            else:
                enemy_hp -= player["attack"] + additional_damage
            time.sleep(1)

            if player["hp"] < 0:
                player["hp"] = 0
            elif enemy_hp < 0:
                enemy_hp = 0
            
            print(f"{player['name']} - {player['hp']}\n{enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        else:
            print(f"{enemy['name']} атакует {player['name']}")

            player["hp"] -= enemy['attack'] - player["armor"]
            time.sleep(1)

            if player["hp"] < 0:
                player["hp"] = 0
            elif enemy_hp < 0:
                enemy_hp = 0
            
            print(f"{player['name']} - {player['hp']}\n{enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        round += 1
    
    if player['hp'] > 0:
            print(f"Враг - {enemy['name']} - {enemy['win']}")
            current_enemy += 1
    else:
            print(f"Враг - {enemy['name']} - {enemy['loss']}")
            player["hp"] = 1
    return current_enemy

def training(training_type):
    skip = 2
    if items["2"]["name"] in player["inventory"]:
        skip = 1

        print("Вы пропустили ожидание")

    if skip == 2:
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')

            time.sleep(1.5)

    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')

    elif training_type == '2':
        player['armor'] += 0.09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    
    elif training_type == "3":
        player['speed'] += 0.5
        print(f'Тренировка окончена! Теперь ваш персонаж имеет скорость {player["speed"]}')

    print()

def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')

def display_enemy(current_enemy):
    enemy = enemies[current_enemy]

    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')

def display_inventory():
    print("Ваши предметы")

    for value in player["inventory"]:
        print(value)

    print(f"Ваша сумма денег: {player['money']}")

    print()
    if "Зелье удачи" in player["inventory"]:
        potion = input("Выпить зелье удачи? 1 - да 2 - нет")
        if potion == "1":
            player["luck"] += 5
            print(f"Вы выпили зелье и теперь у ваш шанс крита {player['luck']}%")
            player["inventory"].remove("Зелье удачи")

def shop():
    print("Добро пожаловать в магазин, что хотите?")
    print(f"У вас {player['money']}")

    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']} : {value['description']}")

    item = input()

    if item in player["inventory"]:
        print(f"У вас уже есть {items[item]['name']}")
    elif player["money"] >= items[item]["price"]:
        print(f"Вы купили {items[item]['name']}")

        player["inventory"].append(items[item]['name'])
        player["money"] -= items[item]["price"]
    else:
        print('Не хватает монет для покупки')
    print()

    print("До встречи")
    
    print()

def earn():
    print("Вы пошли в пещеру чтобы добыть золотую руду. У вас есть шанс 60% заработать от 10 до 50 монет, 30% ничего, 10% потерять от 1 до 20 монет")

    result = random.randint(0, 100)
    time.sleep(1.5)

    print("Вы добыли руду")

    time.sleep(1.5)

    print("Вы пришли продавать")

    time.sleep(1.5)

    if result < 60:
        sum = random.randint(10, 50)

        print(f"Ваша руда была качественной и вы заработали {sum} монет")
        player["money"] += sum
    elif result < 90:
        print("Ваша руда была не качественной и вы не смогли её продать")
    else:
        sum = random.randint(1, 20)

        if player['money'] > sum:
            print(f"При продаже руды на вас напали грабители и вы потеряли {sum} монет")
            player["money"] -= sum
        else:
            print("При продаже руды на вас напали грабители и оставили вас без денег")
            player["money"] = 0

def Healing():
    if player["hp"] <= player["maxhp"]:
        treatment_cost = (player['maxhp'] - player['hp']) / 2
        choice = input(f"Ваше здоровье сейчас {player['hp']}. Вы точно хотите Вылечится до {player['maxhp']} за {treatment_cost}\n 1 - да \n 2 - нет")

    if choice == "1" and treatment_cost < player['money']:
        player['hp'] = player['maxhp']
        player['money'] -= treatment_cost

        print("Вы полностью здоровы!")
    else:
        print("Ну ладно")
