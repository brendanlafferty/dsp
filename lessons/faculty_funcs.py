#!/bin/python3

import sys
import os
import tempfile
from pathlib import Path


facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""


#temp_dir = Path(os.environ['data']).parent

#faculty_path = temp_dir / "faculty.csv"

#faculty_path.write_text(facultycsv)
import re
from collections import defaultdict
# Complete the function below.


def count_degrees(csv_file_name):
    degree_dict = defaultdict(int)
    with open(csv_file_name) as fn:
        for line in fn:
            print(line)
            res = re.search('^.*,\s*(.*),.*,.*$', line)
            print(res)
            deg_list = res.group(1).lower().replace('.', '').split(' ')
            print(deg_list)
            for deg in deg_list:
                degree_dict[deg] += 1
            print(degree_dict)
    return degree_dict

def count_titles(csv_file_name):
    title_dict = defaultdict(int)
    with open(csv_file_name) as fn:
        for no, line in enumerate(fn):
            if no:
                res = re.search('^.*,.*,\s*(.*),.*$',line)
                title = res.group(1).lower().replace('.', '')
                title_dict[title] +=1
    return title_dict

def get_emails(csv_file_name):
    emails = []
    with open(csv_file_name) as fn:
        for no, line in enumerate(fn):
            if no:
                res = re.search('^.*,.*,.*,\s*(.*)$',line)
                emails.append(res.group(1))
    return emails

def last_name_dict_assembler():
    last_name_dict = defaultdict(list)
    with open(faculty_path) as fn:
        for no, line in enumerate(fn):
            if no:
                res = re.search('^.*\s(.*),\s*(.*),\s*(.*),\s*(.*)$',line)
                last_name = res.group(1).split(' ')[-1]
                data = [res.group(n) for n in range(2,5)]
                last_name_dict[last_name].append(data)
    return last_name_dict

def get_faculty_dict():
    faculty_dict = {}
    with open(faculty_path) as fn:
        for no, line in enumerate(fn):
            if no:
                res = re.search('^(.*),(.*),(.*),(.*)$', line)
                name = tuple(res.group(1).split(' '))
                data = [res.group(n) for n in range(2, 5)]
                faculty_dict[name] = data
    return faculty_dict

if __name__ == "__main__":
    faculty_path = "./data/faculty.csv"
    print(get_faculty_dict())
#    print(last_name_dict_assembler()['Li'])
#    print(last_name_dict_assembler()['Localio'])
answer = get_faculty_dict()
for key, val in answer.items():
    print('{key},{val}'.format(key=' '.join(key), val=','.join(val)))
    assert '{key},{val}'.format(key=' '.join(key), val=','.join(val)) in facultycsv
assert len(answer) == facultycsv.count('\n')
