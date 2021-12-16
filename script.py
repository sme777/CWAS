#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import os
  
# create a parser object
parser = argparse.ArgumentParser(description = "A script to generate fasta files for cancer variants")

parser.add_argument('all_genes_file', type=str,
                    help='The file containing all genes')

parser.add_argument('cancer_file', type=str,
                    help='The file containing cancer variants')

parser.add_argument('num_fastas', type=int,
                    help='The number of fasta files you want split into')
  
# parse the arguments from standard input
args = parser.parse_args()


# In[ ]:


num_divisions = args.num_fastas


# In[1]:


#open text file in read mode
all_genes_file = open(args.all_genes_file, "r")
 
#read whole file to a string
all_genes_data = all_genes_file.read()
 
#close file
all_genes_file.close()


# In[6]:


all_genes_data_array = all_genes_data.split("\n\n\n")



# In[8]:


variant_map = {}


# In[9]:


for variant in all_genes_data_array:
    variant_array = variant.split(' ')
    variant_name = variant_array[0][1:]
    variant_map[variant_name] = variant


# In[11]:


#open text file in read mode
cancer_file = open(args.cancer_file, "r")
 
#read whole file to a string
cancer_data = cancer_file.read()
 
#close file
cancer_file.close()


# In[13]:


cancer_array = cancer_data.split("\n")


# In[15]:


cancer_array = cancer_array[1:]


# In[21]:


cancer_gene_list = []


# In[22]:


for cancer_gene in cancer_array:
    cancer_gene_array = cancer_gene.split(',')
    cancer_gene_name = cancer_gene_array[0]
    if cancer_gene_name in variant_map:
        cancer_gene_info = variant_map[cancer_gene_name]
        cancer_gene_list.append(cancer_gene_info)


# In[ ]:


if not os.path.exists('fasta_files'):
    os.mkdir('fasta_files')
    print("Directory " , 'fasta_files' ,  " Created ")
else:    
    print("Directory " , 'fasta_files' ,  " already exists")


# In[27]:


big_fasta = open('fasta_files/big_fasta.fasta', 'w')
for cancer_gene in cancer_gene_list:
    big_fasta.write(cancer_gene + '\n\n')
big_fasta.close()



# In[29]:


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  
# How many elements each
# list should have
n = num_divisions
cancer_lists = list(divide_chunks(cancer_gene_list, n))


# In[ ]:


list_num = 0

for l in cancer_lists:
    fasta = open('fasta_files/fasta' + str(list_num) + '.fasta', 'w')
    for cancer_gene in l:
        fasta.write(cancer_gene + '\n\n')
    fasta.close()
    list_num += 1
    

