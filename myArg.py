import argparse
def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file','-f',metavar = 'filename', required= True)
    parser.add_argument('--verbose','-v',action='store_true')
    return parser.parse_args()