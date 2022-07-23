from models.process import Process
from configs.config import CITIES_IDS

class ProcessController:
    """Class to control the actions performed on the processes by the API."""

    def create_new_process(self, user_id: int) -> bool:
        """Creates a new process in the database given a user identifier.

        Args:
            user_id (int): user identifier
        """
        process = Process.objects(user_id=user_id).first()
        if process is None:
            new_process = Process(user_id=user_id)
            new_process.save()
            return True
        return False

    def check_progress_process(self, user_id: int) -> float:
        """Checks the progress of data collection given a user identifier.

        Args:
            user_id (int): user identifier

        Returns:
            float: percentage of data collection
        """
        process = Process.objects(user_id=user_id).first()
        if process is not None:
            progess = (len(process.data) / len(CITIES_IDS))*100
            return progess
        return None
