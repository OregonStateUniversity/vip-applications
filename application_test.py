'''
Name: Daniel Reti
OSU Email: retid@oregonstate.edu
Desc: Fork of vip-application, custom map function
'''
import turtle
import unittest
from application import map

class mapTurltleTester(unittest.TestCase):
    
    def test_display(self):
        #test that the default information displays
        self.assertEqual(map(),([0,0,0,0,'dog']))
    
    #test for upper case
    def test_to_upper(self):
        self.assertEqual(map(str.upper),([0,0,0,0,'DOG']))
     #test for lower case
    def test_to_lower(self):
        self.assertEqual(map(str.lower,["CaT","DoG",10, "%"]),(["cat","dog",10, "%"])) 
     #test for float cast
    def test_casting_to_float(self):
        self.assertEqual(map(float,[10,4,55,"Man",10.2]),([10.0,4.0,55.0,"Man",10.2]))
    #test for cast to str
    def test_casting_to_str(self):
        self.assertEqual(map(str,[10,4,55,"Man",10.2]),(['10','4','55',"Man",'10.2']))
if __name__ == '__main__':
   unittest.main()