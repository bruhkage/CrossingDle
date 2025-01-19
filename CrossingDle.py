
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
import random
from datetime import datetime
global count
import os
import sys
import tkinter as tk
count=0




def Menu():
    global menu
    menu = Tk()
    menu.title("CrossingDle")
    menu.geometry("600x600")
    menu.configure(background='white')
    menu.attributes("-fullscreen", True)
    menu.bind("<Escape>", lambda event: escape_window(event, menu))

    title=Label(text="Crossingdle \n The Animal Crossing Guessing Game",font="Arial 40",bg="white")
    title.place(x=520,y=30)
    daily = Button(text="Daily",command=lambda:Main_game(True),font="Arial 60",padx=79)
    daily.place(x=780,y=200)

    unlimited = Button(text="Unlimited", command=lambda: Main_game(False), font="Arial 60")
    unlimited.place(x=780, y=380)

    quit = Button(text="Quit", command=menu.destroy, font="Arial 60", padx=95)
    quit.place(x=780, y=560)
    menu.mainloop()

def escape_window(event,window):
    # Check the current state of fullscreen

    if window.attributes("-fullscreen"):  # If the window is fullscreen
        window.attributes("-fullscreen", False)  # Exit fullscreen
        window.geometry("600x600")  # Restore to normal size with title bar
    else:
        window.attributes("-fullscreen", True)  # Go fullscreen
        #root.geometry("1920x1080")  # Set fullscreen size, or choose other size


def Main_game(State):
    global count
    global df
    pd.set_option('display.max_colwidth', None)
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))

    # Construct the full path to the CSV file
    csv_file_path = os.path.join(base_path, "villagers.csv")

    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path)
    menu.destroy()
    global RandomVillager

    if State == True:
        today = datetime.now()

        # Format the date as a string (e.g., '20250116' for January 16, 2025)
        date_string = today.strftime('%Y%m%d')

        # Convert the string to an integer to use as a seed
        seed = int(date_string)

        # Set the seed for the random module
        random.seed(seed)

        indices = df.index.tolist()

        # Select a random index
        random_index = random.choice(indices)

        # Retrieve the row at the selected index
        RandomVillager = df.loc[[random_index]]
        print(RandomVillager)

    if State == False:
        RandomVillager = df.sample(n=1)

    global root
    root = Tk()
    root.title("CrossingDle")  # Set the title
    root.geometry("600x600")  # Initial size
    root.configure(background='white')
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda event: escape_window(event, root))





    print(RandomVillager.to_string())


    Gender0=Label(text="Gender",font="Arial 15",bg="white")
    Personality0=Label(text="Personality",font="Arial 15",bg="white")
    Species0=Label(text="Species",font="Arial 15",bg="white")
    Hobbies0=Label(text="Hobbies",font="Arial 15",bg="white")
    Style10=Label(text="Style 1",font="Arial 15",bg="white")
    Style20=Label(text="Style 2",font="Arial 15",bg="white")
    Song0=Label(text="Song",font="Arial 15",bg="white")


    Gender0.place(x=504, y=63)
    Personality0.place(x=684, y=63)
    Species0.place(x=864, y=63)
    Hobbies0.place(x=1044, y=63)
    Style10.place(x=1224, y=63)
    Style20.place(x=1404, y=63)
    Song0.place(x=1584, y=63)


    Gender=Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Personality=Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Species=Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Hobbies=Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style1=Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style2=Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Song=Label(text="",bg="green",font="Arial 16",height=5,width=10,wraplength=100)
    image = Label(text="",bg="white",font="Arial 16",wraplength=100)

    Gender2 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Personality2 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Species2 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Hobbies2 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style12 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style22 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Song2 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    image2 = Label(text="",bg="white",font="Arial 16",wraplength=100)

    Gender3 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Personality3 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Species3 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Hobbies3 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style13 =Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style23 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Song3 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    image3 = Label(text="",bg="white",font="Arial 16",wraplength=100)

    Gender4 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Personality4 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Species4 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Hobbies4 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style14 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style24 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Song4 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    image4 = Label(text="",bg="white",font="Arial 16",wraplength=100)

    Gender5 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Personality5 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Species5 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Hobbies5 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style15 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style25 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Song5 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    image5 = Label(text="",bg="white",font="Arial 16",wraplength=100)

    Gender6 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Personality6 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Species6 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Hobbies6 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style16 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style26 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Song6 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    image6 = Label(text="",bg="white",font="Arial 16",wraplength=100)

    Gender7 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Personality7 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Species7 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Hobbies7 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style17 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Style27 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    Song7 = Label(text="",bg="green",font="Arial 16",height=5,width=10)
    image7 = Label(text="",bg="white",font="Arial 16",wraplength=100)


    count=0
    def guess(event):
        global clicked
        global Selected
        global count
        global df
        global RandomVillager
        global correct
        searchbar.delete(0, tk.END)

        attributes = ["Gender", "Species", "Hobby", "Personality", "Favorite Song", "Style 1", "Style 2"]

        clicked = listbox.get(listbox.curselection())
        Selected = df[df["Name"] == clicked]
        print(Selected)
        df = df[df["Name"] != clicked]
        Selected=Selected.reset_index()
        listbox.place(x=10000)
        print(count)

        if count == 0:
            Gender["text"] = Selected["Gender"].to_string(index=False)
            Species["text"] = Selected["Species"].to_string(index=False)
            Personality["text"] = Selected["Personality"].to_string(index=False)
            Hobbies["text"] = Selected["Hobby"].to_string(index=False)
            Style1["text"] = Selected["Style 1"].to_string(index=False)
            Style2["text"] = Selected["Style 2"].to_string(index=False)
            Song["text"] = Selected["Favorite Song"].to_string(index=False)


            Names = [Gender, Species, Hobbies, Personality, Song, Style1, Style2]

            i=0
            correct=0
            for attr in attributes:

                if Selected[attr].iloc[0] == RandomVillager[attr].iloc[0]:

                    Names[i]["bg"] = "#52eb71"
                    i+=1
                    correct+=1
                else:
                    Names[i]["bg"] = "#eb5a52"
                    i+=1

            Gender.place(x=500, y=90)
            Personality.place(x=680, y=90)
            Species.place(x=860, y=90)
            Hobbies.place(x=1040, y=90)
            Style1.place(x=1220, y=90)
            Style2.place(x=1400, y=90)
            Song.place(x=1580, y=90)
            image.place(x=320, y=90)



        elif count == 1:

            Gender2["text"] = Selected["Gender"].to_string(index=False)
            Species2["text"] = Selected["Species"].to_string(index=False)
            Personality2["text"] = Selected["Personality"].to_string(index=False)
            Hobbies2["text"] = Selected["Hobby"].to_string(index=False)
            Style12["text"] = Selected["Style 1"].to_string(index=False)
            Style22["text"] = Selected["Style 2"].to_string(index=False)
            Song2["text"] = Selected["Favorite Song"].to_string(index=False)

            Names = [Gender2, Species2, Hobbies2, Personality2, Song2, Style12, Style22]

            i = 0
            correct = 0
            for attr in attributes:

                if Selected[attr].iloc[0] == RandomVillager[attr].iloc[0]:

                    Names[i]["bg"] = "#52eb71"
                    i += 1
                    correct += 1
                else:
                    Names[i]["bg"] = "#eb5a52"
                    i += 1

            Gender.place(x=500, y=235)
            Personality.place(x=680, y=235)
            Species.place(x=860, y=235)
            Hobbies.place(x=1040, y=235)
            Style1.place(x=1220, y=235)
            Style2.place(x=1400, y=235)
            Song.place(x=1580, y=235)
            image.place(x=320, y=235)

            Gender2.place(x=500, y=90)
            Personality2.place(x=680, y=90)
            Species2.place(x=860, y=90)
            Hobbies2.place(x=1040, y=90)
            Style12.place(x=1220, y=90)
            Style22.place(x=1400, y=90)
            Song2.place(x=1580, y=90)
            image2.place(x=320, y=90)


        elif count == 2:

            Gender3["text"] = Selected["Gender"].to_string(index=False)
            Species3["text"] = Selected["Species"].to_string(index=False)
            Personality3["text"] = Selected["Personality"].to_string(index=False)
            Hobbies3["text"] = Selected["Hobby"].to_string(index=False)
            Style13["text"] = Selected["Style 1"].to_string(index=False)
            Style23["text"] = Selected["Style 2"].to_string(index=False)
            Song3["text"] = Selected["Favorite Song"].to_string(index=False)

            Names = [Gender3, Species3, Hobbies3, Personality3, Song3, Style13, Style23]

            i = 0
            correct = 0
            for attr in attributes:

                if Selected[attr].iloc[0] == RandomVillager[attr].iloc[0]:

                    Names[i]["bg"] = "#52eb71"
                    i += 1
                    correct += 1
                else:
                    Names[i]["bg"] = "#eb5a52"
                    i += 1

            Gender.place(x=500, y=380)
            Personality.place(x=680, y=380)
            Species.place(x=860, y=380)
            Hobbies.place(x=1040, y=380)
            Style1.place(x=1220, y=380)
            Style2.place(x=1400, y=380)
            Song.place(x=1580, y=380)
            image.place(x=320, y=380)

            Gender2.place(x=500, y=235)
            Personality2.place(x=680, y=235)
            Species2.place(x=860, y=235)
            Hobbies2.place(x=1040, y=235)
            Style12.place(x=1220, y=235)
            Style22.place(x=1400, y=235)
            Song2.place(x=1580, y=235)
            image2.place(x=320, y=235)

            Gender3.place(x=500, y=90)
            Personality3.place(x=680, y=90)
            Species3.place(x=860, y=90)
            Hobbies3.place(x=1040, y=90)
            Style13.place(x=1220, y=90)
            Style23.place(x=1400, y=90)
            Song3.place(x=1580, y=90)
            image3.place(x=320, y=90)


        elif count == 3:

            Gender4["text"] = Selected["Gender"].to_string(index=False)
            Species4["text"] = Selected["Species"].to_string(index=False)
            Personality4["text"] = Selected["Personality"].to_string(index=False)
            Hobbies4["text"] = Selected["Hobby"].to_string(index=False)
            Style14["text"] = Selected["Style 1"].to_string(index=False)
            Style24["text"] = Selected["Style 2"].to_string(index=False)
            Song4["text"] = Selected["Favorite Song"].to_string(index=False)

            Names = [Gender4, Species4, Hobbies4, Personality4, Song4, Style14, Style24]

            i = 0
            correct = 0
            for attr in attributes:

                if Selected[attr].iloc[0] == RandomVillager[attr].iloc[0]:

                    Names[i]["bg"] = "#52eb71"
                    i += 1
                    correct += 1
                else:
                    Names[i]["bg"] = "#eb5a52"
                    i += 1

            Gender.place(x=500, y=525)
            Personality.place(x=680, y=525)
            Species.place(x=860, y=525)
            Hobbies.place(x=1040, y=525)
            Style1.place(x=1220, y=525)
            Style2.place(x=1400, y=525)
            Song.place(x=1580, y=525)
            image.place(x=320, y=525)

            Gender2.place(x=500, y=380)
            Personality2.place(x=680, y=380)
            Species2.place(x=860, y=380)
            Hobbies2.place(x=1040, y=380)
            Style12.place(x=1220, y=380)
            Style22.place(x=1400, y=380)
            Song2.place(x=1580, y=380)
            image2.place(x=320, y=380)

            Gender3.place(x=500, y=235)
            Personality3.place(x=680, y=235)
            Species3.place(x=860, y=235)
            Hobbies3.place(x=1040, y=235)
            Style13.place(x=1220, y=235)
            Style23.place(x=1400, y=235)
            Song3.place(x=1580, y=235)
            image3.place(x=320, y=235)

            Gender4.place(x=500, y=90)
            Personality4.place(x=680, y=90)
            Species4.place(x=860, y=90)
            Hobbies4.place(x=1040, y=90)
            Style14.place(x=1220, y=90)
            Style24.place(x=1400, y=90)
            Song4.place(x=1580, y=90)
            image4.place(x=320, y=90)


        elif count == 4:

            Gender5["text"] = Selected["Gender"].to_string(index=False)
            Species5["text"] = Selected["Species"].to_string(index=False)
            Personality5["text"] = Selected["Personality"].to_string(index=False)
            Hobbies5["text"] = Selected["Hobby"].to_string(index=False)
            Style15["text"] = Selected["Style 1"].to_string(index=False)
            Style25["text"] = Selected["Style 2"].to_string(index=False)
            Song5["text"] = Selected["Favorite Song"].to_string(index=False)

            Names = [Gender5, Species5, Hobbies5, Personality5, Song5, Style15, Style25]

            i = 0
            correct = 0
            for attr in attributes:

                if Selected[attr].iloc[0] == RandomVillager[attr].iloc[0]:

                    Names[i]["bg"] = "#52eb71"
                    i += 1
                    correct += 1
                else:
                    Names[i]["bg"] = "#eb5a52"
                    i += 1
            Gender.place(x=500, y=670)
            Personality.place(x=680, y=670)
            Species.place(x=860, y=670)
            Hobbies.place(x=1040, y=670)
            Style1.place(x=1220, y=670)
            Style2.place(x=1400, y=670)
            Song.place(x=1580, y=670)
            image.place(x=320, y=670)

            Gender2.place(x=500, y=525)
            Personality2.place(x=680, y=525)
            Species2.place(x=860, y=525)
            Hobbies2.place(x=1040, y=525)
            Style12.place(x=1220, y=525)
            Style22.place(x=1400, y=525)
            Song2.place(x=1580, y=525)
            image2.place(x=320, y=525)

            Gender3.place(x=500, y=380)
            Personality3.place(x=680, y=380)
            Species3.place(x=860, y=380)
            Hobbies3.place(x=1040, y=380)
            Style13.place(x=1220, y=380)
            Style23.place(x=1400, y=380)
            Song3.place(x=1580, y=380)
            image3.place(x=320, y=380)

            Gender4.place(x=500, y=235)
            Personality4.place(x=680, y=235)
            Species4.place(x=860, y=235)
            Hobbies4.place(x=1040, y=235)
            Style14.place(x=1220, y=235)
            Style24.place(x=1400, y=235)
            Song4.place(x=1580, y=235)
            image4.place(x=320, y=235)

            Gender5.place(x=500, y=90)
            Personality5.place(x=680, y=90)
            Species5.place(x=860, y=90)
            Hobbies5.place(x=1040, y=90)
            Style15.place(x=1220, y=90)
            Style25.place(x=1400, y=90)
            Song5.place(x=1580, y=90)
            image5.place(x=320, y=90)


        elif count == 5:

            Gender6["text"] = Selected["Gender"].to_string(index=False)
            Species6["text"] = Selected["Species"].to_string(index=False)
            Personality6["text"] = Selected["Personality"].to_string(index=False)
            Hobbies6["text"] = Selected["Hobby"].to_string(index=False)
            Style16["text"] = Selected["Style 1"].to_string(index=False)
            Style26["text"] = Selected["Style 2"].to_string(index=False)
            Song6["text"] = Selected["Favorite Song"].to_string(index=False)

            Names = [Gender6, Species6, Hobbies6, Personality6, Song6, Style16, Style26]

            i = 0
            correct = 0
            for attr in attributes:

                if Selected[attr].iloc[0] == RandomVillager[attr].iloc[0]:

                    Names[i]["bg"] = "#52eb71"
                    i += 1
                    correct += 1
                else:
                    Names[i]["bg"] = "#eb5a52"
                    i += 1

            Gender.place(x=500, y=815)
            Personality.place(x=680, y=815)
            Species.place(x=860, y=815)
            Hobbies.place(x=1040, y=815)
            Style1.place(x=1220, y=815)
            Style2.place(x=1400, y=815)
            Song.place(x=1580, y=815)
            image.place(x=320, y=815)

            Gender2.place(x=500, y=670)
            Personality2.place(x=680, y=670)
            Species2.place(x=860, y=670)
            Hobbies2.place(x=1040, y=670)
            Style12.place(x=1220, y=670)
            Style22.place(x=1400, y=670)
            Song2.place(x=1580, y=670)
            image2.place(x=320, y=670)

            Gender3.place(x=500, y=525)
            Personality3.place(x=680, y=525)
            Species3.place(x=860, y=525)
            Hobbies3.place(x=1040, y=525)
            Style13.place(x=1220, y=525)
            Style23.place(x=1400, y=525)
            Song3.place(x=1580, y=525)
            image3.place(x=320, y=525)

            Gender4.place(x=500, y=380)
            Personality4.place(x=680, y=380)
            Species4.place(x=860, y=380)
            Hobbies4.place(x=1040, y=380)
            Style14.place(x=1220, y=380)
            Style24.place(x=1400, y=380)
            Song4.place(x=1580, y=380)
            image4.place(x=320, y=380)

            Gender5.place(x=500, y=235)
            Personality5.place(x=680, y=235)
            Species5.place(x=860, y=235)
            Hobbies5.place(x=1040, y=235)
            Style15.place(x=1220, y=235)
            Style25.place(x=1400, y=235)
            Song5.place(x=1580, y=235)
            image5.place(x=320, y=235)

            Gender6.place(x=500, y=90)
            Personality6.place(x=680, y=90)
            Species6.place(x=860, y=90)
            Hobbies6.place(x=1040, y=90)
            Style16.place(x=1220, y=90)
            Style26.place(x=1400, y=90)
            Song6.place(x=1580, y=90)
            image6.place(x=320, y=90)


        elif count == 6:

            Gender7["text"] = Selected["Gender"].to_string(index=False)
            Species7["text"] = Selected["Species"].to_string(index=False)
            Personality7["text"] = Selected["Personality"].to_string(index=False)
            Hobbies7["text"] = Selected["Hobby"].to_string(index=False)
            Style17["text"] = Selected["Style 1"].to_string(index=False)
            Style27["text"] = Selected["Style 2"].to_string(index=False)
            Song7["text"] = Selected["Favorite Song"].to_string(index=False)

            Names = [Gender7, Species7, Hobbies7, Personality7, Song7, Style17, Style27]

            i = 0
            correct = 0
            for attr in attributes:

                if Selected[attr].iloc[0] == RandomVillager[attr].iloc[0]:

                    Names[i]["bg"] = "#52eb71"
                    i += 1
                    correct += 1
                else:
                    Names[i]["bg"] = "#eb5a52"
                    i += 1

            for name in Names:
                if name["bg"] == "#eb5a52":
                    root.after(1000,lambda: LoseOrWin(False))






            Gender.place(x=500, y=960)  # 800 + 145
            Personality.place(x=680, y=960)
            Species.place(x=860, y=960)
            Hobbies.place(x=1040, y=960)
            Style1.place(x=1220, y=960)
            Style2.place(x=1400, y=960)
            Song.place(x=1580, y=960)
            image.place(x=320, y=960)

            Gender2.place(x=500, y=815)
            Personality2.place(x=680, y=815)
            Species2.place(x=860, y=815)
            Hobbies2.place(x=1040, y=815)
            Style12.place(x=1220, y=815)
            Style22.place(x=1400, y=815)
            Song2.place(x=1580, y=815)
            image2.place(x=320, y=815)

            Gender3.place(x=500, y=670)
            Personality3.place(x=680, y=670)
            Species3.place(x=860, y=670)
            Hobbies3.place(x=1040, y=670)
            Style13.place(x=1220, y=670)
            Style23.place(x=1400, y=670)
            Song3.place(x=1580, y=670)
            image3.place(x=320, y=670)

            Gender4.place(x=500, y=525)
            Personality4.place(x=680, y=525)
            Species4.place(x=860, y=525)
            Hobbies4.place(x=1040, y=525)
            Style14.place(x=1220, y=525)
            Style24.place(x=1400, y=525)
            Song4.place(x=1580, y=525)
            image4.place(x=320, y=525)

            Gender5.place(x=500, y=380)
            Personality5.place(x=680, y=380)
            Species5.place(x=860, y=380)
            Hobbies5.place(x=1040, y=380)
            Style15.place(x=1220, y=380)
            Style25.place(x=1400, y=380)
            Song5.place(x=1580, y=380)
            image5.place(x=320, y=380)

            Gender6.place(x=500, y=235)
            Personality6.place(x=680, y=235)
            Species6.place(x=860, y=235)
            Hobbies6.place(x=1040, y=235)
            Style16.place(x=1220, y=235)
            Style26.place(x=1400, y=235)
            Song6.place(x=1580, y=235)
            image6.place(x=320, y=235)

            Gender7.place(x=500, y=90)
            Personality7.place(x=680, y=90)
            Species7.place(x=860, y=90)
            Hobbies7.place(x=1040, y=90)
            Style17.place(x=1220, y=90)
            Style27.place(x=1400, y=90)
            Song7.place(x=1580, y=90)
            image7.place(x=320, y=90)





        print(Selected["Image"][0])
        response = requests.get(Selected["Image"][0])

        # If the request is successful (status code 200)
        if response.status_code == 200:

            # Open the image using Pillow from the binary content
            img = Image.open(BytesIO(response.content))

            # Resize image to fit within the Tkinter window
            img = img.resize((86, 140))

            # Convert the image to a format Tkinter can display (PhotoImage)
            img_tk = ImageTk.PhotoImage(img)


            # Create a Label widget to display the image
            if count==0:
                image.config(image=img_tk)
                image.image = img_tk  # Keep a reference to the image to avoid garbage collection


                # Create a Label widget to display the image
            if count == 1:
                image2.config(image=img_tk)
                image2.image = img_tk  # Keep a reference to the image to avoid garbage collection

            if count == 2:
                image3.config(image=img_tk)
                image3.image = img_tk  # Keep a reference to the image to avoid garbage collection

            if count == 3:
                image4.config(image=img_tk)
                image4.image = img_tk  # Keep a reference to the image to avoid garbage collection

            if count == 4:
                image5.config(image=img_tk)
                image5.image = img_tk  # Keep a reference to the image to avoid garbage collection

            if count == 5:
                image6.config(image=img_tk)
                image6.image = img_tk  # Keep a reference to the image to avoid garbage collection

            if count == 6:
                image7.config(image=img_tk)
                image7.image = img_tk  # Keep a reference to the image to avoid garbage collection

        if correct==7:
            root.after(1000, lambda: LoseOrWin(True))
        count+=1

    def search(event):
        listbox.delete(0, END)  # Clears the listbox (used for resetting searches)

        query = searchbar.get().lower()

        if query == "":  # Checks if the search bar is blank
            listbox.place(x=10000)  # Hide listbox when search bar is empty
        else:
            # Separate names starting with the query and others
            starts_with_query = df[df['Name'].str.lower().str.startswith(query)]
            contains_query = df[
                df['Name'].str.lower().str.contains(query) & ~df['Name'].str.lower().str.startswith(query)]

            # Combine the results: starts first, then contains
            results = pd.concat([starts_with_query, contains_query])

            if results.empty:  # If no results were found, revert to previous search behavior
                searched_df = df[df['Name'].str.contains(query, case=False, na=False)]
                for name in searched_df["Name"]:
                    listbox.insert(END, name)
                listbox.place(x=500, y=50, width=315, height=387)  # Show listbox with original behavior
            else:
                # Insert names from the filtered results (starts with query first)
                for name in results['Name']:
                    listbox.insert(END, name)
                listbox.place(x=500, y=50, width=315, height=387)

    searchbar=Entry(font="Arial 14",bg="#f0f0f0")
    searchbar.place(x=500, y=30,width=600)
    listbox = Listbox(root, bg="white",)

    listbox.bind("<<ListboxSelect>>",guess)
    searchbar.bind("<KeyRelease>",search)
    root.mainloop()


def LoseOrWin(won):
    global win
    global RandomVillager
    root.destroy()
    win=Tk()
    win.title("Crossingdle")
    win.geometry("600x600")
    win.configure(background='white')
    win.attributes("-fullscreen", True)
    win.bind("<Escape>", lambda event: escape_window(event, win))

    response = requests.get(RandomVillager["Image"].to_string(index=False ))
    print(response)

    image = Label(text="", bg="white", font="Arial 16", wraplength=100)
    image.place(x=860, y=60)

    if won == True:
        Result = Label(text="You Win", bg="white", font="Arial 35")
        Result.place(x=860,y=400)
    else:
        Result = Label(text="You Lose", bg="white", font="Arial 35")
        Result.place(x=860, y=400)

    character=RandomVillager["Name"].to_string(index=False)
    label = Label(text=f"The Character Was {character}",bg="white", font="Arial 35")
    label.place(x=700,y=500)
    return_to_menu = Button(win, text="Menu", command=lambda: (win.destroy(), Menu()), font="Arial 45")
    return_to_menu.place(x=860,y=570)
    quit=Button(text="Quit",command=win.destroy,font="Arial 55")
    quit.place(x=860, y=700)

    # If the request is successful (status code 200)
    if response.status_code == 200:
        # Open the image using Pillow from the binary content
        img = Image.open(BytesIO(response.content))

        # Resize image to fit within the Tkinter window (optional)
        img = img.resize((169, 320))  # You can adjust the size as needed

        # Convert the image to a format Tkinter can display (PhotoImage)
        img_tk = ImageTk.PhotoImage(img)

        image.config(image=img_tk)
    win.mainloop()

Menu()