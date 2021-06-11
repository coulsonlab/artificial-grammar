from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
import pandas as pd
from psychopy import sound

sounds_dir_map = {
    'words': '00_words',
    'drums': '01_drums',
    'silences': '02_silences'
}

silences_file_map = {
    'silence_intersequence_250ms': 'X_silence-intersequence-250ms.wav',
    'silence_interblock_1250ms': 'X_silence-interblock-1250ms.wav'
}

def create_sequence(protocol, sound_type, sounds_dir, filename_map):
    protocol_file = filename_map[protocol]
    sound_map_file = filename_map[sound_type]
    
    protocol_df = pd.read_csv(protocol_file)
    sound_map_df = pd.read_csv(sound_map_file, sep=';', index_col=False)
    sound_map_df.set_index('stimulus_id', inplace=True)
    
    sequence = []
    for idx, row in protocol_df.iterrows():
        stim_id = row['stimulus_id']
        
        file_path = sounds_dir + '/'
        if 'silence' in stim_id:
            file_path += sounds_dir_map['silences'] + '/'
            file_path += silences_file_map[stim_id]
        else:
            file_path += sounds_dir_map[sound_type] + '/'
            file_path += sound_map_df.loc[stim_id]['file_name']
        package = {
            'row': row,
            'file_path': file_path,
            'full_label': sound_map_df.loc[stim_id]['full_label']
        }
        sequence.append(package)
        
    return sequence