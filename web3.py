import streamlit as st
st.subheader("🤣 瘋狂填詞遊戲")

name = st.text_input("輸入一個名字")
place = st.text_input("輸入一個地點")
action = st.selectbox("選擇一個動作", ["示愛", "睡覺", "吃泡麵", "唱歌"])

if st.button("生成故事"):
    st.success(f"有一天，{name} 跳到了 {place}，突然開始 {action}，路人一看，也跟著一起了！")