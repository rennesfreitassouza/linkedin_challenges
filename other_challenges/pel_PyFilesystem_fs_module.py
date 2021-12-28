from fs.osfs import OSFS
from os import chdir, getcwd

# https://www.linkedin.com/learning/python-essential-libraries/challenge-pyfilesystem
print("---My challenge solution---")

directory =  "PyFilesystem"
file_type_filter = "*"

chdir(directory)
full_path = getcwd()

with OSFS(".") as myfs:
    totalSize = 0
    for path, info in myfs.walk.info(namespaces=["details"], filter=[file_type_filter]):
        totalSize += info.size
    print(f"'{full_path}' total size of files is: {totalSize} bytes")
