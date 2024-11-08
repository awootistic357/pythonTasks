def abs(*args, **kwargs): # real signature unknown
    """ Return the absolute value of the argument. | Возвращает абсолютное значение аргумента"""
    pass


def all(*args, **kwargs):  # real signature unknown
    """
    Return True if bool(x) is True for all values x in the iterable. | Возвращает True, если bool(x) является True для всех
    If the iterable is empty, return True.                           | значений x в списке. Если элемент списка пуст, возвращает True
    """
    pass

def any(*args, **kwargs):  # real signature unknown
    """
    Return True if bool(x) is True for any x in the iterable.  | Возвращает True, если bool(x) является True для любого x в списке.
    If the iterable is empty, return False.                    | Если элемент списка пуст, возвращает False.
    """
    pass

def ascii(*args, **kwargs):  # real signature unknown
    """
    Return an ASCII-only representation of an object.                        | Возвращает строковое представление объекта, содержащее только символы ASCII
    As repr(), return a string containing a printable representation of an   | Как и repr(), возвращает строку, содержащую отображаемое представление
    object, but escape the non-ASCII characters in the string returned by    | объекта, но заменяет не-ASCII символы в возвращаемой строке на
    repr() using \\x, \\u or \\U escapes. This generates a string similar    | экранированные последовательности \\x, \\u или \\U. Это генерирует строку,
    to that returned by repr() in Python 2.                                  | похожую на ту, которую возвращает repr() в Python 2.
    """
    pass

def bin(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
    """
    Return the binary representation of an integer.     | Возвращает бинарное представление типа integer
       >>> bin(2796202)
       '0b1010101010101010101010'
    """
    pass


def breakpoint(*args, **kws):  # real signature unknown; restored from __doc__
    """
    breakpoint(*args, **kws)

    Call sys.breakpointhook(*args, **kws).  sys.breakpointhook() must accept    | Вызывает sys.breakpointhook(*args, **kws). Функция
    whatever arguments are passed.                                              |sys.breakpointhook() должна принимать любые переданные аргументы.
                                                                                |
    By default, this drops you into the pdb debugger.                           | По умолчанию, это переводит вас в отладчик pdb.
    """
    pass


def callable(i_e_, some_kind_of_function):  # real signature unknown; restored from __doc__
    """
    Return whether the object is callable (i.e., some kind of function).    | Возвращает данные о том, можно ли вызывать данный объект или нет (т.е. является ли он какой-либо функцией)

    Note that classes are callable, as are instances of classes with a      | Заметьте, что классы это вызываемые объекты, так же как и экземпляры классов с методом __call__().
    __call__() method.
    """
    pass

def chr(*args, **kwargs): # real signature unknown
    """ Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.    | Возвращает строку Unicode с одним символом с порядковым номером i; 0 <= i <= 0x10ffff."""
    pass


def compile(*args, **kwargs):  # real signature unknown
    """
    Compile source into a code object that can be executed by exec() or eval(). | Компилирует исходный код в объект кода, который может быть
                                                                                | выполнен с помощью exec() или eval().
    The source code may represent a Python module, statement or expression.     | Исходный код может представлять собой модуль Python, оператор или выражение.
    The filename will be used for run-time error messages.                      | Имя файла будет использовано для сообщений об ошибках времени выполнения.
    The mode must be 'exec' to compile a module, 'single' to compile a          | Режим должен быть 'exec' для компиляции модуля, 'single' для компиляции
    single (interactive) statement, or 'eval' to compile an expression.         | одного (интерактивного) оператора или 'eval' для компиляции выражения.
    The flags argument, if present, controls which future statements influence  | Аргумент flags, если указан, контролирует, какие future-операторы влияют
    the compilation of the code.                                                | на компиляцию кода.
    The dont_inherit argument, if true, stops the compilation inheriting        | Аргумент dont_inherit, если установлен в true, предотвращает наследование
    the effects of any future statements in effect in the code calling          | эффектов любых future-операторов, действующих в коде, вызывающем
    compile; if absent or false these statements do influence the compilation,  | compile; если аргумент отсутствует или равен false, эти операторы
    in addition to any features explicitly specified.                           | будут влиять на компиляцию, дополнительно к любым явно указанным особенностям.
    """
    pass

def copyright(*args, **kwargs): # real signature unknown
    """
    interactive prompt objects for printing the license text, a list of     | Интерактивные объекты для вывода текста лицензии, списка
        contributors and the copyright notice.                              | участников и уведомления об авторских правах.
    """
    pass


def delattr(x, y):  # real signature unknown; restored from __doc__
    """
    Deletes the named attribute from the given object.  | Удаляет названный атрибут из данного объекта
    delattr(x, 'y') is equivalent to ``del x.y''        | delattr(x, 'y') эквивалентен ``del x.y''
    """
    pass


def dir(p_object=None):  # real signature unknown; restored from __doc__
    """
    dir([object]) -> list of strings                                                    | dir([object]) -> список строк
                                                                                        |
    If called without an argument, return the names in the current scope.               | Если вызывается без аргумента, возвращает имена в текущей области видимости.
    Else, return an alphabetized list of names comprising (some of) the attributes      | В противном случае возвращает отсортированный по алфавиту список имен,
    of the given object, and of attributes reachable from it.                           | состоящий (частично) из атрибутов переданного объекта и атрибутов,
    If the object supplies a method named __dir__, it will be used; otherwise           | доступных через него.
    the default dir() logic is used and returns:                                        | Если объект предоставляет метод с именем __dir__, он будет использован;
      for a module object: the module's attributes.                                     | в противном случае будет применена логика dir() по умолчанию, которая возвращает:
      for a class object:  its attributes, and recursively the attributes               | для объекта-модуля: атрибуты модуля.
        of its bases.                                                                   | для объекта-класса: его атрибуты и рекурсивно атрибуты его базовых классов.
      for any other object: its attributes, its class's attributes, and                 | для любого другого объекта: его атрибуты, атрибуты его класса и
        recursively the attributes of its class's base classes.                         | рекурсивно атрибуты базовых классов его класса.
    """
    return []

def divmod(x, y): # known case of builtins.divmod
    """ Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.     | Вернуть кортеж (x//y, x%y).  Постоянный: div*y + mod == x. """
    return (0, 0)


def eval(*args, **kwargs):  # real signature unknown
    """
    Evaluate the given source in the context of globals and locals.     | Выполняет оценку переданного исходного кода в контексте globals и locals.

    The source may be a string representing a Python expression         | Источником может быть строка, представляющая выражение Python
    or a code object as returned by compile().                          | или объектом кода, возвращенным функцией compile().
    The globals must be a dictionary and locals can be any mapping,     | Аргумент globals должен быть словарем, а locals может быть любым отображением,
    defaulting to the current globals and locals.                       | по умолчанию используются текущие globals и locals.
    If only globals is given, locals defaults to it.                    | Если передан только globals, то locals по умолчанию принимает его значение.
    """
    pass


def exec(*args, **kwargs):  # real signature unknown
    """
    Execute the given source in the context of globals and locals.          | Выполняет данный исходный код в контексте globals и locals.
                                                                            |
    The source may be a string representing one or more Python statements   | Источником может быть строка, представляющая выражение Python
    or a code object as returned by compile().                              | или объектом кода, возвращенным функцией compile().
    The globals must be a dictionary and locals can be any mapping,         | Аргумент globals должен быть словарем, а locals может быть любым отображением,
    defaulting to the current globals and locals.                           | по умолчанию используются текущие globals и locals.
    If only globals is given, locals defaults to it.                        | Если передан только globals, то locals по умолчанию принимает его значение.
    """
    pass
