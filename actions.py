# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


'''Importing modules'''
import re
from email.message import EmailMessage
from rasa_sdk import Action, Tracker
import numpy as np
from rasa_sdk.events import SlotSet
import pandas as pd
df = pd.read_csv("./zomato.csv",encoding='latin1')


###################################################################################################################################
### Code for getting restaurant details
### We will re use the function to make code neat

####################################################################################################################################


################################################################################################################################
## This token is for login. I have saved username and password in a csv file
##############################################################################################################################
creds = pd.read_csv("./access.csv")
def authenticate(creds = creds):
    user_name = creds.iloc[0,0]
    password = creds.iloc[0,1]
    print(user_name,password)
    return user_name,password






def generate_details(loc,cusine,rows,df=df,price_low=None,price_high=None,isEmail=False):
    message = ""
    if price_low == None and price_high == None:
        return "No Restaurants Found"
    else:
        df['City'] = df["City"].apply(lambda x: x.lower())
        loc = loc.lower()
        if price_low == None:
            records = df[(df["Cuisines"].apply(lambda x: True if cusine.lower() in x.lower() else False)) & (df['City'] == loc) & (df["Average Cost for two"] > price_high)]
        
        elif price_high == None:
            records = df[(df["Cuisines"].apply(lambda x: True if cusine.lower() in x.lower() else False)) & (df['City'] == loc) & (df["Average Cost for two"] < price_low)]
        
        else:
            records = df[(df["Cuisines"].apply(lambda x: True if cusine.lower() in x.lower() else False)) & (df['City'] == loc) &(df["Average Cost for two"] >= price_low) & (df["Average Cost for two"] <= price_high)]


        if(isEmail):
            message = "Dear Sir/Madam, \n\n\n The restaurants found are listed below \n\n"


        records = records.sort_values(by="Aggregate rating",ascending=False)
        records = records.iloc[: rows,:]
        rest_names = records["Restaurant Name"]
        rest_locality_addr = records["Address"]
        avg_budget = records["Average Cost for two"]
        
        user_rating = records["Aggregate rating"]
        for rows in range(records.shape[0]):
            #print(rows)
            message += f"Name: {rest_names.iloc[rows]}\nAddress:  {rest_locality_addr.iloc[rows]}\nPrice for two: {avg_budget.iloc[rows]}\nRating: {str(user_rating.iloc[rows])}\n\n\n"
        
        if(isEmail):
            message += "Thanks and Regards,\n Zomato Bot"

        return message



#####################################################################################################################################






class RestaurantSearch(Action):

    def name(self):
        return "action_search_restaurants"

    def run(self,dispatcher,tracker,domain,df = df):
        loc = tracker.get_slot("location")
        cusine = tracker.get_slot("cuisine")
        pl = tracker.get_slot("priceLow")
        if pl != None:
            try:
                pl = int(pl)
            except ValueError:
                dispatcher.utter_message("The input is invalid")
                
        ph = tracker.get_slot("priceHigh")

        if ph != None:
            try:
                ph = int(ph)
            except ValueError:
                dispatcher.utter_message("The input is invalid")
        print(pl,ph)
        query = generate_details(loc,cusine,5,df=df,price_low=pl,price_high=ph)
        dispatcher.utter_message(query)







class ValidateLocation(Action):
    def name(self):
        return 'action_check_loc'

    def run(self,dispatcher,tracker,domain):
        tier_1 =  ['Ahmedabad', 'Bangalore', 'Chennai', 'New Delhi', 'Hyderabad', 'Kolkata', 'Mumbai' ,'Pune']
        tier_1 = list(map(lambda x: x.lower(),tier_1))
        tier_2 = "Agra, Ajmer, Aligarh, Amravati, Amritsar, Asansol, Aurangabad, Bareilly, Belgaum, Bhavnagar, Bhiwandi, Bhopal, Bhubaneswar, Bikaner, Bilaspur, Bokaro Steel City, Chandigarh, Coimbatore, Cuttack, Dehradun, Dhanbad, Bhilai, Durgapur, Dindigul, Erode, Faridabad, Firozabad, Ghaziabad, Gorakhpur, Gulbarga, Guntur, Gwalior, Gurgaon, Guwahati, Hamirpur, Hubli–Dharwad, Indore, Jabalpur, Jaipur, Jalandhar, Jammu, Jamnagar, Jamshedpur, Jhansi, Jodhpur, Kakinada, Kannur, Kanpur, Karnal, Kochi, Kolhapur, Kollam, Kozhikode, Kurnool, Ludhiana, Lucknow, Madurai, Malappuram, Mathura, Mangalore, Meerut, Moradabad, Mysore, Nagpur, Nanded, Nashik, Nellore, Noida, Patna, Pondicherry, Purulia, Prayagraj, Raipur, Rajkot, Rajahmundry, Ranchi, Rourkela, Ratlam, Salem, Sangli, Shimla, Siliguri, Solapur, Srinagar, Surat, Thanjavur, Thiruvananthapuram, Thrissur, Tiruchirappalli, Tirunelveli, Tiruvannamalai, Ujjain, Bijapur, Vadodara, Varanasi, Vasai-Virar City, Vijayawada, Visakhapatnam, Vellore , Warangal"
        tier_2 = tier_2.lower().split(',')
        tier_2 = list(map(lambda x: x.strip(),tier_2))
        city = tracker.get_slot("location")

        if city.lower() not in tier_1 and city.lower() not in tier_2:
            print(city)
            dispatcher.utter_message("I am sorry, We do not operate There")
        else:
            dispatcher.utter_message("Great We operate here !!!. Happy to help you. :)")






import smtplib
class SmtpMail(Action):
    
    
    def name(self):

        return "send_mail"

    def run(self,dispatcher,tracker,domain,df = df):
        try:
            
            to = tracker.get_slot("email")
            loc = tracker.get_slot("location")
            cusine = tracker.get_slot("cuisine")
            
            
            #price_low = tracker.get_slot("priceLow")


            pl = tracker.get_slot("priceLow")
            
            
            
            if pl != None:
                try:
                    pl = int(pl)
                except ValueError:
                    dispatcher.utter_message("The input is invalid")



                
            ph = tracker.get_slot("priceHigh")

            if ph != None:
                try:
                    ph = int(ph)
                except ValueError:
                    dispatcher.utter_message("The input is invalid")

            
            message = generate_details(loc,cusine,10,df=df,price_low=pl,price_high=ph,isEmail=True)
           
            mail_opt = tracker.get_slot("mailopt")
            if mail_opt.lower() == 'yes':


                if to != None:    
                    if re.search("[A-Za-z0-9_\.]+@[A-Za-z_\.]",to):
                        print("regex_validated")
                        msg = EmailMessage()
                        msg['From'] = 'sce@jhbvr.com' 
                        
                        msg["Subject"] = f"Restaurants in {loc} with {cusine}"
                        msg["To"] = to

                        ### Retrive creds
                        user_name,password = authenticate(creds=creds)

                        msg.set_content(message)
                        smtpObj = smtplib.SMTP("smtp.gmail.com",587)
                        smtpObj.ehlo()
                        smtpObj.starttls()
                        smtpObj.login(user_name,password)
                    
                        
                        smtpObj.send_message(msg)
                        dispatcher.utter_message("Mail sent Thanks and have a good day !!!! :)")
                    else:
                        dispatcher.utter_message("Email Address invalid")
                
                else:
                    dispatcher.utter_message("Please provide the email address !!")


            else:
                 dispatcher.utter_message("Okay")
                    
        except: 
            dispatcher.utter_message("Mail Not sent please verify the email address")


            


