import os
import time

started = time.time()


class FilesList:

    def __init__(self, fileDirectory):
        self.directory = fileDirectory

    def searchFiles(self):

        files = os.listdir(self.directory)
        wordCount = 0

        for file in files:
            fileDirectory = str('{0}/{1}'.format(self.directory, file))
            with open(fileDirectory, 'r') as f:
                for line in f:
                    words = line.split()
                    wordCount += len(words)

                filesAndWordCount[file] = wordCount
                wordCount = 0

        sortedFiles = sorted(filesAndWordCount.items(), key=lambda x: x[1])
        print(sortedFiles)


directory = '/Users/JohonAlimov/PycharmProjects/multithreading_task/files'
filesAndWordCount = {}
filesList = FilesList(directory)
filesList.searchFiles()
timeExecuted = (time.time() - started) * 1000
print(timeExecuted)
