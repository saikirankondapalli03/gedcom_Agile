import unittest
from us_test.sprint01_tests.test01 import UserStory01Test
from us_test.sprint01_tests.test02 import UserStory02Test
from us_test.sprint01_tests.test03 import UserStory03Test
from us_test.sprint01_tests.test04 import UserStory04Test
from us_test.sprint01_tests.test05 import UserStory05Test
from us_test.sprint01_tests.test06 import UserStory06Test
from us_test.sprint01_tests.test07 import UserStory07Test
from us_test.sprint01_tests.test08 import UserStory08Test

class Sprint01_Test(unittest.TestCase):
    UserStory01Test()
    UserStory02Test()
    UserStory03Test()
    UserStory04Test()
    UserStory05Test()
    UserStory06Test()
    UserStory07Test()
    UserStory08Test()
        
        
if __name__ == "__main__":
    unittest.main()