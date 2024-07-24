# Preventing a Function From Modifying a List Using [:]

unprinted_school_designs = [
    'University of North Texas',
    'Texas A&M University',
    'Michigan State University',
    'Tsinghua University',
    'University of Oxford']

completed_school_designs = []


def sort_school_designs(unsorted_designs):
    """
    Sort schools alphabetically.
    """
    unsorted_designs.sort(reverse=True)


def print_school_designs(unprinted_designs):
    """
    Print school designs until there are none left.
    """
    # unprinted_designs.sort(reverse=True)  # use this line or the user-defined sort function above
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing design for: {current_design}")
        completed_school_designs.append(current_design)


sort_school_designs(unprinted_school_designs)
print_school_designs(unprinted_school_designs[:])  # [:] sends a copy of the original list to the function
print(f"Original list of unprinted school designs: {unprinted_school_designs}")
print(f"Completed list of printed school designs: {completed_school_designs}")
