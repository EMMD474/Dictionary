import requests as r
import customtkinter as c
from urllib3.exceptions import NameResolutionError
from requests.exceptions import RequestException


def get_meaning():
    try:
        textbox.delete("1.0", "end")
        word: str = entry.get()
        headers = {
            "User-Agent": "Mozilla/5.0 (iphone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebkit/605.1.15 (KHTML, "
                          "like Gecko)"
                          " Version/16.1 Mobile/15E148 Safari/604.1"
        }

        response = r.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word, headers=headers)

        json_data = response.json()
        meanings = json_data[0]["meanings"]
        for meaning in meanings:
            definition = meaning["definitions"][0]["definition"]
            part_of_speech = meaning["partOfSpeech"]
            textbox.insert("end", f"Part of Speech: {part_of_speech} \n")
            textbox.insert("end", f"Definition: {definition} \n")
            try:
                example = meaning["definitions"][0]['example']
                textbox.insert("end", f"Example: {example} \n")
            except:
                textbox.insert("end", "no example \n")

            textbox.insert("end", "------------------- \n")

    except RequestException:
        textbox.insert("0.0", "You are Offline, Check your Internet Connection!")

    except NameResolutionError:
        textbox.insert("0.0", "You are Offline, Check your Internet Connection!")

    except KeyError:
        textbox.insert("0.0", "Sorry, Word not found. Check word spelling")


def change_mode():
    if switch_var.get() == "off":
        c.set_appearance_mode("light")
    else:
        c.set_appearance_mode("dark")


c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")

root = c.CTk()
root.geometry("500x500")

frame = c.CTkFrame(root)
frame.pack(pady=30, padx=60, fill="both", expand=True)
label = c.CTkLabel(frame, text="Dictionary", text_color=("#12002f", "#000"), font=("Sans-serif", 28))

label.pack(pady=12, padx=20)

switch_var = c.StringVar(value="on")
switch = c.CTkSwitch(frame, text="light / dark mode", text_color=("#222", "white"), font=("sans-serif", 15),
                     variable=switch_var, onvalue="on", offvalue="off",
                     command=change_mode)
switch.pack(pady=12, padx=10)

entry = c.CTkEntry(frame, width=300, height=32, placeholder_text="Word", placeholder_text_color=("#222", "#000"),
                   text_color=("#222", "#000"), font=("Sans-serif", 14))
entry.pack(pady=12, padx=10)

btn = c.CTkButton(frame, width=150, height=32, text="Get Meaning", font=("Sans-serif", 14), fg_color=("teal", "#12002f")
                  , hover_color=("#12002f", "purple"), command=get_meaning)
btn.pack(pady=12, padx=12)

textbox = c.CTkTextbox(frame, width=400)
textbox.pack(pady=20, padx=20, fill="both", expand=True)

root.mainloop()
