import sys
from io import StringIO

original_print = sys.stdout

sys.stdout = StringIO()
y = sys.stdout

print('Yea')
print('U know')

sys.stdout = original_print
print(y.getvalue())