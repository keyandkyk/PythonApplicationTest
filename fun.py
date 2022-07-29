def hello(message, msg = ""):
    print("hello " + message + msg)

#def hello(msg1, msg2): 파이썬에서는 함수 오버로딩이 지원 안 됨
#    print(msg1 + msg2) 만일 같은 이름의 함수를 정의하면 가장 가까운 이름의 함수로 정의되고 그 위에 정의된 함수는 인식 안 됨
#  인수는 튜플 등으로 정의가 가능하다. 인수 정의에 초기값을 둬서 호출 코드에는 인수 생략이 가능하다

def get_max(*number):
    result = 0
    for n in number:
        if (n > result):
           result = n
    return result

def Collatz_Getstep(num): #입력한 값이 콜라츠 추측 계산 횟수를 반환
    i = 1 #반복횟수를 지정(처음값은 1)
    while(num != 1): #콜라츠 추측에 따라 1이 될때 까지 num을 반복
        if num % 2 == 0: #짝수이면 나누기 2를 한다
            num /= 2
        else: #홀수이면 3*num+1을 한다
            num = (3 * num) + 1
        i += 1 #반복 횟수를 늘린다
    return i