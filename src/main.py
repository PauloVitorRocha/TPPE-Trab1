from activity_diagram import ActivityDiagram
import os

if __name__ == "__main__":
    opt = input("Deseja criar uma nova atividade? ")

    if opt.lower() == "sim":
        name = input("Nome do Diagrama de Atividade: ")
        act = ActivityDiagram(name)
        while(1):
            os.system("clear")
            option = int(input("Deseja escolher inserir\n1 - Atividade\n2 - Transicao\n3 - Sair\n-> "))
            if option == 1:
                act.create_elements()

            elif option == 2:
                act.create_transitions()

            else:
                act.create_xml()
                break

    else:
        print("Entao me mama")