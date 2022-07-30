'''Load modules for getting data from different media'''



class Xloader:
    '''Master class for load transactional data'''
    def __init__(self):
        '''Init function'''
        self.transactions = {}

    def load(self):
        '''Load data from media'''

        

class Fileloader(Xloader):
    '''Class for load from files'''
    def __init__(self, Filepath, Fields, Readall = True, Readchunk = 100, Filetype = "cvs"):
        Xloader.__init__(Xloader)
        self.file_path = Filepath
        self.file_type = Filetype
        self.fields = Fields
        self.chunk = Readchunk
        self.current_line = 0
        self.read_all = Readall

    def readfile(self):
        '''Read file function'''
        try:
            with open(self.file_path, 'r') as f:

        except IOError as e:
            print 'Operation failed: %s' % e.strerror


    


if __name__ == "__main__":
    Loader = Xloader()
    print(Loader.transactions)
  
