from validator import *
import os
import  sys

input_rel_path = '../../../lib/src/Localization/Localization.txt'

current_directory=os.getcwd()
directory_path=os.path.join(current_directory,__file__)
path = os.path.dirname(directory_path)
input_path=os.path.join(path,input_rel_path)

output_directory=os.path.join(path,"..\\bin\\")
output_path=os.path.join(output_directory,"untranslated_keys.csv")
if not os.path.exists(output_directory):
   os.makedirs(output_directory);

encode=detecting_encoding(input_path)
if encode == "UTF-16":
   filter(input_path, output_path)
else:
   sys.exit("utf is not utf 16")
