from userStory01 import user_story01_main
from print_main import printTables

def sprint_1_user_stories():
    printTables("mytestfile.ged")
    error_list = []
    error_list.extend(user_story01_main()) 

    

if __name__ == "__main__":
    sprint_1_user_stories()