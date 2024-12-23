import sys  # Import sys module to interact with the Python runtime environment.
from src.logger import logging  # Import a custom logging module for structured logging.

# Function to extract and format detailed error messages
def error_message_detail(error, error_detail: sys):
    '''
    Captures detailed information about an error, including file name and line number.

    Parameters:
    error (Exception): The original exception object.
    error_detail (sys): The system module, used to fetch exception information.

    Returns:
    str: A formatted string containing error details (file name, line number, and error message).
    '''
    # Extract the traceback object using sys.exc_info()
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the name of the script where the error occurred.
    
    # Create a detailed error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class that enhances the standard Exception class
class CustomException(Exception):
    '''
    Custom exception class to log and handle detailed error messages.

    Parameters:
    error_message (str): The error message to be displayed.
    error_detail (sys): The system module, used to fetch detailed error information.
    '''
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the base Exception class initializer.
        # Store the detailed error message using the helper function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        '''
        String representation of the exception.

        Returns:
        str: The detailed error message.
        '''
        return self.error_message


# if __name__ =="__main__":
#     try:
#         a= 1/10
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e,sys)
    