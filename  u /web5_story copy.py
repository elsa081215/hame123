#前提概要
import streamlit as st
import time
#儲存
if "story_done" not in st.session_state:
    st.session_state.story_done = False
if "gender_pass" not in st.session_state:
    st.session_state.gender_pass = False
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
#story 
story = [
    "你不知道自己是什麼時候開始「想回家」的。",
    "這個世界沒有天空。",
    "只有一條筆直的路。",
    "——『歡迎來到家』。",
    "延伸到看不見的黑暗裡。還有一個聲音。",
    "你低頭，看見自己的手在顫抖。",
    "掌心裡握著五瓶藥水，像是某種預先準備好的救命手段。",
    "你不記得自己是誰。但你知道",
    "你要回去"
]
container = st.empty()

with container.container():
    for i in story:
        st.success(i)
        time.sleep(2)

st.snow()
time.sleep(3)
container.empty()
image_area = st.empty()
with image_area.container():
    st.image(
        "data:image/jpeg;base64,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",
     caption="'歡迎來到家,這是一個只有一關的遊戲，你將在這裡操縱一名想要回家的角色打敗這一關的怪物,你將在這裡操縱一名想要回家的角色打敗這一關的怪物"
)
time.sleep(3)
image_area.empty()

#設定
import streamlit as st
st.subheader("玩家設定")

#name
name = st.text_input("輸入一個名字")
if st.button("確定這名字"):
 st.session_state["player_name"] = name
 st.success(f"{name}呀,真不錯")
#gender
gender = st.selectbox("選擇一個性別 ", ["男", "女", "中", "一個性別",])
if st.button("確定這性別"):
    if gender == "男":
       st.write("呀勒勒，看來你沒懂阿,哈哈")
       st.title("G A M E  O V E R")
       st.stop()
    elif gender == "女":
       st.write("呀，真是可惜")
       st.title("G A M E  O V E R")
       st.stop()
    elif gender == "中":
       st.write("你是在？")
       st.title("G A M E  O V E R")
       st.stop()
    elif gender == "一個性別":
       st.write("真是聰明")
       answer = st.text_input("你還記得自己是誰嗎？")
       if answer == "阿燁":
        st.error("你怎麼知道你是誰的？你重新了嗎？")
        time.sleep(2)
        st.success("恭喜通關")
        st.balloons()
       elif answer==name:st.write("沒事,看來你記憶蠻好的")
       else:
         print("ok你沒了")
         st.title("G A M E  O V E R")
         st.stop()

       





