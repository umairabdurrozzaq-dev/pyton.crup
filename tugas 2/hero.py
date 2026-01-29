class hero:

    def __init__(self, name, job, hero_type, hp):
        self.name = name
        self.job = job
        self.type = hero_type  # hero / normal / boss

        self.max_hp = hp
        self.hp = hp

        # role behavior
        if job == "Warrior":
            self.damage = 15
            self.heal_power = 10
        elif job == "Mage":
            self.damage = 25
            self.heal_power = 5
        elif job == "Healer":
            self.damage = 10
            self.heal_power = 30
        else:  # monster / boss
            self.damage = 20
            self.heal_power = 0

        self.rage = False
        print(f"✨ {self.name} memasuki arena! (HP: {self.hp})")

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy, damage):
        if not self.is_alive():
            print(f"❌ {self.name} sudah mati dan tidak bisa menyerang")
            return

        if damage <= 0:
            print("❌ Damage tidak valid")
            return

        # Rage Mode Boss
        if self.type == "boss" and self.hp <= self.max_hp / 2:
            if not self.rage:
                self.rage = True
                print("😈 Raja Iblis memasuki RAGE MODE!")
            damage *= 2
            print("💥 CRITICAL HIT!")

        print(f"⚔️ {self.name} menyerang {enemy.name} ({damage} damage)")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"💔 {self.name} menerima {damage} damage")
        print(f"❤️ HP {self.name}: {self.hp}")

        if self.hp == 0:
            print(f"☠️ {self.name} TELAH MATI")

    def heal(self, target):
        if self.job != "Healer":
            print(f"❌ {self.name} bukan Healer dan tidak bisa menyembuhkan")
            return

        

print("===party hero ===")
warior = hero("Zilong", "Warrior", "hero", 100)
mage = hero("Eudora", "Mage", "hero", 80)
healer = hero("Angela", "Healer", "hero", 70)
monster = hero("Goblin", "Monster", "normal", 60)
print("=================")
warior.attack(monster, warior.damage)
mage.attack(monster, mage.damage)
healer.heal(warior)
monster.attack(warior, monster.damage)
healer.heal(warior)
boss = hero("Raja Iblis", "Monster", "boss", 150)
print("=================")
boss.attack(warior, boss.damage)
boss.attack(mage, boss.damage)

mage.attack(boss, mage.damage)
warior.attack(boss, warior.damage)


healer.heal(warior)

boss.attack(warior, boss.damage)
healer.heal(warior)
mage.attack(boss, mage.damage)
warior.attack(boss, warior.damage)
