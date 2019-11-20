from fileChecker import fileChecker
import time
import os
import ntpath as nt
fc=fileChecker('/Users/armanmasangkay/Downloads')



#print(nt.basename('/Users/armanmasangkay/Downloads/Visual Studio Code.app'))

#check if it is in the excluded file
def isExclude(filePath):
    f=open('MoverApp/exclude.txt','r')
    excludes=f.read()
    if filePath in excludes:
        f.close()
        return True
    else:
        f.close()
        return False

#categorize based on their extension 
def categorize(filePath):
    _,fileExtension=os.path.splitext(filePath)
    
    compressed=open('MoverApp/formats/compressed.txt','r')
    documents=open('MoverApp/formats/documents.txt','r')
    image=open('MoverApp/formats/image.txt','r')
    programs=open('MoverApp/formats/programs.txt','r')

    compressedList=compressed.read()
    documentsList=documents.read()
    imageList=image.read()
    programsList=programs.read()
    res=''
    if fileExtension in compressedList:
        res= 'compressed'
    elif fileExtension in documentsList:
        res= 'documents'
    elif fileExtension in imageList:
        res= 'images'
    elif fileExtension in programsList:
        res= 'programs'
    else:
        res= 'uncategorized'
    
    compressed.close()
    documents.close()
    image.close()
    programs.close()
    return res

def setDestination(source, absolutePath):
    cat=categorize(source)
    fileName=nt.basename(source)
    destination=absolutePath+'/'+cat.capitalize()+'/' +fileName
    return destination

def move(source,destination):
    dest=setDestination(source,destination)
    res=False
    if not isExclude(source):
        os.rename(source,dest)
        res=True
    return res
    
   






#starts checking the directory
def start(delay):
    while (True):
        files=fc.getFiles()
        for file in files:
            res=move(file,'/Users/armanmasangkay/Documents')
            if res:
                print (file + ' moved')
            else:
                print ('waiting..')
        time.sleep(delay)

start(5)
# fileName,fileExtension=os.path.splitext('/Users/armanmasangkay/Downloads/2F TopicLog Lec.docx')
# print (fileExtension)
#files=listdir_nohidden('/Users/armanmasangkay/Downloads')

#os.rename('/Users/armanmasangkay/Downloads/mysql-connector-java-8.0.18','/Users/armanmasangkay/Documents/mysql-connector-java-8.0.18')