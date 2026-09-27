from tkinter import *
from tkinter import messagebox, StringVar
from project.personal_info.person_module import *

person_list = []


def save_click():
    try:
        n_id = national_id.get()
        p_num = phone_number.get()
        c_num = card_number.get()
        pl_num = plate_number.get()
        b_id = bill_id.get()


        person = {
            "national_id": check_national_id(n_id),
            "phone_number": check_phone_number(p_num),
            "card_number": check_card_number(c_num),
            "plate": check_plate_number(pl_num),
            "bill_id": check_bill_id(b_id)
        }

        person_list.append(person)
        messagebox.showinfo(title="Saved", message="Person saved")


        national_id.set("")
        phone_number.set("")
        card_number.set("")
        plate_number.set("")
        bill_id.set("")

    except Exception as e:
        messagebox.showerror(title="Error", message=f"{e}")


window = Tk()
window.geometry("600x300")


Label(window, text="National ID").place(x=20, y=20)
national_id = StringVar()
Entry(window, textvariable=national_id).place(x=120, y=20)

Label(window, text="Phone Number").place(x=20, y=60)
phone_number = StringVar()
Entry(window, textvariable=phone_number).place(x=120, y=60)

Label(window, text="Card number").place(x=20, y=100)
card_number = StringVar()
Entry(window, textvariable=card_number).place(x=120, y=100)

Label(window, text="Plate number").place(x=20, y=140)
plate_number = StringVar()
Entry(window, textvariable=plate_number).place(x=120, y=140)

Label(window, text="Bill ID").place(x=20, y=180)
bill_id = StringVar()
Entry(window, textvariable=bill_id).place(x=120, y=180)

Button(window, text="Inquiry", command=save_click).place(x=80, y=250, width=80)

window.mainloop()