import function as ft
import getpass

while True:
    ft.cle()
    ft.l()
    ft.nome()
    print("   "*7, "by Riyuzinn")
    ft.l()

    ft.vz()
    print("  [ 1 ] CRIPTOGRAFAR")
    print("  [ 2 ] DESCRIPTOGRAFAR")
    ft.vz()
    print("  [ 99 ] SAIR")
    ft.vz()
    ft.l()

    e = input("Digite sua escolha: ")
    if e == "1":
        ft.cle()
        ft.l()
        ft.vz()
        e1 = input("Digite a frase a ser criptografada: ")
        ft.cle()
        ft.l()
        ft.vz()
        print(f"A frase \033[2m{e1}\033[m criptografada fica:")
        print(f"    {ft.cript(e1)}")
        ft.vz()
        ft.l()
        enter = getpass.getpass("PRESS ENTER")
        continue
    elif e == "2":
        ft.cle()
        ft.l()
        ft.vz()
        e1 = input("Digite a frase a ser descriptografada: ")
        ft.cle()
        ft.l()
        ft.vz()
        print(f"A frase \033[2m{e1}\033[m descriptografada fica:")
        print(f"    {ft.decript(e1)}")
        ft.vz()
        ft.l()
        enter = getpass.getpass("PRESS ENTER")
        continue
    elif e == "99":
        ft.cle()
        ft.l()
        ft.vz()
        bye = getpass.getpass("PRESS ENTER")
        break
    else:
        continue

ft.cle()
