import re
string = "Th@#$% at is a 32264_bha \n ext1c test \\ string. \\tThismn all is a 32264bha 1c test string"

print('is' in string)
print(string.find('is'))
print(string.index('is'))

print(re.search('is', string))
print(re.search('[123][abc]', string))
print(re.search('[0-9]{5}[abh]{2,3}', string))
print(re.search('^This', string))
print(re.search('Th..', string))
print(re.search(r'\.', string))


matched = re.search(r'\\', string)
print(matched.group(0))
print(re.search('\\\\', string))

print(re.search('Th.{4} ', string))
print(re.search('Th.*? ', string).group(0))
print(re.search('Th.+ ', string).group(0))
print(re.search('Th.+? ', string).group(0))
print(re.findall('Th.+? ', string))
print(list(re.finditer('Th.+? ', string)))

match_instace = re.search('Th.+? ', string)

# \w = [0-9a-zA-Z_]
# \W = [^0-9a-zA-Z_]
print(re.search('\w{7}', string))
print(re.search('\W+', string).group(0))
# \d [0-9]
# \D [^0-9]
# \s \S
print(re.findall('\w+?\s', string))
print(re.findall('\s\w+?\s', string))
print(re.search('([1-9]\w)+?', string).group(1))

compiled_reg = re.compile('\w+?\s')
print(re.search('.*', string, re.DOTALL))

# compiled_reg.finditer()
# []
# '1a'
# '1b'
# '1c'
# '2a'
# ..
# '3c'


doc_string = """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl. repl can be either a string or a callable
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used."""


print(*map(lambda x: x.strip(), re.findall('.*?\.', doc_string, re.DOTALL)), sep='\n')
print(*map(lambda x: x.strip(), re.findall('(?<=\.)\s+?\w+?(?=\s)', doc_string, re.DOTALL)), sep='\n')
print(re.findall('e$', doc_string, re.MULTILINE))

print(*re.split('[,.;]', doc_string), sep='\n')