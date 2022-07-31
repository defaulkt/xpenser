'''Load modules for getting data from different media'''

import logging


class Fileloader():
    '''Class for load from files'''
    def __init__(self, Filepath, Header = True, Filetype = "cvs", Encoding = "utf8"):
        self.transactions = []
        self.file_path = Filepath
        if Filetype == "csv":
            self.divder = ","
        elif Filetype == "tsv":
            self.divder = "\t"
        else:
            self.divder = ","
         
        self.encoding = Encoding
        self.logger = logging.getLogger(__name__)


    def load(self):
        '''Read file function'''
        
        try:
            with open(self.file_path, "r", encoding=self.encoding) as file_descriptor:
                for line in file_descriptor:
                    parsed_line = line.strip().split(self.divder)
                    self.logger.debug("Reading a line from the file: %s", parsed_line)
                    self.transactions.append(parsed_line)
        except IOError as io_exception:
            self.logger.critical('Operation failed: %s' , str(io_exception.strerror))
        file_descriptor.close()

    

if __name__ == "__main__":
    pass


 
  
