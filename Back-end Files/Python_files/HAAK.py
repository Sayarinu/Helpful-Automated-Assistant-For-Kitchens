import emailInterfacing
import languageProcessingInterfacing as nlp
import setup
import yelpInterfacing as y
import locationInterfacing as loc
import emailInterfacing as email


class HAAKChatbot:
    def __init__(self, user_email=None, user_name=None, user_location=None):
        self.state = "INITIAL"
        self.cuisine_preferences = None
        self.selected_restaurant = None
        self.current_restaurants = None
        self.historical_restaurants = None
        self.user_email = user_email
        self.location = user_location
        self.user_name = user_name
        #this is to check if the current recommendation is the same as the history preference.
        self.current_cuisine = None
        self.match = None


    def reset_state(self):
        # Reset only the attributes that are relevant to starting a new conversation flow
        self.state = "INITIAL"
        self.cuisine_preferences = None
        self.selected_restaurant = None
        self.current_restaurants = None
        self.history_restaurants = None
        #this is to check if the current recommendation is the same as the history preference.
        self.current_cuisine = None
        self.match = None

    def handle_interaction(self, message: str):
        if self.state == "INITIAL":
            return self.generate_initial_greeting()
        elif self.state == "AWAITING_LOCATION_CONFIRMATION":
            return self.process_location_confirmation(message)
        elif self.state == "AWAITING_LOCATION":
            return self.process_location(message)
        elif self.state == "AWAITING_LOCATION_SAVING_CONFIRMATION":
            return self.save_location_to_db(message)
        elif self.state == "AWAITING_CUISINE":
            return self.process_cuisine(message)
        elif self.state == "ASK_RESERVATION":
            return self.process_reservation_request(message)
        elif self.state == "GET_RESTAURANT_SELECTION":
            return self.process_restaurant_number(message)
        elif self.state == "GET_RESERVATION_TIME":
            return self.process_reservation_time(message)
        else:
            return "I'm not sure what you are asking. Could you please specify?"

    def generate_initial_greeting(self):
        if self.user_name:
            greeting = f"Hello {self.user_name}! It's HAAKY here, your restaurant chatbot assistant."
            if self.location:
                greeting += f" Is {self.location} the right location for you? (yes/no)"
                self.state = "AWAITING_LOCATION_CONFIRMATION"
            else:
                greeting += " I will need some information to help best assist you. Could you give a description of the location you would like me to find recommendations?"
                self.state = "AWAITING_LOCATION"
            return greeting
        self.state = 'AWAITING_LOCATION'
        return "Hi, I am HAAKY, your restaurant chatbot assistant, and I am here to help recommend restaurants. Firstly, I will need some information to help best assist you. Please give a description of the location you would like me to find recommendations."


    def process_location(self, location_desc: str):
        location = loc.check_location(location_desc)
        if location is None:
            return "Sorry, I couldn't find that location. Please try a different description."

        self.location = location_desc
        if self.user_email:
            self.state = "AWAITING_LOCATION_SAVING_CONFIRMATION"
            return "Location accepted. Do you want me to save this as your default location? (yes/no)"
        self.state = "AWAITING_CUISINE"
        return "Location accepted. What cuisine are you interested in?"


    def save_location_to_db(self, message: str):
        if message.lower() == "yes":
            conn = setup.connect_to_database()
            cursor = conn.cursor()
            query = "UPDATE Users SET location = %s WHERE email = %s;"
            cursor.execute(query, (self.location, self.user_email))
            conn.commit()
            self.state = "AWAITING_CUISINE"
            return "Location information stored. What cuisine are you interested in?"
        elif message.lower() == "no":
            self.state = "AWAITING_CUISINE"
            return "Sure. What cuisine are you interested in?"
        return "Please enter a yes or no."

    def process_cuisine(self, cuisine_desc: str):
        if type(self.location) != tuple:
            location = loc.check_location(self.location)
        else:
            location = self.location
        self.current_cuisine = cuisine_desc
        user_request = nlp.handle_text(cuisine_desc)

        if self.user_email:
            self.store_user_preference(user_request["categories"][0])
        recommendations = self.fetch_recommendations(user_request["categories"], location)
        if not recommendations:
            return "Sorry, I couldn't find any restaurants matching that description."

        self.state = "ASK_RESERVATION"
        return recommendations


    def store_user_preference(self, category):
        conn = setup.connect_to_database()
        cursor = conn.cursor()
        # Assume user_id can be fetched based on email
        user_id = self.fetch_user_id(self.user_email)
        query = "INSERT INTO usercategory (user_id, category_id) VALUES (%s, %s);"
        cursor.execute(query, (user_id, category))
        conn.commit()
        conn.close()

    def fetch_user_id(self, email):
        conn = setup.connect_to_database()
        cursor = conn.cursor()
        query = "SELECT user_id FROM Users WHERE email = %s;"
        cursor.execute(query, (email,))
        user_id = cursor.fetchone()[0]
        conn.close()
        return user_id

    def fetch_recommendations(self, current_categories, location):
        if self.user_email:
            historical_recommendations = self.fetch_historical_recommendations(location)
            self.historical_restaurants = y.parse_information(historical_recommendations)
        ndisplay = 5
        if self.match == 1:
            ndisplay = 10
        current_recommendations = y.searchYelp(latitude=location[0], longitude=location[1], categories=current_categories, limit = ndisplay)
        self.current_restaurants = y.parse_information(current_recommendations)
        return self.format_combined_recommendations(self.current_restaurants, self.historical_restaurants)

    def format_combined_recommendations(self, current_recommendations, historical_recommendations):
        formatted_current = self.format_restaurants(current_recommendations,1)
        if self.user_email and (self.match != 1):
            formatted_historical = self.format_restaurants(historical_recommendations,6)
            return f"Based on the cuisines you ask for:\n{formatted_current}\n\nFrom your history:\n{formatted_historical}\n\nWould you like to make a reservation? (yes/no)"
        else:
            return f"Based on the cuisines you ask for:\n{formatted_current}\n\nWould you like to make a reservation? (yes/no)"

    def fetch_historical_recommendations(self, location):
        historical_categories = self.get_user_historical_preferences()
        if historical_categories == self.current_cuisine.lower():

            self.match = 1
        if not historical_categories:
            return []
        historical_recommendations = y.searchYelp(latitude=location[0], longitude=location[1],
                                                  categories=historical_categories, limit=5)
        return historical_recommendations

    def get_user_historical_preferences(self):
        conn = setup.connect_to_database()
        cursor = conn.cursor()
        user_id = self.fetch_user_id(self.user_email)

        query = """
            SELECT category_id, COUNT(category_id) AS count
            FROM usercategory
            WHERE user_id = %s
            GROUP BY category_id
            ORDER BY count DESC
            LIMIT 1;
        """

        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        conn.close()

        most_frequent_category = result[0]
        return most_frequent_category

    def process_location_confirmation(self, message: str):
        if message.lower() == "yes":
            self.state = "AWAITING_CUISINE"
            return "That's great! What cuisine are you interested in?"
        elif message.lower() == "no":
            self.state = "AWAITING_LOCATION"
            return "Please enter the new location."
        else:
            return "Please answer with a yes or no."

    def process_reservation_request(self, message: str):
        if message.lower() == "yes":
            if self.user_email:
                self.state = "GET_RESTAURANT_SELECTION"
                return "Please enter the number of the restaurant you want to reserve."
            else:
                return "You need to be logged in to make a reservation."
        else:
            return "Okay. You can always restart the chat if you want to make a reservation."

    def process_restaurant_number(self, message: str):
        '''
        try:
            selection_index = int(message) - 1
            if 0 <= selection_index < 5:
                self.selected_restaurant = self.current_restaurants.restaurant_list[selection_index]
                self.state = "GET_RESERVATION_TIME"
                return "Please enter the date and time for your reservation (format: YYYY-MM-DD HH:MM)."
            elif 5 <= selection_index < 10:
                self.selected_restaurant = self.historical_restaurants.restaurant_list[selection_index-5]
                self.state = "GET_RESERVATION_TIME"
                return "Please enter the date and time for your reservation (format: YYYY-MM-DD HH:MM)."
            else:
                return "Invalid selection. Please select a number from the list."
        except ValueError:
            return "Please enter a number to select a restaurant."
        '''
        try:
            selection_index = int(message) - 1
            if 0 <= selection_index < 5:
                self.selected_restaurant = self.current_restaurants.restaurant_list[selection_index]
                website_url = y.getWebsiteUrl(self.selected_restaurant.restaurant_url)
                if website_url:
                    self.state = "GET_RESERVATION_TIME"
                    return f"To get the most up to date information regarding {self.selected_restaurant.restaurant_name}'s reservation information, please visit {website_url}.\n\nPlease enter the date and time for your reservation (format: YYYY-MM-DD HH:MM)."
                else:
                    self.state = "GET_RESERVATION_TIME"
                    return f"We were unable to find the restaurant's personal page, in order to find the most up to date information please see {self.selected_restaurant.restaurant_url}.\n\nPlease enter the date and time for your reservation (format: YYYY-MM-DD HH:MM)."
            elif 5 <= selection_index < 10: 
                self.selected_restaurant = self.historical_restaurants.restaurant_list[selection_index-5]
                website_url = y.getWebsiteUrl(self.selected_restaurant.restaurant_url)
                if website_url:
                    self.state = "GET_RESERVATION_TIME"
                    return f"To get the most up to date information regarding {self.selected_restaurant.restaurant_name}'s reservation information, please visit {website_url}.\n\nPlease enter the date and time for your reservation (format: YYYY-MM-DD HH:MM)."
                else:
                    self.state = "GET_RESERVATION_TIME"
                    return f"We were unable to find the restaurant's personal page, in order to find the most up to date information please see {self.selected_restaurant.restaurant_url}.\n\nPlease enter the date and time for your reservation (format: YYYY-MM-DD HH:MM)."
            else:
                return "Invalid selection. Please select a number from the list."
        except ValueError:
            return "Please enter a number to select a restaurant."


    def process_reservation_time(self, time: str):
        if not self.user_email:
            return "You need to be logged in to make a reservation."

        # Convert time to suitable format and create calendar event
        utc_timestamp = email.convert_time(time)
        event_summary = f"Reservation at {self.selected_restaurant.restaurant_name}"
        #add_event_to_calendar(event_summary, self.selected_restaurant.address, utc_timestamp)
        email.generate_reservation(
            nameOfRestaurant=self.selected_restaurant.restaurant_name,
            invitedName="You",
            invitedEmail=self.user_email,
            location=self.selected_restaurant.address,
            utctimestamp=utc_timestamp
        )
        # Send confirmation email
        email.send_calendar_email(
            subject="Your Reservation Confirmation",
            message=f"Your reservation at {self.selected_restaurant.restaurant_name} is confirmed for {time}.",
            receiver_email=self.user_email,
            attachment_name="event.ics"
        )

        return f"Reservation confirmed for {time} and details sent to your email."

    def format_restaurants(self, restaurants,a):
        formatted_list = []
        for i, restaurant in enumerate(restaurants.restaurant_list):
            formatted_entry = (
                f"{i + a}.\n"
                f"Name: {restaurant.restaurant_name}\n"
                f"Address: {restaurant.address}\n"
                f"Zipcode: {restaurant.zip_code}\n"
                f"Rating: {restaurant.rating}\n"
                f"Phone: {restaurant.phone}\n"
                f"URL: {restaurant.restaurant_url}\n"
                f"Image URL: {restaurant.image_url}\n\n"
            )
            formatted_list.append(formatted_entry)
        return "\n".join(formatted_list)
