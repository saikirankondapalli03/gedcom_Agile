import unittest
from us_test.sprint02_tests.test12 import UserStory12Test
from us_test.sprint02_tests.test13 import UserStory13Test

class Sprint02_Test(unittest.TestCase):
    UserStory12Test()
    UserStory13Test()
        
        
if __name__ == "__main__":
    unittest.main()