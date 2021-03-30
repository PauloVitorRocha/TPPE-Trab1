class ActivityTransitions():
    def __init__(self, transition_name, transition_prob):
        self.transition_name = transition_name
        self.transition_prob = transition_prob
    
    def print_transitions(self, f):
        f.write("\t\t<Transition name=\"{}\" prob=\"{}\"/>\n".format(self.transition_name, self.transition_prob))
