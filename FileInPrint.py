# File parameter in print() function

import io

dummy_file = io.StringIO()

print('Hello World!!', file=dummy_file)

print(dummy_file.getvalue())