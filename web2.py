import streamlit as st

st.subheader("打折計算機")
st.header("打折計算機")

# ===== 蘋果 =====
st.image("https://waapple.org/wp-content/uploads/2021/06/Variety_Cosmic-Crisp-transparent-658x677.png", caption="蘋果 $20")

apple_price = 20
st.write(f"原價：${apple_price}")

apple_amount = st.number_input("蘋果幾個？", 0, 30, 1, step=1)
apple_discount = st.slider("蘋果打幾折？", 10, 90, 50)

if st.button("計算蘋果"):
    final_price = apple_price * apple_amount * (apple_discount / 100)
    st.header(f"折後價格：${final_price:.0f}")


# ===== 草莓 =====
st.image("http://m.fodizi.tw/uploadfile/201203/24/2314233545.jpg", caption="草莓 $100")

strawberry_price = 100
st.write(f"原價：${strawberry_price}")

strawberry_amount = st.number_input("草莓幾斤？", 0, 30, 1, step=1)
strawberry_discount = st.slider("草莓打幾折？", 10, 90, 50)

if st.button("計算草莓"):
    final_price = strawberry_price * strawberry_amount * (strawberry_discount / 100)
    st.header(f"折後價格：${final_price:.0f}")


# ===== 假瀏海 =====
st.image("https://tshop.r10s.com/37f/b88/7685/14b9/6036/bf66/f005/1188ee84b70242ac110002.jpg?_ex=486x486", caption="假瀏海 $10")

fakebangs_price = 10
st.write(f"原價：${fakebangs_price}")

fakebangs_amount = st.number_input("假瀏海幾個？", 0, 30, 1, step=1)
fakebangs_discount = st.slider("假瀏海打幾折？", 10, 90, 50)

if st.button("計算假瀏海"):
    final_price = fakebangs_price * fakebangs_amount * (fakebangs_discount / 100)
    st.header(f"折後價格：${final_price:.0f}")


# ===== 假髮 =====
st.image("https://down-tw.img.susercontent.com/file/sg-11134201-22110-e6wrevmprfkvdd", caption="假髮 $10")

wig_price = 10
st.write(f"原價：${wig_price}")

wig_amount = st.number_input("假髮幾個？", 0, 30, 1, step=1)
wig_discount = st.slider("假髮打幾折？", 10, 90, 50)

if st.button("計算假髮"):
    final_price = wig_price * wig_amount * (wig_discount / 100)
    st.header(f"折後價格：${final_price:.0f}")