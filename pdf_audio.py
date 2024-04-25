import PyPDF2 , pyttsx3

path =open('')

#creating a pdffile reader object
pdfreader=PyPDF2.PdfFileReader(path)

#get an engine instance for the speech synthesis
speak=pyttsx3.init()

for pages in range(pdfreader.numPages):
    text=pdfreader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()
    
speak.stop()