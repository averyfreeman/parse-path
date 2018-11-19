import fileinput

filename = "./tree.txt"
open(filename).read()
print("\n\tReplaced \\ with / and saved as "+ filename + ".posixpath")
with fileinput.FileInput(filename, inplace=True) as file:
    for str in file:
        print(str.replace('\\', '/'), end='')
print("all done")