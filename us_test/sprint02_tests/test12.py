from userstories.sprint02_us.userStory12 import us12_parents_not_too_old
import unittest 

class UserStory12Test(unittest.TestCase):

    def test_us12(self):
        
       error_list = us12_parents_not_too_old("gedfilestest/sprint02_ged/us12testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US12: The age difference of child:I19 and mother:I07 is greater than or equal to 60',
                                    'ERROR: INDIVIDUAL: US12: The age difference of child:I19 and father:I01 is greater than or equal to 80',
                                    'ERROR: INDIVIDUAL: US12: The age difference of child:I26 and mother:I07 is greater than or equal to 60',
                                    'ERROR: INDIVIDUAL: US12: The age difference of child:I26 and father:I01 is greater than or equal to 80'])        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     