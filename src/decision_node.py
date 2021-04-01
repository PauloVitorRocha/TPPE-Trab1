from transitions import ActivityTransitions


class DecisionStream():
    def __init__(self):
        self.transitions = []
        self.merge_node = None
        self.final_node = None
        self.activity_node = []
        self.elements = []

    def read_activity(self):
        act_name = input("Nome da atividade: ")
        self.activity_node.append(act_name)
        self.elements.append(0)

    def read_transition(self):
        transition_name = input("Nome da transicao: ")
        transition_prob = input("Probabilidade da transicao: ")
        transition = ActivityTransitions(transition_name, transition_prob)
        self.transitions.append(transition)
        
    def read_final(self):
        final_name = input("Nome do no final: ")
        self.final_node = final_name
        self.elements.append(1)
        
    def read_merge(self):
        merge_name = input("Nome do no de merge: ")
        self.merge_node = merge_name
        self.elements.append(2)
    
    def decision_stream_to_xml(self, f, k):
        f.write("\t\t\t<DecisionStream count=\"{}\">\n".format(k+1))
        a_count = 0
        m_count = 0
        f_count = 0
        for i in self.elements:
            if i == 0:
                f.write("\t\t\t\t<Activity name=\"{}\"/>\n".format(self.activity_node[a_count]))
                a_count += 1
            elif i == 1:
                f.write("\t\t\t\t<FinalNode name=\"{}\"/>\n".format(self.final_node[f_count]))
                f_count += 1
            elif i == 2:
                f.write("\t\t\t\t<MergeNode name=\"{}\"/>\n".format(self.merge_node[m_count]))
                m_count += 1
        
        for transition in self.transitions:
            transition.transition_to_xml(f, True)
            
        f.write("\t\t\t</DecisionStream>\n")

    
    
    

