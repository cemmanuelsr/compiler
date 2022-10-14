from processes.WriteDotFile import Writer


class List(list):
    def __init__(self, __owner):
        super(List, self).__init__()
        self.__owner = __owner

    def append(self, __object) -> None:
        super(List, self).append(__object)
        Writer.link_parent_and_child(__object, self.__owner)
