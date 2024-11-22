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


def format(*args, **kwargs):  # real signature unknown
    """
    Return value.__format__(format_spec)                                            | Возвращщает value.__format__(format_spec)
                                                                                    |
    format_spec defaults to the empty string.                                       | по умолчанию format_spec равен пустой строке
    See the Format Specification Mini-Language section of help('FORMATTING') for    | Подробнее см. разделе "Format Specification Mini-Language" в help('FORMATTING')
    details.                                                                        |
    """
    pass

def getattr(object, name, default=None): # known special case of getattr
    """
    getattr(object, name[, default]) -> value                                       | getattr(object, name[, default]) -> value
                                                                                    |
    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.     | Возвращает значение атрибута обьекта с указанным именем; getattr(x, 'y') эквивалентна x.y.
    When a default argument is given, it is returned when the attribute doesn't     | Если указан аргумент default и атрибут не существует, возвращается его значение
    exist; without it, an exception is raised in that case.                         | Если нет, выбрасывается исключение.
    """
    pass


def globals(*args, **kwargs):  # real signature unknown
    """
    Return the dictionary containing the current scope's global variables.          | Возвращает словарь, содержащий глобальные переменные текущей области видимости
                                                                                    |
    NOTE: Updates to this dictionary *will* affect name lookups in the current      | Примечание: изменения в этом словаре влияют на поиск имен в гл. видимой области и наоборот
    global scope and vice-versa.                                                    |
    """
    pass


def hasattr(*args, **kwargs):  # real signature unknown
    """
    Return whether the object has an attribute with the given name.             | Возвращает, имеет ли обьект атрибут с указанным именем
                                                                                |
    This is done by calling getattr(obj, name) and catching AttributeError.     | Это достигается вызовом getattr(obj, name) с перехватом исключения AttributeError
    """
    pass


def hash(*args, **kwargs):  # real signature unknown
    """
    Return the hash value for the given object.                                     | Возвращает хэш для заданного обьекта
                                                                                    |
    Two objects that compare equal must also have the same hash value, but the      | Два обьекта, которые сравниваются как одинаковые, должны иметь одинаковый хеш,
    reverse is not necessarily true.                                                | но обратное не обязательно
    """
    pass


def help():  # real signature unknown; restored from __doc__
    """
    Define the builtin 'help'.                                                      | Определяет встроенную функцию 'help'
                                                                                    |
        This is a wrapper around pydoc.help that provides a helpful message         | Это оболочка pydoc.help, которая выводит полезное сообщение
        when 'help' is typed at the Python interactive prompt.                      | при вводе 'help' в интерактивной консоли Python
                                                                                    |
        Calling help() at the Python prompt starts an interactive help session.     | Вызов help() в интрактивной консоли Python  запускает интерактивную вспомогательную сессию
        Calling help(thing) prints help for the python object 'thing'.              | Вызов help(thing) выводит справку для обьекта Python'thing'
    """
    pass


def hex(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
    """
    Return the hexadecimal representation of an integer.    | возвращает шестнадцатеричное представление целого числа
                                                            |
       >>> hex(12648430)
       '0xc0ffee'
    """
    pass


def id(*args, **kwargs):  # real signature unknown
    """
    Return the identity of an object.                                       | Возвращает id обьекта
                                                                            |
    This is guaranteed to be unique among simultaneously existing objects.  | Это гарантированно уникальный идентификатор среди одновременно существующих обьектов
    (CPython uses the object's memory address.)                             |
    """
    pass


def input(*args, **kwargs):  # real signature unknown
    """
    Read a string from standard input.  The trailing newline is stripped.           |
                                                                                    |
    The prompt string, if given, is printed to standard output without a            |
    trailing newline before reading input.                                          |
                                                                                    |
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.    |
    On *nix systems, readline is used if available.                                 |
    """
    pass


def isinstance(x, A_tuple):  # real signature unknown; restored from __doc__
    """
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
    """
    pass


def issubclass(x, A_tuple):  # real signature unknown; restored from __doc__
    """
    Return whether 'cls' is a derived from another class or is the same class.

    A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
    or ...`` etc.
    """
    pass


def iter(source, sentinel=None):  # known special case of iter
    """
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
    """
    pass


def len(*args, **kwargs):  # real signature unknown
    """ Return the number of items in a container. """
    pass


def license(*args, **kwargs):  # real signature unknown
    """
    interactive prompt objects for printing the license text, a list of
        contributors and the copyright notice.
    """
    pass


def locals(*args, **kwargs):  # real signature unknown
    """
    Return a dictionary containing the current scope's local variables.

    NOTE: Whether or not updates to this dictionary will affect name lookups in
    the local scope and vice-versa is *implementation dependent* and not
    covered by any backwards compatibility guarantees.
    """
    pass


def max(*args, key=None):  # known special case of max
    """
    max(iterable, *[, default=obj, key=func]) -> value                  |
    max(arg1, arg2, *args, *[, key=func]) -> value                      |
                                                                        |
    With a single iterable argument, return its biggest item. The       | Если был введён один аргумент-итератор, возвращает его наибольший элемент.
    default keyword-only argument specifies an object to return if      | Ключевое слово default укащывает на обьект, который будет возвращен, если
    the provided iterable is empty.                                     | предоставленный итератор пустой.
    With two or more arguments, return the largest argument.            | Если аргументов 2 или более, возвращает наибольший аргумент
    """
    pass


def min(*args, key=None):  # known special case of min
    """
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its smallest item. The  | Если был введён один аргумент-итератор, возвращает его наименьший элемент.
    default keyword-only argument specifies an object to return if  | Ключевое слово default укащывает на обьект, который будет возвращен, если
    the provided iterable is empty.                                 | предоставленный итератор пустой.
    With two or more arguments, return the smallest argument.       | Если аргументов 2 или более, возвращает наименьший аргумент
    """
    pass


def next(iterator, default=None):  # real signature unknown; restored from __doc__
    """
    next(iterator[, default])

    Return the next item from the iterator. If default is given and the iterator    | Возвращает следующий элемент из итератора. Если указан
    is exhausted, it is returned instead of raising StopIteration.                  | default и итератор исчерпан, возвращается значение default вместо генерации исключения StopIteration
    """
    pass


def oct(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
    """
    Return the octal representation of an integer.  | Возвращает восьмеричное представление целого числа.

       >>> oct(342391)
       '0o1234567'
    """
    pass


def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None,
         closefd=True):  # known special case of open
    """
    Open file and return a stream.  Raise OSError upon failure.                     | Открывает файл и возвращает поток. Генерирует исключение OSError в случае ошибки
                                                                                    |
    file is either a text or byte string giving the name (and the path              | Файл либо текст либо байт строки
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)

    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.

    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.

    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.

    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:

    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.

    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.

    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.

    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.

    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:

    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.

    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.

    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.

    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).

    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.

    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.
    """
    pass


def ord(*args, **kwargs):  # real signature unknown
    """ Return the Unicode code point for a one-character string. """
    pass


def pow(*args, **kwargs):  # real signature unknown
    """
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
    """
    pass


def print(self, *args, sep=' ', end='\n', file=None):  # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass


def quit(*args, **kwargs):  # real signature unknown
    pass


def repr(obj):  # real signature unknown; restored from __doc__
    """
    Return the canonical string representation of the object.

    For many object types, including most builtins, eval(repr(obj)) == obj.
    """
    pass
