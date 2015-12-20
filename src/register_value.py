from __future__ import division, absolute_import, print_function, unicode_literals


class RegisterValue(object):
    """ Represents a single 8-bit register.
        Allows booleans and int members to be packed into and unpacked from the register value.
        Removes the need to keep ANDing and ORing everything.

        To use: add a static FORMAT class variable which is a list of 2-tuples, in the order
        they're packed into the register (MSB first). The first element of the tuple is the name
        of the class member, the second is the number of bits it takes up.
        """
    def pack(self):
        result = 0
        pos = 8
        for field, length in self.FORMAT:
            pos -= length
            assert pos >= 0
            if isinstance(field, basestring):
                val = getattr(self, field)
            else:
                val = field
            result |= int(val) << pos
        return result

    @classmethod
    def unpack(cls, value):
        reg = cls()
        pos = 8
        for field, length in reg.FORMAT:
            pos -= length
            bits = (value >> pos) & (2**length - 1)
            if isinstance(field, basestring):
                setattr(reg, field, type(getattr(reg, field))(bits))
        return reg

    def __repr__(self):
        info = []
        for field, length in self.FORMAT:
            if isinstance(field, basestring):
                val = getattr(self, field)
                if type(val) is int:
                    val = ("{0:#0%sb}" % (length + 2)).format(val)
                info.append("%s: %s" % (field, val))
        return """<Register {0:s}: {1:#4x} {1:#10b} - {2:s}>""".format(self.__class__.__name__,
                                                                             self.pack(), ", ".join(info))
