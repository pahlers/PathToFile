from os import path


class PathToFileLanguages(object):
    """PathToFileLanguages
       Methods with language specific knowledge of paths
    """

    def _abspath(self, view, start_path, end_path):
        """
        Absolute path (guesstimate)
        """
        new_start_path = start_path

        for folder in view.window().folders():
            if start_path.find(folder) != -1:
                new_start_path = folder

        return path.normpath(path.join(new_start_path, end_path[1:]))

    def _relpath(self, view, start_path, end_path):
        """
        Relative path
        """
        return path.normpath(path.join(start_path, end_path))

    def default(self, view, selection):
        """
        default path builder
        """
        start_path = path.dirname(view.file_name())
        end_path = view.substr(selection)

        if path.isabs(end_path):
            return self._abspath(view, start_path, end_path)
        else:
            return self._relpath(view, start_path, end_path)
