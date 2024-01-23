from .base_command import BaseCommand
import os
import shutil
from typing import List

class MoveCommand(BaseCommand):
    def __init__(self, options: List[str], args: List[str]) -> None:
        """
        Initialize the MoveCommand object.

        Args:
            options (List[str]): List of command options.
            args (List[str]): List of command arguments.
        """
        super().__init__(options, args)

        # Override the attributes inherited from BaseCommand
        self.description = 'Move a file or directory to another location'
        self.usage = 'Usage: mv [source] [destination]'

        # TODO 5-1: Initialize any additional attributes you may need.
        # Refer to list_command.py, grep_command.py to implement this.
        # ...
        
        self.interactive_mode = '-i' in options
        self.verbose_mode = '-v' in options

    def execute(self) -> None:
        """
        Execute the move command.
        Supported options:
            -i: Prompt the user before overwriting an existing file.
            -v: Enable verbose mode (print detailed information)
        
        TODO 5-2: Implement the functionality to move a file or directory to another location.
        You may need to handle exceptions and print relevant error messages.
        """
        # Your code here
        if len(self.args) < 2:
            print("Missing source or destination")
            return

        source, destination = self.args[0], self.args[1]

        try:
            if self.interactive_mode and self.file_exists(destination):
                confirm = input(f"{destination} already exists. Overwrite? (y/N): ")
                if confirm.lower() != 'y':
                    print("No Move.")
                    return

            shutil.move(source, destination)

            if self.verbose_mode:
                print(f"Moved {source} to {destination}")

        except Exception as e:
            print(f"Error during moving: {e}")

    
    def file_exists(self, directory: str, file_name: str) -> bool:
        """
        Check if a file exists in a directory.
        Feel free to use this method in your execute() method.

        Args:
            directory (str): The directory to check.
            file_name (str): The name of the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        file_path = os.path.join(directory, file_name)
        return os.path.exists(file_path)
