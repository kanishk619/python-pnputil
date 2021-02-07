
__all__ = ['InterfaceCache']

from collections import OrderedDict


class InterfaceCache(object):
    __instance = None
    __interfaces = OrderedDict()

    def __init__(self):
        if InterfaceCache.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            InterfaceCache.__instance = self

    @staticmethod
    def get_instance():
        if InterfaceCache.__instance is None:
            InterfaceCache()
        return InterfaceCache.__instance

    @staticmethod
    def add_interface_to_cache(guid, interface):
        if str(guid) not in InterfaceCache.get_instance().__interfaces:
            InterfaceCache.get_instance().__interfaces[str(guid)] = []

        if interface is not None:
            InterfaceCache.get_instance().__interfaces[str(guid)].append(interface)

    @staticmethod
    def has_interface(guid: str = None):
        return True if str(guid) in InterfaceCache.get_instance().__interfaces else False

    @staticmethod
    def get_interface(guid: str = None):
        return InterfaceCache.get_instance().__interfaces[str(guid)]

    @staticmethod
    def clear():
        InterfaceCache.get_instance().__interfaces.clear()
