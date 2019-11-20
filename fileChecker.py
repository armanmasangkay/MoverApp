import os

class fileChecker:
    
    def __init__(self,directory):
        self.directory=directory
       

    def __listdir_nohidden(self):
        res=[]
        for f in os.listdir(self.directory):
            if not f.startswith('.'):
                res.append(self.directory+"/"+f)
        return res

    def getFiles(self):
        res=self.__listdir_nohidden()
        return res


        