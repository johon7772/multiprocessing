import os
import threading
import time
import sys

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


# directory = '/Users/JohonAlimov/PycharmProjects/multiprocessing/files'

directory = sys.argv[1]
if not os.path.exists(directory):
    print('No such direction: ' + str(sys.argv[1])/
          'Exiting program')
    sys.exit()

filesAndWordCount = {}
threadList = []
maxNumberOfThreads = 5
threadLimiter = threading.BoundedSemaphore(maxNumberOfThreads)

for fileDirectory in os.listdir(directory):
    if not str(fileDirectory).startswith('.'):
        threadList.append(FilesList('{0}/{1}'.format(directory, fileDirectory)))

threadLimiter.acquire()
for thread in threadList:
    thread.start()
    # print(threading.active_count())

for thread in threadList:
    thread.join()
threadLimiter.release()

timeExecuted = (time.time() - started) * 1000
6
