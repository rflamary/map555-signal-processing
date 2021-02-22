#!/usr/bin/python

import glob


title_remove='<h1>MAP555 : Signal Processing </h1>'


def file_replace(fname,str1,str2):

    with open(fname,'r') as reader:

        new=[]

        for line in reader.readlines():

            new.append(line.replace(str1,str2))

    with open(fname,'w') as reader:

        reader.writelines(new)

    


def main():

    lst_nodes=glob.glob('node-*.html')

    def key(txt):
        return int(txt.split('-')[1].split('.')[0])
    lst_nodes.sort(key=key)

    #print(lst_nodes)

    for f in lst_nodes:
        print(f)
        file_replace(f,title_remove,'<h1></h1>')



if __name__ == "__main__":
    main()

