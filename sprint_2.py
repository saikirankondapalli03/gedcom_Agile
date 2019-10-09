from userstories.sprint02_us.userStory12 import us12_parents_not_too_old
from userstories.sprint02_us.userStory13 import us13_siblings_spacing
from print_main import printTables

def sprint_2_user_stories():
    master_file_name="gedfilestest/sprint02-testdata_2.ged"
    indTable,famTable= printTables(master_file_name)
    error_list = []
    error_list.extend(us12_parents_not_too_old(master_file_name))
    error_list.extend(us13_siblings_spacing(master_file_name)) 
    

    for each_error in error_list:
        print(each_error)
    
    with open('sprint2output.txt','w') as file:
        file.write('\n\nIndividuals Information----------------------->\n')
        file.write(indTable.get_string())
        file.write("\n")
        file.write('\n\nFamily Information----------------------->\n')
        file.write(famTable.get_string())
        file.write("\n")
        for each_error in error_list:
            file.write(each_error+"\n")
        
        
if __name__ == "__main__":
    sprint_2_user_stories()