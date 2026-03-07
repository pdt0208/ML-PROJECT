# src/mlproject/exceptions.py
import sys
import os
import traceback

def error_message_detail(error_message, error_details=None):
    """
    Builds a detailed error message with traceback info if available.
    """
    try:
        if error_details:
            exc_type, exc_obj, exc_tb = error_details.exc_info()
            if exc_tb:
                file_name = exc_tb.tb_frame.f_code.co_filename
                line_number = exc_tb.tb_lineno
                return f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{error_message}]"
        # fallback if no exc_tb
        return f"Error: {error_message}"
    except Exception as e:
        return f"Error while creating error message: {str(e)}"

class CustomException(Exception):
    def __init__(self, error_message, error_details=None):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message