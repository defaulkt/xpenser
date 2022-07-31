'''Load modules for getting data from different media'''

import logging


class Fileloader():
    '''Class for load from files'''
    def __init__(self, Filepath, Fields, Header = True, Filetype = "cvs", Encoding = "utf8"):
        self.transactions = []
        self.file_path = Filepath
        if not isinstance(Fields, dict):
            print("Fields must be a dictinary: {'field_name': field_number} ")
            self.fields = {}
        elif min(Fields.values()) < 1:
            print("Fields positions cannot be < 1")
            self.fields = {}
        else:
            self.fields = Fields
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
                    transaction = {}
                    parsed_line = line.strip().split(self.divder)
                    self.logger.debug("Reading a line from the file: %s", parsed_line)
                    if len(parsed_line) < max(self.fields.values()):
                        pass
                    for field_name, field_position in self.fields.items():
                        transaction[field_name] = parsed_line[field_position-1]
                    self.transactions.append(transaction)
        except IOError as io_exception:
            self.logger.critical('Operation failed: %s' , str(io_exception.strerror))
        file_descriptor.close()

    

    


if __name__ == "__main__":
    Loader = Fileloader("/Users/vakimov/Desktop/currentTransaction_5953.csv", {"Date": 1, "Payee": 3, "Amount": 5})
    Loader.load()
    for item in Loader.transactions:
        print(item)
 
  
