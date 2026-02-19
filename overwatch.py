import random

overwatch=["리알토","샴발리 수도원", "오아시스","일리오스", "66번국도","지브롤터","도라도",
           "서킷 로얄","쓰레기촌","하바나","눔바니","미드타운","블리자드 월드", "아이헨발데",
           "왕의 길", "파라이수","할리우드", "남극 반도","네팔", "리장 타워", "사모아", "부산",
           "오아시스", "일리오스", "뉴 퀸 스트리트", "루나사피", "이스페란사", "콜로세오",
           "뉴 정크 시티", "수라바사"
           ]

def sample():
    sample_list = random.sample(overwatch,1)
    return sample_list

def alllist():
    return overwatch