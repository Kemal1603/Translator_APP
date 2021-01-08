# ---------------------------- IMPORTED MODULES ------------------------------- #
import tkinter
import pandas
import random

# ---------------------------- CONSTANTS  & GLOBAL VARS------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
DATA_FROM_CSV = pandas.read_csv("language.csv")
random_word = ''


# ---------------------------- FUNCTIONS  ------------------------------- #
# NEXT TURKISH WORD
def next_turkish_word():
    turkish_words_list = [i for i in DATA_FROM_CSV['Turkish']]
    global random_word
    main_card.itemconfig(main_image, image=front_image)
    main_card.itemconfig(title, text="На Турецком", fill="black")
    random_word = random.choice(turkish_words_list)
    if random_word in turkish_words_list:
        turkish_words_list.remove(random_word)
    main_card.itemconfig(word, text=f"{random_word}", fill="black")
    window.after(9000, russian_translate)


# RUSSIAN TRANSLATION OF WORD
def russian_translate():
    main_card.itemconfig(main_image, image=back_image)
    main_card.itemconfig(title, text="На русском", fill="white")
    csv_data_to_dict = {row.Turkish: row.Russian for (index, row) in DATA_FROM_CSV.iterrows()}
    main_card.itemconfig(word, text=f"{csv_data_to_dict[random_word]}", fill="white")
    window.after(9000, russian_translate)


# ---------------------------- UI SETUP ------------------------------- #
# MAIN WINDOW
window = tkinter.Tk()
window.title("Самоучитель Турецкого")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# TURKISH SIDE OF CARD
main_card = tkinter.Canvas(width=800, height=526, highlightthickness=0)
front_image = tkinter.PhotoImage(file="images/card_front.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")
main_image = main_card.create_image(400, 261, image=front_image)
title = main_card.create_text(400, 150, fill='black', font=('Ariel', 40, 'italic'))

word = main_card.create_text(400, 263, text='Для старта нажмите на: ✅ ', fill='black', font=('Ariel', 30, 'bold'))
main_card.grid(row=0, column=1, columnspan=2)

# "No" Button
cancel_image = tkinter.PhotoImage(file="images/wrong.png")
cancel_button = tkinter.Button(image=cancel_image, highlightthickness=0, command=next_turkish_word)
cancel_button.grid(row=1, column=1)

# "Yes" Button
accept_image = tkinter.PhotoImage(file="images/right.png")
accept_button = tkinter.Button(image=accept_image, highlightthickness=0, command=next_turkish_word)
accept_button.grid(row=1, column=2)

# MAIN LOOP
window.mainloop()
