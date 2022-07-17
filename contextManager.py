from contextlib import contextmanager


@contextmanager
def open_file_name(fileName):
    f = open('fileName', 'w')
    try:
        yield f
    finally:
        f.close()


with open_file_name('name.txt') as f:
    f.write('things to do')
