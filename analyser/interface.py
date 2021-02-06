#! python3
"""
Start of the UI for the analysis tool
TODO - Update UI responses
TODO - Progress bar
TODO - Change layout/window after click of analysis
TODO - Fix Close button
"""
import PySimpleGUI as sg
import film_colour_analyser

sg.theme('DarkAmber')
# All the stuff inside your window.
layout = [[sg.Text('Welcome to the film colour analyser. Please select your film and output destination.')],
          # [sg.Text('Select Film', size=(15, 1)), sg.In(), sg.FileBrowse(file_types=(("AVI/MP4 Files", ["*.mp4", "*.avi"]),), key='file_select')],
          # [sg.Text('Select Output Folder', size=(15, 1)), sg.In(), sg.FolderBrowse(key='folder_select')],
          # [sg.Button('Analyse', key='analyse'), sg.Button('Cancel', key='cancel')]]
          [sg.Text('Select Film', size=(15, 1)), sg.In(), sg.FileBrowse(file_types=(("AVI/MP4 Files", ["*.mp4", "*.avi"]),))],
          [sg.Text('Select Output Folder', size=(15, 1)), sg.In(), sg.FolderBrowse()],
          [sg.Button('Analyse'), sg.Button('Close')]]

# Create the Window
window = sg.Window('Film Colour Analyser v0.1', layout)
# window.Finalize()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        print('Exiting')
        break

    if event == 'Analyse':
        print('Triggered for the following values...')
        print('Film Selected: ' + values[0])
        print('Output Destination: ' + values[1])
        # window['file_select'].update(disabled=True)
        # window['folder_select'].update(disabled=True)
        # window['analyse'].update(disabled=True)
        window.disable()
        analysis = film_colour_analyser.Analyser(values[0], values[1])
        result = analysis.analyse()
        window.enable()
        sg.popup(result)
        # window['file_select'].update(disabled=False)
        # window['folder_select'].update(disabled=False)
        # window['analyse'].update(disabled=False)
        # print(result)

#    print('You entered... but how did I get here? ', values[0])

window.close()
