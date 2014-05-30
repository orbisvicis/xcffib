import xcffib
import struct
import cStringIO
_events = {}
_errors = {}
class ClientMessageData(xcffib.Union):
    def __init__(self, parent, offset, size):
        xcffib.Union.__init__(self, parent, offset, size)
        self.data8 = xcffib.List(parent, offset, 20, "B", 1)
        self.data16 = xcffib.List(parent, offset, 10, "H", 2)
        self.data32 = xcffib.List(parent, offset, 5, "I", 4)