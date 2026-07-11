import streamlit as st
st.subheader(" 瘋狂填詞遊戲")

name = st.text_input("輸入一個名字")
place = st.text_input("輸入一個地點")
action = st.selectbox("選擇一個動作", ["示愛", "睡覺", "吃泡麵", "唱歌",])
exaggerate_amount = st.number_input("誇張程度？", 0, 5, 1, step=1)
if st.button("生成故事"):
    if exaggerate_amount ==1:
        st.success(f"有一天，{name}  走到了 {place}，突然開始 {action}，路人表示！")
    elif exaggerate_amount ==2:
     st.success(f"有一天，{name}  跳到了 {place}，突然開始 {action}，路人一看，也跟著一起了！")
    elif exaggerate_amount ==3:
     st.success(f"有一天，一位阿公 跳到了{name}身上，路人看到，趕快拉著{name}和阿公飛到了{place}接著突然開始 {action} ,{name}和阿公很開心！")
    elif exaggerate_amount ==4:
       st.success(f"有一天，一隻小鳥 跳到了{name}身上，於是{name}趕快飛起來到小鳥身上,接著突然開始 {action} ,路人便將他們送到了{place}然後小鳥開始 {action},{name}覺得遇到知音了，於是他們結婚了")
    elif exaggerate_amount ==5:
       st.success(f"有一天，一隻小鳥 瘋狂陰暗潮濕爬行在{name}身上，於是{name}趕快爬到{place},接著突然開始 {action} ,路人摸著鬍鬚道：「好久沒看到少爺這麼開心了")   