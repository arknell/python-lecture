"""
lecture-04 python module, package, exception
"""

# 01 module
# 1) mod.py -> 사용할 모듈 이름
# 일반적 모듈 파이썬 파일 작성
def add(a, b):
	return a + b

def sub(a, b): 
	return a-b
    
# 2) main.py -> 사용할 메인 모듈
# 모듈을 사용할 메인 모듈 작성
import mod  # mod.py를 import 함. 파일 디렉토리에 있을 경우(./test/mode.py) -> import test.mode (package 에서 상세히)
print(mod.add(1, 2))

# 3) main1-1.py
# 메인 모듈에서 디렉토리 안의 모듈을 사용할 때 주의
import test.mod 
print(mod.add(1, 2))  # error
# ----
print(test.mod(1, 2))  # success
# ---- 
import test.mod as mod
print(mod.add(1, 2))  # success

# 4) main2.py
# 모듈 내 함수만 참조
from mod import add
print(add(1, 2))

# 5) mod.py
# 모듈 파일 작성 시 주의점
def add(a, b):
	return a + b

def sub(a, b): 
	return a-b
	
print(add(1, 4))
print(sub(4, 2))

# if __name__ == "__main__":
#	print(add(1, 4))
#	print(sub(4, 2))

# ※ __name__ -> 직접 실행 시 __main__ 값 저장, 외부 참조 시 해당 파일의 이름 저장(.py는 제외)

# 02 package
# 1) main3.py
from test import mod
print(mod.add(1, 2))  # not work

# 2) __init__.py (test 디렉토리에 생성)
# 비어 있는 파일 1) solved

# 3) main4.py
from test import *
print(mod.add(1, 2))  # not work

# 4) __init__.py
__all__ = ['mod']  # 3) solved

# ※ __all__ -> __init__.py가 있는 디렉토리 내 import * 로 사용 가능한 모듈 정의

# 03 exception
# 1) exception.py
# 예외처리 일반
try:
    4 / 0
except ZeroDivisionError as e:  # 발생 에러 as 발생 에러 변수
    print(e)
	
# 2) exception2.py
# 변수 없는 예외처리
try:
	4 / 0
except:
	print('영으로 나누려 하였습니다!!')

# 3) exception3.py
# 여러 예외처리
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
except:
	print("예기치 않은 오류가 발생하였습니다.")
	
# 4) exception4.py
# 예외처리 한번에 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 5) raise.py
# 예외 발생
class Bird:
    def fly(self):
        raise NotImplementedError
		
# 6) MyError.py
# 발생 에러 정의
class MyError(Exception):
    def __str__(self):
		return "오류 메시지"
# 정의한 에러 사용
try:
    # some code
	if 어떤 조건:
		raise MyError()
except MyError as e:
    print(e)
	
