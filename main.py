from Jogo import jogo
obj_jogo = jogo
resP = ['sim','yes','sí','s','s','yes','y']

while True:
    print("-------------------------- Bem vindo ------------------------------ ")
    print(f"Quer Jogar Cruadinha?")
    r = input()
    if r.lower() in resP:
        print("\n" * 130)
        obj_jogo.start()
    else:
        break