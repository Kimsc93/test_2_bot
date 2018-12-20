import re

'''
함수 : input_pre_processing
매개변수 : user_input (type - string)
리턴 값 : 0~2(type - integer)

0 = 다시 입력
1 = 버스노선 검색
2 = 공지사항 출력

'''
def input_pre_processing(user_input):
    numbers = re.findall("\d+", user_input)

    if len(numbers) > 1:
        result = 0
    elif numbers == 1:
        result = 1
    else:
        result = 2

    return result

if __name__ == "__main__":
    input_ = "37번 버스 노선 알려줘111"
    print(input_pre_processing(input_))