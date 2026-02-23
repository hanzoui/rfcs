from abc import ABC, abstractmethod

'''
Hanzo Studio API available to custom nodes.
'''
class HanzoStudio(ABC):
    @abstractmethod
    def some_method(self):
        pass
