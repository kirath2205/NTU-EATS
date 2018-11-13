#######################################################################################################################################################################    
#######################################################################################################################################################################
###################################################################        WELCOME        ########################################################################################
###################################################################              TO               ########################################################################################
###################################################################             NTU             ########################################################################################
###################################################################            EATS            ########################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################



from tkinter import * #tkinter is a standard GUI library that provides a fast and easy way to create GUI applications
from tkinter import simpledialog
import pygame #pygame is a standard python library used for making multimedia applications
import time
import sys #provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter

import datetime #it is a class that deals with the current date and time
from tkinter import messagebox #it is used to display messageboxes in the GUI
import tkinter as tk
import os #it is used to open the text files


Dict1={}
Dict2={}

#The function MouseClick is used to get the user's current location with the help of a mouse click on NTU's campus map 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MouseClick():
    
    pygame.init() #used to initialize the pygame terminal
    introScreen=pygame.image.load("Intro.jpg")                             #this statement is used to display a full sized intro image as soon as the program is executed
    sc=pygame.display.set_mode((800,800),pygame.RESIZABLE) #it is used to set the frame of the pygame terminal
    sc.blit(introScreen,(0,0))
    pygame.display.flip()
    pygame.time.delay(5000) #used to introduce a delay to show the intro image for a significant amount of time
    pygame.display.update()
    pygame.init() #used to initialize the pygame terminal
    
    pygame.quit()
    
    introScreenImage=pygame.image.load("ntucampus2.0.png")
    screen=pygame.display.set_mode((1221,862))      #this statement is used to display NTU's campus map in-order to get user's current locaion
    
    screen.blit(introScreenImage,(-4.5,-4.5))
    pygame.display.flip()
    flag=True
#----------------------------------------A sentinent control loop has been used to display the image untill the user clicks his current location , and terminates as soon as the user clicks his location---------------------------------------    
    while flag:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if e.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                flag=False
                break
            
        pygame.display.update()
    return(mx,my)   #this return statement returns the co-ordinates of the user's current location



pygame.init()
pygame.quit() #this statement is used to quit the pygame terminal

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#main database  Dict1-containing name of the canteen, exact address , opening time ,  closing time , seating capacity , number of stalls
#backend database Dict2- containing average cost per person, average rating(out of 5.0), hygiene grade , halal certification( H for yes and N for no), telephone number , cusines availabe
#Hygiene rating
#A-excellent
#B-good
#C-average
#D-below average
#E-poor
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------Various canteens have been alloted a rank according to a survey done last year--------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
Dict1={}

Dict2={}

Dict1[0]=["McDONALD'S","NORTH SPINE PLAZA 76 NANYANG DRIVE N2 1-01-08 SINGAPORE 637331",'07:00','00:00',999,1]

Dict2[0]=[5.0,4.7,'A','H',"Telephone number : 6792 9917",["Fast-food"]]

Dict1[1]=["SUBWAY","NORTH SPINE PLAZA 76 NANYANG DRIVE N2 1-01-07 SINGAPORE 637331",'08:00','21:00',999,1]

Dict2[1]=[7.0,4.5,'A','H',"Telephone number : 6462 5238",["Fast-food"]]

Dict1[2]=["KFC","NORTH SPINE PLAZA 76 NANYANG DRIVE N2 1-01-04 SINGAPORE 637331",'07:30','22:00',999,1]

Dict2[2]=[7.0,4.1,'A','H',"Telephone number : 6762 6124",["Fast-food"]]

Dict1[3]=["PIZZA HUT EXPRESS","NORTH SPINE PLAZA 76 NANYANG DRIVE N2 1-01-04 SINGAPORE 637331",'11:00','22:00',999,1]

Dict2[3]=[8.0,4.2,'A','H',"Telephone number : 6762 6124",["Fast-food"]]

Dict1[4]=["STARBUCKS","NORTH SPINE PLAZA 76 NANYANG DRIVE N2 1-01-06 SINGAPORE 637331",'07:00','22:00',999,1]

Dict2[4]=[6.5,4.7,'A','H','Telephone number : 6910 1245',["Fast-food","Beverages", "Bakery"]]

Dict1[5]=["FOOD COURT 1","21 NANYANG CIRCLE ,SINGAPORE-639778, HALL 1",'07:00','21:00',310,9]

Dict2[5]=[5.0,3.8,'A','H','Telephone number : 63344 3033',["Singaporean"]]

Dict1[6]=["FOOD COURT 2","35 STUDENTS WALK , SINGAPORE-639548 , HALL 2",'07:00','21:00',446,10]

Dict2[6]=[6.5,4.0,'B','H',"Telephone number : 6334 3033",["Singaporean"]]

Dict1[7]=["FOOD COURT 9","50 NANYANG AVENUE SINGAPORE 639798 ,HALL 9",'07:00','21:00',293,9]

Dict2[7]=[4.5,4.3,'B','H',"Telephone number : 9692 3456",["Indian","Singaporean","Korean"]]

Dict1[8]=["FOOD COURT 11","20 NANYANG AVENUE SINGAPORE 639809 ,HALL 11",'07:00','21:00',210,6]

Dict2[8]=[4.5,3.7,'B','H',"Telephone number : 9786 6726",["Korean","Indian","Japanese"]]

Dict1[9]=["FOOD COURT 13","32 NANYANG CRESCENT SINGAPORE 637658 ,HALL 13",'07:00','21:00',210,8]

Dict2[9]=[4.0,2.9,'B','N',"Telephone number : 9851 0908",["Chinese","Korean"]]

Dict1[10]=["FOOD COURT 14","34 NANYANG CRESCENT SINGAPORE 637634 , HALL 14",'07:00','21:00',270,6]

Dict2[10]=[5.5,3.2,'B','N',"Telephone number : 8112 7239",["Japanese","Singaporean"]]

Dict1[11]=["FOOD COURT 16","50 NANYANG WALK SINGAPORE 639929 , HALL 16",'07:00','21:00',304,5]

Dict2[11]=[3.5,3.0,'C','H',"Telephone number : 9450 5893",["Singaporean","Japanese","Indian"]]

Dict1[12]=["Ananda Kitchen","60 NANYANG CRESCENT BLOCK 19A SINGAPORE 636957 , NORTH HILL",'12:00','22:00',90,1]

Dict2[12]=[6.0,4.0,'A','H',"Telephone number : 9878 0595",["Indian"]]

Dict1[13]=["FOODGLE FOOD COURT","38 NANYANG CRESCENT SINGAPORE BLOCK 23",'07:00','21:00',440,9]

Dict2[13]=[5.5,3.5,'B','H',"Telephone number : 8296 3633",["Indian","Korean","Chinese"]]

Dict1[14]=["NORTH HILL FOOD COURT","60 NANYANG CRESCENT BLOCK 21A SINGAPORE 636957 , NORTH HILL",'07:00','21:00',440,8]

Dict2[14]=[5.5,3.0,'B','N',"Telephone number : 8508 0232",["Italian","Korean", "Singaporean"]]

Dict1[15]=["PIONEER FOOD COURT","162 NANYANG CRESCENT SINGAPORE 637033 , PIONEER HALL",'07:00','21:00',408,12]

Dict2[15]=[6.0,3.5,'C','N',"Telephone number : 8513 8731",["Persian","Korean","Indonesian"]]

Dict1[16]=["QUAD CAFE ","60 NANYANG DRIVE SBS-B1N-10 SINGAPORE 637551, SCHOOL OF BIOLOGICAL SCIENCES",'07:00','21:00',500,8]

Dict2[16]=[7.0,3.1,'A','N',"Telephone number : 8713 4890",["Indian","Singaporean"]]

Dict1[17]=["KOUFU","50 NANYANG AVENUE SS3-B4 SINGAPORE 639798 , SOUTH SPINE",'07:00','21:00',1050,15]

Dict2[17]=[7.0,4.0,'A','H',"Telephone number : 6790 0355",["Singaporean","Indian", "Italian"]]

Dict1[18]=["NORTH SPINE FOOD COURT","50 NORTH SPINE PLAZA 76 NANYANG DRIVE NS2 1-02-03/01A SINGAPORE 637331",'07:00','21:00',1838,19]

Dict2[18]=[5.0,4.4,'A','H',"Telephone number : 6465 8588",["Chinese","Italian","Korean"]]

Dict1[19]=["BAKERY CUISINE","NORTH SPINE PLAZA 50 NANYANG AVENUE NS3-01-22 SINGAPORE 639798",'07:00','21:00',0,1]

Dict2[19]=[2.5,3.7,'A','N',"Telephone number : 6423 8588",["Bakery Items"]]

Dict1[20]=["SANDWICH GUYS","NORTH SPINE PLAZA 50 NANYANG AVENUE NS3-01-22 SINGAPORE 639798",'10:00','20:00',0,1]

Dict2[20]=[4.5,4.0,'A','H',"Telephone number : 6423 8878",["Fast-food"]]

Dict1[21]=["EACH A CUP","NORTH SPINE PLAZA 50 NANYANG AVENUE NS3-01-21 SINGAPORE 639798",'09:00','21:00',0,1]

Dict2[21]=[3.5,4.3,'A','N',"Telephone number : 9182 9307",["Beverages"]]

Dict1[22]=["Long John Silver's","NORTH SPINE PLAZA 76 NANYANG DRIVE N2 1-01-05 SINGAPORE 637331","07:30","22:00",999,1]

Dict2[22]=[7.5,4.2,'A','H',"Telephone number : 6314 0181",["Seafood"]]





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# a list is being used to store whether the canteen is open on sundays and public holidays or not





#CANTEENS LIKE QUAD CAFE AND KOUFU CLOSE EARLY ON SATURDAY


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_halal():
    
    dict_3={}
    dict_4={}
    
#---------------------------------------------2 separate dictionaries have been created to store the details of only those canteens from the database which have a halal certification------------------------------------------------------------    
    c=-1

#---------------------------------------------------------------------The below loop is to store the canteens with halal certification  in the newly created list---------------------------------------------------------------------------------------  

#The searching technique used below is linear search
    for i in range(len(Dict1)):
        
        if(Dict2[i][3]=='H'):
            c+=1
            dict_3[c]=Dict1[i]
            dict_4[c]=Dict2[i]
        
    length_1=len(dict_3)
    

    print("The canteens listed below have a halal certification  :-")
    print()

#----------------------------------------------------------------------In this part of the code we print the details of the canteens with halal certification------------------------------------------------------------------------------------------   
    for i in range(length_1):
            if dict_4[i][3]=='H':
            
                print("Halal Certified")
            else:
            
                print("No Halal certification")
        
        
            print("Name of canteen :","\t",dict_3[i][0])
            print("Address :","\t",dict_3[i][1])
            print("Opening time :",'\t',dict_3[i][2])
            print("Closing time :","\t",dict_3[i][3])
            print("Seating capacity available :","\t",dict_3[i][4])
            print("Number of stalls :","\t",dict_3[i][5])
            print("Average cost per person :","\t",dict_4[i][0])
            print("Average rating out of 5 :","\t",dict_4[i][1])
            print("Hygiene rating :","\t",dict_4[i][2])
            print("Telephone number :","\t",dict_4[i][4])
        
            length_2=len(dict_4[i][5])
        
            print("Cusines Available :",end="  ")
        
            for k in range(length_2):
            
                if k==length_2-1:
                
                    print(dict_4[i][5][k],end=" ")
                else:
                
                    print(dict_4[i][5][k],end=" , ")

#------the function print_details has not been used in this function as this function will print halal certified first before displaying other details which could not have been donw using the standard print_details() function--------------                
            print()
            print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------The function check_hygiene has been used to print the details of the canteens which have A grade hygiene rating-------------------------------------------------------------------------

def check_hygiene():
    
    dict_3={}
    dict_4={}
    
    #---------------------------------------------This part of the code is used to store the details of the canteens which have A grade hygiene rating------------------------------------------------------------------------------------------------
    c=-1
    for i in range(len(Dict1)):
        
        if(Dict2[i][2]=='A'):
            c+=1
            dict_3[c]=Dict1[i]
            dict_4[c]=Dict2[i]
        
    length_1=len(dict_3)
    
#---------------------------------------------------------------------------This part of the code is used to print canteens which have A grade hygiene certification-------------------------------------------------------------------------------------------------------
    print("The canteens listed below have been awarded the best hygiene grade  :-")
    print()
    for i in range(length_1):
        
        print("Hygiene rating :","\t",dict_4[i][2])
        print("Name of canteen :","\t",dict_3[i][0])
        print("Address :","\t",dict_3[i][1])
        print("Opening time :",'\t',dict_3[i][2])
        print("Closing time :","\t",dict_3[i][3])
        print("Seating capacity available :","\t",dict_3[i][4])
        print("Number of stalls :","\t",dict_3[i][5])
        print("Average cost per person :","\t",dict_4[i][0])
        print("Average rating out of 5 :","\t",dict_4[i][1])
        
        if dict_4[i][3]=='H':
            
            print("Halal Certified")
        else:
            
            print("No Halal certification")
            
        print(dict_4[i][4])
        length_2=len(dict_4[i][5])
        print("Cusines Available :",end="  ")
        
        for k in range(length_2):
            
            if k==length_2-1:
                print(dict_4[i][5][k],end=" ")
                
            else:
                print(dict_4[i][5][k],end=" , ")
#----------------------------------------the standard print_details function has not been used as in this functions hygiene grade needs to be displayed first before the rest of the details-----------------------------------------------------                
        print()
        print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------The function show_map is used to display the campus map, in case the user wants to take a look at the map.----------------------------------------------------------------------------------------------------     


def show_map():
    
    pygame.init()
    introScreen=pygame.image.load("ntucampus2.0.png")
    sc=pygame.display.set_mode((1221,862),pygame.RESIZABLE)
    sc.blit(introScreen,(0,0))    
    pygame.draw.circle(sc,(0,0,255),(x,y),5,5) #the blue dot shows the user's current location
    pygame.display.flip()
    pygame.time.delay(5000)
    
    
    pygame.display.update()
    pygame.init()
    
    pygame.quit()
    
  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#the function print_details is used to print the details of a particular canteen stored in the database
#______________________________________________________________________________________________________
#---------------------------------------------------------------------------------------------------------------The parameters are the details stored for each canteen------------------------------------------------------------------------------
    
def print_details(dic1,dic2):
    dic={}                                                                                          #a dictionery has been created to help in shortning the print statements used below in this function
    dic[0]=["Name of canteen :","Address :","opening time :","closing time :",
            "seating capacity :","Number of stalls :"]
    dic[1]=["Average cost per person :","Average rating out of 5 :","Hygiene grade :",
            "Halal certification :","Telephone number :","Cusines :"]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    for i in range(0,6):

            print(dic[0][i],"\t",dic1[i])
            

    
    for i in range(0,6):


        if(i==3):


            if(dic2[i]=='H'):

               print(dic[1][i],"\t","Halal Certified")

            elif(not(dic2[i]=='H')):

               print(dic[1][i],"\t","Non Halal Certified")

        elif(i==5):

            print("Cusines :","\t",end="")

            length=len(dic2[5])

            for i in range(0,length):

                if(i<length-1):

                     print(dic2[5][i]," ",end=" , ")
                else:

                    print(dic2[5][i]," ")
                    
                    
        else:
            
            print(dic[1][i],"\t",dic2[i])
            

        
    print()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------The function cost_sorting is used to sort canteens according to the average cost per person of the respective canteen--------------------------------------------------------------------------

#----------------A try and catch block haas used to check if the budget entered by he user is float or not. If the value is not float, it can cause a ValueError ,hence by using the try and catch block, this exception can be handled.----------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#the parameters are
    #1. Database-frontend
    #2.Database-backend
    #3.the budget entered by the user in the search box of the Graphical User Interface

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cost_sorting(dic1,dic2,entered_text):
    
    if((not(entered_text.isdigit()) and (not(isfloat(entered_text))) ) ):
        #--------1st base case-Incase the user enters anything other than float or integer, which includes string ,character,blank spaces or special character,an error message would be displayed in the message box of the GUI.------------
        
        print("Invalid input")
        print("please enter your budget again")
        messagebox.showinfo("Recommendation system","Invalid input please try again")
#-------------------------------the above statement is used to show an error message on account of invalid input by the user in a messagebox which is a component of tkinter-------------------------------------------------------------------
    elif isfloat(entered_text) and (float)(entered_text)<=0:
        print("Invalid input")
        messagebox.showinfo("Recommendation system","Invalid input please try again")
    else:
        
        dic3={}
        dic4={}
#------------------------------------------2 separate dictionaries (dic3,dic4) have been used to store the details of the canteens whose average cost falls within the user's desired budget----------------------------------------------------------------
        count=0
        cost=(float)(entered_text)
        #--------------------------------2st base case-if the user enters a negative value or a 0,an error message would be displayed in the mesage box of the GUI, stating invalid input----------------------------------------------------------
        
        
        
        
        for i in range(23):
            
            if(dic2[i][0]<=cost):
                dic3[count]=dic1[i]
                dic4[count]=dic2[i]
                count=count+1
                
        length=len(dic3)
        #------------3rd base case-Incase there are no canteens whose average cost falls within the user's desired budget, a message stating no canteens uder this budget would be displayed in the messagebox of the GUI-----------------
        if length==0:
            messagebox.showinfo("Recommendation system","No canteens under this budget,please try again")
#-----------------------------------------------------------The sorting used to sort canteens according to average price per person , is bubble sort.------------------------------------------------------------------------------------------------


#----------------------The time complexity of the algorithm has been kept in mind,hence, a variable swapped has been used to terminate the sorting process if there is no swapping at the end of an iteration--------------------------------

        else:
            print("CANTEENS UNDER THE BUDGET OF :","\t",cost," SGD")
            print()
            for i in range(length-1):
            
                swapped=True
            
                for k in range(length-i-1):
                #-------------------------------------------------------------------------- the canteens are sorted in ascending order of their average cost per person---------------------------------------------------------------

                    if(dic4[k][0]>dic4[k+1][0]):
                        t=dic4[k]
                        dic4[k]=dic4[k+1]
                        dic4[k+1]=t
                    
                        j=dic3[k]
                        dic3[k]=dic3[k+1]
                        dic3[k+1]=j
                    
                        swapped=True
                    
                if not swapped:
                    break
            
        for i in range(length):
            #the function print_details has been used to display the details of the sorted canteens on the basis of their cost
            print_details(dic3[i],dic4[i])


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------The function cusine_search is used to search for the user's preferred cusine in all the canteens available in NTU--------------------------------------------------------------------------

#---------------------------------------------------------------------------------------The function would further be used in a search bar available in the GUI---------------------------------------------------------------------------------------



def cusine_search(dic3,dic4,entered_text):
    #------------------------------------------------------------all the cusines available in all the canteens in NTU would be displayed as soon as the user enters his/her desired cusine-----------------------------------------------------
   


    print('The available cuisines are:')

    print('1. Fast-Food')

    print('2. Singaporean')

    print('3. Indian')

    print('4. Chinese')

    print('5. Italian')

    print('6. Korean')

    print('7. Seafood')

    print('8. Japanese')

    print('9. Indonesian')

    print('10. Persian')

    print('11. Beverages')

    print('12. Bakery Items')

    print()
        
    #-------------------------------------------------------a list has been created in order to check the cusine according to user's preference and take care all the base cases----------------------------------------------------------------------
    l=['Fast-food','Singaporean','Indian','Chinese','Italian','Korean','Seafood','Japanese','Indonesian','Persian','Beverages','Bakery Items']
    length=len(l)
    cusine=entered_text
    flag=False
    
    for i in range(0,length):
 #--------------------------------------------------------------------1st base case-upper() function has been used to ensure that there is no issue of invalid input due to change of case------------------------------------------------------------------------       


#------------------2nd base case-in case the user enters a substring of the cusine instead of the cusine, the desired cusine would still be displayed, hence getting no recommendation or an invalid search message is highly unlikely------

        if (cusine.upper() in l[i].upper()):
            cusine=l[i]
            flag=True
            break
        elif(cusine[0].upper() == l[i].upper()):
            cusine1=l[i]
       
            
            
        else:             #-----------------------------------if the search cusine does not match the cusines available , an error message stating invalid input would be displayed in the messagebox--------------------------------------------------
            cusine1=''
            
    if flag==False:
        print("not found try again")
        messagebox.showinfo("Recommendation system","Invalid input please try again")
            
    elif not(cusine1==''):
        cusine=cusine1
        flag=True
            
    elif flag==True:
        print("Canteens in which ","\t",cusine,'\t',"cusine is available :")
        
        for i in range(23):
            
            if(cusine in dic4[i][5]):              #----------------------------- this statement is used to check if the user's desired cusine is available in what all canteens and accordingly displays the details of those canteens-------------------
                print_details(dic3[i],dic4[i])


def rating_sort():
    dic3={}
    dic4={}
    dic3=Dict1
    dic4=Dict2
    length=len(dic3)
    #the sorting used is bubble sort
    for i in range(0,length-1):
        swapped=False
        
        for k in range(0,length-i-1):
            
            if (dic4[k][1]<dic4[k+1][1]):
                
                t=dic4[k][1]
                dic4[k][1]=dic4[k+1][1]
                dic4[k+1][1]=t
                
                t2=dic3[k][1]
                dic3[k][1]=dic3[k+1][1]
                dic3[k+1][1]=t2
                
                swapped=True
        if not swapped:
            break
        
    for i in range(0,23):#print_details i used for printing the details
        print_details(dic3[i],dic4[i])



def canteens_open_now():
    list1=['Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','N','N','N','N','N','Y','N','N','N','Y']
    #A list has been created to check if the canteens is open on Sundays or not
    #Y-canteen is open on Sunday
    #N-canteen is closed on Sunday
    
    print("Canteens open right now are:-")
    
    date_time=datetime.datetime.now()       #this statement is used to get the current date and time  which would then be broken down to print the canteens open currently
    
    dic3={}
    dic4={}
    count=0
    
    time=(str(date_time))[10:]
    #----------------------------------------------the above statement is used to convert variable date_time to string format and then breaking down the string to extarct the time substring -------------------------------------------------
    time1=time[1:6]
    #--------------------------------------------------the above statment is used to remove other characters in the string that could hinder the calculations----------------------------------------------------------------------------------
    day=datetime.date.today().strftime("%A")
    #---------------------------the above statement is used to get the current day of the week which will be used in this function to find out if a canteen is open on that particular day or not---------------------------------------------
    print("The current time is :",'\t',time1)

    print("Day of the week :","\t",day)
    
    num_time=((float)(time1[:2]))+((((float)(time1[3:])/60)))
    #---------------------------------------------- The above statement is used to convert the string time1 to float format in order to check if the canteen is open at the current time o not----------------------------------------------------

    for i in range(23):
        
        time_range1=((float)(Dict1[i][2][:2]))+((((float)(Dict1[i][2][3:])/60)))
        
        time_range2=((float)(Dict1[i][3][:2]))+((((float)(Dict1[i][3][3:])/60)))

        
#--------time_range1 and time_range2 are used to store float format of the opening and closing time of the canteens which would further be used for comparisons to check if the canteen is open at that time or not-------------------


        if time_range2==0:                          #Since some canteens close at 12 at night hence in the 24 h format it changes to 0 therefore if the closing time is  0, then 24 would be stored in time_range2
            time_range2=24
            

        if(num_time>=time_range1 and num_time<=time_range2 ):       #this if statment is used to check if the current time falls between the range of the opening and closing time of the particular canteen
            if day=='Sunday' and list1[i]=='N':                 #since some canteens are closed on Sundays, hence this if statement would check if the canteen is closed on Sunday or not. The list was declared previously in the function
                continue
            
            else:

                #if the canteen is open, the details of the canteen would be stored in the 2 empty dictionaries created previously in this function
                
                dic3[count]=Dict1[i]
                dic4[count]=Dict2[i]
                count=count+1
                
    length=len(dic3)
    #--------------------If the dictionary is empty,it means no canteens are open currently, therefore a message stating no canteens open would be displayed in the messagebox of the GUI--------------------------------------------------
    if length==0:
        messagebox.showinfo("Recommendation system","There are no canteens open currently, please try again later")
    else:
        for i in range(length):
            print_details(dic3[i],dic4[i])
            print()

#######################################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#######################################################################################################################################################################
#######################################################################################################################################################################      


main = Tk()
main.title("NTU EATS")          #this statement is used to show the main title of the trinket GUI terminal
main.configure(background="black") #this changes the background colour to black

Label(main,bg="black").grid(row=0,column=0,sticky=W)
GUIFrame=Frame(main)            #this is used to create a parent frame in the main GUI
GUIFrame.grid(row=0,column=0,sticky=W)
Label(main).grid(row=900,column=800,sticky=W)

        

Label(GUIFrame,text="Enter your desired budget in the box :",bg="black",fg="white",font="none 13 bold",width=30).grid(row=1,column=4,sticky=S) 
textentry=Entry(GUIFrame,width=25,bg="black",fg="white",cursor='pencil')    #this is used to create a searchbar in which the user would enter the desired budget and the canteens whose average cost falls within the desired budget wil be displayed
                                                                                                                                    
textentry.grid(row=2,column=4,sticky=W)

Label(GUIFrame,text="Enter your desired cusine in the box :",bg="black",fg="white",font="none 13 bold",width=30).grid(row=3,column=4,sticky=S)
textentry2=Entry(GUIFrame,width=25,bg="black",fg="white",cursor='pencil')   #this is used to create a searchbar in which the user would enter the food and the canteens which have that parrticular cusine would be displayed
textentry2.grid(row=4,column=4,sticky=W)


Label(GUIFrame,text="Enter the name of the canteen you want to search :",bg="black",fg="white",font="none 13 bold").grid(row=5,column=4,sticky=S) #this is used to search for the details of the canteen
textentry3=Entry(GUIFrame,width=25,bg="black",fg="white",cursor='pencil')
textentry3.grid(row=6,column=4,sticky=W)


#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################

        

def nearby_canteens(dic3,dic4,x,y):
    
    list_x=[350,351,352,352,351,685,750,968,1163,686,818,608,1170,1175,1169,791,218,250,352,355,355,355,353]
    list_y=[303,303,303,303,303,627,511,290,209,92,101,171,333,157,332,787,381,670,303,304,304,304,303]
    #2 lists list_x,list_y have been created to store the co-ordinates of all the canteens in NTU
        #   list_x contains the x co-ordinates of all the canteens
        #   listy contains the y co-ordinates of all the canteens
        
    new_x=(float)(x)
    new_y=(float)(y)
    
    def distance_a_b(location_of_a,location_of_b):
        return (((((float)(location_of_a[0])-(float)(location_of_b[0]))**2)+(((float)(location_of_a[1])-(float)(location_of_b[1]))**2))**(0.5))

    #The function define distance calculates the direct distance between 2 points and returns it which would further be used to sort the canteens on the basis of distance.
    
    distance=[0]*len(dic3)  #a list-distance has been created to store the distance of all the canteens from the user's current location
    
    for i in range(23): #This loop has been used to calculate and store the distance of all the canteens from the user's location with the help of distance_a_b function
        
        distance[i]=distance_a_b([new_x,new_y],[(float)(list_x[i]),(float)(list_y[i])])
        
    length=len(dic3)
    swapped=False
    #the sorting used to sort the canteens on the basis of distance is bubble sorting
    for i in range(0,length-1):
        swapped=False
        
        for k in range(0,length-i-1):
            
            if distance[k]>distance[k+1]:
                t=distance[k]
                distance[k]=distance[k+1]
                distance[k+1]=t

                t1=dic3[k]
                dic3[k]=dic3[k+1]
                dic3[k+1]=t1

                t2=dic4[k]
                dic4[k]=dic4[k+1]
                dic4[k+1]=t2

                swapped=True
        if swapped==False:  #if there is no swapping at the end of one iteration of the top loop, it would mean that the data is already sorted hence a variable swapped has been used to monitor  such case, and if any such case takes place the loop would be terminated, this would ensure that the alogorithm stops as son as the data is sorted
            
            break
    print("Canteens according to distance :-")
    print()
    
    for i in range(23):
        print("Distance from the user's location:-",'\t',round((distance[i]*(2.025)*(10**-3)),2)," ","km.")
        print_details(dic3[i],dic4[i])

        

#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################    
#######################################################################################################################################################################



def open_file(): #th function about_file has been used to display a text file - readme in txt format on notepad
    os.system("notepad.exe readme.txt")

def about_file():   #the function about_file has been used to display a text file-about us in txt format on notepad
    
    os.system("notepad.exe aboutUs.txt")  #this statement opens the text file on notepad


#######################################################################################################################################################################
#######################################################################################################################################################################

def search_canteen_name(): #the function search_canteen_name has been used to search for the details of a particular canteen
    
    found=False
    canteen=textentry3.get()
    if canteen=='' or canteen==' ':
        messagebox.showinfo("Recommendation System","Invalid canteen name")
    else:
        for i in range(23):
            if Dict1[i][0].upper()==canteen.upper():
                print_details(Dict1[i],Dict2[i])
                found=True
                break
        if  found==False:
            for i in range(23):
                if canteen.upper() in Dict1[i][0].upper():
                    print_details(Dict1[i],Dict2[i])
                    found=True
                    break
                
        if  found==False:
            messagebox.showinfo("Recommendation system","Invalid canteen name")


            
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################



def sort_rank(dic3,dic4):       #the function sort_rank is used to sort canteens on the basis of their rank

    #In Sepember,2017 an online survey was conducted to see the most preferred canteens among NTU students and staff members and accordingly the canteens were alloted various ranks.
    
    print("All the canteens according to their alloted rank are:-")
    print()
    
    list1=[1,2,3,5,20,4,6,7,8,9,11,10,12,13,14,15,16,18,17,19,23,22,21]
    #A list list1 has been created to store the ranks of the various canteens in NTU.

    #The sorting used to sort canteens on the basis of their ranks is bubble sort
    
    for i in range(len(dic3)-1):
        swapped=False
        for k in range(len(dic3)-i-1):
            if list1[k]>list1[k+1]:
                t=list1[k]
                list1[k]=list1[k+1]
                list1[k+1]=t

                t1=dic3[k]
                dic3[k]=dic3[k+1]
                dic3[k+1]=t1

                t2=dic4[k]
                dic4[k]=dic4[k+1]
                dic4[k+1]=t2

                swapped=True
        if swapped==False:
            break
                
    for i in range(23):
        print("Rank : ",'\t',list1[i])
        print_details(dic3[i],dic4[i])


#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################
        



main.geometry('1100x1100')
#the buttons below are all the buttons that are used in the main GUI


button1=Button(GUIFrame,text="1:   Show  canteens with Halal certification",width=40,height=3,bg="black",fg="white",font="none 12 ",command=check_halal,cursor='hand2',activebackground="orange",borderwidth=7).grid(row=1,column=0,sticky=W)
button2=Button(GUIFrame,text="2:   Show canteens with A grade Hygiene", width=40,height=3,bg="black",fg="white",font="none 12",command=check_hygiene,cursor='hand2',activebackground="orange",borderwidth=7).grid(row=2,column=0,sticky=W)
button3=Button(GUIFrame,text="7:   Show campus map",width=40,bg="black",fg="white",height=3,font="none 12",command=show_map,cursor='hand2',activebackground="orange",borderwidth=7).grid(row=7,column=0,sticky=W)
button4=Button(GUIFrame,text=" Submit ",width=8,command=lambda :cost_sorting(Dict1,Dict2,textentry.get()),height=1,cursor='hand2',borderwidth=7).grid(row=2,column=5,sticky=W)
button5=Button(GUIFrame,text=" Submit ",width=8,command=lambda : cusine_search(Dict1,Dict2,textentry2.get()),height=1,cursor='hand2',borderwidth=7).grid(row=4,column=5,sticky=W)
button6=Button(GUIFrame,text="3:   Show canteens according to their average rating",height=3,width=40,bg="black",fg="white",font="none 12",command=rating_sort,cursor='hand2',activebackground="orange",borderwidth=7).grid(row=3,column=0,sticky=W)

button7=Button(GUIFrame,text="4:   Canteens open right now",width=40,bg="black",fg="white",height=3,font="none 12",command=canteens_open_now,cursor='hand2',activebackground="orange",borderwidth=7).grid(row=4,column=0,sticky=W)
button9=Button(GUIFrame,text="10:   quit recommendation system",width=40,bg="black",fg="white",height=3,font="none 12",command=main.destroy and GUIFrame.destroy,cursor='hand2' ,borderwidth=7,activebackground="orange").grid(row=10,column=0,sticky=N)
x,y=MouseClick()
pygame.quit()
button10=Button(GUIFrame,text="5:   Show nearby canteens ",width=40,bg="black",fg="white",height=3,font="none 12",command=lambda :nearby_canteens(Dict1,Dict2,x,y),cursor='hand2',activebackground="orange",borderwidth=7).grid(row=5,column=0,sticky=W)
button11=Button(GUIFrame,text="8:   Readme File",width=40,bg="black",fg="white",height=3,font="none 12",command=open_file,cursor='hand2',activebackground="orange",borderwidth=7).grid(row=8,column=0,sticky=W)
button12=Button(GUIFrame,text="9: About Us",width=40,bg="black",fg="white",height=3,font="none 12",command=about_file,cursor='hand2',activebackground="orange",borderwidth=7).grid(row=9,column=0,sticky=W)
button13=Button(GUIFrame,text="6:  Display Canteens According to their rank",width=40,bg='black',fg='white',height=3,command=lambda : sort_rank(Dict1,Dict2),cursor='hand2',activebackground='orange',font='none 12',borderwidth=7).grid(row=6,column=0,sticky=W)
button14=Button(GUIFrame,text=" Submit ",width=8,command=search_canteen_name,height=1,cursor='hand2',borderwidth=7).grid(row=6,column=5,sticky=W)

main.mainloop()
