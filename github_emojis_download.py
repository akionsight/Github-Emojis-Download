import requests
import os
import json


def download_emojis(FOLDER_PATH, EMOJIS_URL, flag=None):
    '''
    download images from the Github Emojis API
    '''
    try:
        os.mkdir(FOLDER_PATH)
    except FileExistsError:
        if flag == 'v':
            print(f'a folder name {FOLDER_PATH} exists, overwriting file')
    emojis = requests.get(EMOJIS_URL).json()
    for emoji in emojis.keys():
        if os.path.exists(FOLDER_PATH + '\\' + emoji):
            print(emoji)
            continue
        if flag == None:
            file = open(FOLDER_PATH + "\\" + emoji + '.png', 'wb')
            file.write(requests.get(emojis[emoji]).content)
            file.close()
            print(emoji)
        if flag == 'v':
            file =  open(FOLDER_PATH + "\\" + emoji + '.png', 'wb')
            print(f'file opened for emoji :- {emoji}')
            con = requests.get(emojis[emoji]).content
            print('requesting server for emoji')
            file.write(con)
            print('writing to emoji file')
            file.close()
            print('closing file, saving')
            print('\n ---x--- \n')
        if flag == 'q':
            file = open(FOLDER_PATH + "\\" + emoji + '.png', 'wb')
            file.write(requests.get(emojis[emoji]).content)
            file.close()
        


if __name__ == "__main__":
    FOLDER = 'emojis' ## enter you folder here
    EMOJIS_URL = 'https://api.github.com/emojis' ## you might change this, but it might not work then
    download_emojis(FOLDER, EMOJIS_URL, flag=None) ## the flags available are verbose('v') and quiet('q') the normal mode is selected by default




