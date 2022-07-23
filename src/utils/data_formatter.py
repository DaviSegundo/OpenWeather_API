class DataFormatter:
    """Class that deals with the organization and formatting of information."""

    def retrive_essencial_city_information(self, json_body: dict) -> dict:
        """Get the essential information about the city that is contained in a JSON data.

        Args:
            json_body (dict): JSON containing all the information about the city

        Returns:
            dict: dictionary with the essential data taken from the complete JSON
        """
        city_id = json_body.get('id')
        main_info = json_body.get('main')
        temperature = main_info.get('temp')
        humidity = main_info.get('humidity')

        data = {
            'city_id': city_id,
            'temperature': temperature,
            'humidity': humidity
        }

        return data
