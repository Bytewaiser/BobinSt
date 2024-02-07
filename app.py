import streamlit as st
import pandas as pd
from PIL import Image


st.title("Buse Naming App")

st.set_page_config(
        page_title="Buse Naming App",
)

data = st.file_uploader("Upload the excel file", type=["xlsx", "xls"], accept_multiple_files=False)
# cols = [] if not data else pd.read_excel(data).columns
# index_col = st.selectbox("Select the index column", options=cols) # type: ignore
imgs = st.file_uploader("Upload an images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)


def get_data(selected):
    data = df[df["Sıralama"] == selected].squeeze()
    return data

if data:
    df = pd.read_excel(data)
    df.columns = df.columns.str.strip()
    index_col = "Sıralama"
    ids = df[index_col]
    st.write(df)

    selected_values = [] # type: ignore
    names = []
    if imgs:
        tabs = st.tabs([f"Tab {idx+1}" for idx in range(len(imgs))])
        for idx, img in enumerate(imgs):
            image = Image.open(img)
            selected = tabs[idx].selectbox("Select the id", ids, key=idx)

            d = get_data(selected)

            machine = d["Çalışılan Makine"]
            no = d["Bobin No"]

            tabs[idx].image(image)
            selected_values.append(selected)
            name = f"{selected} NUMARALI BOBİN {machine} {no}"
            names.append(name)

        st.write(names)






