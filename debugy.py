# A python module created for making debugging easier 
# V1.0

#    ****     ****                **               **                     **********                                                ********                     **         **     **
#   /**/**   **/**               /**              /**       **   **      /////**///                                                **//////**                   //         //**   ** 
#   /**//** ** /**  ******       /**  *****       /**      //** **           /**      ******  **********   ******    ******       **      //   ******  ******    ** **   ** //** **  
#   /** //***  /** //////**   ****** **///**      /******   //***            /**     **////**//**//**//** //////**  **////       /**          **////**//**//*   /**/**  /**  //***   
#   /**  //*   /**  *******  **///**/*******      /**///**   /**             /**    /**   /** /** /** /**  ******* //*****       /**    *****/**   /** /** /    /**/**  /**   **/**  
#   /**   /    /** **////** /**  /**/**////       /**  /**   **              /**    /**   /** /** /** /** **////**  /////**      //**  ////**/**   /** /**    **/**/**  /**  ** //** 
#   /**        /**//********//******//******      /******   **               /**    //******  *** /** /**//******** ******        //******** //****** /***   //*** //****** **   //**
#   //         //  ////////  //////  //////       /////    //                //      //////  ///  //  //  //////// //////          ////////   //////  ///     ///   ////// //     // 

from enum import Enum
from datetime import datetime

class LogLevel(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

class Debugy:
    def __init__(self, timestamp_enabled: bool) -> None:
        self.initialized = True
        self.start_text = ":DEBUG:"
        self.timestamp_enabled = timestamp_enabled

    def print(self, text_to_print: str):
        if self.initialized:
            print(f"{self.start_text} {text_to_print}")
            
    def logmessage(self, log_level: LogLevel, what_to_log: str):
        """Logs something to a file as, INFO, WARNING, ERROR"""
        with open('log.txt', 'a') as file:
            file.write("") # add a space in the log
            if self.timestamp_enabled:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # get the current time
                file.write(f"{time} - :{log_level.value}: {what_to_log}\n")  
                return
            file.write(f":{log_level.value}: {what_to_log}\n")
            
    def clearlogfile(self):
        with open('log.txt', 'w') as file:
            file.write("")
    
def initialize_debugy(**kwargs):
    """initialize debugy, check manual for everything you can setup"""
    # timestamp = true or false : default = false
    timestamp = kwargs.get('timestamp', False)
    return Debugy(timestamp_enabled=timestamp)