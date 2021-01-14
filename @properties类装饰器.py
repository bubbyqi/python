class Student(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be a integer')
        if value < 0 or value > 100:
            raise ValueError('score must bw 0 ~ 100')
        self._score  = value

class Screen(object):
    @property
    def  width(self):
        return self._width
    @width.setter
    def  width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be a interge')
        self._width = value
    @property
    def  height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be a interge')
        self._height = value
    @property
    def resolution(self):
        return self.width * self.height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
