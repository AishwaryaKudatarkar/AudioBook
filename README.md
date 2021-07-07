# AudioBook
Python based project to convert PDF to Audio.

Objectives:
To convert text to speech.
Save the speech as mp3 file.

Theory:
pyttsx3 module is used to convert text to speech and then save the file as mp3.
PyPDF2 module is used to convert PDF to normal text.
.PdfFileReader() creates an instance of a particular PDF.
.init() initialize the instance of pyttsx3.
.extractText() extracts the content from the PDF.
.save_to_file() this is used to save the speech as mp3 file.
.runAndWait() final point, where without this method, audio is not heard.
