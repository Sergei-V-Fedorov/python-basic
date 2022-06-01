class Warrior:

    def __init__(self):
        self.hp = 100

    def get_damage(self, dmg_per_hit=20):
        self.hp -= dmg_per_hit
        return self.hp


class BattleField:

    def __init__(self):
        self.warriors = [Warrior() for _ in range(2)]

    def is_fight(self, warrior_index):
        print(f"Удар нанес Воин {warrior_index}")
        who_take_dmg = warrior_index % 2  # кто получает урон
        last_hp = self.warriors[who_take_dmg].get_damage()  # остаток урона
        if last_hp > 0:
            print(f"\tУ Воина {who_take_dmg + 1} осталось {last_hp} здоровья")
            return True
        else:
            print(f"\tУ Воина {who_take_dmg + 1} не осталось здоровья")
            print(f"\tВоин {warrior_index} победил!!!")
            return False
