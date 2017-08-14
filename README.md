# underthesea TreeBank

This repository contains Vietnamese Treebank. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

## Corpus Summary

* 472 documents
* 9176 sentences

## Usage

On Linux

```
git clone git@github.com:magizbox/underthesea.treebank.git
cd underthesea.treebank
git submodule init
git submodule update

conda env create -f environment-linux.yml
chmod u+x run.sh
./run.sh
```

On Windows

```
git clone git@github.com:magizbox/underthesea.treebank.git
git submodule init
git submodule update

cd underthesea.treebank
conda env create -f environment.yml
.\run.bat
```
