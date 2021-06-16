from abc import *

class PrinterBase(metaclass=ABCMeta): # 추상클래스 1
    @abstractmethod
    def dframe(self):
        pass

class ReaderBase(metaclass=ABCMeta): # 추상클래스 2

    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass
