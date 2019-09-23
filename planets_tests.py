import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    #Test for user input "136"
    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())
    
    #Test for user input "100"
    def test_02(self):
        sys.stdin = io.StringIO("100")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 38.0 pounds.\nOn Jupiter you would weigh 234.0 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())
        
if __name__ == "__main__":
        unittest.main()