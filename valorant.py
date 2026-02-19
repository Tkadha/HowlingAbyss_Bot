import random
valorant=["스플릿", "바인드", "헤이븐","어센트","아이스박스","브리즈","프랙처","펄","로터스","선셋","어비스"]
val_lotate_list=["스플릿", "바인드", "헤이븐", "프랙처", "펄", "로터스", "어비스"]
another_list=[]
def sample():
    sample_list = random.sample(val_lotate_list,1)
    return sample_list

def alllist():
    return valorant


def lotate_list():
    return val_lotate_list