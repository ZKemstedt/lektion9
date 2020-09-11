# Övningar 1-t.o.m 7, 16 samt 17
# Övningar 8-13 valfria
from pathlib import Path
from sys import argv
from random import randint


SILENT = False


def next_uppg(i: int = 0, skip: bool = False) -> None:
    """uppg seperator function

    description:
        Prints some spacing and a header inbetween each
        exercise user has to press enter to go to the next exercise
    params:
        i :int: the uppgift identifier, defaults to 0
        skip :bool: whether to skip waiting for the user, defaults to False
    """
    if SILENT:
        return
    if not skip:
        _ = input('press enter key to continue...')
    if i:
        title = f'\t\t  Uppgift {i}'
    else:
        title = '~ Finding path and touching your files... (in a lewd way) ~'
    text = (f"""
\n================================================
{title}
""")                # This is a mess...
    print(text)     # See? this is why I prefer my normal way of doing it.


next_uppg(0)

if len(argv) > 1:
    try:
        if 'silent'[0:len(argv) - 1] == argv[1]:
            SILENT = True
    except Exception:
        pass

try:
    p = Path(argv[0].replace(".py", "-text.txt"))
    p.touch(exist_ok=True)
except Exception as e:
    print(f'Error: {e}')
    print('Unable to touch file, aborting.')
    exit()


# 1. Write a Python program to read an entire text file.
next_uppg(1)

try:
    with p.open(mode='r') as f:
        print(f'   ~~ contents of {p.name} ~~')
        for i, line in enumerate(f):
            print(f'{i + 1} {line}', end='')
except Exception as e:
    print(f'Error: {e}')


# 2. Write a Python program to read first n lines of a file.
next_uppg(2)

n = 17  # sample value
try:
    with p.open(mode='r') as f:
        print(f'   ~~ contents of {p.name} ~~')
        for i, line in enumerate(f):
            if i == n:
                break
            print(f'{i + 1} {line}', end='')
except Exception as e:
    print(f'Error: {e}')


# 3. Write a Python program to append text to a file and display the text.
next_uppg(3)

try:
    with open(argv[0]) as i:  # we're gonna append lines from this file.
        with p.open(mode='a') as f:
            f.seek(0, 2)
            for _ in range(10):  # 10 lines is enough.
                word = i.readline()
                f.write(word)
                if not SILENT:
                    print(f' wrote {word} to {f.name}')
except Exception as e:
    print(f'Error: {e}')


# 4. Write a Python program to read last n lines of a file.
next_uppg(4)

# using same n as defined in # 2.
lines = []
try:
    with p.open(mode='r') as f:
        for i in range(n):
            f.seek(-i, 2)
            lines.append(f'{f.readline()}') # todo: linecounter ?
except Exception as e:
    print(f'Error: {e}')
else:
    for i, line in enumerate(lines):
        if not SILENT:
            print(f'line {len(lines) - i}: {line}', end='')


# 5. Write a Python program to read a file line by line and
#   store it into a list.
next_uppg(5, skip=True)

lines = []
try:
    with p.open(mode='r') as f:
        for line in f:
            lines.append(line)
except Exception as e:
    print(f'Error: {e}')
else:
    if not SILENT:
        for i, line in enumerate(lines):
            print(f'line {i + 1}: {line}', end='')


# 6. Write a Python program to read a file line by line store
#   it into a variable.
next_uppg(6, skip=True)

lines = []
try:  # yeah, it's actually just the same thing...
    with p.open(mode='r') as f:
        for line in f:
            lines.append(line)
except Exception as e:
    print(f'Error: {e}')
else:
    if not SILENT:
        for i, line in enumerate(lines):
            print(f'line {i + 1}: {line}', end='')


# 7. Write a Python program to read a file line by line store it into an array.
next_uppg(7, skip=True)

lines = []
try:  # okay this is a bit silly...
    with p.open(mode='r') as f:
        for line in f:
            lines.append(line)
except Exception as e:
    print(f'Error: {e}')
else:
    if not SILENT:
        for i, line in enumerate(lines):
            print(f'line {i + 1}: {line}', end='')


# 8. Write a python program to find the longest words.
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

    if not SILENT:
        print('The largest word is: ... ', end='')
        print(big_word)


# 9. Write a Python program to count the number of lines in a text file.
next_uppg(9)

try:  # Have I seen this code before?
    with p.open(mode='r') as f:
        if not SILENT:
            print(f'{p.name} has {len([line for line in f])} lines.')
except Exception as e:
    print(f'Error: {e}')


# 10. Write a Python program to count the frequency of words in a file.
next_uppg(10)
n = '\n'

try:
    words = {}
    lines = []
    with p.open(mode='r') as f:
        for line in f:
            lines.append(line)
except Exception as e:
    print(f'Error: {e}')
else:
    for line in lines:
        for word in line.split(' '):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    if not SILENT:
        for word, count in words.items():
            print(f'`{word.rstrip(n)}` appeared `{count}` times.')


# 11. Write a Python program to get the file size of a plain file.
next_uppg(11)

# method 1
size = p.stat().st_size
if not SILENT:
    print(f'filesize: {size}')


# method 2
def file_len(fname):
    with open(fname) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


if not SILENT:
    print(f'filesize: {file_len(p)}')


# 12. Write a Python program to write a list to a file.
next_uppg(12)


lines = [str(randint(0, 100)) + '\n' for _ in range(20)]

try:
    with p.open(mode='w') as f:
        for i in lines:
            f.write(i)
            if not SILENT:
                print(f'wrote {i.rstrip(n)} to {p.name}')

except Exception as e:
    print(f'Error: {e}')


# 13. Write a Python program to copy the contents of a file to another file.
next_uppg(13)

file_out = Path(argv[0].replace('.py', '-copy.txt'))
clear = False
if file_out.exists():
    clear = True
file_out.touch(exist_ok=True)

try:
    with file_out.open(mode='w') as i:
        with p.open(mode='r') as f:
            if clear:
                i.truncate()
                if not SILENT:
                    print(f'truncated {file_out.name}')
            for line in f:
                i.write(line)
                print(f'copied {line.rstrip(n)} from '
                      f'{p.name} to {file_out.name}')
except Exception as e:
    print(f'Error: {e}')


# 16. Write a Python program to assess if a file is closed or not.



# 17. Write a Python program to remove newline characters from a file.
