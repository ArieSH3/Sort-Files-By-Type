"""
A class that sorts files in a directory by their file type.
It creates separate folders for each file type and moves the files accordingly.
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox


class Sort_Files_By_Type:
    def __init__(self):
        self.path = None
        self.files_by_type = {}
        
    # get a list of all files in the directory
    def _get_files(self):
        path = self.path
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                self._get_file_extension(file)

    def _get_file_extension(self, filename):
        self.files_by_type [filename] = \
                            filename.split(".")[-1]
    
    def _loop_trough_files(self):
        for file in self.files_by_type:
            self._create_folder_for_file_type(self.files_by_type[file])
                           
    def _create_folder_for_file_type(self, file_type):
        path = self.path
        if not os.path.exists(os.path.join(path, file_type)):
            os.mkdir(os.path.join(path, file_type))
    
    def _sort_by_file_extension(self):
        overwrite_all = False
        for file in self.files_by_type:
            source_path = os.path.join(self.path, file)
            destination_path = os.path.join(self.path, self.files_by_type[file], file)
            # file already exists, prompt user what to do
            if os.path.exists(destination_path):
                if not overwrite_all:
                    response = messagebox.askyesno('File Exists', f'File "{file}" already exists in "{self.files_by_type[file]}" folder. Overwrite?')
                    if response:
                        overwrite_all = messagebox.askyesno('Overwrite All', 'Do you want to overwrite all existing files?')
                    else:
                        print(f'File: "{file}" was skipped.')
                        continue
                if overwrite_all:
                    # overwrite the file
                    os.replace(source_path, destination_path)
                    print(f'File: "{file}" was moved from "{source_path}" to "{destination_path}" successfully.')
                else:
                    # skip the file
                    print(f'File: "{file}" was skipped.')
            else:
                # file doesn't exist, move it
                os.rename(source_path, destination_path)
                print(f'File: {file} was moved from {source_path} to {destination_path} successfully.')
    
    def browse_folder(self):
        root = tk.Tk()
        root.withdraw()
        self.path = filedialog.askdirectory()
        print(f'Selected directory: {self.path} (all files in the directory will be sorted.)')
        
    def prompt_user_to_confirm(self):
        root = tk.Tk()
        root.withdraw()
        response = messagebox.askyesno('Confirm', f'Are you sure you want to sort the files in "{self.path}"?')
        if response:
            return True
        else:
            return False
        
    def run(self):
        self._get_files()
        self._loop_trough_files()
        self._sort_by_file_extension()

if __name__ == '__main__':
    
    soft_files = Sort_Files_By_Type()
    soft_files.browse_folder()
    if soft_files.prompt_user_to_confirm():
        soft_files.run()
    else:
        print('Sorting cancelled.')

