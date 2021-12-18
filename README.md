# CWAS (cancer-wide association study)

The first script to run is `breakdown.py`, followed by `web.py`, and finally `concat.py`.

# Control Flow
### Setting up `breakdown.py`

`breakdown.py` is a Python script that looks for cancer type specific genes from files downloaded from the COSMIC Cancer Browser and queries a file containing sequences for all genes that the COSMIC Cancer Browser contains in order to generate many smaller files containing the sequences for the genes associated with a specific cancer type.

#### Setting up Local Environment 

###### Assumption 1
The script, the file containing sequences for every gene, and the file containing the genes associated with a specific type of cancer must all be in one common directory.

###### Assumption 2
The file containing sequences for every gene and and the file containing the genes associated with a specific type of cancer must be in .txt format.

### Running `breakdown.py`
The script can be ran with the command `python3 breakdown.py {filename of file containing sequences for all genes} {filename of file containing cancer specific genes} {number of desired sequences per output file}`.
The script will generate a directory `fasta_files` which will contain the many smaller files. 

### Setting up `web.py`

`web.py` is a Python script that uses selenium webdriver to upload `fasta` files into the DeepSEA website, wait for the analysis to 
finish and download the results archive compressed file (`tar.gz` format). `web.py` makes a few assumption, some of which would have
already been handled for you if you followed the suggetsed pipeline and ran `script.py` to generate the `fasta` files.

#### Setting up Local Environment 

###### Assumption 1

A list of `fasta` files is located in a folder following the naming convetion of `fasta#{id}.fasta` `#{cancer_type}#{#id}.fasta`.
To configure between these provide an optional argument `--cancer <cancer-name>` where `<cancer-name>`. For example, if the files
are stored like `bone0.fasta, bone1.fasta, ...` you will need to provide `--cancer bone` as an optional argument. There is no need
to provide any arguments if the names of files are like `fasta#{id}.fasta`.

###### Assumption 2

All fasta files are less than **1 MB** in size. DeepSEA has a cap on the size of uploads which is limited to about ~ **1 MB** or
20,000 lines. To gurantee having file sizes less than **1 MB** we recommend running `script.py` with # of mutations set to <ins>100</ins>.

###### Assumption 3

You have Firefox installed as well as `geckodriver`. If you are on MacOS the command to install `geckodriver` is `brew install geckodriver`.
For GNU/Linux the command is `apt install geckodriver`. It's possible that none of these commands work depending on what tools you have
available on your machine. We recommend chceking out [this stackoverflow post](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path) for troubleshooting.

In the first version, `web.py` only supports Firefox as the webdriver, however, future work will extend to other browsers, and one
can be specified by an optional command like `--webdriver <webdriver-name>`. Primarily, we will focus on headless chrome because
it gives real browser context without the memory overhead of running a full version of Chrome.

###### Assumption 4

We rely on the selenium library to execute the script. Installing `selenium` can be done through `pip`. When running the script
we assume you have insatlled sleenium by running `pip install selenium`. Checkout the `PyPi` for details: https://pypi.org/project/selenium/

### Running `web.py`

The script can be ran with the command python3 web.py --windows {# of  files to run} --folder {the input folder} --path {the output folder}. The script will generate a directory from the output folder name which will contain the output files from DeepSEA.


### Setting up `concat.py`

`concat.py` is a Python script that unzips and extract the `tsv` files from the DeepSEA's output files generated from `web.py`, and concatenates the tables together removing any uncessary column headers. The script takes in one mandatory field for the input folder and an optional `--cancer` flag so the outputs will be named after that caner type.

### Running `concat.py`

The script can be ran with the command `python3 concat.py {folder name containing the compressed DeapSEA files} --cancer {name of the cancer}`.
The script will generate a single file `<caner-name>_merge.tsv` which will contain concatonated `tsv` files for that cancer.
