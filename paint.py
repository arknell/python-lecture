"""
과제: Stamp 그림판 만들기
1. 해당 windows app은 python tkinter를 이용하였음
2. 마우스 왼쪽 클릭 시 사각형, 삼각형 또는 다이아몬드 도장을 그려줌
3. 마우스 오른쪽 버튼 클릭 시 도장 종류가 바뀜
4. 키보드 u 버튼 클릭 시 undo
5. 키보드 r 버튼 클릭 시 redo
6. # --- start TODO: ~~
   # --- end
   주석 블록으로 채워져있는 곳을 코딩하면 완성
"""
from tkinter import *


# --- start TODO: BLOCK 1 - 삼각형, 마름모 class 생성
class SimpleStack:
	"""
	implements for packaging
	"""
	def __init__(self):
		self.current = 0
		self.__numbers = []

	def __iter__(self):
		return self

	def __next__(self):
		if self.current == len(self.__numbers):
			self.current = 0
			raise StopIteration
		else:
			self.current += 1
			return self.__numbers[self.current - 1]

	def push(self, num):
		self.__numbers.append(num)

	def pop(self, num):
		length = len(self.__numbers)
		if length == 0:
			return -1

		return self.__numbers.pop(length - 1)


class Shape:
	def __init__(self, start_point):
		self._start_point = start_point
		self._point = [self._start_point]

	def get_point(self):
		serialize = []
		for point in self._point:
			if len(point) == 2:
				serialize.append(point[0])
				serialize.append(point[1])

		return serialize


class Rect(Shape):
	def __init__(self, start_point):
		super().__init__(start_point)
		self._point.append((start_point[0] + 20, start_point[1]))
		self._point.append((start_point[0] + 20, start_point[1] + 20))
		self._point.append((start_point[0], start_point[1] + 20))
# --- end


window = None												# windows 창
canvas = None												# 도장 그리기 캔버스
static_mode = ["Rectangle", "Triangle", "Diamond"]		# 전체 도장 모드
mode = 0													# 현재 도장 모드
stack = SimpleStack()										# undo 스택
redo_stack = SimpleStack()									# redo 스택


def mouse_drop(event):
	"""
	마우스 왼쪽 버튼 up 이벤트
	"""
	global mode, canvas, stack
	x = event.x
	y = event.y
	s = None
	if mode == 0:
		s = Rect((x, y))
		stack.push(s)
	# --- start TODO: BLOCK 2 - 객체를 생성하고 그리기
	# --- end

	canvas.delete("all")

	for shape in stack:
		if isinstance(shape, Shape):
			arr = shape.get_point()
			canvas.create_polygon(*arr, outline="red", width=2)


def change_mode(event):
	"""
	마우스 오른쪽 버튼 down 이벤트
	"""
	global mode
	global static_mode
	global window
	if mode < len(static_mode) - 1:
		mode = mode + 1
	else:
		mode = 0

	window.title(static_mode[mode])


def undo_redo(event):
	"""
	키보드 입력 이벤트
	"""
	if event.char.lower() == 'u':
		# --- start TODO: BLOCK 3 - undo
		# --- end
		pass
	elif event.char.lower() == 'r':
		# --- start TODO: BLOCK 4 - redo
		# --- end
		pass


window = Tk()
window.title(static_mode[mode])
canvas = Canvas(window, height=600, width=600)
canvas.bind("<ButtonRelease-1>", mouse_drop)
canvas.bind("<ButtonRelease-3>", change_mode)
window.bind("<Key>", undo_redo)
canvas.grid(row=0, column=0)
canvas.pack()
# button_change = Button(window, text="triangle", width=15)
# button_change.grid(row=1, column=0)
# button_change.pack()
window.mainloop()


# 파이썬으로 만드는 그림판
