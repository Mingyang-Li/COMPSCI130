'''Q1-Q3'''


class MyPoint:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return str((self.__x, self.__y))

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new):
        if new >= 0:
            self.__x = new

    def set_y(self, new):
        if new >= 0:
            self.__y = new

    def get_distance(self, other_point):
        import math
        x2 = self.get_y()
        x1 = self.get_x()
        y2 = other_point.get_y()
        y1 = other_point.get_x()
        return math.sqrt(((x2 - y2) ** 2) + ((x1 - y1)**2))

    def is_near_by(self, other_point):
        return self.get_distance(other_point) < 5.0


'''Q4-Q6'''


class MyLine:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__start_point = MyPoint(x1, y1)
        self.__end_point = MyPoint(x2, y2)

    def __str__(self):
        return '{} to {}'.format(self.__start_point, self.__end_point)

    def set_end_point(self, x2, y2):
        if x2 >= 0 and y2 >= 0:
            self.__end_point = MyPoint(x2, y2)
        elif x2 < 0 and y2 >= 0:
            self.__end_point = MyPoint(0, y2)
        elif x2 >= 0 and y2 < 0:
            self.__end_point = MyPoint(x2, 0)

    def get_end_point(self):
        return self.__end_point

    def set_start_point(self, x1, y1):
        if x1 >= 0 and y1 >= 0:
            self.__start_point = MyPoint(x1, y1)
        elif x1 < 0 and y1 >= 0:
            self.__start_point = MyPoint(0, y1)
        elif x1 >= 0 and y1 < 0:
            self.__start_point = MyPoint(x1, 0)

    def get_start_point(self):
        return self.__start_point

    def get_length(self):
        return self.__start_point.get_distance(self.__end_point)


'''Q7-Q9'''


class MyCircle:
    def __init__(self, x=0, y=0, radius=1):
        self.__centre_point = MyPoint(x, y)
        self.__radius = radius

    def __str__(self):
        return 'Circle at {}, radius = {}'.format(self.__centre_point, self.__radius)

    def set_radius(self, radius):
        if radius >= 0:
            self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_centre_point(self, x, y):
        self.__centre_point.set_x(x)
        self.__centre_point.set_y(y)

    def get_centre_point(self):
        return self.__centre_point

    def get_distance(self, another_circle):
        return self.__centre_point.get_distance(another_circle.get_centre_point())


'''Q10'''


class MyMultiLine:
    def __init__(self, points=[]):
        self.__points = points

    def __str__(self):
        myStr = ''
        for tp in self.__points:
            myStr += str(tp)
        return myStr

    def get_length(self):
        ptsArr = self.__points
        disance = 0
        for i in range(0, len(ptsArr) - 1):
            disance += ptsArr[i].get_distance(ptsArr[i+1])
        return disance

