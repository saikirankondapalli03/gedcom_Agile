from collections import OrderedDict

from prettytable import PrettyTable

import datetime

import shutil

import os

from famClass import famClass

from indClass import indClass

def dateFormating(myDate):
        myMonths = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}
        
        myDate = myDate.split()
        
        if int(myDate[0]) in range(1,10):
            finalDay = '0' + myDate[0]
        
        else:
            finalDay = myDate[0]
            
        
        finalMonth = myMonths[myDate[1]]
        
        finalYear = myDate[2]

        return (finalYear + '-' + finalMonth + '-' + finalDay)



def addAges(indDict):
        for iD in indDict: 
            if (indDict[iD].Birthday != 'NA'):
                start = datetime.datetime.strptime(indDict[iD].Birthday, "%Y-%m-%d")
                #print(start)
                end = datetime.date.today()
                #print(end)
                finalAge = end.year - start.year - ((end.month, end.day) < (start.month, start.day))
                
                indDict[iD].ageSet(finalAge)
                #print(finalAge)
                
                
def addAlives(indDict):
    
    #alive = True
    
    for iD in indDict:
        if(indDict[iD].Death != 'NA'):
            indDict[iD].aliveSet(False)
        else:
            #alive
            indDict[iD].aliveSet(True)
    
 
def main():
    myFile = open("test.ged")
    
    indDict = OrderedDict()
    
    famDict = OrderedDict()
    
    indTable = PrettyTable()
    
    famTable = PrettyTable()
    
    myFlag = ''
    
    myFlag1 = ''
    
    myFlag2 = ''
    
    for line in myFile:
        lineData = line.strip().split(" ")
        
        if lineData[0]:
            myLevel = lineData[0]
            
            myTag = lineData[1]
            
            myArg = lineData[2:]
            
            myArg1 = " ".join(myArg)
            
            if myArg1 == 'INDI' or myArg1 == 'FAM':
                if myLevel == '0':
                    myFlag = myTag
                    
                    if myArg1 == 'INDI':
                        indDict[myFlag] = indClass(myTag)
                    
                    elif myArg1 == 'FAM':
                        famDict[myFlag] = famClass(myTag)
                        
            if myLevel == '1':
                if (myTag == 'NAME'):
                    #print(myArg1)
                    indDict[myFlag].nameSet(myArg1)
                    
                elif (myTag == 'SEX'):
                        indDict[myFlag].sexSet(myArg1)
                    
                elif (myTag == 'BIRT'):
                        myFlag1 = 'Birthday'
                    
                elif (myTag == 'DEAT'):
                        myFlag1 = 'Death'
                    
                elif (myTag == 'FAMC'):
                        indDict[myFlag].childSet(myArg1)
                    
                elif (myTag == 'FAMS'):
                        indDict[myFlag].spouseSet(myArg1)
                    
                elif (myTag == 'HUSB'):
                        famDict[myFlag].husbandSet(myArg1)
                    
                    
                elif (myTag == 'WIFE'):
                        famDict[myFlag].wifeSet(myArg1)
                    
                elif (myTag == 'CHIL'):
                        famDict[myFlag].multChildSet(myArg1)
                    
                elif (myTag == 'MARR'):
                        myFlag1 = 'Marriage'
                    
                elif (myTag == 'DIV'):
                        myFlag1 = 'Divorce'
                    
            elif myLevel == '2':
                if myTag == 'DATE':
                        
                    if (myFlag1 == 'Birthday'):
                        indDict[myFlag].birthdaySet(myArg1)
                        
                    elif (myFlag1 == 'Death'):
                        indDict[myFlag].deathSet(myArg1)
                        
                    elif (myFlag1 == 'Marriage'):
                        myHusb = famDict[myFlag].husbandGet()
                            
                        myWif = famDict[myFlag].wifeGet()
                            
                        indDict[myHusb].marriageSet(myArg1)
                            
                        indDict[myWif].marriageSet(myArg1)
                            
                        famDict[myFlag].marriageSet(myArg1)
                        
                    elif (myFlag1 == 'Divorce'):
                        myHusb = famDict[myFlag].husbandGet()
                            
                        myWif = famDict[myFlag].wifeGet()
                            
                        indDict[myHusb].divorceSet(myArg1)
                            
                        indDict[myWif].divorceSet(myArg1)
                            
                        famDict[myFlag].divorceSet(myArg1)
                            
    
    addAges(indDict)
    
    addAlives(indDict)
    
    indTable.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
   
    
    #print(famDict)
    
    for iD in indDict:
        indTable.add_row([indDict[iD].indID.strip('@'), indDict[iD].Name, indDict[iD].Sex, indDict[iD].Birthday, indDict[iD].Age, indDict[iD].Alive, indDict[iD].Death, indDict[iD].Child.strip('@'), indDict[iD].Spouse.strip('@')])
  
    
    #print(famDict)

    
    #print(famDict)
    print('\n\nIndividuals Information----------------------->\n')
    print (indTable)

    famTable.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
   
    
    #print(famDict)
    
    
    for famID in famDict:
        s=famDict[famID].multChild
        childrenarr=[];
        for lin in s:
            childrenarr.append(lin.strip("@"))
        famTable.add_row([famDict[famID].famID.strip('@'), famDict[famID].Marriage, famDict[famID].Divorce, famDict[famID].Husband.strip('@'), indDict[famDict[famID].Husband].Name, famDict[famID].Wife.strip('@'), indDict[famDict[famID].Wife].Name,childrenarr])
    
   
    
    #print(famDict)
   
    
    #print(famDict)
    print('\n\nFamily Information----------------------->\n')
    print (famTable)
                        
                    
                
                
            

if __name__ == '__main__':
    main()