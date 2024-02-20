input("Começa o jogo !!!!                 ")
hp = 1000000000000000000000000
dmg_done = 0
lvls = 0
dmg = 1
while hp > 0:
    print("ele tem", hp, "de vida")
    input("Ataca ")
    hp -= dmg
    dmg_done += dmg
    lvls = dmg_done // 100
    dmg_done -= 100 * lvls
    dmg += lvls
    if lvls > 0:
        print("Subiste de nível", lvls, "vezes!!!!!!\nO teu dano total é agora", dmg, "!!!!!!!!")
        #pass
    lvls = 0
print("Ele morreu! :)")
input()