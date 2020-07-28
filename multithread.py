import os
import threading
import time

started = time.time()


class FilesList(threading.Thread):

    def __init__(self, fileDirectory):
        threading.Thread.__init__(self)
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
filesList = FilesList(directory)

filesAndWordCount = {}
threadList = []
maxNumberOfThreads = 5
threadLimiter = threading.BoundedSemaphore(maxNumberOfThreads)

for fileDirectory in os.listdir(directory):
    threadList.append(FilesList('{0}/{1}'.format(directory, fileDirectory)))

threadLimiter.acquire()
for thread in threadList:
    thread.start()
    print(thread)

for thread in threadList:
    thread.join()
threadLimiter.release()

timeExecuted = (time.time() - started) * 1000
print(timeExecuted)
sortedFiles = sorted(filesAndWordCount.items(), key=lambda x: x[1])
print(sortedFiles)
