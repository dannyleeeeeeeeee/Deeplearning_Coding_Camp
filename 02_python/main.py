import argparse
import logging
from utils.command_handler import CommandHandler
from utils.command_parser import CommandParser

# TODO 1-1
parser = argparse.ArgumentParser(description="Command Line File Manager")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-l", "--log_file", type=str)
args = parser.parse_args()

# TODO 1-2
logging.basicConfig(filename=args.log_file, level=logging.DEBUG if args.verbose else logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

command_parser = CommandParser()
handler = CommandHandler(command_parser)

while True:
    command = input(">> ")
    handler.execute(command)
