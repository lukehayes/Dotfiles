import os
root_dir = "."
file_set = set()

for dir_, _, files in os.walk(root_dir):
    for filename in files:
      if not filename.startswith('lolspec-'):
        os.system("mv {0} lolspec-{0}".format(filename))
      else:
        print("Ignoring {}".format(filename))

        # os.system("echo {0} lolspec-{0}".format(file_name))

os.system("mv lolspec-default.ase default.ase")
os.system("mv lolspec-rename.py rename.py")
