from .base_command import BaseCommand
import os
import shutil
from typing import List

class ChangeDirectoryCommand(BaseCommand):
    def __init__(self, options: List[str], args: List[str]) -> None:
        """
        Initialize the ChangeDirectoryCommand object.

        Args:
            options (List[str]): List of command options.
            args (List[str]): List of command arguments.
        """
        super().__init__(options, args)

        # Override the attributes inherited from BaseCommand
        self.description = 'Change the current working directory'
        self.usage = 'Usage: cd [options] [directory]'

        # TODO 7-1: Initialize any additional attributes you may need.
        # Refer to list_command.py, grep_command.py to implement this.
        # ...
        self.verbose_mode = '-v' in options

    def execute(self) -> None:
        """
        Execute the cd command.
        Supported options:
            -v: Enable verbose mode (print detailed information)
        
        TODO 7-2: Implement the functionality to change the current working directory.
        You may need to handle exceptions and print relevant error messages.
        """
        try:
            if self.args:
                new_path = self.args[0]
                os.chdir(new_path)
                BaseCommand.update_current_path(new_path)

                if self.verbose_mode:
                    print(f"Changed directory to {new_path}")
            else:
                raise ValueError("No directory specified")
        except Exception as e:
            print(f"Error change directory: {e}")