#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from psychopy import gui  # Fetch default gui handler (qt if available)
from psychopy import __version__ # Get the PsychoPy version currently in use

import glob  # for reading file names
import re  # for string splitting

def prompt():
    # Specify fields for dlg as a dict
    info = {'Protocols Folder':'20210601_everything_for_local+unstructured/01_protocols', 
        'PsychoPy Version': __version__,
        'Participant': '',
        'Session Number': 0,
        'Mappings Folder': '20210601_everything_for_local+unstructured/00_wav-mapping',
        'Sounds Folder': '20210601_everything_for_local+unstructured/00_wavs',
        'Logs Folder': 'logs',
        'Trigger Code': True}
    # Use this dict to create the dlg
    infoDlg = gui.DlgFromDict(dictionary=info, 
        title='Artificial Grammar Experiment',
        order=['PsychoPy Version', 'Mappings Folder', 'Sounds Folder', 'Protocols Folder', 'Logs Folder', 'Participant', 'Session Number', 'Trigger Code'],
        tip={'Protocols Folder': 'relative path to folder containing protocols as csv files'},
        fixed=['PsychoPy Version'])  # This attribute can't be changed by the user
    # Script will now wait for the dlg to close...

    if not infoDlg.OK:
        print('User canceled, exiting')
        quit()

    protocols_path = info['Protocols Folder']
    protocols_filepaths = glob.glob(protocols_path + "/*.csv")
    protocols_names = []
    filename_map = {}
    for filepath in protocols_filepaths:
        filepath_split = re.split("/|'\\'", str(filepath))
        filename = filepath_split[-1]
        tokens = re.split("_", filename)
        # 0:    "format2"
        # 1, 2: "all_blocks"
        # 3:    "local" or "unstructured"
        # 4:    "shuffled"
        # 5:    date created (?)
        # 6:    version number
        # 7:    label
        name = tokens[4] + '_' + tokens[7]
        if len(tokens) == 9:
            name += '_' + tokens[8]
        name = name.split('.')[0]
        protocols_names.append(name)
        filename_map[name] = filepath
    
    mappings_path = info['Mappings Folder']
    mappings_filepaths = glob.glob(mappings_path + "/*.csv")
    mappings_names = []
    
    for filepath in mappings_filepaths:
        filepath_split = re.split("/|'\\'", str(filepath))
        filename = filepath_split[-1]
        tokens = re.split("_|-", filename)
        name = tokens[3]
        mappings_names.append(name)
        filename_map[name] = filepath

    selection = {
        'Protocol': protocols_names,
        'Sound Type': mappings_names
    }
    selectionDlg = gui.DlgFromDict(
        dictionary=selection,
        title='Experiment Configuration'
    )

    if not selectionDlg.OK:
        print('User canceled, exiting')
        quit()
        
    return {**info, **selection}, filename_map
