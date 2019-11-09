import os
import subprocess
import unittest
mock
# from tic_tac_toe import X_0

p = subprocess.Popen(
    ['python3', './tic_tac_toe.py'], stdin=subprocess.PIPE,
    stdout=subprocess.PIPE, universal_newlines=True
)
out, err = p.communicate('A')
print(p.stdout, '++')
p.stdin.write('A')
p.stdin.write('B')
# while out:
#     out = p.stdout.readline()
#     print(out, end='')

print('dd\n', '\b' + out, err, '---')
# out, err = p.communicate()
p.stdin.write('A')
p.stdin.write('B')
# print('asdfdddddddddd')
# out, err = p.communicate("B\n")
# out, err = p.communicate("0\n")
# out, err = p.communicate("3\n")
# out, err = p.communicate("1\n")
# out, err = p.communicate("4\n")
# out, err = p.communicate("2\n")
print('begin')
print(out, '***')

# p=subprocess.Popen("test.exe", stdin =subprocess.PIPE, stdout =subprocess.PIPE, stderr =subprocess.PIPE )
# p.communicate("текст от пользователя \n")

# import subprocess
# import sys
# child = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
# while True:
#     out = child.stderr.read(1)
#     if out == '' and child.poll() != None:
#         break
#     if out != '':
#         sys.stdout.write(out)
#         sys.stdout.flush()

# class TestX_0(unittest.TestCase):
#     def test_X_0(self):
#         name1 = 'A'
#         name2= 'B'
#         expected_output = '''             |     |
#           0  |  1  |  2
#         _____|_____|_____
#              |     |
#           3  |  4  |  5
#         _____|_____|_____
#              |     |
#           6  |  7  |  8
#              |     |   '''
#         with os.popen(f"echo '{name1}' | python3 tic_tac_toe.py") as o:
#             output = o.read()
#         with os.popen(f"echo {name2}' | python3 tic_tac_toe.py") as o:
#             output = o.read()
#         output = output.strip()
#         self.assertEqual(output, expected_output)


# if __name__ == '__main__':
#     unittest.main()
