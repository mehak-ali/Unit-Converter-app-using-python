
import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts Weight, Length, and Time Instantly")
st.write("Welcome! Select a category, enter the value, and get converted result in real time.")

# Category selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Choose conversion unit based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⌛ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Days", "Days to Hours"])

# Input value
value = st.number_input("Enter the value to convert", min_value=0.0)

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None

# Convert and show result
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is: {result:.4f}")
    else:
        st.error("Invalid conversion.")