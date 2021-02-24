#!/usr/bin/python



def main():
    
    txt=[]
    txt.append("%This file has been generated automatically from notation.tex\n")
    txt.append("%It should not be modified by the users\n\n")
    txt.append("\\begin{warpHTML}\n")
    
    with open('notations.tex','r') as reader:
        for i,line in enumerate(reader.readlines()):
            
            if line=='\n' or line.startswith('%'):
                txt.append(line)
            elif line.startswith(r'\def'):
                cmd=line.split('{')[0].replace(r'\def','')
                cmd_def=line[line.find('{'):-1]
                txt.append("\\CustomizeMathJax{{\\newcommand{{{}}}{{{}}}}}\n".format(cmd,cmd_def))
                print(txt[-1])
            elif line.startswith(r'\newcommand'):
                txt.append("\\CustomizeMathJax{{{}}}".format(line[:-1]))
            else :
                print('Warning line {} not processed : {}'.format(i,line))
    txt.append("\n\end{warpHTML}\n")

    with open('notations_lwarp.tex','w') as reader:
        reader.writelines(txt)  

if __name__ == "__main__":
    main()



