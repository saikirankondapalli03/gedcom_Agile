from userstories.sprint02_us.userStory11 import us11_no_bigamy
import unittest 

class UserStory11Test(unittest.TestCase):

    def test_us11(self):
        
       error_list = us11_no_bigamy("gedfilestest/sprint02_ged/us11testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US11: I01: Individual Married to two persons in two families F23 and F24',
'ERROR: INDIVIDUAL: US11: I19: Individual Married to two persons in two families F25 and F26', 
'ERROR: INDIVIDUAL: US11: I29: Individual Married to two persons in two families F27 and F28'])        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     