#!/usr/bin/python

import glob
import re

title_remove='<h1>MAP555 : Signal Processing </h1>'
link_bib='<a href="{bibfile}#r{i}">{bibtxt}</a>'
div_bib='<a name="r{i}">{txt}</a>'


def file_replace(fname,str1,str2):

    with open(fname,'r') as reader:

        new=[]
        for line in reader.readlines():
            new.append(line.replace(str1,str2))

    with open(fname,'w') as reader:

        reader.writelines(new)

def file_replace_list(fname,lst1,lst2):

    with open(fname,'r') as reader:
        new=[]
        for line in reader.readlines():
            for str1,str2 in zip(lst1,lst2):
                #print(str1,str2)
                line=line.replace(str1,str2)
            new.append(line)

    with open(fname,'w') as reader:
        reader.writelines(new)


def remove_titles(lst_nodes):

    for f in lst_nodes:
        print('Remove title from: ',f)
        file_replace(f,title_remove,'<h1></h1>')

def find_biblio(lst_nodes):
    res=''
    # 
    prog = re.compile('<h3 id="autosec-\d+">Bibliography</h3>')
    for f in lst_nodes:
         with open(f,'r') as reader:
            for line in reader.readlines():
                if prog.match(line) is not None:
                    res=f
    return res

def extract_biblio(fname):
    lst_bib=[]
    # return biblio items
    prog = re.compile('\[.+, \d+\]')
    with open(fname,'r') as reader:
        for line in reader.readlines():
            lst_bib.extend(prog.findall(line))
    return lst_bib

def add_link_scholar(fname):
    
    with open(fname,'r') as reader:
        new=[]
        for line in reader.readlines():
            if line.startswith('['):
                txt=line.split(']&#x2003; ')[1]
                txt=txt.replace('<i>','')
                txt=txt.replace('</i>','')
                line=line+' <a href="https://scholar.google.fr/scholar?q={}">[Google Scholar]</a>.'.format(txt)
            new.append(line)

    with open(fname,'w') as reader:
        reader.writelines(new)



def main():

    lst_nodes=glob.glob('node-*.html')

    def key(txt):
        return int(txt.split('-')[1].split('.')[0])
    lst_nodes.sort(key=key)

    #remove tje h1 titles (but keep the h1 for better space)
    remove_titles(lst_nodes)

    biblio_file=find_biblio(lst_nodes)
    print('Biblio file :', biblio_file)
    
    lst_bib=extract_biblio(biblio_file)
    print('Biblio :', lst_bib)
    
    # replace all 
    lst_bibnames=[s[1:-1] for s in lst_bib]
    
    lst_bibdiv=[div_bib.format(i=i,txt=s[1:-1]) for i,s in enumerate(lst_bib)]
    
    lst_biblinks=[link_bib.format(bibfile=biblio_file,bibtxt=s[1:-1],i=i) for i,s in enumerate(lst_bib)]
    print(lst_bibnames)
    
    file_replace_list(biblio_file,lst_bibnames,lst_bibdiv)
    add_link_scholar(biblio_file)
    
    for f in lst_nodes:
        if not f==biblio_file:
            print('Processing biblio in file :', f)
            file_replace_list(f,lst_bibnames,lst_biblinks)

if __name__ == "__main__":
    main()


#%% debug



# tes="""<p>
# [Haykin and Van&nbsp;Veen, 2007]&#x2003; Haykin, S. and Van&nbsp;Veen, B. (2007). <i>Signals and systems</i>. John Wiley &amp; Sons.
# </p>
# </li>
# <li>
# <p>
# [Oppenheim et&nbsp;al., 1997]&#x2003; Oppenheim, A.&nbsp;V., Willsky, A.&nbsp;S., and Nawab, S.&nbsp;H. (1997). Signals and systems prentice hall. <i>Inc., Upper Saddle River, New Jersey</i>, 7458.
# </p>
# <p>"""

# print(prog.findall(""))


