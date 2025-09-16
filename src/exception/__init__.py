import sys
import logging

def error_message_details(error: Exception, error_details:sys) -> str:
    """
    Extracts detailed error information including file name, line number and the exact error message

    :params error - the exception that occurred 
    :params error_details : the sys module to access traceback details.
    :return : A formatted error string message 
    """
    # extract traceback details
    _, _, exc_tb = error_details.exc_info()

    # get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # line no
    line_no = exc_tb.tb_lineno
    error_message = f"error occurred in python script: [{file_name}] at line number [{line_no}] : {str(error)}"

    # log the error in logs
    logging.error(error_message)

    return error_message

class MyException(Exception):
    def __init__(self, error_message:str, error_details:sys):
        super().__init__(error_message)

        self.error_message = error_message_details(error_message,error_details)
    
    def __str__(self):
        return self.error_message
    
    
