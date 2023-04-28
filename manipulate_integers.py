# import module
import PySimpleGUI as sg
import os
import pyperclip
import time

# Define loading function bar

    # Update the progress bar until the loop is interrupted by a cancel event or the progress bar is complete
    
    # Close the show_loading_bar function

# Define the PySimpleGUI layout for initiating a file

# Create the PySimpleGUI window

# Create a loop to process events and update the GUI

    # If the user clicks the "Exit" button or closes the window, exit the loop   

    # If the user clicks the "Process File" button, execute the file processing

        #Show loading bar

        # Open the selected file in read mode

        # Split the contents into a list of integers

        # Initialize two empty lists to store the doubled even and tripled integers integers

        # Sort each integer into the appropriate list based on parity

        # Create a string to display the squared integers

        # Create a string to display the cubed integers

        # Update the file path text element with the selected file path

        # Create a PySimpleGUI pop-up window to display the output

        # Wait for the user to close the output window

            #If the user clicks the "Button", exit the loop

            # If the user clicks the "Save File" button, write the output to a file

                # Get the current working directory

                # Specify the full file paths for the squared and cubed files

                # Update the file path text element with the selected file path

                # Open and Write the squared integers to the file

                    # Open and write the cubed integers to the file
                
                # Define the PySimpleGUI layout for the "File Saved" window

                # Create the PySimpleGUI window for the "File Saved" message

                # Wait for the user to close the file saved window


                # Define the PySimpleGUI layout for file location
                
                # Create the PySimpleGUI window for file location

                # Event loop to handle PySimpleGUI events for file location window

                    # If the user selects "exit" button or exit window 

                    # If the user selects 'Copy Even' button to copy its file path

                    # If the user selects 'Copy Odd' button to copy its file path

                        # Open the directory where the files were saved

                # Close the file saved window

                # Close the output window

        # Close the output window

# Close the main window