import streamlit as st

# text 를 입력히는 검색창을 하나 만듭니다.
# ani_list에 있는 글자가 일부라도 들어가면

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

t_input = st.text_input("검색하실 애니메이션")

if t_input:
    for ani in ani_list:
        if t_input in ani:
            st.image(img_list[ani_list.index(ani)])