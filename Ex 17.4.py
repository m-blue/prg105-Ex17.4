class Point(object):

    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "%s, %s" % (self.x,self.y)

    def __add__(self, other):
        self.x += other
        self.y += other
        return self.x, self.y


some = Point()
print some

some + 4

print some
