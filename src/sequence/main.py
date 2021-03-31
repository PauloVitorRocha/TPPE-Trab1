from sequence_diagrams import SequenceDiagrams
import os

if __name__ == "__main__":
    seq = SequenceDiagrams()
    while(1):
        os.system("clear")
        option = int(input("Deseja escolher inserir\n1 - Lifeline\n2 - Fragmentos\n3 - Diagrama de Sequencia\n4 - Sair\n-> "))
        if option == 1:
            seq.create_and_persist_lifelines()

        elif option == 2:
            seq.create_and_persist_fragments()

        elif option == 3:
            seq.create_single_sequence_diagram()

        else:
            seq.create_xml()
            break