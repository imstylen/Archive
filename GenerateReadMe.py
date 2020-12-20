from os import listdir
from os import path
from os.path import isfile, join
from os import getcwd

blacklist = ['.git', '.gitattributes', 'README.md', 'GenerateReadMe.py']

def main():
    print("Generating a new readme file...")
    a = Generate(getcwd(),0)
    print(a)
    f = open("README.md","w")
    f.write("Archive  \n")
    f.write("A collection of useful information and code snippets  \n  \n")
    f.write(a)
    f.close()


def Generate(folder_path,indent):
    items = listdir(folder_path)
    line_list = []
    folders = []

    indentstr = ""
    for _ in range(0,indent):
        indentstr += "  "

    for item in items:
        if item in blacklist:
            continue

        this_path = join(folder_path,item)
        if isfile(this_path):
            line_list.append(indentstr + "*" + item + "  \n")
        else:
            folders.append(item)

    buffer = []
    for folder in folders:
        if not str.startswith(folder,"."):


            buffer += indentstr + "*" + folder + "  \n"
            n = (Generate(join(folder_path,folder),indent+1))

            s = ""
            if n != []:
                buffer += s.join(n)

        
    line_list += buffer
    val = "".join(line_list)
    return "".join(line_list)
    
if __name__ == "__main__":

    main()




