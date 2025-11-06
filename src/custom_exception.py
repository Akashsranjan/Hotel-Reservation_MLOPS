# traceback → helps you get the exact line number and code trace where an error happened.

# sys → gives system-level information (like exception details, file name, etc.).

import sys

class CustomException(Exception):
    def __init__(self, error_message, error_detail: Exception):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail: Exception):
        # Get the current exception traceback
        exc_type, exc_value, exc_tb = sys.exc_info()
        if exc_tb:  # If traceback exists
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f"Error in {file_name}, line {line_number}: {error_message} | Exception: {error_detail}"
        else:
            return f"{error_message} | Exception: {error_detail}"

    def __str__(self):
        return self.error_message
