# seaWAS

# Control Flow

### `web.py`

`web.py` is a selenium script that uploads `fasta` files into the DeepSEA website, waits for the analysis to 
finish and downloads the results archive compressed file (`tar.gz` format). `web.py` makes a few assumption, some of which would have
already been handled for you if you followed the suggetsed pipeline and ran `script.py` to generate the `fasta` files.

#### Seting up Local Environment 

###### Assumption 1

A list of `fasta` filesi located in a folder following the naming convetion of `fasta#{id}.fasta` `#{cancer_type}#{#id}.fasta`.
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
