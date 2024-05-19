# -*- coding: utf-8 -*-
"""

Created on Mon May  6 15:47:35 2024

@author: IAN CARTER KULANI
Phone:+265(0)988061969
E-mail:iancarterkulani@gmail.com
Purpose: The software prompts the user to enter total number of published centers,total 
number of registered  voters, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes 
and displays the results on the screen.
#NOTE: For a candidate to be a majority winner of an election, the candidate total valid votes should 
be greater than majority votes, which is Fifty plus one. 

"""

print("=========================================SOUTH AFRICA 2004 PRESIDENTIAL ELECTION=========================================\n\n")

percent=100
#Get total number of published centers
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes
Totalvalidvotes=int(input("Enter Total Valid Votes:"))


#Get Total Vald Votes for African National Congress
Totalvalidvotesfor_African_National_Congress=int(input("Enter Total Valid Votes for African National Congress:"))
#Get Total Vald Votes for Democratic Alliance
Totalvalidvotesfor_Democratic_Alliance=int(input("Enter Total Valid Votes for Democratic Alliance:"))
#Get Total Vald Votes for Inkatha Freedom Party  
Totalvalidvotesfor_Inkatha_Freedom_Party=int(input("Enter Total Valid Votes for Inkatha Freedom Party:"))
#Get Total Vald Votes for  United Democratic Movement
Totalvalidvotesfor_United_Democratic_Movement=int(input("Enter Total Valid Votes for United Democratic Movement:"))
#Get Total Vald Votes for Independent Democrats
Totalvalidvotesfor_Independent_Democrats=int(input("Enter Total Valid Votes for Independent Democrats:"))
#Get Total Valid Votes for New National Party
Totalvalidvotesfor_New_National_Party=int(input("Enter Total Valid Votes for New National Party:"))
#Get Total Vald Votes for African Christian Democratic Party
Totalvalidvotesfor_African_Christian_Democratic_Party=int(input("Enter Total Valid Votes for African Christian Democratic Party:"))
#Get Total Vald Votes for Freedom Front Plus
Totalvalidvotesfor_Freedom_Front_Plus=int(input("Enter Total Valid Votes for Freedom Front Plus:"))
#Get Total Vald Votes for United Christian Democratic Party
Totalvalidvotesfor_United_Christian_Democratic_Party=int(input("Enter Total Valid Votes for United Christian Democratic Party:"))
#Get Total Vald Votes for Pan Africanist Congress
Totalvalidvotesfor_Pan_Africanist_Congress=int(input("Enter Total Valid Votes for Pan Africanist Congress:"))
#Get Total Vald Votes for Minolity Front
Totalvalidvotesfor_Minolity_Front=int(input("Enter Total Valid Votes for Minolity Front:"))
#Get Total Vald Votes for Azanian People's Organisation
Totalvalidvotesfor_Azanian_Peoples_Organisation=int(input("Enter Total Valid Votes for Azanian Peolple's Organisation:"))
#Get Total Vald Votes for Christian Democratic Party
Totalvalidvotesfor_Christian_Democratic_Party=int(input("Enter Total Valid Votes for Christian Democratic Party:"))
#Get Total Vald Votes for National Action
Totalvalidvotesfor_National_Action=int(input("Enter Total Valid Votes for National Action:"))
#Get Total Vald Votes for Peace and Justice
Totalvalidvotesfor_Peace_and_Justice=int(input("Enter Total Valid Votes for Peace and Justice:"))
#Get Total Valid Votes for Socialist Party of Azania
Totalvalidvotesfor_Socialist_Party_of_Azania=int(input("Enter Total Valid Votes for Socialist Party of Azania:"))
#Get Total Valid Votes for  New Labour Party
Totalvalidvotesfor_New_Labour_Party=int(input("Enter Total Valid Votes for New Labour Party:"))
#Get Total Valid Votes for United Front
Totalvalidvotesfor_United_Front=int(input("Enter Total Valid Votes for United Front:"))
#Get Total Valid Votes for Employment Movement for South Africa
Totalvalidvotesfor_Employment_Movement_for_South_Africa=int(input("Enter Total Valid Votes for Employment Movement for South Africa:"))
#Get Total Valid Votes for The Organisation Party
Totalvalidvotesfor_The_Organisation_Party=int(input("Enter Total Valid Votes for The Organisation Party:"))
#Get Total Vald Votes for Keep it Straight and Simple Party
Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party=int(input("Enter Total Valid Votes for Keep it Straight and Simple Party:"))
#Decision Making
if Totalvalidvotesfor_African_National_Congress>Totalvalidvotes/2+1 :
        print("Congratulations to the African National Congress For Winning 2004 Election\n\n")
        
elif Totalvalidvotesfor_Democratic_Alliance>Totalvalidvotes/2+1: 
    print("Congratulations to the  Democratic Alliance  For Winning 2004 Election\n\n")
    
elif Totalvalidvotesfor_Inkatha_Freedom_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Inkatha Freedom Party For Winning 2004 Election\n\n")
    
    
elif Totalvalidvotesfor_United_Democratic_Movement>Totalvalidvotes/2+1: 
    print("Congratulations to the United Democratic Movement For Winning 2004 Election\n\n")
    
    
elif Totalvalidvotesfor_Independent_Democrats>Totalvalidvotes/2+1: 
    print("Congratulations to the Independent Democrats For Winning 2004 Election\n\n")
    
    
elif Totalvalidvotesfor_New_National_Party>Totalvalidvotes/2+1 :
        print("Congratulations to the New_National Party For Winning 2004 Election\n\n")
        
        
elif Totalvalidvotesfor_African_Christian_Democratic_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the African Christian Democratic Party For Winning 2004 Election\n\n")
    
    
elif Totalvalidvotesfor_Freedom_Front_Plus>Totalvalidvotes/2+1: 
    print("Congratulations to the Freedom Front Plus For Winning 2004 Election\n\n")
    
   
    
elif Totalvalidvotesfor_United_Christian_Democratic_Party>Totalvalidvotes/2+1:
      print("Congratulations to the United Christian Democratic Party For Winning 2004 Election\n\n")
  
      
elif Totalvalidvotesfor_Pan_Africanist_Congress>Totalvalidvotes/2+1:
      print("Congratulations to Pan Africanist Congress For Winning 2004 Election\n\n")

            
elif Totalvalidvotesfor_Minolity_Front>Totalvalidvotes/2+1:
        print("Congratulations to Minolity Front For Winning 2004 Election\n\n")    
      
                 
elif Totalvalidvotesfor_Azanian_Peoples_Organisation>Totalvalidvotes/2+1:
        print("Congratulations to Azanian People's Organisation For Winning 2004 Election\n\n")
       
     
elif Totalvalidvotesfor_Azanian_Peoples_Organisation>Totalvalidvotes/2+1:
        print("Congratulations to Azanian People's Organisation For Winning 2004 Election\n\n")      

      
elif Totalvalidvotesfor_Christian_Democratic_Party>Totalvalidvotes/2+1 :
        print("Congratulations to Christian Democratic Party For Winning 2004 Election\n\n")
        
     
elif Totalvalidvotesfor_National_Action>Totalvalidvotes/2+1 :
        print("Congratulations to National Action For Winning 2004 Election\n\n")        
        
        
elif Totalvalidvotesfor_Peace_and_Justice>Totalvalidvotes/2+1: 
    print("Congratulations to the Peace and Justice For Winning 2004 Election\n\n")
    
    
elif Totalvalidvotesfor_Socialist_Party_of_Azania>Totalvalidvotes/2+1: 
    print("Congratulations to the Socialist Party of Azania For Winning 2004 Election\n\n")
    
elif Totalvalidvotesfor_New_Labour_Party>Totalvalidvotes/2+1 :
     print("Congratulations to the New Labour Party For Winning 2004 Election\n\n")
      
elif Totalvalidvotesfor_United_Front>Totalvalidvotes/2+1: 
  print("Congratulations to the United Front Convention For Winning 2004 Election\n\n")
   
elif Totalvalidvotesfor_Employment_Movement_for_South_Africa>Totalvalidvotes/2+1: 
    print("Congratulations to the Employment Movement for South Africa For Winning 2004 Election\n\n")
  
elif Totalvalidvotesfor_The_Organisation_Party>Totalvalidvotes/2+1 :
        print("Congratulations to the Organisation Party For Winning 2004 Election\n\n")
        
        
elif Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Keep it Straight and Simple Party For Winning 2004 Election\n\n")
    
    
else:
    print("No majority winner was found RUNOFF may be required\n")

print("__________________________________________________________ELECTION STATISTICS__________________________________________________________\n")
#calculating percentage 
#Calculating percentage for total votes cast
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#Calculating percentage for Total Registered voters/turnout
Percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for African National Congress
Percentage=round(Totalvalidvotesfor_African_National_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African National Congress in Percentage=",Percentage)
#Calculating percentage for Democratic Alliance
Percentage=round(Totalvalidvotesfor_Democratic_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Democratic Alliance in percentage=",Percentage)
#Calculating percentage for Inkatha Freedom Party  
Percentage=round(Totalvalidvotesfor_Inkatha_Freedom_Party *percent/Totalvalidvotes, 2);
print("Total Valid Votes for Inkatha Freedom Party in percentage=",Percentage) 
#Calculating percentage for United Democratic Movement
Percentage=round(Totalvalidvotesfor_United_Democratic_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Democratic Movement in Percentage=",Percentage)
#Calculating percentage for Independent Democrats
Percentage=round(Totalvalidvotesfor_Independent_Democrats*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Independent Democrats Party in percentage=",Percentage)
#Calculating percentage for New National Party
Percentage=round(Totalvalidvotesfor_New_National_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for New National Party in percentage=",Percentage) 
#Calculating percentage for African Christian Democratic Party
Percentage=round(Totalvalidvotesfor_African_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Christian Democratic Partyin Percentage=",Percentage)
#Calculating percentage for Freedom Front Plus
Percentage=round(Totalvalidvotesfor_Freedom_Front_Plus*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Freedom Front Plus in percentage=",Percentage)
#Calculating percentage for United Christian Democratic Party
Percentage=round(Totalvalidvotesfor_United_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Christian Democratic Party in percentage=",Percentage) 
#Calculating percentage for Pan Africanist Congress
Percentage=round(Totalvalidvotesfor_Pan_Africanist_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan Africanist Congress in percentage=",Percentage) 
#Calculating percentage for Minolity Front     
Percentage=round(Totalvalidvotesfor_Minolity_Front*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Minolity Front in percentage=",Percentage) 
#Calculating percentage for Azanian People's Organisation     
Percentage=round(Totalvalidvotesfor_Azanian_Peoples_Organisation*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Azanian People's Organisation t in percentage=",Percentage) 
#Calculating percentage for Christian Democratic Party    
Percentage=round(Totalvalidvotesfor_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Christian Democratic Party in percentage=",Percentage) 
#Calculating percentage for National Action
Percentage=round(Totalvalidvotesfor_National_Action*percent/Totalvalidvotes, 2);
print("Total Valid Votes for National Action in Percentage=",Percentage)
#Calculating percentage for Peace and Justice
Percentage=round(Totalvalidvotesfor_Peace_and_Justice*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Peace and Justice in percentage=",Percentage)
#Calculating percentage for Socialist Party of Azania
Percentage=round(Totalvalidvotesfor_Socialist_Party_of_Azania*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Socialist Party of Azania in percentage=",Percentage)
#Calculating percentage for New Labour Party
Percentage=round(Totalvalidvotesfor_New_Labour_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for New Labour Party in percentage=",Percentage) 
#Calculating percentage for United Front
Percentage=round(Totalvalidvotesfor_United_Front*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Front in Percentage=",Percentage)
#Calculating percentage for Employment Movement for South Africa
Percentage=round(Totalvalidvotesfor_Employment_Movement_for_South_Africa*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Employment Movement for South Africa in percentage=",Percentage)
#Calculating percentage for The Organisation Party
Percentage=round(Totalvalidvotesfor_The_Organisation_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for The Organisation Party in percentage=",Percentage)
#Calculating percentage for Keep it Straight and Simple Party
Percentage=round(Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Keep it Straight and Simple Party in percentage=",Percentage)


print("=========================================================================================================================\n\n")   






































































