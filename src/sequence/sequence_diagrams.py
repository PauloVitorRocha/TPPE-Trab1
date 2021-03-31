from sequence_diagram_block import SequenceDiagramBlock
from lifelines import Lifelines
from fragments import Fragments
import os
from excepts import EmptyOptionalFragment, EmptyGuardConditionException, MessageFormatException

class SequenceDiagrams():
    def __init__(self):
        self.sequence_diagrams = []
        self.lifelines = []
        self.fragments = []

    def create_and_persist_lifelines(self):
        lifeline_name = input("Nome da lifeline: ")
        lifeline = Lifelines(lifeline_name)
        self.lifelines.append(lifeline)

    def create_and_persist_fragments(self):
        fragment_name = input("Nome do fragmento: ")

        if self.sequence_fragment_exists(fragment_name) == False: 
            raise EmptyOptionalFragment  

        fragment_represented = input("Fragmento representado por: ")

        if self.sequence_diagram_exists(fragment_represented) == True:   
            fragment = Fragments(fragment_name, fragment_represented)
            self.fragments.append(fragment)
        else:
            raise EmptyOptionalFragment

    def lifeline_exists(self, name):
        for i in self.lifelines:
            if i.name == name:
                return True
        return False

    def sequence_diagram_exists(self, name):
        for i in self.sequence_diagrams:
            if i.name == name:
                return True
        return False
                
    def create_single_sequence_diagram(self):
        s_name = input("Nome do diagrama: ")
        guard_condition = input("Condicao de guarda: ")

        if bool(guard_condition) == False: 
            raise EmptyGuardConditionException

        sequence_diagram = SequenceDiagramBlock(s_name, guard_condition)
        while True:
            os.system("clear")
            option = int(input("Deseja escolher inserir\n1 - Mensagem\n2 - Fragmento\n3 - Sair\n-> "))
            if option == 1:
                m_name = input("Nome da mensagem: ")
                m_prob = input("Probabilidade da mensagem: ")
                source_lifeline = input("Lifeline de origem: ")
                target_lifeline = input("Lifeline alvo: ")

                if not self.lifeline_exists(source_lifeline) and not self.lifeline_exists(target_lifeline):
                    raise MessageFormatException

                sequence_diagram.persist_messages(m_name, m_prob, source_lifeline, target_lifeline)
                sequence_diagram.elements_update(option - 1)

            elif option == 2:
                fragment_name = input("Nome do fragmento: ")
                sequence_diagram.persist_fragments(fragment_name)
                sequence_diagram.elements_update(option - 1)
            else:
                break
        self.sequence_diagrams.append(sequence_diagram)
        
        

    def create_lifelines_xml(self, f):
        f.write("\t<Lifelines>\n")
        for lifeline in self.lifelines:
            lifeline.lifeline_to_xml(f)
        f.write("\t</Lifelines>\n")
    
    def create_fragments_xml(self, f):
        f.write("\t<Fragments>\n")
        for fragment in self.fragments:
            fragment.fragments_to_xml(f)
        f.write("\t</Fragments>\n")

    def create_sequence_diagrams_xml(self, f):
        for diagram in self.sequence_diagrams:
            m_count = 0
            f_count = 0

            f.write("\t<SequenceDiagram name=\"{}\" guard_condition=\"{}\">\n".format(diagram.name, diagram.guard))
            for i in diagram.elements:
                if i == 0:
                    diagram.xml_message_by_position(m_count, f)
                    m_count += 1
                elif i == 1:
                    diagram.xml_fragment_by_position(f_count, f)
                    f_count += 1
            
            f.write("\t</SequenceDiagram>\n".format(diagram.name))

    def create_xml(self):
        f = open("sequence_diagram.xml", "w")
        f.write("<SequenceDiagrams>\n")
        self.create_lifelines_xml(f)
        self.create_fragments_xml(f)
        self.create_sequence_diagrams_xml(f)
        f.write("</SequenceDiagrams>\n")
        f.close()
