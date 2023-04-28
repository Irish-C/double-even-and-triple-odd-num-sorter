# import module
import PySimpleGUI as sg
import os
import pyperclip
import time
import sys

# Define loading function bar
def show_loading_bar():
    loading_layout = [    
        [sg.Text('Loading...', font=('Helvetica', 14))],
        [sg.ProgressBar(10, orientation='h', size=(20, 20), key='progressbar')],
        [sg.Button('Cancel')]
    ]

    # Create a loading window
    loading = sg.Window('Loading...', loading_layout)
    loading.finalize()

    # Update the progress bar until the loop is interrupted by a cancel event or the progress bar is complete
    for i in range(10):
        event, values = loading.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        loading['progressbar'].UpdateBar(i+1)
        time.sleep(0.1)
    
    # Close the show_loading_bar function
    loading.close()

# Define the PySimpleGUI layout for initiating a file
layout = [
    [sg.Text("Hi! I'm here to process your selected file and manipulate numbers within it.")],
    [sg.Text("Select a file to process:")],
    [sg.Input(), sg.FileBrowse()],
    [sg.Text("", size=(50, 1), key="file_path")],
    [sg.Button("Process File"), sg.Button("Exit")]
] 

# Create the PySimpleGUI window
window = sg.Window("Odd-Even Number Manipulator", layout)

# Create a loop to process events and update the GUI
while True:
    event, values = window.read()

    # If the user clicks the "Exit" button or closes the window, exit the loop
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break   

    # If the user clicks the "Process File" button, execute the file processing
    if event == "Process File":

        #Show loading bar
        show_loading_bar()

        # Open the selected file in read mode
        with open(values[0], "r") as num_file:
            content = num_file.read()

        # Split the contents into a list of integers
        numbers = [int(i) for i in content.split()]

        # Initialize two empty lists to store the doubled even and tripled integers integers
        doubled_int = []
        tripled_int = []

        # Sort each integer into the appropriate list based on parity
        for num in numbers:
            if num % 2 == 0:
                squared_num = num**2
                doubled_int.append(str(squared_num))
            else:
                cubed_num = num**3
                tripled_int.append(str(cubed_num))

        # Create a string to display the squared integers
        doubled_text = "SQUARED EVEN INTEGERS\n\n" + "\n".join(doubled_int)

        # Create a string to display the cubed integers
        tripled_text = "TRIPLED ODD INTEGERS\n\n" + "\n".join(tripled_int)

        # Update the file path text element with the selected file path
        window["file_path"].update(values[0])

        # Create a PySimpleGUI pop-up window to display the output
        output_layout = [
            [sg.Multiline(doubled_text, size=(30, 20)), sg.Multiline(tripled_text, size=(30, 20))],
            [sg.Button("Save File"), sg.Button("OK")],
        ]
        output_window = sg.Window("Output", output_layout)

        # Wait for the user to close the output window
        while True:
            event, values = output_window.read()

            #If the user clicks the "Button", exit the loop
            if event == sg.WINDOW_CLOSED or event == "OK":
                break

            # If the user clicks the "Save File" button, write the output to a file
            if event == "Save File":   

                # Get the current working directory
                cwd = os.getcwd()

                # Specify the full file paths for the squared and cubed files
                doubled_file = os.path.join(cwd, "double.txt")
                tripled_file = os.path.join(cwd, "triple.txt")

                # Update the file path text element with the selected file path
                window["file_path"].update(values[0])

                # Open and Write the squared integers to the file
                with open("double.txt", "w") as num_file:
                    num_file.write("SQUARED EVEN INTEGERS\n")
                    for num in doubled_int:
                        num_file.write(str(num) + "\n")

                # Open and write the cubed integers to the file
                with open("triple.txt", "w") as num_file:
                    num_file.write("CUBED ODD INTEGERS\n")
                    for num in tripled_int:
                        num_file.write(str(num) + "\n")

                # Define the PySimpleGUI layout for the "File Saved" window
                file_saved_layout = [
                    [sg.Text("File saved successfully!", key ="saved")],
                    [sg.Button("OK")]
                ]

                # Create the PySimpleGUI window for the "File Saved" message
                file_saved_window = sg.Window("File Location", file_saved_layout)

                # Wait for the user to close the file saved window
                while True:
                    file_event, values = file_saved_window.read()
                    if file_event in (sg.WINDOW_CLOSED, "OK"):
                        break

                # Define the PySimpleGUI layout for file location
                visit_layout = [
                    [sg.Text("File saved successfully!")],
                    [sg.Text("The files are located in the following directory:"), sg.Button('Copy Doubled Even'), sg.Button('Copy Tripled Odd')],
                    [sg.Text("", size=(80,1), key='filepath')],
                    [sg.Button("Visit Save Files", key="visit"), sg.Button("Exit")]
                ]
                
                # Create the PySimpleGUI window for file location
                visit_window = sg.Window('File Location', visit_layout)

                # Event loop to handle PySimpleGUI events for file location window
                while True:
                    visit_event, visit_values = visit_window.read()

                    # If the user selects "exit" button or exit window 
                    if visit_event == sg.WIN_CLOSED or visit_event == "Exit":
                        break

                    # If the user selects 'Copy Cubed Even' button to copy its file path
                    elif visit_event == 'Copy Doubled Even':
                        path = os.path.dirname(os.path.abspath(__file__))
                        filepath = os.path.join(path, "double.txt")
                        pyperclip.copy(filepath)
                        sg.Popup('File path copied to clipboard!')
                        continue

                    # If the user selects 'Copy Cubed Odd' button to copy its file path
                    elif visit_event == 'Copy Tripled Odd':
                        path = os.path.dirname(os.path.abspath(__file__))
                        filepath = os.path.join(path, "triple.txt")
                        pyperclip.copy(filepath)
                        sg.Popup('File path copied to clipboard!')
                        continue
                    # If the user selects "visit" button, 
                    elif visit_event == 'visit':
                        # Open the directory where the files were saved
                        os.startfile(cwd)
                        break

                # Close the file saved window
                file_saved_window.close()
                # Close the output window
                visit_window.close()

        # Close the output window
        output_window.close()

# Close the main window
window.close()
#Exit the system
sys.exit()