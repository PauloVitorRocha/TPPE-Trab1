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
                start_node = input("Nome do Nó Inicial: ")
                act.create_initial_node(start_node)

                while(1):
                    os.system("clear")
                    
                    option1 = int(input(
                        "-- Inserir Elemento no Diagrama de Atividades --\n"+
                        "1 - Atividade\n"+
                        "2 - Nó de Decisão\n"+
                        "3 - Nó de Fusão\n"+
                        "4 - Nó Final\n"+
                        "5 - Sair\n"
                        +"-> "
                    ))
                    if option1 == 1:
                        activity_name = input("Nome da Atividade: ")
                        act.elements.create_activity(activity_name)
                        
            # COMEÇAR AQUI O DIAGRAMA DE SEQUÊNCIA ??
                    elif option1 == 2:
                        decision_node = input("Nome do Nó de Decisão: ")
                        act.elements.create_decision(decision_node)
                    elif option1 == 3:
                        merge = input("Nome do Nó de Fusão: ")
                        act.elements.create_merge(merge)
                    elif option1 == 4:
                        final = input("Nome do Nó Final: ")
                        act.elements.create_final(final)
                    elif option1 == 5:
                        break
                    else:
                        pass



                # TODO: TRATAR SOBRESCRIÇÃO DE ELEMENTOS

            elif option == 2:
                name = input("Nome da transicao: ")
                prob = float(input("Probabilidade da transicao: "))
                act.create_transitions(name, prob)

            else:
                act.create_xml()

                # TODO: TRATAR DIAGRAMA VAZIO

                break

    else:
        print("Saindo...\n")
