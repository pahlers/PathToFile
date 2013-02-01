import sublime_plugin
import os
from os import path
try:
    # Python 3
    from PathToFile.PathToFileLanguages import PathToFileLanguages
except:
    # Python 2
    from PathToFileLanguages import PathToFileLanguages


class PathToFile(sublime_plugin.TextCommand):
    def run(self, edit):
        """
        __init__ of this plugin
        """
        view = self.view
        syntax = self.getsyntax(view)
        selections = view.sel()
        window = view.window()

        for selection in selections:
            if selection.empty():
                window.new_file()
            else:
                try:
                    new_path = getattr(PathToFileLanguages(), syntax)(view, selection)
                except AttributeError:
                    new_path = PathToFileLanguages().default(view, selection)

                self.checkdirectory(new_path)
                window.open_file(new_path)

    def getsyntax(self, view):
        """
        return the syntax of the current file
        """
        syntax = view.settings().get('syntax')

        return path.basename(syntax).split('.', 1)[0].lower()

    def checkdirectory(self, new_path):
        """
        check directory

        if doesn't exists
            make directory
        """
        directory = path.dirname(new_path)
        if(path.exists(directory) == False):
            os.makedirs(directory)
