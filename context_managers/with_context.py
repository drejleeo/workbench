from contextlib import contextmanager


# The "with" Statement & Context Managers

def with_statement_use(file_path):
    with open(file_path, 'w') as f:
        f.write('hello')


# Build a Context Manager class

class ManagedFile(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# Context manager Decorator:

@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'<{name}>')


# Main section

if __name__ == '__main__':

    # 1st example
    with_statement_use('example1.txt')

    # 2nd example
    with ManagedFile('example2.txt') as f:
        f.write('written with class context manager')

    # 3rd example
    with tag('h1'):
        print('foo')
