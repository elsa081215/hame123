import  random
story = '''歡迎來到「家」，這是一個只有一關的遊戲
你將在這裡操縱一名想要回家的角色,通過....'''
# ===== 黑化值 =====
class prision:
    def __init__(self):
        self.blackening_value = 0

    def add_blackening(self, value):
        self.blackening_value += value
        print(f"黑化值增加 {value}，目前：{self.blackening_value}")

    def is_dead(self):
        return self.blackening_value >= 100 
    # ===== player角色 =====
class Player:
    def __init__(self, bag):
        self.bag = bag
        self.prision = prision()

    def atk(self, monster):
        damage = 10
        monster.hp -= damage
        print(f"你攻擊造成 {damage} 傷害")

    def take_damage(self, damage):
        self.bag.HP -= damage
        print(f"你受到 {damage} 傷害")
   
   
class bag: 
    def __init__(self, elixir, date=0, HP=100): #初始生命值和date
        self.HP = HP
        self.elixir = elixir
        self.date = date

    def oneday(self):
        self.date += 1
        self.HP -= 1

    def use_elixir(self):
        if self.elixir > 0:
            self.elixir -= 1
            self.HP += 20
            print("使用藥水 HP +20")
        else:
            print("沒有藥水了！")


# 建立 Bag藥水
my_bag = bag(elixir=5)
# 建立 Player
alen = Player(my_bag)
#  Bag 功能
print("初始 HP:", alen.bag.HP)
print("初始 date:", alen.bag.date)
print("藥水數量:", alen.bag.elixir)

print("------ 過一天 ------")
alen.bag.oneday()

print("HP:", alen.bag.HP)
print("date:", alen.bag.date)

print("------ 使用藥水 ------")
alen.bag.use_elixir()

print("HP:", alen.bag.HP)
print("藥水剩餘:", alen.bag.elixir)
import time
for line in story.split("\n"):
    print(line)
    time.sleep(1)
 


# ===== Monster怪物 =====
class monster:
    def __init__(self, hp=100, atk=20, speed=50):
        self.hp = hp
        self.atk = atk
        self.speed = speed

    def attack(self):
        self.speed += random.randint(5, 28)
        return self.atk

    def is_alive(self):
        return self.hp > 0

p = prision()   
# ===== 戰鬥開始 =====
m=monster()
print(" 阿燁...戰鬥開始！")
while True:

    print("\n玩家HP:", alen.bag.HP, "/ 怪物HP:", m.hp)

    # 角色行動(機率)
    action = input("1=攻擊 2=喝藥水: ")

    if action == "1":
        hit = random.randint(1, 100)

        if hit <= 70:
            print("打中")
            alen.atk(m)
        else:
            print("打不到")

    elif action == "2":
        alen.bag.use_elixir()
    else:
        print("輸入錯誤")
        continue
    
    # 怪物死亡+隱藏
    if m.hp<=20:
       print( "怪物說了句『g/ b4ej94xk4』,『jo6vu03』,「283家」 ")
    if not m.is_alive():
        print("🎉 怪物被打敗！")
        break

    # 怪物攻擊
    damage = m.attack()
    alen.take_damage(damage)

    # 玩家死亡
    if alen.bag.HP <= 0:
        print("你被擊敗，被關進監獄")
        # 回復HP繼續
        alen.bag.HP = 57
        print("你重新站起來 HP回復到 57")
        # 黑化增加
        alen.prision.add_blackening(30)
        # 黑化死亡
        if alen.prision.is_dead():
            print("黑化過高，角色死亡")
            break
 # ===== 戰鬥結束 =====
if not m.is_alive():
    print("打敗怪物之後,會獲得4片碎片,有三個選擇")
    print("你有40秒可以選擇")

    start_time = time.time()

    action = input("A:一次用完 B:分3次 C:不用 ").strip().upper()

    # ===== 超時判定 =====
    if time.time() - start_time > 40:
        print("時間到了，你什麼都沒選擇，碎片消失了...哈哈你終於死了阿燁我終於...")

    else:
        if action == "A":
            print('嘻嘻你死了，人心不足蛇吞象～')

        elif action == "B":
            print('這就一關分什麼分？你死了')

        elif action == "C":
            print('裝啥？你死了')

        elif action == "家":
            print("……")
            time.sleep(1)
            print("你回來了嗎？")
            time.sleep(2)
            print("不你不是")
            print('我在期待什麼？')
            print("阿燁")    
            

            from STORY import storys

            for paragraph in storys.split("\n\n"):
                print(paragraph.strip())
                input("\n(按 Enter 繼續）\n")