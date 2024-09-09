import streamlit as lit
import datetime

lit.set_page_config(layout="wide")
background_css = """
    <style>
    body {
        background-color: #F0F2F6;
    }
    .main {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .css-18e3th9 {
        padding-top: 2rem;
    }
    </style>
"""
lit.markdown(background_css, unsafe_allow_html=True)



lit.title("Crypto Currency")
lit.text('Day to day update')



col1, col2, col3 = lit.columns(3)
with col1:
    lit.metric(label='Bitcoin', value="$55,190", delta="1.39%")

with col2:
    lit.metric(label='Ethereum', value="$2,325", delta="1.13%")

with col3:
    lit.metric(label='Sunpnr', value="$0.982", delta="-1.7")

lit.subheader('***Register here to the world of Crypto***')

nam, dofb, agee, gen = lit.columns(4)
with nam:
    lit.text_input("Enter your Name", key="name")
with dofb:
    lit.date_input("Enter your DOB", datetime.date(2005, 1, 1))
with agee:
    lit.number_input("Enter your Age", min_value=0, max_value=100, value=25)
with gen:
    lit.radio("Select your Gender", ("Male", "Female"))

lit.checkbox("I Agree The Terms And Conditions")
lit.selectbox("Choose your crypto coin", ('Bitcoin', 'Ethereum', 'Sunpnr'))
lit.multiselect("Choose coins you like to buy in the future", ('PI', 'TronBull', 'USDC', 'Solona', 'Shiba', 'LiteCoin'))


button_html = """
    <style>
    .button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #000000;
        border: none;
        border-radius: 8px;
        box-shadow: 0 4px #999;
    }

    .button:hover {background-color: #444444}

    .button:active {
        background-color: #444444;
        box-shadow: 0 2px #666;
        transform: translateY(2px);
    }

    a.button {
        text-decoration: none; 
        color: #fff; 
    }
    </style>
    <a href="#" class="button">Save</a>
"""
lit.markdown(button_html, unsafe_allow_html=True)

bit, sun = lit.columns(2)
bit, sun = lit.tabs(['About Crypto', 'About Our Page'])


with bit:
    lit.video("https://youtu.be/rYQgy8QDEBI?si=Sf1kVDXX3puh3VZ3")
    lit.write("")


with sun:
    expan = lit.expander("We care about your privacy")
    expan.write("""We care about your privacy. We and our partners store and access personal data like browsing data or unique identifiers, on your device. Selecting "I Accept" enables tracking technologies to support the purposes shown under "we and our partners process data to provide," whereas selecting "Reject All" or withdrawing your consent will disable them. Your choices will have effect within our Website. For more details, refer to our Privacy Policy.""")
