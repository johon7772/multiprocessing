import os
import multiprocessing as mp
import time

started = time.time()


class FilesList(mp.Process):

    def __init__(self, fileDirectory):
        mp.Process.__init__(self)
        self.fileDirectory = fileDirectory

    def run(self):
        file = self.fileDirectory
        wordCount = 0

        with open(file, 'r') as f:
            for line in f:
                words = line.split()
                wordCount += len(words)

            filesAndWordCount[file] = wordCount
            print(filesAndWordCount)
            wordCount = 0


directory = '/Users/JohonAlimov/PycharmProjects/multiprocessing/files'
filesAndWordCount = {}
processList = []
processLimiter = mp.BoundedSemaphore(5)

if __name__ == '__main__':

    for fileDirectory in os.listdir(directory):
        if not str(fileDirectory).startswith('.'):
            processList.append(FilesList('{0}/{1}'.format(directory, fileDirectory)))

    for process in processList:
        process.start()

    for process in processList:
        process.join()

    timeExecuted = (time.time() - started) * 1000
    print(timeExecuted)
