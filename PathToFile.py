import sublime_plugin
import os
from os import path
from PathToFileLanguages import PathToFileLanguages


class Pathtofile(sublime_plugin.TextCommand):
    def run(self, edit):
        """
        __init__ of this plugin
        """
        view = self.view
        syntax = self.getsyntax(view)
        selections = view.sel()

        for selection in selections:
            try:
                new_path = getattr(PathToFileLanguages(), syntax)(view, selection)
            except AttributeError:
                new_path = PathToFileLanguages().default(view, selection)

            self.checkdirectory(new_path)
            view.window().open_file(new_path)

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
