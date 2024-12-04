# A python module created for making debugging easier 
# V1.0
from enum import Enum
from datetime import datetime

class LogLevel(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

LOGFILE = "log.txt"
PROFILERFILE = "profiler.txt"

class Debugy:
    def __init__(self, timestamp_enabled: bool) -> None:
        self.initialized = True
        self.start_text = ":DEBUG:"
        self.timestamp_enabled = timestamp_enabled
        self.last_log_level

    def print(self, text_to_print: str):
        if self.initialized:
            print(f"{self.start_text} {text_to_print}")
            
    def logmessage(self, log_level: LogLevel, what_to_log: str):
        """Logs something to a file as, INFO, WARNING, ERROR"""
        with open(LOGFILE, 'a') as file:
            # If its a different log_level then add a space
            if last_log_level is not log_level:
                file.write("")

            if self.timestamp_enabled:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # get the current time
                file.write(f"{time} - :{log_level.value}: {what_to_log}\n")  
                return
            file.write(f":{log_level.value}: {what_to_log}\n")

            self.last_log_level = log_level
            
    def clearlogfile(self):
        """This clears the current log file."""
        with open('log.txt', 'w') as file:
            file.write("")
    
def initialize_debugy(**kwargs):
    """initialize debugy, check manual for everything you can setup"""
    # timestamp = true or false : default = false
    # logfilename = any name for a log file : default = "log.txt"
    timestamp = kwargs.get('timestamp', False)
    LOGFILE = kwargs.get('logfilename', 'log.txt')
    if LOGFILE.endswith(".txt"):
        continue
    else:
        LOGFILE = f"{logfilename}.txt"
    return Debugy(timestamp_enabled=timestamp)
