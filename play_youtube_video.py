import pywhatkit

try:

    song=input('Enter song name: ')
    pywhatkit.playonyt(song)

    #this will open a web browser and play the youtube video corresponding to the search term
    print('Successfully played')

except:
    print('An unexpected error')