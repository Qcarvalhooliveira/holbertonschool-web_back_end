#!/usr/bin/env python3
"""
Filter_datum module
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Function that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}=[^;{separator}]*", f"{field}={redaction}", message)
    return message
