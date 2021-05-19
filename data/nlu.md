## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hi

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi](location)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant with [Mughlai](cuisine)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- [Continental](cuisine)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- Show me the restaurants in [Hyderabad](location) with [Mexican](cuisine) food.
- Find me the restaurants that offer [pizza][cuisine]
- Show me restaurants with price range of [300](priceLow) to [700](priceHigh)
- Show me the restaurants with the price below [400](priceLow)
- Show me the restaurants with the price above [700](priceHigh)
- Give me the details of restaurants in [Bangalore](location) with the price in the range [300](priceLow) Rs to [700](priceHigh) Rs
- More than [700](priceHigh)
- Rs. [300](priceLow) to [700](priceHigh)
- less than [300](priceLow)
- Give me the details of restaurants in [Mumbai](location) with the price in the range [300](priceLow) Rs to [700](priceHigh) Rs in [North Indian](cuisine)
- show me hotels with price < [300](priceLow)
- show me hotels with price > [300](priceHigh)
- Greater than [600](priceHigh)
- Show me restaurants in [Latur](location)
- I am searching for restaurants
- [Aurangabad](location)
- Lesser than Rs. [300](priceLow)
- Show me all restaurants with [Italian](cuisine) Cusine
- Ratnagiri[]{"entity": "location", "value": "Ratnagiri"}
- Show me the restaurants with [north Indian](cuisine) food
- In [Mumbai](location)
- Show me all the pizza restaurants in [Bangalore](location)[Bangalore](location)[]{"entity": "cuisine", "value": "pizza"}
- Show me the restaurants in [Chennai](location) with [South Indian](cuisine) Dishes with the price above [700](priceHigh) Rs
- Show me [Chinese]{"entity": "cuisine", "value": "chinese"} restaurants in [Delhi](location)
- Show me restaurants in [Patna](location)[Patna](location) with price below [600](priceHigh)[]{"entity": "price_low", "value": "600"}
- Show me all [chinese](cuisine) restaurants
- [Ahmedabad](location)
- Give me [south Indian](cuisine) Restaurants in [Bangalore](location) with the price in the range [500](priceLow) to [2000](priceHigh)
- Show me the [chinese](cuisine) restaurants
- [chennai](location)
- Show me all the [North Indian](cuisine) Restaurants
- [Pune](location)

## intent:ask_mail:
- [yes](mailopt)
- [no](mailopt)
- [yes](mailopt) please send me mail to [abc@xyz.com](email)
- [no](mailopt) I do not need an email
- [demo@gmail.com](email)
- send it to [rao.msv@gmail.com](email)
- [yes](mailopt) pls send it to [rao.msv@gmail.com](email)
- [yes](mailopt) send it to [shrieducation1@gmail.com](email)
- [rao.msv@gmail.com](email)
- [panindra.mysorekar@gmail.com](email)
- [yes](mailopt)[yes](mailopt)


## synonym:4
- four

## synonym:Gurgaon
- Gurugram

## synonym:New Delhi
- Delhi
- delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:no
- n
- nope

## synonym:vegetarian
- veggie
- vegg

## synonym:yes
- ya
- Yup
- yeah
- y

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:priceHigh
- [0-9]{3}

## regex:priceLow
- [0-9]{3}
