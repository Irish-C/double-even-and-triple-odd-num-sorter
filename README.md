# double-even-and-triple-odd-num-sorter
A python method that reads source text file "integers.txt" that contains 20 integers. Then, integers are separated into two: The first output file "double.txt" contains square of even numbers and the second file is "triple.txt" contains cube of odd numbers.

## Installation
To run the program, you'll need to have [Python 3](https://www.python.org/downloads/) installed on your computer. <br/>
>**Note: This program works only for windows os.**
<br/>

I used [VS Code](https://code.visualstudio.com/download) to create and run the program.

## Dependencies
The script requires the following Python packages:

* PySimpleGUI
* pyperclip
<br/>

```pip install PySimpleGUI pyperclip```

## How the code works
1. Clone the repository or download the manipulate_integers.py and integers.txt files.
2. Open a terminal and navigate to the directory containing the script:
``cd /path/to/directory``
3. Run the script using python:
``python manipulate_integers.py``
4. When prompted, use the "Browse" button to select the file to process.
5. To sort the odd and even integers in the file, click the "Process File" button.
6. While the script is processing the file, a loading bar will show.
7. When the processing is finished, the even and odd numbers that has been doubled and tripled will be shown in separate text boxes, respectively. By pressing the "Save File" option, you can save them as independent text files. However, if you click "OK" the file 
9. Click the "Copy Doubled Even" or "Copy Tripled Odd" buttons to transfer the contents of the even or odd text boxes to the clipboard.
10. Click the "Exit" button or close the window to exit the script.
