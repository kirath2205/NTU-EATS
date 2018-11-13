** README FILE :- **
_____________________________________________________________________________________________________________________________________________________________________________________________

What is NTU EATS?

NTU consists of more than 20 canteens, with 5 stalls on an average in each canteen, hence for new commers-eg. exchange students,freshies,new staff members,etc. there really is'nt any
online portal or an application that provides canteen suggestions based on thier requirements. Hence, this is where NTU EATS comes in, our application provides all the requisite features
that an appication must possess in order to ensure that the user gets what he needs.


NTU EATS is a dedicated application, coded on python, that provides canteen suggestions based on user's specifications. The GUI has been constructed using tkinter to make the
application look attractive, at the same time ensuring workability and providing a user friendly interface for providing recommendations.

_____________________________________________________________________________________________________________________________________________________________________________________________

**	REQUIREMENTS	**

1.Since the NTU EATS application uses a variety of packages, hence the user must ensure that he/she has all the requiste packages available before running this on his/her system.
	** Given below are the packages used to develop NTU EATS :-**
		
		I)tkinter
		II)pygame
		III)datetime
		IV)sys
		V)os
		VI)messagebox

2.Before running this application also ensure that you have python version 3.6+ installed on your system

3.In order to view the introduction image, campus map and the about us, readme files, the user must have the introduction image in .png format,campus image in .jpeg format, and both the
  text files in .txt format, with all the files stored in the same directory as the NTU EATS application. 

____________________________________________________________________________________________________________________________________________________________________________________________

** Functions used to code NTU EATS application :- **

1.MouseClick()-This function is used to get the user's current location, on the NTU's campus map with the help of mouseclick.At the beginning of the program, the NTU campus map would be 
	       displayed for the user to click his/her location on NTU campus map. The location of the user in terms of x,y co-ordinates would then be stored in the system to provide
	       the user canteen suggestions.

2.check_halal()-This is an additional feature of our application.This function is used to display canteens in NTU that are halal certified. This is extremely useful for people who follow
                Islamism, as they prefer halal meat over other meats.

3.check_hygiene()-This is an additional feature of our application. This function is used to display canteens in NTU that have A grade hygiene rating. In order to ensure the hygiene of the
                  food served in all the canteens,NTU conducts yearly hygiene inspections and allots a hygiene grade to all the canteens.Since most of the people prefer a place that has
                  a good hygiene rating hence this function is quite useful for them.

4.show_map()-This is an additional feature of our application.This function is used to display the campus map.In case the user does not know the route from his/her current location to a 
	     nearby canteen, this function would come in handy as it would allow the user to view the map even after the user has entered his/her location with the help of mouseclick.

5.print_details()-This is a functon that is used to display the details of any canteen.The concept of Abstraction has been kept in mind while developing this fucntion as it will be used
	          to display the details of canteens in a plethora of other funcions used in this application.

6.isfloat()-This is a function that is used to handle the ValueError exception in case the user inputs a string instead of a integer or a float value for the budget.

6.cost_sorting(dic1,dic2,entered_text)-This function sorts the canteens whose average price per person falls below or equal to the user's preferred budget, on the basis of their average
				       cost per person.There will be a searchbar in the main GUI where the user can enter his/her preferred budget and accordingly the recommendations
				       would be displayed on the python terminal.The function makes use of the concept of decompostion to ensure robustness. The function handles all the 
				       base cases which involves the user entering wrong input that can be a string,float, negative value,0 etc.The function first checks of the entered 
				       value is correct,if not, a messagebox stating invalid input is displayed.If yes,the input is then compared to the averaga price per person of various
				       canteens and accordingly the output is displayed.In case there is no canteen that falls in the desired range, a messagebox stating no canteens 
	 			       available for this budget is displayed.The output is displayed using print_details() function , thereby making use of Abstraction.

7.cusine_search(dic1,dic2,entered_text)-This function is used to display canteens which have the user's desired food cusine.There will be a searchbar in the main GUI where the user can
					enter his/her desired cusine of food and accordingly the canteens would be displayed in the python terminal.The functions has been developed 
					keeping the concept of Decomposition in mind.The function handles all the base case where the user enters an invalid input that can be a float,
					integer,etc.The function breaks the problem into parts by first checking if the input is valid, if not a message would be displayed on the messagebox
					If not, the function then checks if the entered_text is a substring of all the available kinds of food,therby making use of pattern recognition, 
					this ensures that the user gets recommendation even if he enters a substring or a part of the desired food.For ex if the user enters ind ,Indian food canteens would be displayed.
					The output is displayed using print_details() funcion , thereby making use of Abstraction

8.rating_sort()-This function is used to sort and display canteens based on their average rating out of 5.0.The ouput is printed using print_details() therby making use of Abstraction

9.canteens_open_now()-This function is used to display only those canteens that are open currently.The function makes use of Decomposition by breaking a complex problem into parts.
		      In order to ensure the correctness of the recommendations,the user is not prompted to enter the date,time,day of the week instead the date,time ,day of the week is 
		      obtained using the datetime module available in python.Th function then extracts the current time from a big string containing various unncecessary texts the extracted
		      time is then convert to a float value and compared with the opening and closing time of all canteens,besides that, the function will also look out for canteens
		      that are closed on Sundays, incase the current day of the week is Sunday, hence those canteens would be ommitted from the output.The output would be displayed using
		      print_details()function.

10.nearby_canteens(dic1,dic2,x,y)-This function is used to sort and display all the canteens based on the proximity of various canteens from the user's location. The x,y co-ordinates of various canteens
		     would be stored in 2 lists and accordinly the distance of various canteens from the user's location would be displayed.The function uses Abstraction as the process
		     of calculating the distance using the distance formula is done by a hidden method called distance_a_b. The function also uses the concept of Decompostition.

11.open_file()-This function is used to open this readme file on notepad

12.about_file()-This function is used to open the about us file

13.search_canteen_name()-This function is used to display the details of a particular canteen.There will be a searchbar in the main GUI where the user can enter the name of a canteen in order
			 to obtain the details of a particular canteen.The function display an output even if the user enters a substring of a particular canteen therby ensuring the
			 robustness of the function.

14.sort_rank()-This function is used to sort canteen son the basis of their alloted rank.The ranks of all the canteens would be stored in a list and accrodingly the canteens would be sorted
	       and displayed.

15.distance_a_b(location_of_a,location_of_b)-This function is a hidden function which is used to find the distance between 2 locations with the help of distance formula.It is a part of
					     nearby_canteens() function.

____________________________________________________________________________________________________________________________________________________________________________________________

**  STEPS TO USE NTU EATS **

1.Run the main program on your system.

2.An introduction image would be displayed on the screen.

3.Then the NTU campus map would be displayed on the pygame terminal.

4.Enter your current location with the help of mouseclick, location would then be stored in the system.

5.The main GUI would be displayed containing all the main functions and features of the application.

6.In order to find canteens with halal certification, click the 'Show canteens with halal cerification' button, all the canteens with halal certification would be displayed in the python terminal.

7.In order to find canteens with A grade hygiene rating, click the 'Show canteens with A grade hygiene rating' button , all the canteens with A grade hygiene rating would be displayed in the python terminal.

8.In order to sort canteens according to their average rating, click the 'Show canteens according to their average rating' button , all the canteens will be sorted according to their average
  rating and would be displayed in the python terminal.

9.In order to find the canteens open right now, click the 'Canteens open right now' button, all canteens open currently would be displayed in the python terminal.

10.In order to find the nearby canteens, click the 'Show nearby canteens' button, all canteens will be sorted and displayed in order of their proximity from your current location.

11.In order to sort canteens according to their rank, click the 'Display canteens according to their rank' button, all canteens will be sorted according to their rank and would be displayed
   in python terminal.

12.In order to view the campus map, click the 'Show campus map' button,and the NTU campus map would be diplayed on the pygame terminal.

13.In order to view the readme file,click the 'readme' button, and the readme text file would pop up on notepad.

14.In order to view the about us file click the 'AboutUs' button and the about us text file would pop up on notepad.

15.In order to view canteens that fall under your desired budget, enter your budget in the 'Enter your desired budget' black searchbar, all the canteens whose average price per person falls under
   your desired budgt would be sorted and displayed in the python terminal.

16.In order to view canteens with your desired food , enter your food name in the 'Enter your desired cusine' black searchbar , all the canteens which have that particular cusine would be 
   displayed on the python terminal.

17.In order to view the details of a certain canteen , enter the name of the canteen in the 'Enter the name of the canteen you want ton search' , the details of the canteen that you entered,
   would be displayed n the python terminal.

18 If you want to quit the NTU EATS appplication, click 'quit recommendation system' button in the GUI  in order to exit the application.A blank scrren would appear, then exit by clicking
   the top cross button.

____________________________________________________________________________________________________________________________________________________________________________________________