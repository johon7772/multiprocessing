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
            wordCount = 0


directory = '/Users/JohonAlimov/PycharmProjects/multithreading_task/files'
filesAndWordCount = {}
processList = []
processLimiter = mp.BoundedSemaphore(5)

if __name__ == '__main__':
    fileDirectory = os.listdir(directory)

    6
    for f in fileDirectory:
        processList.append(FilesList('{0}/{1}'.format(directory, f)))
        # print('{0}/{1}'.format(directory, f), processList)

    for process in processList:
        print(process)
        process.start()

    for process in processList:
        process.join()

    timeExecuted = (time.time() - started) * 1000
    print(timeExecuted)
    sortedFiles = sorted(filesAndWordCount.items(), key=lambda x: x[1])
    print(sortedFiles)


