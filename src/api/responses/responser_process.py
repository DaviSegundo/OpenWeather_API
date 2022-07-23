
class ProcessResponser:
    
    def get_by_id(self, progress: float):
        """Handles possible response cases for GET requests by identifier

        Args:
            progress (float): data collection progress

        Returns:
            tuple(message_body, status_code): returns the body of the message and its status code
        """
        if progress is not None:
            message_response = {
                "message": f"the percentage of your data collection is in {progress:.2f}%",
                "percentage": progress
            }
            status_code = 200
        else:
            message_response = {"message": f"data collection processes for this user identifier have not yet started"}
            status_code = 404

        return message_response, status_code

    def post(self, check: bool, user_id: int):
        """Handles possible response cases for POST requests

        Args:
            check (bool): value to know if the user already exists in the database
            user_id (int): user identifier

        Returns:
            tuple(message_body, status_code): returns the body of the message and its status code
        """
        if check:
            message_response = {"message": f"new data collection started for id: {user_id}"}
            status_code = 202
        else:
            message_response = {"message": f"the user identifier {user_id} is already in use, please try another one."}
            status_code = 409
        
        return message_response, status_code
