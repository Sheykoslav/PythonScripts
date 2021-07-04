import os
import math
import collections


class Detector(object):
    """
    Detect encrypted/compressed files in given directory.
    Scanned files stored in list of tuples: (confidence, filename).
    """
    def __init__(self, dirname):
        self.file_confidence = []
        self.scan_directory(dirname)

    @staticmethod
    def entropy(data):
        """
        Calculate Shannon entropy of the specified file
        :param data: list of numeric representations for every character in file
        """
        e = 0

        counter = collections.Counter(data)
        l = len(data)
        for count in counter.values():
            p_x = count / l
            e += - p_x * math.log2(p_x)

        return e

    def confidence(self, filename):
        """
        Calculate confidence level(in percents) of a file by its entropy to
        determine if it is encryped/compressed.
        :param filename: absolute path to the file
        """
        f = open(filename, 'rb')
        content = list(f.read())
        f.close()

        file_entropy = self.entropy(content)

        return (round(file_entropy / 8 * 100), filename)

    def scan_directory(self, dirname):
        """
        Check confidence level of all files in specified directory and save
        results to the list.
        :param dirname: path to the directory
        """
        if not dirname:
            dirname = os.getcwd()

        if os.path.exists(dirname):
            for item in os.listdir(dirname):
                item_path = os.path.join(dirname, item)
                if os.path.isfile(item_path):
                    self.file_confidence.append(self.confidence(item_path))
        else:
            raise FileNotFoundError('Directory does not exist. Change your path and try again')

    def handle_output(self, parameters):
        """
        Make user friendly output using CLI flags.
        :param parameters: CLI parameters
        """
        if not self.file_confidence or not parameters:
            raise ValueError("List is empty or parameters value is wrong")

        if parameters.descending:
            self.file_confidence.sort(reverse=True, key=lambda elem: elem[0])

        if parameters.ascending:
            self.file_confidence.sort(key=lambda elem: elem[0])

        for item in self.file_confidence:
            if item[0] >= parameters.confidence:
                if parameters.print_confidence:
                    print(f"{item[0]}% {os.path.basename(item[1])}")
                else:
                    print(os.path.basename(item[1]))

def cli_config():
    from argparse import ArgumentParser

    parser = ArgumentParser(usage='detect encrypted/compressed files in a specified directory')
    parser.add_argument('-d', '--dir', default="", type=str,
        help='specifies the path to directory where to look for encrypted/compressed files'
    )
    parser.add_argument('-c', '--confidence', default=80, type=int,
        help='specifies the threshold level of confidence (in percents from 0 to 100) to treat a certain file as encryped/compressed'
    )
    parser.add_argument('-ds', '--descending', default=False, const=True, type=bool, nargs='?',
        help='all files in the program output should be sorted by confidence level descending'
    )
    parser.add_argument('-as', '--ascending', default=False, const=True, type=bool, nargs='?',
        help='all files in the program output should be sorted by confidence level ascending'
    )
    parser.add_argument('-p', '--print-confidence', default=False, const=True, type=bool, nargs='?',
        help='print the confidence level along with the file name'
    )

    return parser.parse_args()


if __name__ == '__main__':
    cli_args = cli_config()

    detector = Detector(cli_args.dir)
    detector.handle_output(cli_args)
