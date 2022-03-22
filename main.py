import datetime

def logger(old_function):

    def _logger(*args, **kwargs):
        date_time = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        function_name = old_function.__name__
        #function_args = f"args: {args}\nkwargs:{kwargs}"
        with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f'Дата: {date_time}\n'
                        f'Имя функции: {function_name}\n'
                        f'*args: {args}\n'
                        f'*kwargs: {kwargs}\n'
                        f'Результат: {result}\n'
                        f'---------------------')
        return result
    return _logger

def path_logger(path):

    def logger(old_function):
        def _logger(*args, **kwargs):
            date_time = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            function_name = old_function.__name__
            # function_args = f"args: {args}\nkwargs:{kwargs}"
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'Дата: {date_time}\n'
                        f'Имя функции: {function_name}\n'
                        f'*args: {args}\n'
                        f'*kwargs: {kwargs}\n'
                        f'Результат: {result}\n'
                        f'---------------------\n')
            return result

        return _logger
    return logger


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

# Iterator
class flatiterator():
    def __init__(self, nested_list):
        self.flat_list = []
        self.make_flat_list(nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.flat_list) == 0:
            raise StopIteration
        return self.flat_list.pop(0)

    def make_flat_list(self, list_item):
        for i in list_item:
            if isinstance(i, list):
                self.make_flat_list(i)
            else:
                self.flat_list.append(i)

# Generator
flat_list_gen = []


@path_logger('log.txt')
def make_flat_list(nested_list):
    for i in nested_list:
        if isinstance(i, list):
            make_flat_list(i)
        else:
            flat_list_gen.append(i)


def flatgenerator(nested_list):
    make_flat_list(nested_list)
    while len(flat_list_gen) !=0:
        yield flat_list_gen.pop(0)


if __name__ == '__main__':
    for item in flatiterator(nested_list):
        print(item)
    flat_list = [item for item in flatiterator(nested_list)]
    print()
    print('Comprehension: ', flat_list)
    print()
    for item in flatgenerator(nested_list):
        print(item)
