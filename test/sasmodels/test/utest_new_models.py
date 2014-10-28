"""
    Unit tests for specific models
    @author: Ricardo M. F. Leal
"""

import unittest, time, math

# Disable "missing docstring" complaint
# pylint: disable-msg=C0111
# Disable "too many methods" complaint 
# pylint: disable-msg=R0904 
# Disable "could be a function" complaint 
# pylint: disable-msg=R0201


class TestCyl(unittest.TestCase):
    """Unit tests for cylinder"""
    
    def setUp(self):

        from sasmodels.CylinderModel import CylinderModel
        self.comp = CylinderModel()
        
    def test1D(self):
        """ Test 1D model of a cylinder """ 
        self.assertAlmostEqual(self.comp.run(0.2), 0.041761386790780453, 4)
       
    def testTime(self):
        """ Time profiling """
        self.comp.run(2.0)
        t0 = time.clock()
        self.assertTrue(time.clock()-t0<1e-5)
     
    def test2D(self):
        """ Test 2D model of a cylinder """ 
        self.comp.setParam('cyl_theta', 10.0)
        self.comp.setParam('cyl_phi', 10.0)
        self.assertAlmostEqual(self.comp.run([0.2, 2.5]), 
                               #0.038176446608393366, 2) 
                                0.052822284, 2)
    def test2DXY(self):
        """ Test 2D model of a cylinder """ 
        self.comp.setParam('cyl_theta', 10.0)
        self.comp.setParam('cyl_phi', 10.0)
        self.assertAlmostEqual(self.comp.runXY([0.01, 0.02]), 
                               #14.89, 2)
                                23.035643, 2) 
 
         

        

if __name__ == '__main__':
    unittest.main()