# --------------------
# capsulizing
# inheritance
# ---------------------


class SimpleStack:
	"""
	implements for packaging
	"""
	def __init__(self):
		self.a = 1
		self._b = 2
		self.__c = 3
		self.__numbers = []

	def push(self, num):
		self.__numbers.append(num)

	def pop(self, num):
		length = len(self.__numbers)
		if length == 0:
			return -1

		return self.__numbers.pop(length - 1)


# main code for capsulizing
# private : class 만 사용
# public : 모두 사용
# protected : 상속 받은 class까지 사용

stack = SimpleStack()
stack.__numbers.clear()  # access to private member

# 변수 선언
word = "hello world"

# 문자 접근
for char in word:
  stack.push(char)

newWord = ""
# 새 문자 생성
for char in word:
  newWord += stack.pop()

print(newWord)
# Quiz 1. stack 을 이용한 문자열 reverse 구현
# "hello world" -> "dlrow olleh" 로 출력
# Quiz 1-2. number 맴버를 public으로 교체
#           문자열 입력 후 4번째 인덱스 제거
#           출력


class Shape:
	"""
	1. parent class for paint Application
	"""
	def __init__(self):
		self.__secret = -1
		self._corner = 0
		self._point = [(0, 0)]

	def _set_corner(self, corner):
		self._corner = corner

	def get_corner(self):
		return self._corner

	def set_point(self, *args):
		self._point = []
		for i in range(*args):
			self._point.append(args[i])

	def get_point(self):
		return self._point

	def to_string(self):
		return "my shape has %d corners" % self._corner


class Rect(Shape):
	"""
	2. child class from Shape
	Point : [Top left, Top right, Bottom left, Bottom right]
	"""
	def __init__(self):
		super().__init__()
		self._set_corner(4)
		self.__secret = 5
		super().__secret = 6

	def to_string(self):
		return "my rectangle has %d corners" % self._corner

	def get_width(self):
		if len(self._point) == 4:
			return self._point[2][0] - self._point[1][0]

		return 0


class Triangle(Shape):
	"""
	2-1. child class from Shape
	"""
	def __init__(self):
		super().__init__()
		self._set_corner(3)

	def to_string(self):
		return "my triangle has %d corners" % self._corner


class Diamond(Rect):
	"""
	3. grand child class from Shape and child class from Rect
	"""
	def __init__(self):
		super().__init__()

	def to_string(self):
		return "my diamond has %d corners" % self._corner


# Quiz 2. Polygon class 만들어 보기 (n각형)
# Quiz 2-1. 4, 5, 6각형의 Polygon object 만들어서 to_string() 매소드 사용해보기


# main code for test

sh = Shape()
print("shape corner is %d" % sh.get_corner())

rect1 = Rect()
rect1.set_point((4, 0), (8, 0), (2, 5), (6, 6))

print("rectangle width is %d" % rect1.get_width())
# print("shape width is %d" % sh.get_width())


# 4. inheritance usage
def get_description(shape):
	if isinstance(shape, Shape):
		return shape.to_string()

	return "this is not Shape's instance."

get_description(Shape())
get_description(Rect())
get_description(Triangle())
get_description(Diamond())

# Quiz 3. Quiz 2에서 만든 polygon object를 get_description으로 사용해보기
# Quiz 4. get_description 함수의 isinstance(shape, Shape)를 isinstance(shape, Rect)로 바꾸어 보기
