import pytest
from activity_diagram import ActivityDiagram
from elements import ActivityElements
from transitions import ActivityTransitions
import mock


def test_activity_diagram():
    obj = ActivityDiagram('ad1')
    assert 'ad1'==obj.name

def test_activity_diagram2():
    obj = ActivityDiagram('ad2')
    assert 'ad2'==obj.name

def test_activity_diagram3():
    obj = ActivityDiagram('ad3')
    assert 'ad3'==obj.name

def test_create_initial_node():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    assert 'n1'==obj.elements.start_node

def test_create_initial_node2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    assert 'n2'==obj.elements.start_node

def test_create_initial_node3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    assert 'n3'==obj.elements.start_node

def test_create_activity():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_activity('at1')
    assert 'at1'==obj.elements.activity_name[0]

def test_create_activity2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_activity('at2')
    assert 'at2'==obj.elements.activity_name[0]

def test_create_activity3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_activity('at3')
    assert 'at3'==obj.elements.activity_name[0]

def test_create_decision():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_decision('d1')
    assert 'd1'==obj.elements.decision_node[0]

def test_create_decision2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_decision('d2')
    assert 'd2'==obj.elements.decision_node[0]

def test_create_decision3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_decision('d3')
    assert 'd3'==obj.elements.decision_node[0]

def test_create_merge():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_merge('m1')
    assert 'm1'==obj.elements.merge_node[0]

def test_create_merge2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_merge('m2')
    assert 'm2'==obj.elements.merge_node[0]

def test_create_merge3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_merge('m3')
    assert 'm3'==obj.elements.merge_node[0]

def test_create_final():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.create_final('f1')
    assert 'f1'==obj.elements.final_node[0]

def test_create_final2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.create_final('f2')
    assert 'f2'==obj.elements.final_node[0]

def test_create_final3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.create_final('f3')
    assert 'f3'==obj.elements.final_node[0]
