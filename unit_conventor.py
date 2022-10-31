from tkinter import *


def reset():
    input_field.delete(0, END)
    output_field.delete(0, END)

    input_value.set(SELECTIONS[0])
    output_value.set(SELECTIONS[0])

    input_field.focus_set()


def convert():
    inputVal = float(input_field.get())

    input_unit = input_value.get()
    output_unit = output_value.get()

    conversion_factors = [input_unit in length_units and output_unit in length_units,
                          input_unit in weight_units and output_unit in weight_units,
                          input_unit in temperature_units and output_unit in temperature_units,
                          input_unit in area_units and output_unit in area_units,
                          input_unit in volume_units and output_unit in volume_units]

    if any(conversion_factors):
        if input_unit == "celsius" and output_unit == "fahrenheit":
            output_field.delete(0, END)
            output_field.insert(0, (inputVal * 1.8) + 32)
        elif input_unit == "fahrenheit" and output_unit == "celsius":
            output_field.delete(0, END)
            output_field.insert(0, (inputVal - 32) * (5 / 9))
        else:
            output_field.delete(0, END)
            output_field.insert(0, round(inputVal * unitDict[input_unit] / unitDict[output_unit], 5))

    else:
        output_field.delete(0, END)
        output_field.insert(0, "ERROR")


if __name__ == "__main__":
    unitDict = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1000.0,
        "foot": 0.3048,
        "mile": 1609.344,
        "yard": 0.9144,
        "inch": 0.0254,
        "square meter": 1.0,
        "square kilometer": 1000000.0,
        "square centimeter": 0.0001,
        "square millimeter": 0.000001,
        "are": 100.0,
        "hectare": 10000.0,
        "acre": 4046.856,
        "square mile": 2590000.0,
        "square foot": 0.0929,
        "cubic meter": 1000.0,
        "cubic centimeter": 0.001,
        "litre": 1.0,
        "millilitre": 0.001,
        "gallon": 3.785,
        "gram": 1.0,
        "kilogram": 1000.0,
        "milligram": 0.001,
        "quintal": 100000.0,
        "ton": 1000000.0,
        "pound": 453.592,
        "ounce": 28.3495
    }

    length_units = [
        "millimeter", "centimeter", "meter", "kilometer", "foot", "mile", "yard", "inch"
    ]
    temperature_units = [
        "celsius", "fahrenheit"
    ]
    area_units = [
        "square meter", "square kilometer", "square centimeter", "square millimeter",
        "are", "hectare", "acre", "square mile", "square foot"
    ]
    volume_units = [
        "cubic meter", "cubic centimeter", "litre", "millilitre", "gallon"
    ]
    weight_units = [
        "gram", "kilogram", "milligram", "quintal", "ton", "pound", "ounce"
    ]

    SELECTIONS = [
        "Select Unit",
        "millimeter",
        "centimeter",
        "meter",
        "kilometer",
        "foot",
        "mile",
        "yard",
        "inch",
        "celsius",
        "fahrenheit"
        "square meter",
        "square kilometer",
        "square centimeter",
        "square millimeter",
        "are",
        "hectare",
        "acre",
        "square mile",
        "square foot"
        "cubic meter",
        "cubic centimeter",
        "litre",
        "millilitre",
        "gallon"
        "gram",
        "kilogram",
        "milligram",
        "quintal",
        "ton",
        "pound",
        "ounce"
    ]

guiWindow = Tk()
guiWindow.title("Unit Converter - Yavor Vladev")
guiWindow.geometry("500x500+500+250")
guiWindow.resizable(0, 0)
guiWindow.configure(bg="#085482")

header_frame = Frame(guiWindow, bg="#085482")
body_frame = Frame(guiWindow, bg="#085482")

header_frame.pack(expand=True, fill="both")
body_frame.pack(expand=True, fill="both")

header_label = Label(
    header_frame,
    text="Enter a value to convert",
    font=("albertus extra bold", 22),
    bg="#085482",
    fg="#e8f6f3"
)

header_label.pack(expand=True, fill="both")

input_value = StringVar()
output_value = StringVar()

input_value.set(SELECTIONS[0])
output_value.set(SELECTIONS[0])

input_label = Label(
    body_frame,
    text="From:",
    bg="#085482",
    fg="#d0ece7"
)
output_label = Label(
    body_frame,
    text="To:",
    bg="#085482",
    fg="#d0ece7"
)

input_label.grid(row=1, column=1, padx=50, pady=20, sticky=W)
output_label.grid(row=2, column=1, padx=50, pady=20, sticky=W)

input_field = Entry(
    body_frame,
    bg="#e8f8f5"
)

output_field = Entry(
    body_frame,
    bg="#e8f8f5"
)

input_field.grid(row=1, column=2)
output_field.grid(row=2, column=2)

input_field = Entry(
    body_frame,
    bg="#e8f8f5"
)

output_field = Entry(
    body_frame,
    bg="#e8f8f5"
)

input_field.grid(row=1, column=2)
output_field.grid(row=2, column=2)

input_menu = OptionMenu(
    body_frame,
    input_value,
    *SELECTIONS
)
output_menu = OptionMenu(
    body_frame,
    output_value,
    *SELECTIONS
)

input_menu.grid(row=1, column=3, padx=20)
output_menu.grid(row=2, column=3, padx=20)

convert_button = Button(
    body_frame,
    text="CONVERT",
    bg="#0b5345",
    fg="#ffffff",
    command=convert
)

reset_button = Button(
    body_frame,
    text="RESET",
    bg="#f7dc6f",
    fg="#000000",
    command=reset
)

convert_button.grid(row=3, column=2)
reset_button.grid(row=3, column=3)

# running the application
guiWindow.mainloop()

