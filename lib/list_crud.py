def create_an_empty_list():
    return list()

def create_a_list():
    return list([0,1,2,3])

def add_element_to_end_of_list(l, element):
    return l[l, element]

def add_element_to_start_of_list(l, element):
    return [l, element]

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
