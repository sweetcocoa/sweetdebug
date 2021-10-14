import sys
import backtrace


def sweetdebug():
    backtrace.hook(align=True)
    old_hook = sys.excepthook

    def new_hook(type_, value, tb):
        old_hook(type_, value, tb)
        if type_ != KeyboardInterrupt:
            import pdb

            pdb.post_mortem(tb)

    sys.excepthook = new_hook
