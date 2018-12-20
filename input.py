import re

'''
함수 : input_pre_processing
매개변수 : user_input (type - string)
리턴 값 : 0~2(type - integer)

0 = 다시 입력
1 = 버스노선 검색
2 = 공지사항 출력
3 = 정거장 확인

'''

CHECK = ["정거", "정류"]
RESULT =["다시입력", "버스노선 검색", "공지사항 출력", "정거장 확인"]

def input_pre_processing(user_input):
    numbers = re.findall("\d+", user_input)


    if len(numbers) > 1:
        result = 0
    elif len(numbers) == 1:
        result = 1
    else:
        for word in CHECK:
            if word in user_input:
                result = 3
                return result
        result = 2

    return result

if __name__ == "__main__":
    input_ = "37번 버스 노선 알려줘111"
    print(RESULT[input_pre_processing(input_)])
    input_1 = "11번 버스 노선 알려줘!"
    print(RESULT[input_pre_processing(input_1)])
    input_2 = "공지사항 알려줘"
    print(RESULT[input_pre_processing(input_2)])
    input_3 = "정광고 버스 정류장 상황 알려줘"
    print(RESULT[input_pre_processing(input_3)])