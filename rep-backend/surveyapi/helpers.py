def duration_to_num(duration):
    mapping = {"one": 1, "two":2, "three": 3, "four": 4}
    return mapping[duration.split(' ')[0]]
def num_to_duration(num):
    mapping = {1: "one lective hour (50 minutes)", 2: "two lective hours", 
               3: "three lective hours", 4: "four lective hours"}
    return mapping(num)

def sub_grouping_to_num(sub_grouping):
    mapping = {"group": -1, "individual": 1, "whole": 0}
    return mapping[sub_grouping.split(' ')[0]]
def num_to_sub_grouping(num):
    mapping = {-1: "group of students", 1: "individual intervention", 0: "whole class"}
    return mapping(num)
