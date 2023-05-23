def duration_to_num(duration):
    mapping = {"one": 1, "two":2, "three": 3, "four": 4}
    return mapping[duration.split(' ')[0].lower()]
def num_to_duration(num):
    mapping = {1: "One lective hour (50 minutes)", 2: "Two lective hours", 
               3: "Three lective hours", 4: "Four lective hours"}
    return mapping[num]

def sub_grouping_to_num(sub_grouping):
    mapping = {"group": -1, "individual": 1, "whole": 0}
    return mapping[sub_grouping.split(' ')[0].lower()]
def num_to_sub_grouping(num):
    mapping = {-1: "Group of students", 1: "Individual intervention", 0: "Whole class"}
    return mapping[num]
