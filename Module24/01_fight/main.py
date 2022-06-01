import random
from duel import BattleField


new_duel = BattleField()

while True:
    who_hit = random.randint(1, 2)  # кто нанес удар
    if not new_duel.is_fight(who_hit):  # дуэль закончилась
        break
