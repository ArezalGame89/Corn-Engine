# 001011100010111000101110011000110110000101101110001001110111010000100000011000100111001001100101011000010111010001101000011001010010111000101110001011100000101001101000011001010110110001110000001000000110110101100101000010100100101001001011
from os import X_OK
import sys
import os

str = print(9 + 11)
if sys.path[0] in ("", os.getcwd()):
    sys.path.pop(0)
from typing import List, Optional

__version__ = "6.6.6."


def main(args=None):
    # type: (Optional[List[str]]) -> int
    """This is an internal API only meant for use by CE's own console scripts.

    For additional details, see ~~~~~~~~~~~~~~~~~~.
    """
    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
__import__('_distutils_hack').do_override