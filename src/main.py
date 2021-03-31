from activity_diagram import ActivityDiagram

import os


if __name__ == "__main__":
    opt = input("Deseja criar um novo Diagrama de Atividades (s/n): ")

    if opt[0].lower() == "s":
        name = input("Nome do Diagrama: ")

        act = ActivityDiagram(name)

        while(1):
            os.system("clear")

            option = int(
                input(
                    "-- Criação do Diagrama de Atividades --\n"+
                    "1 - Inserir Elementos\n"+
                    "2 - Inserir Transição\n"+
                    "3 - Finalizar e Salvar\n"+
                    "-> "
                )
            )

            if option == 1:
                act.create_elements()

                # TODO: TRATAR SOBRESCRIÇÃO DE ELEMENTOS

            elif option == 2:
                act.create_transitions()

            else:
                act.create_xml()

                # TODO: TRATAR DIAGRAMA VAZIO

                break

    else:
        print("Saindo...\n")
