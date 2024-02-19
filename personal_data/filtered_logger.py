#!/usr/bin/env python3
"""
Filter_datum module
"""

import re

def filter_datum(fields, redaction, message, separator):
    """
    Function that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}=[^;{separator}]*", f"{field}={redaction}", message)
    return message
