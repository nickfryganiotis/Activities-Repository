def duration_to_num(duration):
    mapping = {"1": 1, "2":2, "3": 3, "4": 4}
    return mapping[duration.split(' ')[0].lower()]
def num_to_duration(num):
    mapping = {1: "1 hour", 2: "2 hours", 
               3: "3 hours", 4: "4 hours"}
    return mapping[num]

def sub_grouping_to_num(sub_grouping):
    mapping = {"small": -1, "individual": 1, "whole class": 0, 'large': 2}
    return mapping[sub_grouping.split(' ')[0].lower()]
def num_to_sub_grouping(num):
    mapping = {-1: "Small group", 1: "Individual intervention", 0: "Whole class", 2: "Large group"}
    return mapping[num]
