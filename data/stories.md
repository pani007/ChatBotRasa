
## train_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Latur"}
    - slot{"location": "Latur"}
    - action_check_loc
    

## train_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Aurangabad"}
    - slot{"location": "Aurangabad"}
    - action_check_loc
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"priceLow": "300"}
    - slot{"priceLow": "300"}
    - action_search_restaurants
    - utter_check_mail_required
* ask_mail:{"mailopt": "yes"}
    - slot{"mailopt": "yes"}
    - send_mail
* ask_mail:{"email": "rao.msv@gmail.com"}
    - slot{"email": "rao.msv@gmail.com"}
    - send_mail
* goodbye
    - utter_goodbye

## train_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "Ratnagiri"}
    - slot{"location": "Ratnagiri"}
    - action_check_loc


## train_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "north Indian"}
    - slot{"cuisine": "north Indian"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_loc
    - utter_ask_price
* restaurant_search{"priceHigh": "700"}
    - slot{"priceHigh": "700"}
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "yes", "email": "rao.msv@gmail.com"}
    - slot{"mailopt": "yes"}
    - slot{"email": "rao.msv@gmail.com"}
    - send_mail

## train_story_5
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore", "cuisine": "pizza"}
    - slot{"cuisine": "pizza"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - utter_ask_price
* restaurant_search{"priceLow": "300", "priceHigh": "700"}
    - slot{"priceLow": "300"}
    - slot{"priceHigh": "700"}
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "yes", "email": "shrieducation1@gmail.com"}
    - slot{"mailopt": "yes"}
    - slot{"email": "shrieducation1@gmail.com"}
    - send_mail


## train_story_6
* greet
    - utter_greet
* restaurant_search{"location": "Chennai", "cuisine": "South Indian", "priceHigh": "700"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Chennai"}
    - slot{"priceHigh": "700"}
    - action_check_loc
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "no"}
    - slot{"mailopt": "no"}
    - send_mail
 * goodbye
    - utter_goodbye


## train_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_check_loc
    - utter_ask_price
* restaurant_search{"priceLow": "300", "priceHigh": "700"}
    - slot{"priceLow": "300"}
    - slot{"priceHigh": "700"}
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "no"}
    - slot{"mailopt": "no"}
    - send_mail
* goodbye
    - utter_goodbye


## train_story_8
* greet
    - utter_greet
* restaurant_search{"location": "Patna", "priceHigh": "600", "price_low": "600"}
    - slot{"location": "Patna"}
    - slot{"priceHigh": "600"}
    - action_check_loc
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "yes"}
    - slot{"mailopt": "yes"}
    - send_mail
* ask_mail:{"email": "rao.msv@gmail.com"}
    - slot{"email": "rao.msv@gmail.com"}
    - send_mail


    

## train_story_9
* restaurant_search{"cuisine": "south Indian", "location": "Bangalore", "priceLow": "500", "priceHigh": "2000"}
    - slot{"cuisine": "south Indian"}
    - slot{"location": "Bangalore"}
    - slot{"priceLow": "500"}
    - slot{"priceHigh": "2000"}
    - action_check_loc
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "yes"}
    - slot{"mailopt": "yes"}
    - send_mail
* ask_mail:{"email": "rao.msv@gmail.com"}
    - slot{"email": "rao.msv@gmail.com"}
    - send_mail

## train_story_10
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"priceLow": "300", "priceHigh": "700"}
    - slot{"priceLow": "300"}
    - slot{"priceHigh": "700"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_loc
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "yes"}
    - slot{"mailopt": "yes"}
    - send_mail
* goodbye
    - utter_goodbye




## train_story_11
* restaurant_search{"cuisine": "Pizza"}
    - slot{"cuisine": "Pizza"}
    - utter_ask_price
* restaurant_search{"priceLow": "300", "priceHigh": "700"}
    - slot{"priceLow": "300"}
    - slot{"priceHigh": "700"}
    - utter_ask_location
* restaurant_search{"location": "Aurangabad"}
    - slot{"location": "Aurangabad"}
    - action_check_loc
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "yes"}
    - slot{"mailopt": "yes"}
    - send_mail
* goodbye
    - utter_goodbye


## train_story_12
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"priceHigh": "700"}
    - slot{"priceHigh": "700"}
    - utter_ask_location
* restaurant_search{"location": "Aurangabad"}
    - slot{"location": "Aurangabad"}
    - action_check_loc
    - action_search_restaurants
    - utter_query_mail
* ask_mail:{"mailopt": "yes"}
    - slot{"mailopt": "yes"}
    - send_mail
* goodbye
    - utter_goodbye
