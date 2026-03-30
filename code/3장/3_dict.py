# 3_dict.py
famous_ppl = {
        1: {
        "name": "Hank Aaron",
        "job": "baseball player",
        "age": "dead",
        "born": "1934/02/05",
        "died": "2021/01/22"
        },	
        2: {
        "name": "이순신",
        "job": "장군",
        "age": "사망",
        "탄생": "1545/04/28",
        "사망": "1598/12/16"
        }
    }

print(famous_ppl)
print(famous_ppl[2]['name']) # [n]에서 n은 배열 인덱스가 아닌 키 값(0부터가 아닌 1부터 시작)임.