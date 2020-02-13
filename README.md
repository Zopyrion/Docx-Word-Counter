# Docx Word Counter
Program to help count multiple docx files and visualize how many words are written everyday.

Gives the word count of every docx file under current path. Writes any increase in wordcount to a textfile which keeps track of progress.


### Usage
```
python main.py
```
or run executable.

### Output

Example directory structure.
```
current_path/
├── css/
│   ├── file1
│   └── file2
├── @progress.txt
├── word0.docx
├── word1.docx
├── word2.docx
├── bootstrap.js
└── textfile.txt
```
Stdout
```
word0.docx: 120
word1.docx: 50
word2.docx: 0
--------------
Total: 170
```

Textout in progress.txt
```
170
2018-01-01: 100
2018-01-02: 10
2018-01-03: 60
```
