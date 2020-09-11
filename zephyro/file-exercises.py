# Övningar 1-t.o.m 7, 16 samt 17
# Övningar 8-13 valfria
import typing as t

from pathlib import Path
from sys import argv
from random import randint


SILENT = False
THIS_FILE = argv[0]
TEXT_FILE = argv[0].replace(".py", "-text.txt")
COPY_FILE = argv[0].replace(".py", "-copy.txt")


# cannot use backslash in an argument to function calls inside f-strings
# for example: print(f'some {text.rstrip("\n")}') -> Error
nl = '\n'

if len(argv) > 1:
    if 'silent'[:len(argv)] == argv[1]:
        SILENT = True


def prints(text: str, *args, **kwargs) -> None:
    """print text is silent mode is off."""
    if not SILENT:
        print(text, *args, **kwargs)


def next_uppg(i: int = 0, skip: t.Optional[bool] = False) -> None:
    """
    Prints some spacing and a header inbetween each exercise. \
    User has to press enter to go to the next exercise
    """
    if SILENT:
        return
    if not skip:
        _ = input('\npress enter to continue...')
    if i:
        title = f'\t\t  Uppgift {i}'
    else:
        title = '  ~ Finding path and touching your files... ~'
    spacer = '================================================'
    print(f'\n{spacer}\n{title}\n{spacer}\n')


next_uppg(0, skip=True)

try:
    p = Path(TEXT_FILE)
    p.touch(exist_ok=True)
    q = Path(COPY_FILE)
    q.touch(exist_ok=True)
except Exception as e:
    print(f'Error: {e}')
    print('Unable to create text file, aborting.')
    exit()


##############################################################################
#
# 1. Write a Python program to read an entire text file.
#
next_uppg(1)

try:
    with p.open(mode='r') as f:
        prints(f'contents of {p.name}:\n')
        for i, line in enumerate(f):
            prints(f'{i + 1} {line}', end='')
except Exception as e:
    print(f'Error: {e}')


##############################################################################
#
# 2. Write a Python program to read first n lines of a file.
#
next_uppg(2)

n = 17  # sample value
try:
    with p.open(mode='r') as f:
        print(f'contents of {p.name}:\n')
        for i, line in enumerate(f):
            if i == n:
                break
            prints(f'{i + 1} {line}', end='')
except Exception as e:
    print(f'Error: {e}')


##############################################################################
#
# 3. Write a Python program to append text to a file and display the text.
#
next_uppg(3)

try:  # we're gonna append lines from this file.
    with Path(THIS_FILE).open(mode='r') as f, p.open(mode='a') as o:
        o.seek(0, 2)
        for _ in range(10):  # 10 lines is enough.
            word = f.readline()
            o.write(word)
            prints(f' wrote {word.rstrip(nl)} to {p.name}')
except Exception as e:
    print(f'Error: {e}')


##############################################################################
#
# 4. Write a Python program to read last n lines of a file.
#
next_uppg(4)

# using same n as defined in # 2.
lines = []
try:
    with p.open(mode='r') as f:
        for i in range(n):  # does this start from the last line or the
            f.seek(-i, 2)   # second last? -1 offset from last line.... ?
            lines.append(f'{f.readline()}')  # todo: linecounter ?
except Exception as e:
    print(f'Error: {e}')
else:
    for i, line in enumerate(lines):
        prints(f'line {len(lines) - i}: {line}', end='')


##############################################################################
#
# uppg 5, 6, 7 are combined
#

# mypy complains about a missing return statement,
# but the return value is optional >.>
def uppg(uppg: int, skip: bool = True) -> t.Optional[t.List[str]]:
    """
    uppg 5, 6 and 7 are written exactly the same,
    so just call this function 3 times.
    """
    next_uppg(uppg, skip=skip)

    try:
        with p.open(mode='r') as f:
            lines = [line for line in f]
    except Exception as e:
        print(f'Error: {e}')
    else:
        for i, line in enumerate(lines):
            prints(f'line {i + 1}: {line}', end='')
        return lines


# 5. Write a Python program to read a file line by line and
#   store it into a list.

i_am_a_list = uppg(5, True)  # a list can be assigned to a variable


# 6. Write a Python program to read a file line by line store
#    it into a variable.

i_am_a_variable = uppg(6, True)


# 7. Write a Python program to read a file line by line store it into an array.
# next_uppg(7, skip=True)

i_am_an_array = uppg(7, True)  # array == list (at least in python)


##############################################################################
#
# 8. Write a python program to find the longest words.
#
next_uppg(8)

try:
    big_word = ''
    with p.open(mode='r') as f:
        lines = [line for line in f]
except Exception as e:
    print(f'Error: {e}')
else:
    for line in lines:
        for word in line.split(' '):
            if word > big_word:
                big_word = word

    prints(f'The largest word is: ... \n{big_word}')


##############################################################################
#
# 9. Write a Python program to count the number of lines in a text file.
#
next_uppg(9)

try:
    with p.open(mode='r') as f:
        prints(f'{p.name} has {len([line for line in f])} lines.')
except Exception as e:
    print(f'Error: {e}')


##############################################################################
#
# 10. Write a Python program to count the frequency of words in a file.
#
next_uppg(10)

try:
    with p.open(mode='r') as f:
        lines = [line for line in f]
except Exception as e:
    print(f'Error: {e}')
else:
    words: t.Dict[str, int] = {}
    for line in lines:
        for word in line.split(' '):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    for word, count in words.items():
        prints(f'`{word.rstrip(nl)}` appeared `{count}` times.')


##############################################################################
#
# 11. Write a Python program to get the file size of a plain file.
#
next_uppg(11)

prints(f'filesize: {p.stat().st_size} bytes')


##############################################################################
#
# 12. Write a Python program to write a list to a file.
#
next_uppg(12)


lines = [str(randint(0, 100)) + '\n' for _ in range(20)]

try:
    with p.open(mode='w') as o:
        for line in lines:
            o.write(line)
            prints(f'wrote {line.rstrip(nl)} to {p.name}')
except Exception as e:
    print(f'Error: {e}')


##############################################################################
#
# 13. Write a Python program to copy the contents of a file to another file.
#
next_uppg(13)

try:
    with p.open(mode='r') as f, q.open(mode='w') as o:
        for line in f:
            o.write(line)
            prints(f'copied {line.rstrip(nl)} from '
                   f'{p.name} to {q.name}')
except Exception as e:
    print(f'error copying from text-file to copy-file: {e}')


##############################################################################
#
# 16. Write a Python program to assess if a file is closed or not.
#
next_uppg(16)

# for file-objects previously opened with python
prints(f'{f.closed}')

# This doesn't work well for files that have not been opened...
prints('is the file \'sql-exercises.sql\' closed?')
try:
    file = Path('sql-exercises.sql')
    prints(f'{file._closed}')  # mypy does not see this method? because of _ ?
except Exception as e:
    print(f'Error: {e}')

# files that are open by other processes are not accounted for.

# it is possible to check if another process has a file open in a locked state
# by simply trying to open it, you'll get an error.


##############################################################################
#
# 17. Write a Python program to remove newline characters from a file.
#
next_uppg(17)

try:
    with p.open(mode='r') as f:
        lines = [line for line in f]
except Exception as e:
    print(f'Error: {e}')
else:
    try:
        with p.open(mode='w') as o:
            for i, line in enumerate(lines):
                o.write(line.rstrip(nl))
                prints(f'removed newline from line {i + 1}'
                       f': `{line.rstrip(nl)}` in {p.name}')
    except Exception as e:
        print(f'Error: {e}')
