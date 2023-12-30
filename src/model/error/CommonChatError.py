from src.model.error.Error import Error
from src.model.error.ErrorSource import ErrorSource


class CommonChatException(Exception):
    def __init__(self, message: str = None):
        message = message if message is not None else ""
        self.message = Error(0, message, ErrorSource.COMMON).build()
        super().__init__(self.message)
