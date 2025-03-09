import streamlit as sl

# Function for conversion
def convert_unit(value, unit_from, unit_to):
    # Dict for conversion units
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "centimeters_meters": 0.01,
        "meters_centimeters": 100,
        "millimeters_meters": 0.001,
        "meters_millimeters": 1000,
        "liters_milliliters": 1000,
        "milliliters_liters": 0.001,
        "pounds_kilograms": 0.453592,
        "kilograms_pounds": 2.20462
    }

    key = f"{unit_from}_{unit_to}"  # _ is used to separate the units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"

# Streamlit UI title/heading
sl.title("Unit Converter")

# Input fields
value = sl.number_input("Enter the value to convert", min_value=1.0, step=1.0, format="%.4f")

# dropdown to select convert from units
unit_from = sl.selectbox("Convert from", ["meters", "kilometers", "grams", "kilograms", "centimeters", "millimeters", "litters", "milliliters", "pounds"])

# dropdown to select convert to units
unit_to = sl.selectbox("Convert to", ["meters", "kilometers", "grams", "kilograms", "centimeters", "millimeters", "litters", "milliliters", "pounds"])

# Button to trigger conversion
if sl.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    sl.write(f"Converted Value: {result}")
