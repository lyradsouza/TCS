class Car(object):
  def factory(type):
    if type=="sportscar":
	return SportsCar()
    if type=="van":
	return Van()
    if type=="truck":
	return Truck()
    assert 0, "Bad car creation: " + type

  factory = staticmethod(factory)

class SportsCar(Car):
  def __init__(self):
     self.gallons=10
     self.unitsMoved=0

  def move(self):
     self.unitsMoved+=5
     self.gallons-=1
     if self.gallons<0:
       print "out of gas!"
     else:
        print "Sports car at {} with {} gallons of gas".format(self.unitsMoved, self.gallons)


class Van(Car):
  def __init__(self):
     self.gallons=15
     self.unitsMoved=0

  def move(self):
     self.unitsMoved+=3
     self.gallons-=1
     if self.gallons<0:
       print "out of gas!"
     else:
       print "Van at {} with {} gallons of gas".format(self.unitsMoved, self.gallons)


class Truck(Car):
  def __init__(self):
     self.gallons=25
     self.unitsMoved=0

  def move(self):
     self.unitsMoved+=1
     self.gallons-=1
     if self.gallons<0:
       print "out of gas!"
     else:
       print "Truck at {} with {} gallons of gas".format(self.unitsMoved, self.gallons)

