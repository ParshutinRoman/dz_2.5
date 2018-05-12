import os
import subprocess

source = 'Source'
result = 'Result'
files = [f for f in os.listdir(source)]
if not os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), result)):
    os.mkdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), result))


for file in files:
    inp = os.path.join(os.path.abspath(os.path.dirname(__file__)), source, file)
    output = os.path.join(os.path.abspath(os.path.dirname(__file__)), result, file)
    subprocess.run(['convert.exe', inp, '-resize', '200', output])
