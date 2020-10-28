import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_blockAverages(self): 
        myav = blockAverages( 10, radii )
        for i in range(10) : 
            bav = sum( radii[i*20:(i+1)*20] ) / 20 
            self.assertTrue( np.abs(myav[i]-bav)<1e-7,  "the block averages you have computed are not correct" )
