from elements import ActivityElements
from transitions import ActivityTransitions

import os


class ActivityDiagram():

    def __init__(self, name):
        self.name  = name
        self.elements = None
        self.transitions = []

    def create_elements(self):
        start_node = input("Nome do Nó Inicial: ")

        self.elements = ActivityElements(start_node)

        while(1):
            os.system("clear")

            option = int(input(
                "-- Inserir Elemento no Diagrama de Atividades --\n"+
                "1 - Atividade\n"+
                "2 - Nó de Decisão\n"+
                "3 - Nó de Fusão\n"+
                "4 - Nó Final\n"+
                "5 - Sair\n"
                +"-> "
            ))

            if option == 1:
                self.elements.create_activity()

                # COMEÇAR AQUI O DIAGRAMA DE SEQUÊNCIA ??

            elif option == 2:
                self.elements.create_decision()

            elif option == 3:
                self.elements.create_merge()

            elif option == 4:
                self.elements.create_final()
            
            else:
                break

    def create_transitions(self):
        while(1):
            os.system("clear")
            option = int(input("Deseja escolher inserir\n1 - Criar Transicao\n2 - Sair\n-> "))
            if option == 1:
                name = input("Nome da transicao: ")
                prob = float(input("Probabilidade da transicao: "))

                transition = ActivityTransitions(name, prob)
                self.transitions.append(transition)
            else:
                break

    def create_xml(self):
        f = open("diagram.xml", "w")
        f.write("<ActivityDiagram name=\"{}\">\n".format(self.name))
        self.elements.create_elements_xml(f)
        f.write("\t<ActivityDiagramTransitions>\n")
        for transition in self.transitions:
            transition.print_transitions(f)
        f.write("\t</ActivityDiagramTransitions>\n")
        f.write("</ActivityDiagram>")
        f.close()
            
        
            
        

