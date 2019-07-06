class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_start_from_list(self):
        if not self.__root:
            raise LookupError("can't pop, the list is empty")
        removed_node = self.__root
        self.__root = self.__root.get_next()
        return removed_node

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, text):
        marker = self.__root
        while marker:
            if marker.text == text:
                return marker
            marker = marker.get_next()

        raise LookupError("Can't find {} this text".format(text))

    def size(self):
        count = 0
        marker = self.__root
        while marker:
            count += 1
            marker = marker.get_next()

        return count
