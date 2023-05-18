from validator import *
import os
import  sys



dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.txt')


current_directory=os.getcwd()
directory_path=os.path.join(current_directory,__file__)
path = os.path.dirname(directory_path)
input_path=os.path.join(path,filename)

# output_directory=os.path.join('test.txt')
output_path=os.path.join(dirname,"untranslated_keys.csv")
# if not os.path.exists(output_directory):
#
#  os.makedirs(output_directory);

encode=detecting_encoding(input_path)
if encode == "UTF-16":
   filter(input_path, output_path)
else:
   sys.exit("utf is not utf 16")
