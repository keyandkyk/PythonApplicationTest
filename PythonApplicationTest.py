import fun #사용자 함수 파일
#from fun import * fun에 지정된 함수등을 사용할 때 fun. 을 쓰기 않을 때 사용
#fun이 솔루션 탐색기에 추가가 안 되면 워닝 발생(파일에서 추가한다고 솔루션에서 추가가 안 되는 듯 함)

message = "   파이썬 비쥬얼 스튜디오   "
print(message.strip())
fun.hello(message)
fun.hello(message, "2019")

message = fun.get_max(2,4,6,8,1,3,5,7,9,10)
print(message)

print(fun.Collatz_Getstep(12345))