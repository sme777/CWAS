import tarfile
import os
import argparse

def unzip_file(input_file):
    with tarfile.open(input_file, 'r') as zip_obj:
        list_of_filenames = zip_obj.getnames()

        for file_name in list_of_filenames:
            if file_name.endswith('.tsv'):
                zip_obj.extract(file_name, output_folder_name)


def unzip_dir(input_dir):
    all_files = os.listdir(input_dir)
    for f in all_files:
        unzip_file(input_dir + "/" + f)


def merge_tsvs():
    all_files = os.listdir(output_folder_name)
    with open(output_file_name, 'a') as single_file:
    	first_tsv = True
    	for tsv in all_files:
    	    if tsv == output_file_name:
    	        pass
    	    else:
    	        header = True
    	        for line in open(output_folder_name + "/" + tsv, 'r'):
    	            if first_tsv and header:
    	                single_file.write(line)
    	                first_tsv = False
    	                header = False
    	            elif header:
    	                header = False
    	            else:
    	                single_file.write(line)
    single_file.close()

parser = argparse.ArgumentParser()
parser.add_argument('folder', type=str, help='Input Folder with Compressed Files')
parser.add_argument('--cancer', type=str, help='The Name of Cancer for Generating Output TSV')
args = parser.parse_args()


output_folder_name = "temp_tsv/"
output_file_name = "merge.tsv" if args.cancer == None else args.cancer + "_merge.tsv" 
input_folder = args.folder
unzip_dir(input_folder)
merge_tsvs()

