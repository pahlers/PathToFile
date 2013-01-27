import sublime_plugin
from os import path


class Pathtofile(sublime_plugin.TextCommand):
    def run(self, edit):
        print 'run PathToFile'

        view = self.view
        startPath = path.dirname(view.file_name())
        sels = view.sel()

        for sel in sels:
            newPath = path.normpath(path.join(startPath, view.substr(sel)))

            print 'PathToFile open ' + newPath

            view.window().open_file(newPath)
