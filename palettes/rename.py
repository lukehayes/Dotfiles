# Script that will look through all of the files in this folder and prepend
# "lolspec-" to the original name of the file if it doesn't exist.
import os

for root, _, files in os.walk("."):
    for filename in files:
      if not filename.startswith('lolspec-'):
        os.system("mv {0} lolspec-{0}".format(filename))
      else:
        print("Ignoring {}".format(filename))

# Revert these two files back to their original names.
os.system("mv lolspec-default.ase default.ase")
os.system("mv lolspec-rename.py rename.py")
