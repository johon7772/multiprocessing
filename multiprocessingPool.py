import itertools
import multiprocessing as mp
import os
import sys
import time


class FilesList(mp.Process):

    def __init__(self, fileDirectory):
        mp.Process.__init__(self)
        self.fileDirectory = fileDirectory

    def run(self) -> int:
        fileDirectory = self.fileDirectory
        wordCount = 0

        with open(fileDirectory, 'r') as f:
            for line in f:
                words = line.split()
                wordCount += len(words)

        return wordCount


def workWithClass(directory, file):
    fileDirectory = '{0}/{1}'.format(directory, file)
    fileList = FilesList(fileDirectory)
    wordCount = fileList.run()
    currentProcess = mp.Process().name
    return file, wordCount, currentProcess


def main():
    started = time.time()
    directory = '/Users/JohonAlimov/PycharmProjects/multiprocessing/files'
    # directory = sys.argv[1]

    if not os.path.exists(directory):
        print('The path does not exist. Terminating the program.')
        sys.exit()

    filteredFileList = []
    for file in os.listdir(directory):
        if not file.startswith('.'):
            filteredFileList.append(file)

    pool = mp.Pool(processes=5)
    processes = pool.starmap(workWithClass, zip(itertools.repeat(directory), filteredFileList))

    for file, wordCount, process in processes:
        print('File: {0}, Word count: {1}, {2}'.format(file, wordCount, process))
    pool.close()

    timeExecuted = (time.time() - started) * 1000
    print('Time of execution: ' + str(timeExecuted))


if __name__ == '__main__':
    main()
