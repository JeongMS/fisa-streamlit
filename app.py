import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

data = './README.md' #그냥 파이썬 모드
st.button("클릭미")
st.download_button("Download file", data)

slider_val = None
url = 'https://naver.com'
st.link_button("Go to gallery", url)
st.page_link("pages/app2.py", label="Home")
st.data_editor(df)
st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")
# Use widgets' returned values in variables:
for i in range(int(st.number_input("Num:"))):
    pass
if st.sidebar.selectbox("I:",["f"]) == "f":
    pass
my_slider_val = st.slider("Quinn Mallory", 1, 88)
st.write(my_slider_val)
# Disable widgets to remove interactivity:
# st.slider("Pick a number", 0, 100, disabled=True)

# 출력 메소드
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3])
# st.write_stream(my_generator)
# st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("_Markdown_")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.html("<p>Hi!</p>")

# 데이터 출력
st.dataframe(df)
st.table(df.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)

st.dataframe(df)
st.table(df.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, -2)

# st.image("./header.png")
# st.audio(data)
# st.video(data)
# st.video(data, subtitles="./subs.vtt")
# st.logo("logo.jpg")

st.area_chart(df)
st.bar_chart(df)
st.bar_chart(df, horizontal=True)
st.line_chart(df)
st.map(df)
st.scatter_chart(df)

# Work with user selections
event = st.plotly_chart(
    df,
    on_select="rerun"
)

# event = st.altair_chart(
#     chart,
#     on_select="rerun"
# )
# event = st.vega_lite_chart(
#     df,
#     spec,
#     on_select="rerun"
# )

