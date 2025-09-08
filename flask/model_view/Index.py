class Index:
    def __init__(self):
        self._title = "Index"
        self._head_description = "Upload a xlsx or ods to fill a database"
        self._main_description = "Fill database with file table"
        self._file_size_description = "...be reasonable on file beign uploaded."
        self._detail_footer = ""
            
    @property
    def title(self):
        return self._title
    
    @property
    def head_description(self):
        return self._head_description
    
    @property
    def main_description(self):
        return self._main_description
    
    @property
    def file_size_description(self):
        return self._file_size_description
    
    @property
    def detail_footer(self):
        return self._detail_footer
