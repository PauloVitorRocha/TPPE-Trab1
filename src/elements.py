class ActivityElements():

    def __init__(self, start_node):
        self.start_node = start_node
        self.activity_name = []
        self.decision_node = []
        self.merge_node = []
        self.final_node = []
        self.elements_order = []

    def create_activity(self, name):
        activity = name
        self.activity_name.append(activity)
        self.elements_order.append(0)

    def create_decision(self, name):
        decision = name
        self.decision_node.append(decision)
        self.elements_order.append(1)

    def create_merge(self, name):
        merge = name
        self.merge_node.append(merge)
        self.elements_order.append(2)

    def create_final(self, name):
        final = name
        self.final_node.append(final)
        self.elements_order.append(3)

    def create_elements_xml(self, f):
        f.write("\t<ActivityDiagramElements>\n")
        f.write("\t\t<StartNode name=\"{}\"/>\n".format(self.start_node))
        a_count = 0
        d_count = 0
        m_count = 0
        f_count = 0
        for i in self.elements_order:
            if i == 0:
                f.write("\t\t<Activity name=\"{}\"/>\n".format(self.activity_name[a_count]))
                a_count += 1
            elif i == 1:
                f.write("\t\t<DecisionNode name=\"{}\"/>\n".format(self.decision_node[d_count]))
                d_count += 1
            elif i == 2:
                f.write("\t\t<MergeNode name=\"{}\"/>\n".format(self.merge_node[m_count]))
                m_count += 1
            elif i == 3:
                f.write("\t\t<FinalNode name=\"{}\"/>\n".format(self.final_node[f_count]))
                f_count += 1
        f.write("\t</ActivityDiagramElements>\n")
        