from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm


def export_to_pdf (woorden):
    c = canvas.Canvas("hello-world.pdf", pagesize=A4)

    # Rectangle x,y, width, height
    hoog = 20
    breed = 20
    start_x = 300
    Max_x = 595
    Max_y = 842
    start_y = 500
    Font_size_text = 12  
    Font_size_number = 8  
    Right_margin = 20
    Left_margin = 20 

    # Rechtsuitlijnen van de puzzel
    start_x = Max_x / 2

    #c.setFont("Helvetica", Font_size_text)
    #c.drawString(Max_x-Font_size_text,Max_y-Font_size_text, "X") #rechtboven
    #c.drawString(0,Max_y-Font_size_text, "X") #linksboven
    #c.drawString(Max_x-Font_size_text,0, "X") #rechtsonder
    #c.drawString(0,0, "X") #linkonder

    c.setFont("Helvetica", Font_size_number)

    # Woordstart default
    woord_x = start_x
    woord_y = start_y

    for w in woorden:

        for i in range(len(w)):
            
            #vakje voor de letter
            c.rect(woord_x, woord_y, hoog, breed)

            #getal in het vakje positioneren
            c.setFont("Helvetica", Font_size_number)  
            c.drawString(woord_x-18, woord_y+12, str(i))
            
            #Oplossingstekst plaatsen
            c.setFont("Helvetica", Font_size_text)  
            c.drawString(woord_x+4, woord_y+4, w[i])

            #klaarzeten voor volgende letter
            woord_x = woord_x + breed
        
        woord_x = start_x
        woord_y = woord_y + hoog

    #Tekst voor de clue
    #c.drawString(start_x-300, woord_y, "Vraagnummer" + str(i))  


    c.save()

fruit =["Appels","Peren","bananen","Annanassen"]

export_to_pdf(fruit)