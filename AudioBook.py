import pyttsx3
import PyPDF2

book = open('D:The Alchemist -  Paulo Coelho.pdf', 'rb')  # read bytes of the book
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages  # number of pages
print("Total pages: "+str(pages))

speaker = pyttsx3.init()  # initialize the speaker
speaker.setProperty('rate', 150)  # alter the speed of speech
start = input("Enter Start Page number: ")
print("The Audio Book will Play now...!")

for num in range(int(start)-1, pages):  # page 1 = 0, page 2 = 1.
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.save_to_file(str(text), 'The Alchemist.mp3')  # saved as audio
    speaker.say(text)
    speaker.runAndWait()
    print("Done with page ", num)

print("Hope this was indeed helpfull..!")
