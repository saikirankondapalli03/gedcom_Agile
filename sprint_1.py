from userStory04 import user_story04
from userStory08 import user_story08
from userStory03 import us03_birth_b4_death
from userStory06 import us06_divo_b4_death

from print_main import printTables

def sprint_1_user_stories():
    master_file_name="us04testdata.ged"
    printTables(master_file_name)
    error_list = []
    '''
    error_list.extend(user_story01(master_file_name)) 
    error_list.extend(user_story02(master_file_name)) 
    error_list.extend(user_story03(master_file_name)) 
    '''
    
    error_list.extend(us03_birth_b4_death(master_file_name))
    error_list.extend(user_story04(master_file_name)) 
    '''
    error_list.extend(user_story05(master_file_name)) 
    error_list.extend(user_story06(master_file_name)) 
    error_list.extend(user_story07(master_file_name)) 
    '''
    
    error_list.extend(us06_divo_b4_death(master_file_name))
    error_list.extend(user_story08(master_file_name)) 
    
    for each_error in error_list:
        print(each_error)

    

if __name__ == "__main__":
    sprint_1_user_stories()