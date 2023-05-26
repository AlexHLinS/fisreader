# fisreader
Tool to work with F-CON iS log files
# About
A lot of exported JDM cars has piggy-back ECU F-CON iS prodused by HKS company.
Since this ECU has no free software to tuning it up, I've start to make own utils to resolve this problem.


# Description
fisreader.py - tool to convert ECU F-CON iS datalog files to CSV: Programm get file name via command line and extract log data from it.

Usage: python fisreader.py datalogfilename.fis

# Dependencies 

Libs you're needed: 
- sys 
- csv

Also yor're also need to download this files from repo: 
- paramnames.py 
- fi_calculations.py

# Installations
```git clone https://github.com/AlexHLinS/fisreader.git```

```cd fisreader```

```python fisreader.py datalogfilename.fis```

where datalogfilename.fis is datalog file in F-CON iS log files format

# TODO list:

- [X] Tool for converting iS PowerWriter files to CSV 
- [X] Tool for getting password from ECU
- [ ] Tool for reading/writing ECU calibrations to/from file
- [ ] Tool for editing ECU calibration's files
- [ ] Tool for ECU online calibration

