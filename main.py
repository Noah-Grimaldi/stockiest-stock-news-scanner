
import PySimpleGUI as sg

import requests

from playsound import playsound as play

goodNews = [

    'phase clinical trial',

    'merge',

    ' ipo ',

    'acquisition',

    'nasdaq',

    'cancer',

    'cells',

    'partnership',

    'equity financing',

    ' deal ',

    'fda approval',

    'trial',

    'eps exceeded'

]

decentNews = [

    'contract award',

    'heart monitor',

    'pardon',

    'collaboration',

    'receives',

    'acquire',

    'funding recipients',

    'agreement'

]

good_sound = 'C:/Users/noah/Downloads/cashregister.mp3'

articleGoodNews = []

articleDecentNews = []

seen = []

stockiestIcon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAALiMAAC4jAXilP3YAAAMsaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iSW1hZ2U6OkV4aWZUb29sIDExLjg4Ij4NCiAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4NCiAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+DQogICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0Pg0KICAgICAgPHRpZmY6WFJlc29sdXRpb24+MzAwLzE8L3RpZmY6WFJlc29sdXRpb24+DQogICAgICA8dGlmZjpZUmVzb2x1dGlvbj4zMDAvMTwvdGlmZjpZUmVzb2x1dGlvbj4NCiAgICA8L3JkZjpEZXNjcmlwdGlvbj4NCiAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyI+DQogICAgICA8eG1wTU06RG9jdW1lbnRJRD5hZG9iZTpkb2NpZDpzdG9jazphZDFkODI1MC1lMmEwLTQ5YjQtYjUyYy1jMTFiNDFkMzBmNmY8L3htcE1NOkRvY3VtZW50SUQ+DQogICAgICA8eG1wTU06SW5zdGFuY2VJRD54bXAuaWlkOjI5MGRiZjZiLWVkYjEtNGQ1ZC05N2JhLTg0M2IzYjRiNDVmMzwveG1wTU06SW5zdGFuY2VJRD4NCiAgICA8L3JkZjpEZXNjcmlwdGlvbj4NCiAgPC9yZGY6UkRGPg0KPC94OnhtcG1ldGE+DQo8P3hwYWNrZXQgZW5kPSJyIj8+/0nfMAAAAnJJREFUOE9NUktIVGEUPv/jzp17Rx2vNj6ayRKLkdJaRUIhFUgSSSXSKlyILdpJLYLZJ+160KJVi2gZCEFQEFRCgaY2oVLi29FpdGSejvO4j79z5zrR/b97OOf8/Od8/3d+Qh4IABC4nI8AMYvVhbWMpx2IwNBJ2gYtASqYEFyABA6C+ren3tFnvuc12WkiAeFwYDkAJ8CAlgNCGK7isPRq8ubC0IUGf73aq78RjAgO/0EICTugV27SB29Hz++5Ofk4F59M1HzV+gE7Y2GGtQ9AGJIatWx+wnitPfFkV0fWLm829xiuGpu28/+7hnMH+xAD/+7nvs7acL55vXXAVLzIz2bMK5SkCjhQZ+NO06yLwjTrKG/YXB3SIB2A8DIkgXcQcmp+8IwbTH0qyTFly2LbslPWx5ao0oRj0E3CR+s9sZ245lVimEWqFd6HIuNDnnCw2gDN/1Bc29JVPCAGfFEwvL5aT51UoMxoWX3fXbWDw3RbxXtd7ETbSaCcMCm6nnwZU7mWXuo9rRAkTGkwM3PFtXj/VptbbQXLBKMg9LzIxgjjQlIvVstjCT/tsNYCmor9k3uFR1cDoZ4jEkqUT5Wyu78WFiGfjGxG9xJxyMWPmRFVBl4qWaViQZaYViWbWDCTDC9uRuMpnExXu//7j+XI1tbsRmZk8DpVFK+bsON3X3yZ+Lm8MBdbmc8ktkUx6VOhqUrkUrGJ3xuzuq+e5s62yI/HptrOXZqRg+TGB4tRnJ8AfX//z7KR3qbCAJeqHG5VGgOUUnN76fZcSJH5u85QurGDDI9b3H6DtpSCAqG2ms5LFuhgSKFu5ZMZOJVTGyiBv5OOB5jzcRz6AAAAAElFTkSuQmCC'

canvas = [sg.theme_background_color(color='#025d93')]

popUp = [sg.popup('The hottest day-trading news typically happens around 9:30 - 10:30 a.m. (ET)', title='NOTICE',
                  no_titlebar=True, background_color='black')]

layout = [

    [sg.Text(text='', text_color='white', font='Courier 20 bold', expand_x=True, justification='center', key='running',
             visible=False)],

    [sg.Multiline(size=(150, 30), key='textbox', no_scrollbar=True, disabled=True)],

    [sg.Text('*Error, tickers can only be 5 letters or less.*', text_color='red', justification='right', visible=False, key='ticker_error', background_color='yellow')],

    [sg.Button("Start Filtering", button_color="black on green")],

    [sg.Button("Pause", button_color='black on orange')],

    [sg.Button("Stop Filtering", button_color='black on red')],

    [sg.Text('Ticker Filter'), sg.InputText(size=(10, 1), key='filter')],

    [sg.Button('Apply')]



]

window = sg.Window("Stockiest", layout, finalize=True, size=(1024, 768), resizable=False, use_custom_titlebar=True,
                   titlebar_icon=stockiestIcon, keep_on_top=True, icon=stockiestIcon)


def main():
    running = False

    filter_text = ""

    d_prev = 0

    g_prev = 0

    while True:

        if running:

            resp = requests.get('https://static.newsfilter.io/landing-page/articles-latest-news.json')

            if resp.status_code == 200:

                # loop through every headline...

                for headlines in resp.json():

                    # loop through every word in goodNews...

                    for gNews in goodNews:

                        # set variables for title and ticker..

                        title = f'{headlines["title"]}'.lower()

                        ticker = f'{headlines["symbols"]}'.lower()

                        # if the title has a keyword AND a ticker AND is not a duplicate...

                        if (gNews in title) and (len(ticker) > 2) and (title not in seen):
                            # add it to seen to prevent future duplication

                            seen.append(title)

                            # add the timestamp, title, and ticker to articleGoodNews

                            articleGoodNews.append(f'{headlines["publishedAt"]}: {title}: {ticker}')

                    # loop through every word in decentNews...

                    for dNews in decentNews:

                        # set variables for title and ticker...

                        title = f'{headlines["title"]}'.lower()

                        ticker = f'{headlines["symbols"]}'.lower()

                        # if the title has a keyword AND a ticker AND is not a duplicate...

                        if (dNews in title) and (len(ticker) > 2) and (title not in seen):
                            # add it to seen to prevent future duplication

                            seen.append(title)

                            # add the timestamp, title, and ticker to articleDecentNews

                            articleDecentNews.append(f'{headlines["publishedAt"]}: {title}: {ticker}')

                print(" ")

                print('!!!!!!!!!!!!STOCK NEWS!!!!!!!!!!!!!!!!!!!!!!!!!')

                text = window['textbox']

                # clear current text

                text.update("")

                # print all good news

                for i in articleGoodNews:

                    if len(articleGoodNews) > g_prev:
                        g_prev = len(articleGoodNews)

                        do_sound = True
                    else:
                        do_sound = False

                    if filter_text != "":

                        if filter_text in i:
                            if do_sound:
                                play(good_sound, False)

                            print('GOOD STOCK NEWS: ' + i)

                            text.update(text.get() + "\n\nGood News: " + i)

                    else:

                        print('GOOD STOCK NEWS: ' + i)

                        if do_sound:
                            play(good_sound, False)

                        text.update(text.get() + "\n\nGood News: " + i)

                # print a divider

                if len(articleDecentNews) > 0:
                    print(
                        '===============================================================================================')

                    text.update(
                        text.get() + "\n\n=======================================================================================")

                # print all decent news

                for i in articleDecentNews:

                    if len(articleDecentNews) > d_prev:
                        d_prev = len(articleDecentNews)

                        do_sound = True
                    else:
                        do_sound = False

                    if filter_text != "":

                        if filter_text in i:
                            if do_sound:
                                play(good_sound, False)

                            print('DECENT STOCK NEWS: ' + i)

                            text.update(text.get() + "\n\nDecent News: " + i)

                    else:

                        print('DECENT STOCK NEWS: ' + i)

                        if do_sound:
                            play(good_sound, False)

                        text.update(text.get() + "\n\nDecent News: " + i)

        event, values = window.read(timeout=5000)

        if event == "Start Filtering":
            running = True

            window['running'].Update('Running...', visible=True, background_color='red')

        if event == "Pause":
            running = False

            window['running'].Update('Paused', visible=True, background_color='orange')

        if event == "Apply":
            if len(values['filter']) <= 5 and values['filter'].isalpha():
                current_filter = values["filter"]

                filter_text = current_filter.lower()

                window['ticker_error'].Update(visible=False)
            elif len(values['filter']) == 0:
                current_filter = values["filter"]

                filter_text = current_filter.lower()

                window['ticker_error'].Update(visible=False)
            else:
                window['ticker_error'].Update(visible=True)

        if event == sg.WIN_CLOSED or event == "Stop Filtering":
            running = False

            break

    window.close()


main()

