#!/usr/bin/env python3
"""Filter_datum module
"""

import re
from typing import List
import logging

PII_FIELDS = ('name','email','phone','ssn','password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}=[^;{separator}]*",
                         f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializes the instance of the RedactingFormatter
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Method to filter values in incoming log records
        """
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)
    
    def get_logger() -> logging.Logger:
        """ Function that takes no arguments and returns a logging.Logger.
        """
        logger = logging.getLogger("user_data")
        logger.setLevel(logging.INFO)
        logger.propagate = False

        stream_handler = logging.StreamHandler()
        formatter = RedactingFormatter(PII_FIELDS)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        return logger

    

