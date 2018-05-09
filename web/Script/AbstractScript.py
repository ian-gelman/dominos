from abc import abstractmethod

class AbstractScript(object):

    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def finish(self):
        pass