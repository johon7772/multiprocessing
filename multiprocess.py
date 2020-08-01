import os
import multiprocessing as mp
import time
import sys

started = time.time()
filesAndWordCount = {}


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

            global filesAndWordCount
            filesAndWordCount[file] = wordCount
            wordCount = 0
            print(filesAndWordCount)


def main():
    directory = '/Users/JohonAlimov/PycharmProjects/multiprocessing/files'
    # directory = sys.argv[1]

    if not os.path.exists(directory):
        print('No such directory: ' + str(directory))
        sys.exit()

    processList = []
    processLimiter = mp.BoundedSemaphore(5)

    for fileDirectory in os.listdir(directory):
        if not str(fileDirectory).startswith('.'):
            process = FilesList('{0}/{1}'.format(directory, fileDirectory))
            processList.append(process)
            process.start()

    for process in processList:
        process.join()

    global filesAndWordCount
    print(filesAndWordCount)
    timeExecuted = (time.time() - started) * 1000
    print('Time of execution: ' + str(timeExecuted))


if __name__ == '__main__':
    main()
