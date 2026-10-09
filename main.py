
from pyscript import document

club_members = ["Anikka Lin", "Archi Pantalone", "Marry Sterling", "Lovlie Hertsz"]

def check_member(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    document.getElementById("output").innerText = messages[is_member]
