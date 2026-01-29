class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
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
            print(f"❌ {self.name} bukan healer")
            return

        if not target.is_alive():
            print(f"✨ {self.name} menghidupkan kembali {target.name}")
        else:
            print(f"🍀 {self.name} menyembuhkan {target.name}")

        target.hp += self.heal_power
        if target.hp > target.max_hp:
            target.hp = target.max_hp

        print(f"❤️ HP {target.name}: {target.hp}")


print("\n=== PARTY HERO ===")
warrior = Hero("Zilong", "Warrior", 120)
mage = Hero("Eudora", "Mage", 80)
healer = Hero("Estes", "Healer", 90)

print("\n=== MUSUH BIASA ===")
goblin = Hero("Goblin", "Monster", 60, "normal")

print("\n=== PARTY VS GOBLIN ===")
warrior.attack(goblin, warrior.damage)
mage.attack(goblin, mage.damage)
goblin.attack(warrior, goblin.damage)
mage.attack(goblin, mage.damage)

print("\n=== BOSS FINAL ===")
boss = Hero("Raja Iblis", "Boss", 200, "boss")

print("\n=== PARTY VS RAJA IBLIS ===")
boss.attack(warrior, boss.damage)
boss.attack(mage, boss.damage)

mage.attack(boss, mage.damage)
warrior.attack(boss, warrior.damage)

boss.attack(warrior, boss.damage)  # bisa bikin mati

healer.heal(warrior)

boss.attack(warrior, boss.damage)  # rage mode aktif
