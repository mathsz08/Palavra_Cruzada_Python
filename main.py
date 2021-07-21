from Jogo import jogo
obj_jogo = jogo
resP = ['sim','yes','sí','s','s','yes','y']

while True:
    print("-------------------------- Bem vindo ------------------------------ ")
    print(f"Quer Jogar Cruzadinha?")
    r = input()
    if r.lower() in resP:
        obj_jogo.start()
    else:
        break