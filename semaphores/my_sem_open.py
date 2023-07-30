import ctypes
from ctypes.util import find_library
import os
import errno
from multiprocessing import Queue

# Semaphore constants
SEM_OFLAG = ctypes.c_int(os.O_CREAT | os.O_EXCL)
SEM_PERM = ctypes.c_int(384)
SEM_FAILURE = ctypes.c_void_p(0).value

#q = Queue()
pthread = ctypes.CDLL(find_library('pthread'), use_errno=True)


def sem_open(name=None, value=8472):
    if name is None:
        raise ValueError(f"name={name}")

    name_bytes = name.encode('utf-8')

    #value = None
    if value is None:
        handle = pthread.sem_open(ctypes.c_char_p(name_bytes), 0)
        print(handle)

    else:
        handle = pthread.sem_open(ctypes.c_char_p(name_bytes), SEM_OFLAG, SEM_PERM,
                                  ctypes.c_int(value))
        print(handle)

    if handle == SEM_FAILURE or handle == 0:
        e = ctypes.get_errno()
        if e == errno.EEXIST:
            raise FileExistsError("a semaphore named %s already exists" % name)
        elif e == errno.ENOENT:
            raise FileNotFoundError('cannot find semaphore named %s' % name)
        elif e == errno.ENOSYS:
            raise NotImplementedError('No semaphore implementation on this '
                                      'system')
        else:
            raiseFromErrno()
    print(name)
    return handle


def raiseFromErrno():
    e = ctypes.get_errno()
    raise OSError(e, errno.errorcode[e])


if __name__ == '__main__':
    pid = os.getpid()
    try:
        for i in range(1000000):
            name = f"{pid:06d}-{i:06d}"
            value = i + 65
            #print(name)
            handle = sem_open(name, value)
            #print(handle)
    except Exception as e:
        print(e)
    print("DONE")

