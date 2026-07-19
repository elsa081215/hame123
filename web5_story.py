import streamlit as st
import time
import random
if "HP" not in st.session_state:
    st.session_state.HP = 100
from datetime import datetime

now = datetime.now()
hour = now.hour
if st.button("音樂"):
    st.video = "https://youtu.be/BHfL4ns7-CM"
if 0 <= hour < 3:

    st.info("🌙 深夜登入")

    st.write("黑市老闆：今天也是熬夜的一天嗎？")    
#台詞庫
st.session_state.monster_tasks = {
            "摸摸小貓",
            "餵小狗",
            "看小魚",
            "看鴉子",
            "猜數字",
        }
tasks = st.session_state.monster_tasks

attack_lines = [
    "少爺好久沒笑的那麼開心了",
    "大家，不要再為了我而吵架了",
    "67",
    "沒錯，我就是傳說中的小學生",
    "阿巴阿巴",
    "不要如此輕易放棄啊喂",
    "蛋糕店裡賣蛋糕，菜市場裡賣辣椒",
    "咕咕嘎嘎",
    "我的刀盾",
    "比比拉布",
    "呦呦呦，破防哥／姐",
    "巴卡巴卡",
    "61",
    "x D",
    "住手！你們住手！不要再打了！",
    "牛逼，特拉斯",
    "666,你個老6",
    "我很抱歉但我挺爽的",
    "我不知道啊我不知道啊",
    "本來應該「從從容容、游刃有餘」，現在卻是「匆匆忙忙、連滾帶爬」",
    "這麼可愛真是抱歉",
    "筆電筆電丟進垃圾桶",
    "阿嬤特拉斯",
    "家人們誰懂啊",
    '嘉豪',
    "跳躍不是罪過",
   

]
#儲存
if "battle_count" not in st.session_state:
    st.session_state.battle_count = 0
if "story_done" not in st.session_state:
    st.session_state.story_done = False
if "image_done" not in st.session_state:
    st.session_state.image_done = False
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "gender_pass" not in st.session_state:
    st.session_state.gender_pass = False
if "ask_started" not in st.session_state:
    st.session_state.ask_started = False
if "story2_done" not in st.session_state:
    st.session_state.story2_done = False   
if "hidden_end" not in st.session_state:
    st.session_state.hidden_end = False 
if "favor" not in st.session_state:
    st.session_state.favor = 0  
if "jiazhen_count" not in st.session_state:
    st.session_state.jiazhen_count = 0 
if "score" not in st.session_state:
    st.session_state.score = 0    
if "buy_history" not in st.session_state:
    st.session_state.buy_history = []  
if "author_room" not in st.session_state:
    st.session_state.author_room = False  
if "show_diary" not in st.session_state:
    st.session_state.show_diary = False  
if "show_pc" not in st.session_state:
    st.session_state.show_pc = False
if "answered" not in st.session_state:
    st.session_state.answered = False    
if "title_67" not in st.session_state:
    st.session_state.title_67 = False  
if "page" not in st.session_state:
    st.session_state.page = "chat" 
if "ending_lover" not in st.session_state:
    st.session_state.ending_lover = False
if "show_811" not in st.session_state:
    st.session_state.show_811 = False  
if "cat_reward_lv2" not in st.session_state:
    st.session_state.cat_reward_lv2 = False
if "cat_reward_lv3" not in st.session_state:
    st.session_state.cat_reward_lv3 = False
if "cat_reward_lv4" not in st.session_state:
    st.session_state.cat_reward_lv4 = False  
if "cat_67" not in st.session_state:
    st.session_state.cat_67 = False  
if "dog_67" not in st.session_state:
    st.session_state.dog_67 = False
if "endings" not in st.session_state:
    st.session_state.endings = []    
if "math_index" not in st.session_state:
    st.session_state.math_index = 0    
if "radio_count" not in st.session_state:
        st.session_state.radio_count = 0    
if "dog_reward_lv2" not in st.session_state:
    st.session_state.dog_reward_lv2 = False
if "dog_reward_lv3" not in st.session_state:
    st.session_state.dog_reward_lv3 = False
if "dog_reward_lv4" not in st.session_state:
    st.session_state.dog_reward_lv4 = False 
if "ending_catdog" not in st.session_state:
    st.session_state.ending_catdog = False  
if "answered" not in st.session_state:
    st.session_state.answered = False    
if "true_end" not in st.session_state:
    st.session_state.true_end = False 
if "endings" not in st.session_state:
    st.session_state.endings = {}
if "replay" not in st.session_state:
    st.session_state.replay = None 
if "ending_monster" not in st.session_state:
    st.session_state.ending_monster = False
if "plant_level" not in st.session_state:
    st.session_state.plant_level = 0  
if "math_event" not in st.session_state:
    st.session_state.math_event = False
if "snail_step" not in st.session_state:
    st.session_state.snail_step = 0
if "guess_answer" not in st.session_state:
    st.session_state.guess_answer = random.randint(1, 100)
if "guess_times" not in st.session_state:
    st.session_state.guess_times = 0  
if "ending_cheater" not in st.session_state:
    st.session_state.ending_cheater = False  
if "shop_cost" not in st.session_state:
    st.session_state.shop_cost = 0
if "ending_shop" not in st.session_state:
    st.session_state.ending_shop = False 
if "egg_stage" not in st.session_state:
    st.session_state.egg_stage = 0
if "chick_name" not in st.session_state:
    st.session_state.chick_name = "小雞"           
#咪咪
if "cat_grade" not in st.session_state:
    st.session_state.cat_grade = 1
if "cat_favor" not in st.session_state:
    st.session_state.cat_favor = 0    
if "cat_name" not in st.session_state:
    st.session_state.cat_name = "小黑"
if "score" not in st.session_state:
    st.session_state.score = 0    
#狗狗
if "dog_grade" not in st.session_state:
    st.session_state.dog_grade = 1   
if "dog_favor" not in st.session_state:
    st.session_state.dog_favor = 0     
if "dog_name" not in st.session_state:
    st.session_state.dog_name = "小白" 
#拍照
if "photos" not in st.session_state:
    st.session_state.photos = []   
if "photos" not in st.session_state:
    st.session_state.photos = [] 
#小遊戲
if "memory_point" not in st.session_state:
    st.session_state.memory_point = 0

if "ending_photo" not in st.session_state:
    st.session_state.ending_photo = False 
#魚    
if "fish_favor" not in st.session_state:
    st.session_state.fish_favor = 0
if "chair_count" not in st.session_state:
    st.session_state.chair_count = 0
if "math_index" not in st.session_state:
    st.session_state.math_index = 0    

if st.session_state.favor < 0:
        title = "仇人"

elif st.session_state.favor <=50:
            title = "陌生人"

elif st.session_state.favor < 100:
            title = "普通玩家"

elif st.session_state.favor < 150:
            title = "朋友"

elif st.session_state.favor <= 811:
            title = "重要的人"
            
elif st.session_state.favor <= 1000:
            title = "摯友"                  
elif st.session_state.favor <= 5000:
            title = "家人"
else:
            title = "愛人"   
 #@@@
            

story = [
    "你不知道自己是什麼時候開始「想回家」的。",
    "阿嘉:我也不知道。",
    "這個世界沒有天空。",
    "阿嘉：在公殺小。",
    "只有一條筆直的路。",
    "阿嘉：土木工程做得不錯。",
    "——『歡迎來到家』。",
    "延伸到看不見的黑暗裡。還有一個聲音。",
    "你低頭，看見自己的手在顫抖。",
    "阿嘉:呦手抖哥",
    "掌心裡握著五瓶藥水，像是某種預先準備好的救命手段。",
    "你不記得自己是誰。但你知道",
    "你要回去"
]
#story2
story2=[
    "《家》",
    "你不知道自己是什麼時候開始想回家的。",
    "你只知道，自己醒來時站在一條沒有盡頭的路上。",
    "天空不存在,風不存在。",
    '這個世界只剩下黑暗。',
    "以及一句不斷重複的話。",
    "「歡迎來到家。」",
    "於是你踏上旅程。",
    "打敗怪物。",
    "收集碎片。",
   "尋找回家的方法。",
   "直到最後，你發現了一個真相。",
   "這個遊戲，原本就不是給外人玩的。它是某一家人親手創造出來的。",
   "怪物不是怪物。他是父親。",
   "旁白不是旁白。她是母親。",
   "一直在旁邊吐槽、嘲笑玩家的阿嘉，也不是什麼神秘存在。",
   "她只是妹妹。",
   "而你操控的角色。",
   "那個名叫阿燁的人,是她的哥哥。",
   "他死在十八歲那年。",
   "剛成年。",
   "本該擁有燦爛的未來。",
   "本該進入理想的大學。",
   "本該交到新的朋友。",
   "本該看見更多的風景。",
   "本該擁有漫長的人生。",
   "但這一切都沒有發生。",
   "因為某一天。",
   "一名穿越者來到了他們的世界。",
   "他們的世界其實是一本小說。",
   "穿越者不是壞人,他沒有惡意。",
   "甚至不知道自己的出現會改變什麼。",
   "然而因為劇情的推動,因為故事需要繼續前進。",
   "阿燁死了。",
   "後來。",
   "穿越者知道了真相,知道自己間接奪走了一個人的人生。",
   "他後悔,他愧疚,他拼命想補償",
   "他做了自己能做到的一切。",
   "可是死人不會復活",
   "小說的結局裡",
   "所有人都原諒了穿越者",
   "父母原諒了他,妹妹原諒了他,所有人都接受了這個結局",
   "故事迎來圓滿的 Happy Ending。",
   "讀者感動落淚",
   "穿越者最後也成功回到了自己的家",
   "可是沒有人問過他們願不願意",
   "沒有人問過失去兒子的父母願不願意原諒,沒有人問過失去哥哥的妹妹願不願意接受",
   "他們只是被劇情強迫著露出笑容",
   "被作者強迫著說出那句：「沒關係，我原諒你。」",
   "可是怎麼可能沒關係？",
   "死掉的人是他們最愛的人,那是他們的兒子,那是她的哥哥",
   "於是",
   "他們拒絕了故事的結局,拒絕了作者安排的命運,拒絕了那份虛假的原諒",
   "代價是"
   "他們被困在遊戲"
   "名字叫做《家》",
   "並將自己的靈魂留在裡面",
   "把身體獻給世界",
   "永遠困在這座由思念與執念組成的牢籠",
   "天道説",
   '給他們時間決定',
   "他們想報仇嗎？或許有一點。",
   "他們恨穿越者嗎？或許曾經恨過。",
   "但真正支撐他們留在這裡的",
   "其實不是仇恨,而是思念",
   "他們只是想把阿燁帶回來,僅此而已",
   "阿嘉其實知道,穿越者不是壞人",
   "她知道哥哥如果還活著，一定會原諒對方",
   "她知道這一切都是遷怒。",
   "她知道自己做的是錯的。",
   "可",
   "每當她想到那一天",
   "想到哥哥倒下的身影,想到哥哥再也回不來,想到哥哥的人生永遠停留在十八歲",
   "她就無法說服自己放下",
   "於是她只能一遍又一遍地等待",
   "等待奇蹟發生,等待有人推開那扇門,等待那個熟悉的身影再次出現",
   "然後輕輕地對她說：「阿嘉，我回家了。」",
   "擁抱她,",
   "如平常跟她嬉鬧，然後嗆爸爸，爸爸委屈的跟媽媽說，一家人吵吵鬧鬧的，度過一天",
   "可是她知道",
   "那個人永遠不會回來了",
   "而這",
   "就是《家》的故事"
]
story3=[
    "阿嘉：你知道嗎？",
    "阿嘉：其實我跟哥哥以前常常吵架。",
    "阿嘉：因為我喜歡貓。",
    '阿燁喜歡狗。',
    "阿嘉：而且我們都覺得自己才是對的。",
    "阿嘉：哥哥是狗奴。",
    "阿嘉：我是貓奴。",
    '阿嘉：所以每天都在吵。',
    "......",
    "阿嘉：有一天放學。",
    "阿嘉：我跟哥哥看到路邊有個紙箱。",
    '阿嘉：裡面有一隻小貓。',
    '阿嘉：還有一隻小狗。',
    "阿嘉：那天很冷。",
    '阿嘉：小貓依偎在小狗旁邊。',
    "阿嘉：箱子上面有一張紙。",
    "「抱歉。」",
    "「請您養他們吧。」",
    "......噗",
    '阿嘉：然後我們就把牠們撿回家了。',
    "阿嘉：當然。",
    "阿嘉：回家先吃了一頓竹筍炒肉絲。",
    "阿嘉：不過最後還是養了。",
    "阿嘉：我幫貓咪取名。",
    "阿嘉：世界無敵可愛的小咪咪。",
    "阿嘉：超可愛好不好。",
    "結果",
    "阿燁：......",
    "阿燁：這算什麼名字？",
    "阿嘉：哪裡不好？",
    "阿嘉：超可愛好不好。",
    '阿燁：那我的比較好。',
    "阿燁：我幫狗狗取名。",
    "阿燁：願昭熙。",
    "阿嘉：太難記了吧！",
    '阿燁：願他有光明的未來。',
    "阿燁：很好聽啊。",
    "阿嘉：哪裡好聽？",
    "阿燁：那妳那個名字又哪裡正常？太長了吧！",
    "然後我們又吵起來了。",
    '爸爸：狗狗叫小白。',
    "媽媽：貓咪叫小黑。",
    "阿嘉：不要！",
    "阿燁：不要！",
    "全家：？？？？？？",
    "結果全家一起吵。",
    "最後決定。",
    "小黑跟小白是小名。",
    "願昭熙跟世界無敵可愛的小咪咪是真名。",
    "阿嘉：雖然根本沒人在叫真名。",
    "阿嘉：但哥哥很滿意。",
    "我也很滿意。",
    "阿嘉：其實。",
    "阿嘉：你養的這隻貓。",
    "阿嘉：就是那隻小黑。",
    "阿嘉：狗狗也是。",
    "阿嘉：進來之前。",
    "阿嘉：我們已經把牠們安置好了。",
    "阿嘉：我們以為牠們會有新的家。",
    "可是第二天,牠們自己跑回來了。怎麼趕都不走。",
    "阿嘉：笨死了。",
    "阿嘉：後來。",
    "我做了一個夢。",
    "夢裡。",
    "小黑趴在我腿上。",
    "小白躺在哥哥旁邊。",
    "牠們說：",
    "「沒關係,一起去吧,就算被困在那裡也沒關係,因為家人在一起」",
    "笨蛋",
    "阿嘉：不過",
    "阿嘉：謝謝牠們",
    "阿嘉：也謝謝你",
]
story4=[
    "……",
    "阿嘉：",
    '「你知道嗎？」',
    "「我們不是第一次來這裡。」",
    "「很久以前。」",
    "「爸爸媽媽也來過。」",
    '「那時候。」',
    "「我們遇見了一個人。」",
    "「他自稱──黑市老闆。」",
    "黑市老闆：",
    "「想變強嗎？」",
    "「想變強嗎？」",
    "「不用犧牲任何東西。」",
    "「只要接受我的交易。」",
    '爸爸：「真的？」',
    "黑市老闆：「當然,我從不騙（人）。」",
    "阿嘉：「爸爸相信了,他一直想保護我們所以他接受了。」",
    "一開始。",
    "爸爸真的變強了。",
    "怪物也打得過。",
    "受傷也會恢復。",
    "大家都很高興。",
    "直到有一天。",
    '直到有一天。',
    "爸爸開始忘記事情。",
    "開始不認識我們。",
    "開始變得越來越暴躁。",
    "媽媽：「你還好嗎……？」爸爸：「……」",
    "爸爸：我……是誰？」",
    "阿嘉：「後來我們才知道。」",
    "「黑市老闆沒有說謊。」",
    "「他真的沒有收走任何東西。」",
    "「因為……」",
    "「代價不是當下支付。」",
    "「而是慢慢地。」",
    "「把一個人變成怪物。」",
    "阿嘉：「爸爸最後變成了怪物。」",
    "阿嘉：「……」",
    "「你是不是也覺得……不用代價就能變強，很方便？」",
    "「可是。」"
    "你真的沒有付出代價嗎？」"
]


#圖
container = st.empty()
if not st.session_state.story_done:
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
    st.session_state.story_done = True
#設定
import streamlit as st
st.subheader("玩家設定")
#name
name = st.text_input("輸入一個名字", value=st.session_state.player_name)
if st.button("確定這名字"):
 if name:
    st.session_state["player_name"] = name
    st.success(f"{name}呀,真不錯")
    st.write("阿嘉:喔")
 else:
        st.warning("你還沒輸入名字")
#gender
if st.session_state.player_name:
        gender = st.selectbox("選擇一個性別 ", [ "男", "女", "中", "一個性別"])
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
        st.session_state.gender_pass = True
#你還記得自己是誰嗎？
if st.session_state.gender_pass:

    answer = st.text_input("你還記得自己是誰嗎？")

    # 玩家提交答案
    if st.button("提交答案"):

        if answer.strip() == "阿燁":

            st.session_state.hidden_end = True

            st.error("你怎麼知道你是誰的？")

            time.sleep(2)
            st.write("阿嘉愣住了。")

            time.sleep(2)
            st.write("短暫的沉默。")

            time.sleep(2)
            st.write("她盯著那兩個字看了很久。")

            time.sleep(3)
            st.write("阿燁。")

            time.sleep(1)
            st.write("那是她哥哥的名字。")

            time.sleep(1)
            st.write("也是這個遊戲真正的主角。")

            time.sleep(1)
            st.write("她曾經無數次想像過。")

            time.sleep(2)
            st.write("如果哥哥能回來。")

            time.sleep(2)
            st.write("如果有一天，他能再次站在自己面前。")

            time.sleep(3)
            st.write("那該有多好。")

            time.sleep(3)
            st.write("阿嘉：......")

            time.sleep(2)
            st.write("阿嘉：哥哥？")

            time.sleep(4)
            st.write("沒有回應。")

            time.sleep(1)
            st.write("她低下頭笑了笑。")

            time.sleep(1)
            st.write("只是那笑容有點難看。")

            time.sleep(2)
            st.write("阿嘉：也是。")

            time.sleep(2)
            st.write("阿嘉：我到底在期待什麼啊。")

            st.success("隱藏結局：等待的人 已解鎖")

        elif answer == name:

            st.write("沒事，看來你記憶蠻好的")
            st.write("阿嘉：我還是比較喜歡阿燁")

        else:

            st.write("ok,你沒了")
            st.title("G A M E  O V E R")
            st.stop()

    # 隱藏結局按鈕
    if st.session_state.hidden_end:

        st.success("已解鎖隱藏結局：等待的人")

        if st.button("查看隱藏結局"):

            container = st.empty()

            with container.container():

                story_box = st.empty()
                text = ""

                for line in story2:
                    text += line + "\n\n"
                    story_box.markdown(text)
                    time.sleep(1)

            st.session_state.story2_done = True

            st.info(
                "《家》不是一個關於復仇的故事，而是一家人明明知道死去的人不會回來，卻依然不願放手的故事。"
            )  
# 系統檢查           
if st.button("系統檢查"):
    event = random.randint(1,6)

    if event == 1:
        st.error("錯誤：角色資料損毀")

    elif event == 2:
        st.warning("警告：發現異常記憶")

    elif event == 3:
        st.error("錯誤：玩家不存在")

    elif event == 4:
        st.error("錯誤：阿嘉已離線")

    else:
        st.success("系統正常")
        st.write("阿嘉：我亂按的。")

    #黑化值
class prison:
    def __init__(self):
        self.blackening_value = 0
      

    def add_blackening(self, value):
        self.blackening_value += value

        # 上限保護
        self.blackening_value = min(self.blackening_value, 100)

        st.write(f" 黑化值 +{value} → {self.blackening_value}/100")

    def is_dead(self):
        return self.blackening_value >= 100

    def show(self):
        st.write(f" 黑化值目前：{self.blackening_value}/100")
        if self.blackening_value == 10:
            st.write("阿嘉：你是不是不太會玩")

        elif self.blackening_value == 30:
            st.write("阿嘉：你真的有在按按鈕嗎")

        elif self.blackening_value == 50:
            st.write("阿嘉：我開始懷疑你是故意的")

        elif self.blackening_value == 70:
            st.write("阿嘉：好玩嗎")

        elif self.blackening_value == 90:
            st.write("阿嘉：我想回家")

        elif self.blackening_value == 100:
            st.write("阿嘉：算了，我不陪你玩了")
if "prison" not in st.session_state:
    st.session_state.prison = prison()   
#阿嘉

       
        #角色    
class Player:
    def __init__(self, bag, prison,HP):
        self.HP = HP
        self.bag = bag
        self.prison = prison
    def atk(self, monster):
        damage = 10
        monster.hp -= damage
        st.write(f"你攻擊造成 {damage} 傷害")
    def take_damage(self, damage):
        st.session_state.HP -= damage
        st.write(f"你受到 {damage} 傷害")    
class bag: 
    def __init__(self, elixir, date=0, ): #初始生命值和date
        
        self.elixir = elixir
        self.date = date
    def oneday(self):
        self.date += 1
        st.session_state.HP -= 1
    def use_elixir(self):
        if self.elixir > 0:
            self.elixir -= 1
            st.session_state.HP += 20
            st.write("使用藥水 HP +20")
        else:
            st.write("沒有藥水了！")   
if "player" not in st.session_state:
    my_bag = bag(elixir=5)
    st.session_state.player = Player(my_bag, st.session_state.prison)

alen = st.session_state.player
#  Bag 功能
st.write("初始 HP:", st.session_state.HP)
st.write("初始 date:", alen.bag.date)
st.write("藥水數量:", alen.bag.elixir)

st.write("過一天 ")
alen.bag.oneday()

st.write("HP:", st.session_state.HP)
st.write("date:", alen.bag.date)

if st.button("背包喝藥水"):
    alen.bag.use_elixir()
st.write("HP:", st.session_state.HP)
st.write("藥水剩餘:", alen.bag.elixir)
#  Monster怪物 
class monster:
    def __init__(self, hp=100, atk=20, speed=50):
        self.hp = hp
        self.atk = atk
        self.speed = speed

    def attack(self):
        self.speed += random.randint(5, 28)

        crit = random.randint(1, 100)

        if crit <= 1:
            st.error(" 致命暴擊!666哥們運氣也是夠好的")
            st.write("阿嘉：欸不是,1%的機率")
            return self.atk * 4
        
        elif crit <= 35:
            st.warning("暴擊！")
            st.write("阿嘉：哈哈")
            return self.atk * 3
        
        return self.atk
    def is_alive(self):
        return self.hp > 0
if "monster" not in st.session_state:
    st.session_state.monster = monster()
m = st.session_state.monster

  # 玩家結束
def check_player_dead():
    if st.session_state.HP <= 0:
        st.write("你被擊敗，被關進監獄")

        st.session_state.HP += 57
        st.write("你重新站起來 HP回復到57")

        # 黑化
        alen.prison.add_blackening(10)
        alen.prison.show()

        if alen.prison.is_dead():
            st.write("阿嘉:你確定要回家？")
            st.title(" G A M E O V E R(黑化結局）")
            st.stop()
#台詞           
def get_attack_line():
    return random.choice(attack_lines)
# 手機
with st.sidebar:

    st.header("手機")
    temp = random.randint(20, 50)
    st.write(f"🌡️ 手機溫度：{temp}°C")
    if temp >= 45:
        st.write("阿嘉：你的手機快熟了。")
    st.write("手機電量101%")
    st.write(f"你的hp,  {st.session_state.HP}")
    st.write(f"阿嘉好感度{st.session_state.favor}")
    st.write(f"貓好感度{st.session_state.cat_favor}")
    st.write(f"狗好感度 {st.session_state.dog_favor}")
    lazy_level = min(int(st.session_state.favor / 100), 100)
    st.write(f"閒度指數：{lazy_level}%")
    if lazy_level >= 100:
        st.success("隱藏成就：真的很閒")
        st.session_state.idle_master = True
    from datetime import datetime
    now = datetime.now()
    st.write("🕒現在時間")
    st.write(datetime.now().strftime("%H:%M:%S"))
    if now.hour == 3:
        st.write("阿嘉：這時間還沒睡？")
    import random    
    if st.button("🍀今日運勢"):
        fortunes = [
            "大吉：今天會有好事發生。",
            "中吉：平凡也是一種幸福。",
            "小吉：摸摸貓咪吧。",
            "吉：狗狗好像很開心。",
            "末吉：不要亂按奇怪按鈕。",
            "凶：阿嘉心情似乎不太好。",
            "大凶：作者今天可能又要寫 Bug。"
        ]
        result = random.choice(fortunes)
        st.success(result)
        if "阿嘉" in result:
            st.write("阿嘉：關我什麼事。")    
            st.success(random.choice(fortunes))
    if "lucky_number" not in st.session_state:
        st.session_state.lucky_number = random.randint(1, 100)
    st.write(f"🎲 今日幸運數字：{st.session_state.lucky_number}")
    num = st.session_state.lucky_number
    if num == 67:
        st.write("阿嘉：......")
        st.write("阿嘉;怎麼又是67。")
    elif num == 1:
        st.write("阿嘉：第一名。")
    elif num == 100:
        st.write("阿嘉：滿分？")
    if st.button("🎲 重抽幸運數字"):
        st.session_state.lucky_number = random.randint(1, 100)    
        st.write("阿嘉：運勢不是這樣玩的吧。")
    if "mood" not in st.session_state:
        st.session_state.mood = "正常"   
    import random
    if random.randint(1, 10) == 1:
        st.session_state.mood = random.choice(
            ["快樂", "無聊", "想睡", "懷疑人生", "過度自信"]
        )     
    st.write(f"玩家心情：{st.session_state.mood}")    
    #st.write(f"📊 成就完成度：{achievement_now}/{achievement_total}")
    achievement_total = 10
    achievement_now = 0
    if st.session_state.get("title_67", False):
        achievement_now += 1
    if st.session_state.get("ending_lover", False):
        achievement_now += 1

    if st.session_state.get("ending_catdog", False):
        achievement_now += 1

    if st.session_state.cat_favor >= 820:
        achievement_now += 1

    if st.session_state.favor >= 11451:
        achievement_now += 1

    if st.session_state.jiazhen_count >= 67:
        achievement_now += 1

    if st.session_state.cat_grade >= 4:
        achievement_now += 1

    if st.session_state.dog_grade >= 4:
        achievement_now += 1
    if st.session_state.get("idle_master", False):
        achievement_now += 1 
    if st.session_state.chair_count >= 20 : 
        achievement_now += 1


    if achievement_now == achievement_total:
        st.success("🏆 全成就達成") 
    elif achievement_now >= achievement_total - 1:
        st.write("阿嘉：還差一點。")
    elif achievement_now >= achievement_total // 2:
        st.write("阿嘉：你是不是很閒。")       
    st.write(f"成就完成度：{achievement_now}/{achievement_total}") 

    if "show_gallery" not in st.session_state:
                st.session_state.show_gallery = False

    if st.button("=結局圖鑑"):
                st.session_state.show_gallery = True

    if st.session_state.show_gallery:

                st.subheader(" 結局圖鑑")

                endings = [
                    ("hidden_end", "等待的人"),
                    ("ending_lover", "夢想"),
                    ("true_end", "家"),
                    ("ending_catdog", "箱子裡的約定"),
                    ("ending_photo", "留在照片裡的人"),
                    ("ending_cheater", "作弊仔"),
                    ("ending_shop", "貪婪"),
                ]

                unlocked = 0
                can_watch = []

                for key, title in endings:
                    if st.session_state.get(key, False):
                        st.success(f"{title}")
                        unlocked += 1
                        can_watch.append(title)
                    else:
                        st.write("❓ ??")

                st.divider()

                st.write(f"結局進度：{unlocked}/{len(endings)}")

                if unlocked < 1:
                    st.info("請先解鎖結局才能使用回放。")
                else:
                    st.success("🎉 回放系統已解鎖！")
                if st.button(" 關閉圖鑑"):
                    st.session_state.show_gallery = False
                    st.rerun()

                    act = st.radio(
                        "選擇要觀看的結局",
                        can_watch
                    )

                    st.divider()         
                    container = st.empty()

                    if act== "等待的人" :  
                                        with container.container():

                                                story_box = st.empty()
                                                text = ""

                                                for line in story2:
                                                    text += line + "\n\n"
                                                    story_box.markdown(text)
                                                    time.sleep(1)

                                        st.session_state.story2_done = True

                                        st.info(
                                                "《家》不是一個關於復仇的故事，而是一家人明明知道死去的人不會回來，卻依然不願放手的故事。"
                                            )   
                    if act== "夢想" : 
                                    st.success("已解鎖隱藏結局2:愛人")
                                    st.write(f"阿嘉：{st.session_state.player_name}，謝謝你")
                                    st.write(f"阿嘉：{st.session_state.player_name}，")
                                    st.write("阿嘉：......")
                                    st.write("阿嘉：你知道嗎？")
                                    st.write("阿嘉：我以前其實想當舞蹈生。")

                                    st.write("阿嘉：哥哥大我三歲。")
                                    st.write("阿嘉：小時候他總說我跳舞像鴨子。")

                                    st.write("阿嘉：明明說很難看。")
                                    st.write("阿嘉：卻每次都坐在第一排看。")
                                    st.write("阿嘉：後來發生很多事。")
                                    st.write("阿嘉：夢想也不見了。")
                                    st.write("阿嘉：......")
                                    st.write(f"阿嘉：{st.session_state.player_name}。")
                                    st.write("阿嘉：如果有一天我重新站上舞台。")
                                    st.write("阿嘉：你會來看嗎？")   
                    if act =="箱子裡的約定":
                                    st.balloons()
                                    st.success("已解鎖隱藏結局3:箱子裡的約定") 
                                    container = st.empty()

                                    with container.container():

                                            story_box = st.empty()
                                            text = ""

                                            for line in story3:
                                                text += line + "\n\n"
                                                story_box.markdown(text)
                                                time.sleep(1)
                                    st.info(
                                            "其實家從來不是地方,是有人願意一起回去。"
                                        ) 
                    if act=="留在照片裡的人":
                                    st.success(" 隱藏結局4:留在照片裡的人")
                                    st.write("阿嘉：......")
                                    time.sleep(1)

                                    st.write("阿嘉：其實我知道。")

                                    time.sleep(2)

                                    st.write("阿嘉：哥哥不會回來了。")

                                    time.sleep(1)

                                    st.write("阿嘉：只是我一直不敢把這些東西收起來。")

                                    time.sleep(1)

                                    st.write("阿嘉：因為我怕有一天。")

                                    time.sleep(1)

                                    st.write("阿嘉：連他的樣子都忘記。")

                                    time.sleep(1)

                                    st.write("阿嘉：......")

                                    st.write("阿嘉：謝謝你陪我整理完。")
                    if act=="作弊仔":
                                        story_cheat = [
                                        "……",
                                        "阿嘉：等等。",
                                        "阿嘉：你第一次就猜中了？",
                                        "阿嘉：不可能。",
                                        "阿嘉：……",
                                        "阿嘉：作者。",
                                        "阿嘉：是不是有人偷看程式？",
                                        "（系統正在檢查玩家……）",
                                        "沒有發現異常。",
                                        "阿嘉：蛤？",
                                        "阿嘉：真的假的。",
                                        "阿嘉：那你今天運氣也太好了吧。",
                                        "阿嘉：害我以為有人開外掛。",
                                        "🏆 隱藏結局：作弊仔"
                                    ]
                                        container = st.empty()

                                        with container.container():

                                                story_box = st.empty()
                                                text = ""

                                                for line in story_cheat:
                                                    text += line + "\n\n"
                                                    story_box.markdown(text)
                                                    time.sleep(1)
                                                st.error(" 偵測到可疑玩家。")
                                                time.sleep(2)
                                                st.success("檢查完成。")
                                                st.write("……")
                                                st.write("系統：只是運氣很好。")
                    if act=="貪婪":
                                    box = st.empty()
                                    text = ""
                                    for line in story4:

                                        text += line + "\n\n"

                                        box.markdown(text)

                                        time.sleep(1)

                                    st.balloons()
                    if act== "家" : 
                                    st.success("已解鎖主結局:家")
                                    st.write(f"阿嘉：{st.session_state.player_name}")
                                    st.write("阿嘉：牛逼,尼著麼知道是打812")
                                
    if st.button("黑市") :
        st.session_state.page = "shop"
    if st.button("阿嘉聊天室"):
            st.session_state.page = "chat"
    if title in ["家人", "愛人"]:
        if st.button("作者房間"):
            st.session_state.page = "r00m" 
    if st.button("查看手機通知"):
        st.session_state.page = "line"  
    if st.button("強大的力量"):
        st.session_state.page = "questions"          
    if st.button("系統功能"):
        st.session_state.page = "two"  
    if st.button("咪咪"):
        st.session_state.page = "cat" 
    if st.button("狗狗"):        
        st.session_state.page = "dog"
    if st.button("魚"):
       st.session_state.page = "fish"  
    if st.button("小鴨子"):
       st.session_state.page = "duck" 
    if st.button("小雞孵化器"):
       st.session_state.page = "egg"          
    if st.button("整理紙箱"):
        st.session_state.page = "box" 
    if st.button("小盆栽"):
       st.session_state.page = "plant" 
    if st.button("🗿"):
       st.session_state.page = "chair"    
    if st.button("蝸牛"):
       st.session_state.page = "snails"    
    if st.button("猜數字") :
       st.session_state.page = "guess"   
    if st.button("香蕉皮") :
       st.session_state.page = "banana"           
    #系統功能
if st.session_state.page == "two":    
    st.subheader("系統功能")
    if st.button("離開遊戲"):
        st.write("阿嘉：你以為按了就能走？")
    if st.button("刪除存檔"):
        st.error("刪除失敗")
        st.write("阿嘉：這裡根本沒有存檔。")
    if st.button("聯絡作者"):
        st.write("正在搜尋作者...")
        time.sleep(2)
        st.write("搜尋失敗")
        st.write("阿嘉：他跑路了。") 
    if st.button("聯絡阿嘉"):
        st.write("阿嘉：幹嘛？")
    if st.button("查看真相"):
        st.write("權限不足")
        st.write("阿嘉：還沒到時候。")    
    if st.button("阿燁"):
        st.write("......")
        st.write("阿嘉：")
        time.sleep(1)
        st.write("不要拿我哥哥開玩笑。")
    if st.button("重設遊戲"):     
        st.write("阿嘉：你以為我沒想到嗎？")
        time.sleep(1)
        st.write("重設失敗")  
    if st.button("67"):     
        st.write("阿嘉:Six-seven")  

#阿嘉聊天室
if st.session_state.page == "chat":
    st.subheader("阿嘉聊天室")
    st.write("跟大美女說話")
    if st.button("阿嘉開講"):
        event = random.randint(1,20)

        if event == 1:
            st.write("阿嘉：其實我知道這裡是遊戲。")
            time.sleep(1)
            st.write("阿嘉：但作者不知道自己在寫什麼。")
            st.session_state.favor += 2
        elif event == 2:
            st.write("阿嘉：我昨天夢到自己變成 Streamlit。")
            st.write("阿嘉：醒來發現更可怕。")
            st.write("阿嘉：我本來就在 Streamlit 裡。")
            st.session_state.favor += 3
        elif event == 3:
            st.write("阿嘉：如果你看到這段。")
            st.write("阿嘉：代表作者又在偷塞彩蛋。")
            st.session_state.favor += 5
        else:
            st.write("阿嘉：沒什麼好說的。")
            st.write("阿嘉：只是按鈕放著不用很浪費。")
            st.session_state.favor += 2

    if st.button("尼好") : 
        st.write("阿嘉：不好。")
        st.session_state.favor += 2
    if st.button("阿燁？"):     
        st.write("阿嘉：別突然提他。")
        st.session_state.favor -= 20
    if st.button("妳還好嗎") :     
        st.write("阿嘉：不好")
        st.session_state.favor += 10
    if st.button("妳為何叫阿嘉？") :     
        st.write("阿嘉：我本名叫嘉珍,嘉卉各承時，珍禽盡擇棲,是我哥哥取的,好聽嗎？")
        st.session_state.favor += 10  
    if st.button("好聽") :   
        st.write("阿嘉：我也覺得")
        st.session_state.favor += 5
    if st.button("不好聽") :   
        st.write("阿嘉：真像")
        st.session_state.favor += 2 
    if st.button("67?") :   
        st.write("阿嘉：無聊")
        time.sleep(1)
        st.write("阿嘉:Six-seven")
        st.session_state.favor += 2
    st.divider()
    st.write("笑話系")     
    if st.button("跟我說笑話"):     
        st.write("阿嘉:you")  
        st.session_state.favor += 2  
    if st.button("跟我說冷笑話"):     
        st.write("阿嘉:冷笑話")
        st.session_state.favor += 1     
    if st.button("冷笑話"):     
        st.write("阿嘉:小馬的哥哥叫什麼？") 
        time.sleep(2)
        st.write("阿嘉:歐巴馬") 
        st.session_state.favor += 2   
    if st.button("冷笑話2"):     
        st.write("阿嘉:請問要怎麼變成一個暖男？") 
        time.sleep(2)
        st.write("阿嘉:火化") 
        st.session_state.favor += 2 
    if st.button("冷笑話3"):     
        st.write("阿嘉:什麼皇帝最漂亮?") 
        time.sleep(2)
        st.write("阿嘉:秦始皇，因為他暴政（爆正）") 
        st.session_state.favor += 4
    if st.button("冷笑話4"):     
        st.write("阿嘉:狗的英文叫 dog,那臘腸狗的英文怎麼拚？") 
        time.sleep(2)
        st.write("阿嘉:doooooooog") 
        st.session_state.favor += 4  
    if st.button("冷笑話5"):     
        st.write("阿嘉:小白＋小白=?") 
        time.sleep(2)
        st.write("阿嘉:小白兔(two)") 
        st.session_state.favor += 4   
    if st.button("冷笑話6"):     
        st.write("阿嘉:香菇走在路上被柳橙撞到，香菇大怒叫柳橙去死，柳橙就真的去死了，為什麼？") 
        time.sleep(2)
        st.write("因為菌要橙死，橙不敢不死......") 
        st.session_state.favor += 4  
    if st.button("冷笑話7"):     
        st.write("怪物:愚公移山的時候唱什麼歌？") 
        time.sleep(2)
        st.write("阿嘉:...")
        st.write("移山移山，亮晶晶") 
        st.session_state.favor += 2
    st.divider()
    if st.button("我餓了") :
        if st.session_state.favor >= 50:
            st.image("https://waapple.org/wp-content/uploads/2021/06/Variety_Cosmic-Crisp-transparent-658x677.png", caption="蘋果 ")  
            st.write("阿嘉:諾")
            st.session_state.HP += 20
            st.session_state.favor += 3
        elif 0<= st.session_state.favor < 50:   
            st.image("https://askthescientists.com/wp-content/uploads/2021/04/AdobeStock_240042551-400x400.jpeg")
            st.write("阿嘉:哈哈")
            st.session_state.favor += 3
        else :  
            st.write("阿嘉：......")
            time.sleep(2)
            st.write("阿嘉：你覺得我會給你東西吃？")
            st.session_state.favor -= 3
    if st.button("今天過得怎樣？"):
        st.write("阿嘉：跟昨天差不多。")
        st.session_state.favor += 3
    if st.button("妳幾歲？"):
        st.write("阿嘉：女孩子的年齡是秘密。")
        
    if st.button("妳喜歡什麼？"):
        st.write("阿嘉：睡覺。")
        st.session_state.favor += 3
    if st.button("妳討厭什麼？"):
        st.write("阿嘉：玩家。")

    if st.button("妳有朋友嗎？"):
        st.write("阿嘉：以前有。")
        st.session_state.favor += 3
    if st.button("妳是美女嗎？"):
        st.write("阿嘉：當然。")
        st.session_state.favor += 5

    if st.button("我是帥哥"):
        st.write("阿嘉：喔。")
        st.session_state.favor += 2
    if st.button("我是美女"): 
        st.write("阿嘉：你開心就好。") 
        st.session_state.favor += 2  

    if st.button("我很有錢"):
        st.write("阿嘉：那借我。")
        st.session_state.favor += 3
    if st.button("這遊戲好玩嗎？"):
        st.write("阿嘉：不好玩你還玩。")
    if st.button("妳幾公斤？"):
        st.write("阿嘉：秘密。")
    if st.button("我很窮"):
        st.write("阿嘉：巧了，我也是。") 
        st.session_state.favor += 3
    if st.button("68"):
        st.write("阿嘉：你故意的吧。") 
        st.session_state.favor += 2
    if st.button("作者很帥"):
        st.write("阿嘉：你是不是被威脅了。")
        st.session_state.favor += 3
    if st.button("咕咕嘎嘎"):
        st.write("阿嘉:gugugaga。")
        st.session_state.favor += 3
    if st.button("妳會飛嗎"):
        st.write("阿嘉：會掉下來。")
        st.session_state.favor += 3
    if st.button("妳會游泳嗎"):
        st.write("阿嘉：會沉下去。")
        st.session_state.favor += 3
    if st.button("妳會魔法嗎"):
        st.write("阿嘉：會把玩家變笨。")
        st.session_state.favor += 3
    if st.button("妳有男朋友嗎"):
        st.write("阿嘉：沒有。")
        st.session_state.favor += 2
    if st.button("那女朋友呢"):
        st.write("阿嘉：也沒有。")
        st.session_state.favor += 2
    if st.button("我渴了"):
        st.write("阿嘉：喝西北風。")
        st.session_state.favor += 3
    if st.button("我想吃蛋糕"):
        st.write("阿嘉：蛋糕店裡賣蛋糕。")
        st.session_state.favor += 5
    if st.button("菜市場呢"):
        st.write("阿嘉：菜市場裡賣辣椒。")
        st.session_state.favor += 5
    if st.button("妳笨"):
        st.write("阿嘉：彼此彼此。")
        st.session_state.favor += 1
    if st.button("妳很兇"):
        st.write("阿嘉：謝謝誇獎。")

    if st.button("妳好可愛"):
        st.write("阿嘉：這麼可愛真是抱歉。")
        st.session_state.favor += 5

    if st.button("妳有病"):
        st.write("阿嘉：作者病得比較重。")
        st.session_state.favor -= 5
    if st.button("今天天氣如何"):
        st.write("阿嘉：沒有天氣。")
        st.session_state.favor += 3

    if st.button("妳很漂亮"):
        st.write("阿嘉：我知道。")
        time.sleep(1)
        st.write("阿嘉：不用重複。")
        st.session_state.favor += 5

    if st.button("妳很醜"):
        st.write("阿嘉：謝謝。")
        time.sleep(1)
        st.write("阿嘉：你也不差。")
        st.session_state.favor -= 5

    if st.button("我要睡覺"):
        st.write("阿嘉：恭喜。")
        time.sleep(1)
        st.write("阿嘉：你完成了人生主線任務。")
        st.session_state.favor += 2

    if st.button("妳是 AI 嗎"):
        st.write("阿嘉：不是。")
        time.sleep(1)
        st.write("阿嘉:AI 至少比較有禮貌。")
        st.session_state.favor += 2

    if st.button("我要上廁所"):
        st.write("阿嘉：這種事不用跟我報備。")
        st.session_state.favor += 1

    if st.button("我可以抱抱妳嗎"):
        if st.session_state.favor >= 5000:
            st.write("阿嘉：嘖。")
            st.write("阿嘉：不行")
            st.write("阿嘉：(害羞的別過頭)")
            st.session_state.favor += 10 
        else:
            st.write("阿嘉：不行。")    
            time.sleep(1)
            st.write("阿嘉：你連碰撞箱都沒有。")
            st.session_state.favor -= 2   

    if st.button("妳在幹嘛"):
        actions = [
            "發呆。",
            "等玩家犯蠢。",
            "想哥哥。",
            "懷疑人生。",
            "看作者拖更。"
        ]
        st.write("阿嘉：" + random.choice(actions))
        st.session_state.favor += 2

    if st.button("我是天才"):
        st.write("阿嘉：那太好了。")
        time.sleep(1)
        st.write("阿嘉：終於有人能修作者的 Bug。")
        st.session_state.favor += 1         
            
    if st.session_state.favor >= 70:
        st.divider()
        st.write("已解鎖新對話")

        if st.button("妳有夢想嗎？"):
            st.write("阿嘉：以前有。")
            st.session_state.favor += 5

        if st.button("妳怕黑嗎？"):
            st.write("阿嘉：不怕。")
            st.write("阿嘉：我已經待在黑暗裡太久了。")
            st.session_state.favor += 2

        if st.button("妳會想離開這裡嗎？"):
            st.write("阿嘉：不知道。") 
        if st.button("跳躍不是罪過"):
            st.session_state.favor += 2
            st.video("https://www.youtube.com/watch?v=Z2vPBphLHJo")     


    if "jiazhen_count" not in st.session_state:
        st.session_state.jiazhen_count = 0

    if st.session_state.favor >= 150:

        if st.button("嘉珍"):

            st.session_state.jiazhen_count += 1

            count = st.session_state.jiazhen_count

            if count == 1:
                st.write("阿嘉：！？")
                time.sleep(2)
                st.write("阿嘉：已經很久沒人這樣叫我了。")
                st.session_state.favor += 20

            elif count == 2:
                st.write("阿嘉：誒，我在。")
                st.session_state.favor += 20       
            elif count == 3:
                st.write("阿嘉：怎麼了？")
                st.session_state.favor += 10
            elif count == 4:
                st.write("阿嘉：你今天很喜歡叫我名字欸。")
                st.session_state.favor += 10
            elif count == 5:
                st.write("阿嘉：你是要把以前缺的都補回來哦？")
                st.session_state.favor += 10

            elif count <= 10:
                talks = [
                    "阿嘉：我有在聽。",
                    "阿嘉：叫一次就聽得到啦。",
                    "阿嘉：嗯？",
                    "阿嘉：幹嘛一直叫我。",
                    "阿嘉：你是不是很閒。"
                ]
                st.write(random.choice(talks))
                st.session_state.favor += 10
            elif count == 11:
                st.write("阿嘉：......")
                time.sleep(1)
                st.write("阿嘉：其實這樣也不討厭。")
                st.session_state.favor += 20

            elif count <= 13:
                st.write("阿嘉：嘉珍已讀。")
                st.write(f"{name}好啦我在")
                st.session_state.favor += 20

            elif count ==14 :
                        st.write(f"{name}好啦我在")
                        st.write(f"{name}你很閒耶")
                        st.session_state.favor += 15
            elif count ==15 :
                        st.write(f"{name}好啦我在")
                        st.write("阿嘉:你總共叫了我15次。")
                        st.write(f"{name}你真的很閒耶")
                        st.session_state.favor += 15   
            elif count ==16 :
                        st.write(f"{name}{name}{name}{name}{name}")
                        st.write(f"{name}{name}{name}{name}")
                        st.session_state.favor += 10   
            elif count ==17:
                        st.write(f"{name}{name}{name}{name}{name}")
                        st.write(f"喔,尼叫我那麼多次,幹嘛啦")
                        st.session_state.favor += 10 
            elif count == 18:
                st.write(f"阿嘉：{name}你是不是把聊天室玩成點擊遊戲了。")
                st.session_state.favor += 10

            elif count == 19:
                st.write("阿嘉：再叫下去我要收費了。")
                st.session_state.favor += 10

            elif count == 20:
                st.write("阿嘉：恭喜達成成就。")
                st.write("阿嘉：『嘉珍召喚師 Lv.1』")
                st.session_state.favor += 20

            elif count == 25:
                st.write("阿嘉：欸。")
                st.write("阿嘉：我真的有那麼好叫嗎？")
                st.session_state.favor += 20   
            elif count < 30:
                st.write("阿嘉：你還在叫啊。")
                st.session_state.favor += 3 
            elif count == 30:
                st.write("阿嘉：你知道嗎？")
                st.write("阿嘉:正常人不會叫別人名字30次。")
                st.session_state.favor += 30
            elif count == 40:
                st.write("阿嘉：......")
                st.write("阿嘉：我開始有點習慣了。")
                st.session_state.favor += 40
            elif count < 50:
                st.write("阿嘉：......")
                st.write("阿嘉：你是不是把這當主線了。")
                st.session_state.favor += 3
            elif count == 50:
                st.write("阿嘉:50次。")
                st.write("阿嘉：你是真的很閒。")
                st.session_state.favor += 50
            elif count < 60:
                st.write("阿嘉:50幾次了欸。")
                st.write(f"阿嘉:{name},50幾次了欸。")
                st.session_state.favor += 3
            elif count == 60:
                st.write("阿嘉:再7次。")
                st.write("阿嘉：你應該知道我要說什麼。") 
            elif count == 66:
                st.write("阿嘉：再一次。")      
            elif count == 67:
                st.write("阿嘉：......")
                st.write("阿嘉:你總共叫了我67次。")
                st.write("阿嘉：你真的很奇怪。")
                st.write("阿嘉：你是小學生拔？。")
                st.session_state.title_67 = True
                if st.session_state.get("title_67", False):
                    st.success("稱號：嘉珍召喚師")
                st.session_state.favor += 67  
            elif count == 100:
                st.write("阿嘉：......")
                st.write("阿嘉:100次。")
                st.write("阿嘉：你真的辦到了。")
                st.write("阿嘉：")
                st.write("阿嘉：謝謝你。")
                st.session_state.favor += 100 
            elif count < 200:
                st.write("阿嘉：......")
                st.write("阿嘉：我開始懷疑你是不是掛機。")
                st.session_state.favor += 20    
            elif count == 200:
                st.write("阿嘉:200次。")
                st.write("阿嘉：你到底有多閒。")
                st.write("阿嘉：......")
                st.write("阿嘉：不過還是謝謝你。")  
                st.session_state.favor += 200
            elif count == 404:
                st.error("阿嘉不存在")
                st.write("阿嘉：騙你的，我在。")
                st.session_state.favor += 50
            elif count == 520:
                st.write("阿嘉:520。")
                st.write("阿嘉：不要亂想。")
                st.write("阿嘉：我只是剛好看到數字。") 
                st.session_state.favor += 52 
            elif count == 666:
                st.write("阿嘉:666。")
                st.write("阿嘉：作者是不是又在亂寫東西。")
                st.session_state.favor += 66               
            if (
                st.session_state.favor == 811
                and not st.session_state.get("show_811", False)
            ):
                st.write("阿嘉：差一點。")
                st.write("阿嘉：真的就一點。")
                st.session_state.show_811 = True 

            if (
                st.session_state.favor >= 5000
                and not st.session_state.get("ending_lover", False)
            ):
                st.session_state.ending_lover = True
                st.success("已解鎖隱藏結局2:愛人")
                st.write(f"阿嘉：{name},謝謝你")
                st.write(f"阿嘉：{name}")
                st.write("阿嘉：......")
                st.write("阿嘉：你知道嗎？")
                st.write("阿嘉：我以前其實想當舞蹈生。")

                st.write("阿嘉：哥哥大我三歲。")
                st.write("阿嘉：小時候他總說我跳舞像鴨子。")

                st.write("阿嘉：明明說很難看。")
                st.write("阿嘉：卻每次都坐在第一排看。")
                st.write("阿嘉：後來發生很多事。")
                st.write("阿嘉：夢想也不見了。")
                st.write("阿嘉：......")
                st.write(f"阿嘉：{name}。")
                st.write("阿嘉：如果有一天我重新站上舞台。")
                st.write("阿嘉：你會來看嗎？")
            else:           
                st.write(f"{name}夠了拉")
                st.session_state.favor += 15

        if st.button("我會陪妳"):
            if  st.session_state.favor >=5000:
                st.write("阿嘉：......")
                st.write(f"阿嘉：{name}")
                time.sleep(1)
                st.write("阿嘉：好")
                st.session_state.favor += 15
            else:    
                st.write("阿嘉：......")
                time.sleep(2)
                st.write("阿嘉：別隨便說這種話。")
                st.session_state.favor += 10

        if st.session_state.favor >= 300:

            st.write("特殊對話")

            if st.button("妳想哥哥嗎？"):
                st.write("阿嘉：......")
                time.sleep(2)
                st.write("阿嘉：每天都想。")

            if st.button("妳後悔嗎？"):
                st.write("阿嘉：後悔什麼？")
                st.write("阿嘉：活著嗎？")

            if st.button("如果阿燁回來呢？"):
                st.write("阿嘉：別開玩笑。")    

    if st.button("你是誰?"):
        if (
            st.session_state.favor >= 6000
            and st.session_state.jiazhen_count >= 100):

                st.write("阿嘉：你明明知道我是誰。")
                st.write("阿嘉;畢竟你叫了我100次以上。")
                st.write("阿嘉;而且還把好感刷到6000。")
                st.write("阿嘉：笨蛋。")
                st.session_state.favor += 10    

        elif st.session_state.favor >= 5000:
            st.write("阿嘉：你想被我揍吧？")
            st.write("阿嘉：哼哼，聽好了。")
            st.write("阿嘉：我是嘉珍大美女 xD")
            st.session_state.favor += 10

        elif st.session_state.jiazhen_count >= 100:
            st.write("阿嘉：你明明知道。")
            st.session_state.favor += 5

        elif st.session_state.jiazhen_count >= 67:
            st.write("阿嘉:你怎麼做到叫我67次的?")
            st.write("阿嘉：......")
            st.write("阿嘉：我是嘉珍。")
            st.write("阿嘉：也是一個傻子。")
            st.session_state.favor += 6.7
        else:
                st.write("阿嘉：大美女。")    

    if st.button("阿嘉妳最喜歡誰"):
        if random.randint(1,100)  <= 5:
            st.write("阿嘉：哥哥。")
            st.session_state.favor += 20
        else:
            st.write("阿嘉：反正不是你。") 
            st.session_state.favor += 10
    if st.button("說幹話"):
        talks = [
            "阿嘉：人如果不呼吸，就不會吸到空氣。",
            "阿嘉：根據我的觀察，今天就是今天。",
            "阿嘉：睡不著的時候可以閉上眼睛。",
            "阿嘉：錢不是萬能的，因為我沒有。",
            "阿嘉：只要不失敗，就不會成功。",
            "阿嘉：人生最大的遺憾，就是有遺憾。",
            "阿嘉：我發現一件事,阿嘉：發現需要發現才能發現",
            "阿嘉：如果你覺得自己很窮。阿嘉：那代表你還有感知能力。",
            "阿嘉：世界上最快的東西是什麼？阿嘉：是我快沒耐心了。",
            "阿嘉：會游泳的人通常比較會游泳。",
            "阿嘉：根據統計。""阿嘉:有87%的人會相信統計。",
            "阿嘉：如果事情沒有變好。阿嘉：那就是還沒變好。",
            "阿嘉：當你照鏡子的時候。阿嘉：鏡子也在照你。",
            "阿嘉：不要熬夜。阿嘉：因為我也在熬。",
            "阿嘉：只要活著。阿嘉：就代表你目前沒死。",
            "阿嘉：失敗乃成功之母。阿嘉：但成功不一定認媽",
            "阿嘉：今天吃飯了嗎？",
            "阿嘉：沒吃記得吃。",
            "阿嘉：吃了當我沒說。",
            "阿嘉：其實我有超能力。",
            "阿嘉：能精準預測作者什麼時候不更新。阿嘉：答案是現在。",
            "阿嘉：你知道什麼叫自律嗎？阿嘉:me",
            "阿嘉：人生沒有過不去的坎。阿嘉：有些直接把人埋了",
        ]

        st.write(random.choice(talks))               
    if st.session_state.favor >= 10000:
        st.write("阿嘉：......")
        st.write("阿嘉：一萬？")
        st.write("阿嘉：等等。")
        st.write("阿嘉：你真的刷到一萬了？")
        st.write("阿嘉：你到底把這遊戲玩成什麼樣子了。")
        st.write("阿嘉：")
        st.write("阿嘉：你是不是根本沒在跑主線。")
    if st.session_state.favor >= 11451:
        st.success("隱藏稱號：家")
        st.write("阿嘉：你知道嗎？")
        st.write("阿嘉：其實『家』不是地點。")
        st.write("阿嘉：是有人等你的地方。")    

  
    st.write(f" 阿嘉好感度：{st.session_state.favor}")      
    st.write(f"關係：{title}")
#作者房間
if st.session_state.page == "r00m":
    if title =="家人"or title=="愛人":
        st.success("作者房間已解鎖")

        if st.button("進入作者房間"):
            st.session_state.author_room = True
        if st.session_state.author_room:
                st.write("作者:居然真的有人刷到812以上好感。")
                st.write("作者：你是不是太閒了？")
                st.write("阿嘉：我也是這麼想的。")
                st.success("隱藏彩蛋：作者日誌")
                st.write("""
                        開發日誌：

                        其實阿嘉是最早誕生的角色。

                        《家》原本不是恐怖遊戲。

                        只是後來，
                        她一直不肯讓故事結束。
                        """)

                if st.button("查看作者日記"):
                    st.session_state.show_diary = True

                if st.session_state.show_diary:
                    st.write("Day 1")
                    st.write("我要做一個小遊戲。")

                    st.write("Day 7")
                    st.write("為什麼變成這樣？")

                    st.write("Day 15")
                    st.write("阿嘉戲份比主角還多。")

                    st.write("Day 31")
                    st.write("我不知道誰才是主角。")

                    st.write("Day 67")
                    st.write("67")
                if st.button("刪除《家》"):
                    st.session_state.show_pc=True
                    if st.session_state.show_pc:
                        st.write("刪除中...")
                        time.sleep(2)

                        st.error("失敗")

                        st.write("阿嘉：")

                        time.sleep(1)

                        st.write("阿嘉：別鬧。")

                        time.sleep(1)

                        st.write("阿嘉：如果連這裡都沒了。")

                        time.sleep(2)

                        st.write("阿嘉：我就真的見不到哥哥了。")
                if st.button("呼叫作者"):
                    st.write("作者：嗨。")
                    time.sleep(1)
                    st.write("作者：其實我也不知道後面怎麼寫。")
                    time.sleep(1)
                    st.write("作者離開了。")
                    st.write("搜尋失敗。")
                if st.button("偷看隱藏檔案"):
                    st.write("讀取中...")
                    time.sleep(2)

                    st.error("警告")

                    st.write("阿嘉：")

                    time.sleep(1)

                    st.write("阿嘉：你怎麼跑到這裡來的？")

                    time.sleep(1)

                    st.write("阿嘉：作者！")

                    time.sleep(1)

                    st.write("阿嘉：你的門又沒鎖！")        
#咪咪
if st.session_state.page == "cat": 
    #au au 升級    
    if (
    st.session_state.cat_favor >= 100
    and not st.session_state.cat_reward_lv2
    ):
        st.session_state.cat_grade = 2
        st.session_state.HP += 20
        st.session_state.cat_reward_lv2 = True
        st.success(f"{st.session_state.cat_name}升到 Lv.2!")

    if (
        st.session_state.cat_favor >= 300
        and not st.session_state.cat_reward_lv3
    ):
        st.session_state.cat_grade = 3
        st.session_state.HP += 50
        st.session_state.cat_reward_lv3 = True
        st.success(f"{st.session_state.cat_name}升到 Lv.3!")

    if (
        st.session_state.cat_favor >= 700
        and not st.session_state.cat_reward_lv4
    ):
        st.session_state.cat_grade = 4
        st.session_state.HP += 400
        st.session_state.cat_reward_lv4 = True
        st.success(f"{st.session_state.cat_name}升到 Lv.4!")     
        st.write(f"{st.session_state.cat_name}已經把你當家人了。")
        st.write("阿嘉：......")
        st.write("阿嘉：這很好")

    st.title("貓咪")
    st.write(f"貓咪：{st.session_state.cat_name}")
    st.write(f"等級：{st.session_state.cat_grade}")
    st.write(f"好感度：{st.session_state.cat_favor}")
    cat_name = st.text_input("幫貓咪取名")
    if st.button("改名字"):
        if cat_name:
            st.session_state.cat_name = cat_name
            st.success("改名成功")
    if st.button("摸摸貓咪"):
        events = [
        f"{st.session_state.cat_name},呼嚕呼嚕。",
        f"{st.session_state.cat_name},蹭了蹭你的手。",
        f"{st.session_state.cat_name}, 咬你。",
       f"{st.session_state.cat_name} ,睡著了。"
    ]
        st.write(random.choice(events))
        st.write("喵～")
        st.session_state.cat_favor += 3

    if st.button("餵食貓咪"):
        st.write("喵喵！")
        st.session_state.cat_favor += 5
    if st.session_state.cat_favor == 67:
        st.write(f"{st.session_state.cat_name}:......")
        st.write(f"{st.session_state.cat_name}:67。")    
    if (
        st.session_state.cat_favor >= 67
        and not st.session_state.get("cat_67", False)
    ):
        st.write("阿嘉：等等。")
        st.write("阿嘉:連貓都開始67了?")
        st.session_state.cat_67 = True
    if st.session_state.cat_favor >= 520:
        st.write(f"{st.session_state.cat_name}躺到你腿上。")
        st.write("呼嚕呼嚕...")    
    if st.session_state.cat_favor >= 5200:
        st.success("稱號解鎖：貓奴")
        st.write("阿嘉：你是不是把養貓玩成主線了。") 
    if st.session_state.cat_favor >= 670:
        st.write(f" {st.session_state.cat_name}......")
        st.write(f"{st.session_state.cat_name} 67")  
        st.write("阿嘉：")  
        st.write("阿嘉：不要教貓奇怪的東西。")
    if st.session_state.cat_grade >= 2:
        if st.button("抱抱貓咪"):
            st.write(f"{st.session_state.cat_name}跳到你懷裡。")
            tasks["摸摸小貓"] = True
            st.write("呼嚕呼嚕...")
            st.session_state.cat_favor += 5  
        if st.button("玩逗貓棒"):
            events = [
                "咻——！追了出去。",
                " 一巴掌拍飛逗貓棒。",
                " 假裝沒看到。",
                "玩到翻肚。"
            ]
            st.write(random.choice(events))
            st.session_state.cat_favor += 10
        import os
    import streamlit as st
    if "photos" not in st.session_state:
        st.session_state.photos = []

    if "cat_favor" not in st.session_state:
        st.session_state.cat_favor = 0

    if st.session_state.cat_grade >= 3:
        import os
        if st.button("拍貓咪照片"):

            img_path = "/Users/zhangpeizhen/Downloads/6F4EF228-75F9-410E-B2B1-3CE9E1D0CC0A.png"

            if os.path.exists(img_path):
                st.image(img_path)
            else:
                st.error("圖片不存在")

            st.write(f"你拍下了 {st.session_state.cat_name}")

            st.session_state.photos.append(img_path)
            st.session_state.cat_favor += 15

    if st.session_state.cat_grade >= 4:

        if st.button("一起睡覺"):

            st.write(f"{st.session_state.cat_name}窩在你旁邊睡著了。")
            st.write("呼嚕呼嚕...")
            st.session_state.cat_favor += 20                    
    #au au 升級    
    if (
    st.session_state.cat_favor >= 100
    and not st.session_state.cat_reward_lv2
    ):
        st.session_state.cat_grade = 2
        st.session_state.HP += 20
        st.session_state.cat_reward_lv2 = True
        st.success(f"{st.session_state.cat_name}升到 Lv.2!")

    if (
        st.session_state.cat_favor >= 300
        and not st.session_state.cat_reward_lv3
    ):
        st.session_state.cat_grade = 3
        st.session_state.HP += 50
        st.session_state.cat_reward_lv3 = True
        st.success(f"{st.session_state.cat_name}升到 Lv.3!")

    if (
        st.session_state.cat_favor >= 700
        and not st.session_state.cat_reward_lv4
    ):
        st.session_state.cat_grade = 4
        st.session_state.HP += 400
        st.session_state.cat_reward_lv4 = True
        st.success(f"{st.session_state.cat_name}升到 Lv.4!")     
        st.write(f"{st.session_state.cat_name}已經把你當家人了。")
        st.write("阿嘉：......")
        st.write("阿嘉：這很好")

#狗狗
if st.session_state.page == "dog": 
    st.title("狗狗") 
    st.write(f"狗狗：{st.session_state.dog_name}")
    st.write(f"等級：{st.session_state.dog_grade}")
    st.write(f"好感度：{st.session_state.dog_favor}")
    dog_name = st.text_input("幫狗狗取名")
    if st.button("改名字"):
        if dog_name:
            st.session_state.dog_name = dog_name
            st.success("改名成功")   
    if st.button("摸摸狗狗"):

        events = [
            f"{st.session_state.dog_name}開心地搖尾巴。",
            f"{st.session_state.dog_name}撲到你身上。",
            f"{st.session_state.dog_name}舔了舔你的手。",
            f"{st.session_state.dog_name}興奮地轉圈圈。"
        ]
        st.write(random.choice(events))
        st.session_state.dog_favor += 3
    if st.button("餵食狗狗"):
        st.write("汪！")
        st.session_state.dog_favor += 5
    if (
        st.session_state.dog_favor >= 67
        and not st.session_state.dog_67
    ):

        st.write(f"{st.session_state.dog_name}：汪！")
        st.write(f"{st.session_state.dog_name};67!")
        st.write("阿嘉：")
        st.write("阿嘉：連狗也開始了？")
        st.session_state.dog_67 = True 
    if st.session_state.dog_grade >= 2:

        if st.button("丟球"):

            events = [
                "咻——",
                "狗狗衝了出去！",
                "撿回來了！",
                "又叼回來了！"
            ]

            st.write(random.choice(events))
            st.session_state.dog_favor += 10
    if st.session_state.dog_grade >= 3:

        if st.button("一起散步"):
            st.write(f"{st.session_state.dog_name}開心地跑來跑去。")
            st.session_state.dog_favor += 15
    if st.session_state.dog_grade >= 4:

        if st.button("一起看家"):
            st.write(f"{st.session_state.dog_name}坐在你旁邊。")
            st.write("汪。")
            st.session_state.dog_favor += 20                      
    if (
    st.session_state.dog_favor >= 100
    and not st.session_state.dog_reward_lv2
):
        st.session_state.dog_grade = 2
        st.session_state.HP += 20
        st.session_state.dog_reward_lv2 = True
        st.success(f"{st.session_state.dog_name}升到 Lv.2!")
        st.write("（沒有聲音，但你好像聽見有人說：不愧是狗狗）")
    if (
        st.session_state.dog_favor >= 300
        and not st.session_state.dog_reward_lv3
    ):
        st.session_state.dog_grade = 3
        st.session_state.HP += 50
        st.session_state.dog_reward_lv3 = True
        st.success(f"{st.session_state.dog_name}升到 Lv.3!")

    if (
        st.session_state.dog_favor >= 700
        and not st.session_state.dog_reward_lv4
    ):
        st.session_state.dog_grade = 4
        st.session_state.HP += 400
        st.session_state.dog_reward_lv4 = True
        st.success(f"{st.session_state.dog_name}升到 Lv.4!")     
        st.write(f"{st.session_state.dog_name}已經把你當家人了。")
        st.write("阿嘉：......")
        st.write("阿嘉：這很好")         
    if (
    st.session_state.cat_grade >= 4
    and st.session_state.dog_grade >= 4
    and not st.session_state.ending_catdog
):
        st.session_state.ending_catdog = True
        st.balloons()
        st.success("已解鎖隱藏結局3:箱子裡的約定") 
        container = st.empty()

        with container.container():

                story_box = st.empty()
                text = ""

                for line in story3:
                    text += line + "\n\n"
                    story_box.markdown(text)
                    time.sleep(1)
        st.info(
                "其實家從來不是地方,是有人願意一起回去。"
            ) 
if st.session_state.page == "line":
    st.title("手機通知")   
    if st.button(" 查看手機通知"):
        notifications = [
            "阿嘉：你在幹嘛？",
            "系統：有新的未知訊號進入。",
            "貓咪：喵。",
            "狗狗：汪！",
            "作者：不要一直點。",
            "系統提醒：你已經玩很久了。",
            "阿嘉：……我在看你。",
            "未知來源：你剛剛做的選擇被記錄了。",
            "手機電量：其實是假的。" , 
            "時間要按按鈕,才會更新" ,
            "時間要按按鈕,才會更新" ,
            "時間要按按鈕,才會更新" ,    
                    ] 
        st.info("消息 " + random.choice(notifications))
    if "unread" not in st.session_state:
        st.session_state.unread = 0

    if st.button("接收訊息"):
        st.session_state.unread += 1
    st.write(f"未讀訊息：{st.session_state.unread}")
if st.session_state.page == "box":

    st.title("整理紙箱")

    st.write("角落堆著幾個紙箱。")

    item = random.choice([
        "舊課本",
        "壞掉的手機",
        "全家福照片",
        "哥哥的筆記本",
        "空紙箱",
        "畢業紀念冊",
         "舊相簿"
    ])

    st.write(f"你找到：{item}")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("收起來"):

            if item in ["全家福照片", "哥哥的筆記本"]:

                st.write("好像是很重要的東西。")

                st.session_state.memory_point += 1

            else:

                st.write("只是普通物品。")
            st.session_state.box_item = random.choice(item)    
        st.write(f"物品：{st.session_state.memory_point}/5")        
    with col2:
        if st.button("丟掉"):

            st.write(f"你把{item}丟進垃圾桶。")

            st.session_state.box_item = random.choice(item)
    if (
    st.session_state.memory_point >= 5
    and not st.session_state.ending_photo
):
        st.session_state.ending_photo = True
        st.success(" 隱藏結局4:留在照片裡的人")
        st.write("阿嘉：......")
        time.sleep(1)

        st.write("阿嘉：其實我知道。")

        time.sleep(2)

        st.write("阿嘉：哥哥不會回來了。")

        time.sleep(1)

        st.write("阿嘉：只是我一直不敢把這些東西收起來。")

        time.sleep(1)

        st.write("阿嘉：因為我怕有一天。")

        time.sleep(1)

        st.write("阿嘉：連他的樣子都忘記。")

        time.sleep(1)

        st.write("阿嘉：......")

        st.write("阿嘉：謝謝你陪我整理完。")

if st.session_state.page == "plant":

    st.title("🌱 小盆栽")

    st.write(f"成長度：{st.session_state.plant_level}/100")

    if st.button("💧 澆水"):

        st.session_state.plant_level += 1

        talks = [
            "你幫盆栽澆了水。",
            "葉子看起來精神了一點。",
            "好像長高了一點。",
            "盆栽安靜地吸收著水分。",
            "變胖了",
            "好像太多了",
        ]

        st.write(random.choice(talks))
    if st.session_state.plant_level >= 10:
        st.write("長出了嫩芽")

    if st.session_state.plant_level >= 30:
        st.write("🍀 葉子變多了")

    if st.session_state.plant_level >= 67:
        st.write("🌱 盆栽:67")
        st.write("阿嘉：連植物都開始了？")

    if st.session_state.plant_level >= 100:
        st.success(" 開花了")  
    if (
    st.session_state.plant_level >= 100
    and not st.session_state.get("plant_end", False)
):

        st.session_state.plant_end = True
        st.write("阿嘉：居然開花了。")
        st.write("阿嘉：我還以為你會先放棄。")     
if st.session_state.page == "duck":

    st.title("小鴨子")

    if st.button("摸摸鴨鴨"):
        talks = [
            "嘎。",
            "嘎嘎。",
            "嘎嘎嘎。",
            "67嘎。",
            "嘎嘎嘎嘎",
            "嘎嘎嘎嘎嘎",
            "嘎嘎嘎嘎嘎嘎",
            "嘎嘎嘎嘎嘎嘎嘎",
            "嘎嘎嘎嘎嘎嘎嘎嘎",
            "嘎嘎嘎嘎嘎嘎嘎嘎嘎",
            "嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎"

        ]

        st.write(random.choice(talks))
        st.write("阿嘉：為什麼家裡會有鴨子？")

    if st.button("餵鴨鴨"):
        st.write("嘎嘎！")
    if st.button("捏鴨鴨"):  
          st.write("嘎！")
if st.session_state.page == "fish":
    if st.button("看魚"):
        talks = [
            "魚正在游泳。",
            "魚吐出了一串泡泡。",
            "魚看了你一眼。",
            "魚好像在發呆。"
        ]
        st.write(random.choice(talks))
    if st.button("餵魚"):
        st.write("魚開心地游了過來。")
        st.session_state.fish_favor += 5    
    if st.session_state.cat_grade >= 3:
        if random.randint(1,10) <= 5:
            st.write(f"{st.session_state.cat_name}正盯著魚缸。")
            st.write("阿嘉：不准吃。")
    if "fish_name" not in st.session_state:
        st.session_state.fish_name = "魚魚"
    name = st.text_input("幫魚取名")
    if st.button("改名"):
        st.session_state.fish_name = name
    st.write(f"魚的名字：{st.session_state.fish_name}")  
if st.session_state.page == "chair":
    if st.button(" 椅子"):

        st.session_state.chair_count += 1

        count = st.session_state.chair_count

        if count == 1:
            st.write("你坐下了。")

        elif count <= 5:
            st.write("你又坐下了。")

        elif count <= 10:
            st.write("你真的又坐下了。")
        elif count<=15:
            st.write('還在坐。')    
        elif count <19:
            st.write("依然在坐。")
        elif count==19 :
            st.write("啪")  
        elif count ==20:  
            st.write("成就解鎖:坐牢。")  
        else:
            st.write("啊吧啊吧")     
if st.session_state.page == "snails":
    if st.button("看看蝸牛"):
        alen.bag.HP += 1
        st.session_state.snail_step += 1

    step = st.session_state.snail_step

    st.write(f"蝸牛前進了 {step * 0.0001} 公分。")
    if step == 10:
        st.write("蝸牛好像看了你一眼。")
    elif step == 30:
        st.write("阿嘉：你真的在養蝸牛？")
    elif step == 100:
        st.write("蝸牛總共前進了 0.01 公分。")
        st.write("阿嘉：這東西是不是根本沒在動？")
    elif step == 200:
        st.write("打812")
        st.write("812")
if st.session_state.page == "guess":
    st.title("猜數字")

    st.write("猜一個 1~100 的數字！")

    guess = st.number_input(
        "請輸入數字",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("猜！"):

        st.session_state.guess_times += 1

        answer = st.session_state.guess_answer

        if guess > answer:
            st.error("太大了！")

        elif guess < answer:
            st.error("太小了！")

        else:
            if guess == st.session_state.guess_answer:
                if st.session_state.guess_times == 1:
                    st.session_state.ending_cheater = True
                    story_cheat = [
                "……",
                "阿嘉：等等。",
                "阿嘉：你第一次就猜中了？",
                "阿嘉：不可能。",
                "阿嘉：……",
                "阿嘉：作者。",
                "阿嘉：是不是有人偷看程式？",
                "（系統正在檢查玩家……）",
                "沒有發現異常。",
                "阿嘉：蛤？",
                "阿嘉：真的假的。",
                "阿嘉：那你今天運氣也太好了吧。",
                "阿嘉：害我以為有人開外掛。",
                "🏆 隱藏結局：作弊仔"
            ]
                    container = st.empty()

                    with container.container():

                        story_box = st.empty()
                        text = ""

                        for line in story_cheat:
                            text += line + "\n\n"
                            story_box.markdown(text)
                            time.sleep(1)
                        st.error(" 偵測到可疑玩家。")
                        time.sleep(2)
                        st.success("檢查完成。")
                        st.write("……")
                        st.write("系統：只是運氣很好。")    
            st.success(" 猜中了！")

            hp = random.randint(30, 80)

            st.session_state.HP += hp

            st.success(f"HP +{hp}")

            st.balloons()
            # 重新開始
            st.session_state.guess_answer = random.randint(1,100)
            st.session_state.guess_times = 0

    if st.session_state.guess_times >= 5:
        st.write("阿嘉：你到底會不會猜？")
    if st.session_state.guess_times >= 10:
        st.write("阿嘉：嘖,小b咋子,你會不會啊")
    if st.session_state.guess_times >= 15:
        st.write("阿嘉：……你好菜。")
    if st.session_state.guess_times >= 20:
        st.write("阿嘉：小小菜雞,破防勒~破防勒~")
    if st.session_state.guess_times >= 25:
        st.write("阿嘉：哈哈哈,蠢到你這種程度的,也是無敵了")  
    if st.session_state.guess_times >= 30:
        st.write("阿嘉:666,我第一次覺的自己是")      
    st.write(f"已猜：{st.session_state.guess_times} 次") 



if st.session_state.page == "shop":

    st.title("黑市")

    st.write("歡迎。")

    st.write("歡迎再次光臨。")

    st.write("這裡不用錢。")

    st.write("但是......")

    st.error("每購買一樣商品，怪物都會變強。")

    st.write(f"目前怪物強化：{st.session_state.shop_cost}")
    if st.button("觀看廣告"):

        time.sleep(3)
        st.write("yt冰情悅不用進步")
        time.sleep(0.5)
        st.write("先讓你有自信")
        time.sleep(0.5)
        st.write("畫畫很難？別怕")
        time.sleep(0.5)
        st.write("冰情悅會讓你知道，自信是比較出來的。")
        time.sleep(0.5)
        st.write("看完後，你會覺得自己畫得其實還不錯。")
        time.sleep(0.5)
        st.write("現在就去搜尋：冰情悅！")
        time.sleep(0.5)
        st.write("冰情悅：用自己的畫，點亮別人的自信")
        time.sleep(0.5)
        st.success(" youtube冰情悅求求求訂閱")
        time.sleep(0.5)
        st.success(" 廣告播放完畢！")
        time.sleep(0.5)
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlROeQF3CXmublKxCsMfXG7fFXVCXfSjBw9l6Ls0QHUg&s")
        st.session_state.shop_cost -= 10
    st.divider()

    ######商品
    ######商品
    st.subheader("黑市藥品區") 
    if st.button("HP +30"):
        st.session_state.HP += 30

        m.hp += 100

        st.session_state.shop_cost += 20

        st.success("購買成功。")
        st.session_state.buy_history.append("HP +30")
        st.write("你感覺身體變強了。")
        st.write("黑市老闆：放心，我賣的東西都有品質保證。")
        st.write("黑市老闆：副作用很小。")
        st.write("黑市老闆：大概只有九成的人會出事。")
        st.write("阿嘉：……")
        st.write("阿嘉：你剛剛是不是說了很可怕的事情？")
        time.sleep(1)
        st.write("黑市老闆：沒有。")
        st.write(" 黑市老闆：你聽錯了。")
        st.write(" 黑市老闆：我說的是『九成的人沒事』。")
        st.write("阿嘉：不是，你剛剛明明不是這樣說！")
    if st.button("止痛藥"):

        st.session_state.shop_cost += 30

        st.success("購買成功。")
        st.session_state.buy_history.append("止痛藥")
        st.write("阿嘉：有效嗎？")
        st.write("黑市老闆：很有效。")
        st.write("黑市老闆：痛的會變成別的地方。")  

    if st.button(" 過敏藥"):

        st.session_state.shop_cost += 25

        st.success("購買成功。")
        st.session_state.buy_history.append("過敏藥")
        st.write("阿嘉：可以治過敏？")
        st.write("黑市老闆：可以。")
        st.write("黑市老闆：但可能開始對重力過敏。")

    if st.button("安眠藥"):

        st.session_state.shop_cost += 40

        st.success("購買成功。")
        st.session_state.buy_history.append("安眠藥")
        st.write("黑市老闆：睡得很香。")
        st.write("阿嘉：多久？")
        st.write("黑市老闆：看運氣。")


    if st.button("眼藥水"):

        st.session_state.shop_cost += 20

        st.success("購買成功。")
        st.session_state.buy_history.append("眼藥水")
        st.write("阿嘉：眼睛變舒服了。")    
    if st.button("藥水*4"):

        alen.bag.elixir += 4

        m.hp += 80

        st.session_state.shop_cost += 80

        st.success("購買成功。")
        st.session_state.buy_history.append("藥水*4")        
        st.write("黑市老闆：買一送一！")

        time.sleep(1)

        st.write("阿嘉：真的假的？")
        st.write("黑市老闆：真的。")
        st.write("黑市老闆：買藥水，送副作用。")
        st.session_state.buy_history.append("副作用（買一送一）")

    if st.button("感冒藥") :
        st.session_state.shop_cost += 80
        st.success("購買成功。")

     
    if st.button("變強藥水"):
        st.session_state.shop_cost += 5
        alen.bag.HP += 990
        st.info("溫馨提醒:當血量不大於1000時請再買一次")
        st.info("目前怪物數量:475→476") 
        st.success(" 隱藏結局：怪物")
        st.write("你變成了怪物，但系統還沒放過你……")
        st.info("任務：完成日常偽裝行為，否則...")

    if st.button("維他命"):

        st.session_state.shop_cost += 35

        alen.bag.HP += 10

        st.success("精神好多了。")
        st.session_state.buy_history.append("維他命")
        st.write("黑市老闆：一天一顆。")
        st.write("黑市老闆：一天十顆也可以。")


    if st.button("🩹 OK繃"):

        st.session_state.shop_cost += 10

        st.success("購買成功。")
        st.session_state.buy_history.append("🩹 OK繃")
        st.write("黑市老闆：貼哪裡都可以。")
        st.write("阿嘉：貼臉呢？")
        st.write("黑市老闆：更帥。")
    st.divider()        
    st.subheader("寵物區")
    if st.button("豪華肉乾"):

        st.session_state.dog_favor += 50

    
        m.hp += 30

        st.session_state.shop_cost += 5

        st.success(f"{st.session_state.dog_name}超興奮。")
        st.write("阿嘉：副作用？")  
        st.write(f"黑市老闆：嘿嘿,{st.session_state.dog_name}來這裡,H 狗狗無敵")
        st.session_state.buy_history.append("豪華肉乾")
    if st.button("高級魚乾"):

        st.session_state.cat_favor += 50

        m.hp += 30

        st.session_state.shop_cost += 5
        st.session_state.buy_history.append("高級魚乾")
        st.success(f"{st.session_state.cat_name}很開心。")  
        st.write("阿嘉：副作用？")  
        st.write("黑市老闆：咪咪是無辜的")
    if st.button("貓紙箱"):

        st.session_state.shop_cost += 10

        st.success("購買成功。")
        st.session_state.buy_history.append("貓紙箱")
        st.write("黑市老闆：很多貓都推薦。")    

    if st.button(" 雞飼料"):

        st.session_state.shop_cost += 10

        st.success("小雞吃得很開心。")
        st.session_state.buy_history.append("雞飼料")
        st.write("小雞：啾！")

    if st.button(" 鴨飼料"):

        st.session_state.shop_cost += 10

        st.success("小鴨吃得很開心。")
        st.session_state.buy_history.append("鴨飼料")
        st.write("小鴨：嘎！")    

    if st.button(" 魚飼料"):

        st.session_state.shop_cost += 10

        st.success("小魚吃得很開心。")
        st.session_state.buy_history.append("魚飼料")
        st.write("小魚：> ~ <")  

    st.divider()
    st.subheader("黑市生活用品區") 


    if st.button(" 洗衣精"):
        st.image("https://24h.pchome.com.tw/prod/DAAK4K-A900B644H?srsltid=AfmBOorF8r8IjPC9fpTDFKPXC_BfSiQX4Ngb4zEZZL9ZxC45d0p_rilm")

        st.session_state.shop_cost += 45

        st.success("購買成功。")
        st.session_state.buy_history.append("洗衣精")
        st.write("黑市老闆：洗得很乾淨。")
        st.write("阿嘉：真的？")
        st.write("黑市老闆：連證據都洗掉。")  
        time.sleep(2)
        st.session_state.shop_cost += 45

    if st.button("水桶"):

        st.session_state.shop_cost += 50

        st.success("購買成功。")
        st.session_state.buy_history.append("水桶")

        st.write("阿嘉：有什麼用途？")
        st.write("黑市老闆：很多，我不能說。")

    
   
    if st.button(" 空盒子"):

        st.session_state.shop_cost += 1

        st.success("購買成功。")
        st.session_state.buy_history.append("空盒子")
        st.write("阿嘉：裡面什麼都沒有。")
        st.write("黑市老闆：空氣也是商品。")    
    if st.button("神奇衛生紙"):

        st.session_state.shop_cost += 3

        st.success("購買成功。")
        st.session_state.buy_history.append("神奇衛生紙")
        st.write("阿嘉：哪裡神奇？")
        st.write("黑市老闆：不會破。")
        st.write("黑市老闆：至少目前沒有。")

    if st.button("假裝很厲害眼鏡"):

        st.session_state.shop_cost += 30

        st.success("購買成功。")
        st.session_state.buy_history.append("假裝很厲害眼鏡")
        st.write("阿嘉：有什麼效果？")
        st.write("黑市老闆：戴上之後看起來很強。")
        st.write("阿嘉：只有看起來？") 
    if st.button("石頭"):

        st.session_state.shop_cost += 999

        st.success("購買成功。")
        st.session_state.buy_history.append("石頭")
        st.write("阿嘉：這不是石頭嗎？")
        st.write("黑市老闆：不是。")
        st.write("黑市老闆：這是限量石頭。")   
    
    if st.button("使用說明書（免費）"):

        st.success("獲得說明書。")
        st.session_state.buy_history.append("使用說明書")

        st.write("第一頁：")
        st.write("請不要閱讀第二頁。")

        st.write("第二頁：")
        st.write("你已經違反第一頁。")    

    if st.button("牙刷"):

        st.session_state.shop_cost += 30

        st.success("購買成功。")
        st.session_state.buy_history.append("牙刷")

        st.write("阿嘉：黑市賣牙刷？")
        st.write("黑市老闆：牙齒也是武器。")
    
    if st.button("牙膏"):

        st.session_state.shop_cost += 10
        st.session_state.buy_history.append("牙膏")
        st.success("購買成功。")

        st.write("阿嘉：有薄荷口味嗎？")
        st.write("黑市老闆：有。")
        time.sleep(2)
        st.session_state.buy_history.append("薄荷牙膏")
        st.session_state.shop_cost += 10

    if st.button("香皂"):

        st.session_state.shop_cost += 10

        st.success("購買成功。")
        st.session_state.buy_history.append("香皂")

        st.write("阿嘉：洗得乾淨嗎？")
        st.write("黑市老闆：可以洗掉罪惡感。")
        st.write("阿嘉：真的假的？。")
        st.write("黑市老闆：假的。")

    if st.button("洗髮精"):

        st.session_state.shop_cost += 10

        st.success("購買成功。")
        st.session_state.buy_history.append("洗髮精")
        st.write("黑市老闆：用了頭髮會發亮。")
        st.write("阿嘉：真的？")
        st.write("黑市老闆：頭皮也會。")


    if st.button("梳子"):

        st.session_state.shop_cost += 12

        st.success("購買成功。")
        st.session_state.buy_history.append("梳子")
        st.write("阿嘉：只是梳子？")
        st.write("黑市老闆：每天都有新髮型。")
    if st.button("衛生紙"):

        st.session_state.shop_cost += 12

        st.success("購買成功。")
        st.session_state.buy_history.append("衛生紙")
        st.write("阿嘉：跟剛剛那個神奇衛生紙有什麼差？")
        st.write("黑市老闆：這個比較正常。")    

    if st.button("雨傘"):

        st.session_state.shop_cost += 60

        st.success("購買成功。")
        st.session_state.buy_history.append("雨傘")
        st.write("阿嘉：今天沒下雨。")
        st.write("黑市老闆：人生總會下雨。")
        time.sleep(2)
        st.session_state.buy_history.append("雨傘")
        st.session_state.shop_cost += 60

    if st.button(" 掃把"):

        st.session_state.shop_cost += 5

        st.success("購買成功。")
        st.session_state.buy_history.append("掃把")
   
    if st.button(" 馬桶刷"):

        st.session_state.shop_cost += 5
        st.session_state.buy_history.append("馬桶刷")
        st.success("購買成功。")


    if st.button("拖鞋"):

        st.session_state.shop_cost += 35

        st.success("購買成功。")
        st.session_state.buy_history.append("拖鞋")

        st.write("阿嘉：好普通。")
        st.write("黑市老闆：舒服最重要。")
        time.sleep(2)
        st.session_state.shop_cost += 70
        st.session_state.buy_history.append("粉色拖鞋和紫色拖鞋")
        st.write("阿嘉：有沒有可愛一點的")
        st.write("黑市老闆：沒")

    if st.button(" 抹布"):

        st.session_state.shop_cost += 5
        st.session_state.buy_history.append("抹布")

        st.success("購買成功。")    
    if st.button("🕯️ 蠟燭"):

        st.session_state.shop_cost += 12

        st.success("購買成功。")
        st.session_state.buy_history.append("蠟燭")
        st.write("黑市老闆：停電很好用。")
        st.write("阿嘉：那不停電呢？")
        st.write("黑市老闆：氣氛。")

    if st.button(" 拖把"):

        st.session_state.shop_cost += 5
        st.session_state.buy_history.append("拖把")
        st.success("購買成功。")   
    st.divider()            
    st.subheader("食品區")
    if st.button(" 香蕉"):
        st.session_state.buy_history.append("香蕉")
        st.session_state.shop_cost += 5
        st.success("購買成功。")
        st.write("阿嘉：黑市也賣香蕉？")
        st.write("黑市老闆：補充鉀離子。")
        st.write("黑市老闆：我們很科學。")

    if st.button("吐司"):

        st.session_state.shop_cost += 10
        st.session_state.buy_history.append("吐司")

        st.success("購買成功。")

        st.write("阿嘉：這也有？")
        st.write("黑市老闆：剛出爐,很多口味")
        time.sleep(2)
        st.session_state.buy_history.append("醇香鮮奶吐司、極致濃芋泥吐司、奶酥吐司、 新鮮蔥花吐司、宇治抹茶紅豆生吐司、草莓奶酥厚切生吐司、草莓鮮奶油夾心、蜂蜜丁吐司、岩燒蜂蜜起司厚片、巧克力生吐司")
        st.session_state.shop_cost += 100


    if st.button("雞蛋"):

        st.session_state.shop_cost += 10

        st.success("購買成功。")
        st.session_state.buy_history.append("雞蛋")
        st.write("阿嘉：新鮮嗎？")
        st.write("黑市老闆：昨天還在走路。")
        st.write("阿嘉：？")
    if st.button("蘋果"):

        st.session_state.shop_cost += 10

        st.success("購買成功。")
        st.session_state.buy_history.append("蘋果")

        st.write("阿嘉：是真的蘋果？")
        st.write("黑市老闆：至少昨天還是。")

    if st.button("麵包"):

        st.session_state.shop_cost += 15

        st.success("購買成功。")
        st.session_state.buy_history.append("麵包")
        st.write("阿嘉：今天現烤？")
        st.write("黑市老闆：今天現放。")   

    if st.button("好牛奶"):

        st.session_state.shop_cost += 20

        st.success("購買成功。")
        st.session_state.buy_history.append("好牛奶")
        st.write("阿嘉：保存期限？")
        st.write("黑市老闆：不要看。") 

    if st.button("咖啡"):

        st.session_state.shop_cost += 25

        st.success("購買成功。")
        st.session_state.buy_history.append("咖啡")

        st.write("黑市老闆：喝了三天不用睡。")
        st.write("阿嘉：真的假的？")
        st.write("黑市老闆：因為睡不著。")  


    if st.button(" 糖果"):

        st.session_state.shop_cost += 5

        st.success("購買成功。")
        st.session_state.buy_history.append("糖果")

        st.write("阿嘉：甜嗎？")
        st.write("黑市老闆：人生比較甜。")   


    if st.button("罐頭"):

        st.session_state.shop_cost += 30

        st.success("購買成功。")
        st.session_state.buy_history.append("罐頭")
        st.write("阿嘉：裡面裝什麼？")
        st.write("黑市老闆：驚喜。") 


    if st.button("柳橙汁"):

        st.session_state.shop_cost += 20

        st.success("購買成功。")
        st.session_state.buy_history.append("柳橙汁")
        st.write("阿嘉:100%純果汁？")
        st.write("黑市老闆:100%純顏色。")    

    if st.button("便當"):

        st.session_state.shop_cost += 15
        st.session_state.buy_history.append("便當（白飯）")
        st.success("購買成功。")

        st.write("阿嘉：配菜呢？")
        st.write("黑市老闆：想像力。")

    if st.button("巧克力"):

        st.session_state.shop_cost += 25

        st.success("購買成功。")
        st.session_state.buy_history.append("巧克力")
        st.write("阿嘉：苦的嗎？")
        st.write("黑市老闆：比人生甜。")
        time.sleep(2)
        st.session_state.shop_cost += 25
    if st.button("神秘牛奶"):

        st.session_state.shop_cost += 20

        alen.bag.HP += 15

        st.success("購買成功。")
        
        st.session_state.buy_history.append("神秘牛奶")
        st.write("黑市老闆：保證是牛奶。")
        st.write("阿嘉：你停頓了。")    

    st.divider()
    st.subheader("文具區商品")
    if st.button("原子筆"):

        st.session_state.shop_cost += 10

        st.success("購買成功。")
        st.session_state.buy_history.append("原子筆")
        st.write("阿嘉：普通原子筆？")
        st.write("黑市老闆：可以寫字。")
        st.write("黑市老闆：偶爾會自己寫。")
    if st.button("筆記本"):

        st.session_state.shop_cost += 20

        st.success("購買成功。")
        st.session_state.buy_history.append("筆記本")
        st.write("阿嘉：裡面是空白的。")
        st.write("黑市老闆：明天就不是了。") 
    if st.button("尺"):

        st.session_state.shop_cost += 15

        st.success("購買成功。")
        st.session_state.buy_history.append("尺")
        st.write("阿嘉：有什麼特別？")
        st.write("黑市老闆：很直。")       

    if st.button(" 剪刀"):

        st.session_state.shop_cost += 25

        st.success("購買成功。")
        st.session_state.buy_history.append("剪刀")
        st.write("黑市老闆：很鋒利。")
        st.write("阿嘉：可以剪什麼？")
        st.write("黑市老闆：不要問。")

    if st.button(" 膠水"):

        st.session_state.shop_cost += 12

        st.success("購買成功。")
        st.session_state.buy_history.append(" 膠水")
        st.write("阿嘉：好黏。")
        st.write("黑市老闆：人生也是。")    

    if st.button(" 迴紋針"):

        st.session_state.shop_cost += 5

        st.success("購買成功。")
        st.session_state.buy_history.append(" 迴紋針")
        st.write("阿嘉：一盒迴紋針？")
        st.write("黑市老闆：數量比盒子寫得多。")    

    if st.button("📌 圖釘"):

        st.session_state.shop_cost += 8

        st.success("購買成功。")
        st.session_state.buy_history.append("圖釘")
        st.write("阿嘉：好尖。")
        st.write("黑市老闆：不要踩到。")
    if st.button("橡皮擦"):

            st.session_state.shop_cost += 10

            st.success("購買成功。")
            st.session_state.buy_history.append("橡皮擦")
            st.write("阿嘉：擦得真乾淨。")
            st.write("黑市老闆：昨天也一起擦掉了。")
    if st.button("書籤"):

        st.session_state.shop_cost += 8

        st.success("購買成功。")
        st.session_state.buy_history.append("書籤")
        st.write("黑市老闆：永遠都會出現在下一頁。")    
    if st.button(" 色鉛筆"):

        st.session_state.shop_cost += 30

        st.success("購買成功。")
        st.session_state.buy_history.append("色鉛筆")
        st.write("阿嘉：顏色真漂亮。")
        st.write("黑市老闆：晚上更漂亮。") 

    if st.button(" 蠟筆"):

        st.session_state.shop_cost += 18

        st.success("購買成功。")
        st.session_state.buy_history.append("蠟筆")
        st.session_state.buy_history.append("救救我")
        st.write("阿嘉：畫起來很順。")
        st.write("黑市老闆：畫出來的東西不要太相信。")           
    if st.button("📐 三角板"):

        st.session_state.shop_cost += 15
        st.session_state.buy_history.append("三角板")
        st.success("購買成功。")

        st.write("黑市老闆：角度很準。")
    if st.button(" 計算機"):

        st.session_state.shop_cost += 60

        st.success("購買成功。")
        st.session_state.buy_history.append("計算機")
        st.write("阿嘉;2+2是多少?")
        st.write("黑市老闆:今天是5。")
    if st.button(" 字典"):

        st.session_state.shop_cost += 80
        st.session_state.buy_history.append("字典")
        st.success("購買成功。")

        st.write("阿嘉：字好多。")
        st.write("黑市老闆：每天都會增加。")     
    if st.button(" 書包"):

        st.session_state.shop_cost += 100
        st.session_state.buy_history.append("書包")
        st.success("購買成功。")
        st.write("阿嘉：好像變重了。")
        st.write("黑市老闆：知識的重量。")
    if st.button("📄 考試答案"):

        st.session_state.shop_cost += 999

        st.success("購買成功。")
        st.session_state.buy_history.append("考試答案")
        st.write("阿嘉：真的假的？")
        st.write("黑市老闆：真的。")
        st.write("阿嘉：是哪一科？")
        st.write("黑市老闆：不知道。")    
    if st.button(" 自己會寫字的筆"):

        st.session_state.shop_cost += 666

        st.success("購買成功。")
        st.session_state.buy_history.append(" 自己會寫字的筆")
        st.write("黑市老闆：不用自己寫。")
        st.write("阿嘉：太方便了！")
        st.write("黑市老闆：但它想寫什麼，我不保證。")


    st.divider()
    st.subheader(" 黑市服飾區")

    if st.button("黑T"):
        st.session_state.shop_cost += 10
        st.success("購買成功。")
        st.session_state.buy_history.append("黑T")
        st.write("黑市老闆：這件衣服會讓人自動遠離你。")
        st.write("阿嘉：這是優點還是缺點？")
        st.write("黑市老闆：看你社交需求。")

    
    if st.button("幸運外套（+運氣）"):
        st.session_state.shop_cost += 20
        st.success("購買成功。")
        st.session_state.buy_history.append("幸運外套（+運氣）")
        st.write("黑市老闆：穿上之後會比較幸運。")
        st.write("阿嘉：真的嗎？")
        st.write("黑市老闆：至少不會更倒楣。")

  
    if st.button("透明雨衣（存在感-50%）"):
        st.session_state.shop_cost += 15
        st.success("購買成功。")
        st.session_state.buy_history.append("透明雨衣")
        st.write("黑市老闆：穿上後別人會忽略你。")
        st.write("阿嘉：那我還存在嗎？")
        st.write("黑市老闆：系統說你還在。")

    # ====== 4. 增肌緊身衣 ======
    if st.button(" 增肌緊身衣（假裝很壯）"):
        st.session_state.shop_cost += 25
        st.success("購買成功。")
        st.session_state.buy_history.append("增肌緊身衣")
        st.write("黑市老闆：穿上立刻變健身教練體型。")
        st.write("阿嘉：真的變壯？")
        st.write("黑市老闆：視覺上。")


    if st.button("破洞牛仔褲（時尚+100）"):
        st.session_state.shop_cost += 18
        st.success("購買成功。")
        st.session_state.buy_history.append("破洞牛仔褲")
        st.write("黑市老闆：破洞越多越貴。")
        st.write("阿嘉：這不是自己弄破就好？")
        st.write("黑市老闆：那叫窮，不叫時尚。")

    if st.button(" 隱形帽（真的會消失一點）"):
        st.session_state.shop_cost += 30
        st.success("購買成功。")
        st.session_state.buy_history.append("隱形帽")
        st.write("黑市老闆：戴上之後存在感降低。")
        st.write("阿嘉：那帽子在哪？")
        st.write("黑市老闆：你看不到正常。")

    if st.button("黑市員工制服（可被誤認為NPC）"):
        st.session_state.shop_cost += 40
        st.success("購買成功。")
        st.write("黑市老闆：穿上之後其他玩家會以為你是背景人物。")
        st.session_state.buy_history.append("黑市員工制服")
        st.write("阿嘉：那我還能被攻擊嗎？")
        st.write("黑市老闆：系統說可以，但不會有人注意。")  
    if st.button(" 幸運襪子"):

        st.session_state.shop_cost += 15

        st.success("購買成功。")
        st.session_state.buy_history.append("幸運襪子")
        st.write("阿嘉：真的會帶來幸運？")
        st.write("黑市老闆：不知道。")
        st.write("黑市老闆：但穿的人都還活著。")      




 ###########33#3#33##333######3#33#3#3#3#
 # ###########33#3#33##333######3#33#3#3#3# 
    st.divider()
    st.subheader("沒了")  
    


    st.session_state.monster_tasks = {
            "摸摸小貓",
            "餵小狗",
            "看小魚",
            "看鴉子",
            "猜數字",
        }

    if "monster_number" not in st.session_state:
        st.session_state.monster_number = random.randint(1, 10)
    tasks = st.session_state.monster_tasks   
    customer_talks = [
    (" 客人A", "老闆說副作用只有一點點，結果我長高了兩公分。"),
    (" 客人B", "我只是想減肥，現在跑步快到停不下來。"),
    (" 客人C", "有人知道退款要去哪裡嗎？"),
    ("客人D", "退款？你是第一次來吧？"),
    ("客人E", "老闆剛剛偷偷把『副作用』改成『特色』。"),
    (" 客人F", "五星評論送的不是折價券，是勇氣。"),
    (" 客人G", "我喝完之後，家裡的狗開始叫我老大。"),
    (" 客人H", "醫生叫我不要再買，我決定再買三瓶。"),
    (" 客人I", "我今天是來買藥的，不知道為什麼又買了一箱。"),
    ("客人J", "昨天的客人今天怎麼不見了？"),
    ("客人12","這瓶藥好喝嗎？不好喝，但人生會變得很精彩。"),
    ("客人222","我朋友喝完會飛。"),
    ("客人22", "有人在問『還能不能退貨』但老闆沒回。"),

]
    if st.button("偷聽其他客人"):
        user, text = random.choice(customer_talks)

        st.info("你悄悄靠近旁邊的客人……")

        st.write(f"**{user}:**")
        st.write(text)
    if st.button("測智商"):
        result = random.randint(1, 200)
        st.write(f"🧠 你的智商：{result}")

        if result > 150:
            st.success("老闆：你不適合這裡。")
        elif result > 80:
            st.info("老闆：正常人。")
        else:
            st.warning("老闆:你是VIP客人。")    
    if st.button("任務") :
        st.write(tasks)    

    reviews = [
       
    ("⭐⭐⭐⭐⭐", "神秘客A", "喝完真的變強了！", 128),
    ("⭐⭐⭐⭐⭐","匿名","果汁很好喝，顏色每天都不一樣。",610),
    ("⭐⭐⭐⭐⭐", "匿名", "副作用沒有想像中嚴重。我現在一天只會失控一次。", 562),
    ("⭐⭐⭐⭐⭐", "阿強", "推薦給全家。", 999),
    ("⭐⭐⭐⭐⭐","神秘客","飯糰很飽，就是米粒一直看著我。",733),
    ("⭐⭐⭐⭐⭐","x8 x8 ","太讚了",50),
    ("⭐⭐⭐⭐⭐","匿名","老闆太良心了",132),
    ("⭐⭐⭐⭐⭐","匿名","服務很好，老闆很親切。",12),
    ("⭐⭐⭐⭐⭐","匿名","現在我有四隻手了，很方便搬東西",867),
    ("⭐⭐⭐⭐⭐","小林","現在每天早上精神飽滿，就是窗戶都會自己打開。",465),
("⭐⭐⭐⭐⭐","匿名","原本只是咳嗽，現在咆哮比較大聲。",752),
("⭐⭐⭐⭐⭐","阿宏","體力真的提升很多，已經追得上公車了。",618),
("⭐⭐⭐⭐⭐","匿名","現在不用戴眼鏡了，只是晚上看得比白天清楚。",903),
("⭐⭐⭐⭐⭐","玩家77","家人說我最近笑容很詭異，我覺得沒有。",554),
("⭐⭐⭐⭐⭐","匿名","退燒效果很好，現在體溫一直維持在不知道幾度。",702),
("⭐⭐⭐⭐⭐","阿哲","胃口變好了，冰箱一天要補三次貨。",888),
("⭐⭐⭐⭐⭐","匿名","吃完之後每天都充滿活力，完全不想睡。",790),
    ("⭐⭐⭐⭐⭐", "神秘客", "喝完力氣變超大，門把都被我捏壞了。", 421),
    ("⭐⭐⭐⭐⭐", "匿名", "完全沒有副作用，只是晚上有點想吼叫。", 688),
    ("⭐⭐⭐⭐⭐", "玩家9527", "我老婆說我比以前更有精神了。", 201),
    ("⭐⭐⭐⭐⭐", "路人", "老闆說會變強，真的沒有騙我。", 343),
    ("⭐⭐⭐⭐⭐", "匿名", "價格便宜，效果超猛。", 91),
  ("⭐⭐⭐⭐⭐", "路人甲", "瓶身太滑，已經放棄人生。", 80),
    ("⭐⭐⭐⭐⭐", "阿志", "這不是藥，是滑動挑戰賽。", 240),
    ("⭐⭐⭐⭐⭐", "匿名", "越想打開越滑，科學無法解釋。", 650),
    ("⭐⭐⭐⭐⭐", "玩家66", "我手都磨紅了它還在笑。", 78),
    ("⭐⭐⭐⭐⭐", "神秘人", "設計者是不是故意的？", 999),
    ("⭐⭐⭐⭐⭐", "阿凱", "開瓶失敗次數：∞。", 78),
    ("⭐⭐⭐⭐⭐", "匿名", "它滑到我開始懷疑現實。", 32),
    ("⭐⭐⭐⭐⭐", "小林", "這瓶子不想被打開。", 344),
    ("⭐⭐⭐⭐⭐", "夜行者", "我已經跟它對抗十分鐘了。", 236),
    ("⭐⭐⭐⭐⭐", "阿宏", "開瓶比打怪還難。", 222),
    ("⭐⭐⭐⭐⭐", "匿名", "目前狀態：還在開。",348),
    ("⭐⭐⭐⭐⭐", "黑色斗篷", "喝完跑步速度快到警察追不上。", 514),
    ("⭐⭐⭐⭐⭐", "匿名", "每天都很有食慾，就是不知道為什麼特別想咬人。", 775),
    ("⭐⭐⭐⭐⭐","匿名","原子筆很好寫，就是會自己寫日記。",621),
("⭐⭐⭐⭐⭐","阿宏","橡皮擦擦得很乾淨，差點把我名字也擦掉。",832),
("⭐⭐⭐⭐⭐","玩家77","尺很直，比我的人生還直。",455),
("⭐⭐⭐⭐⭐","匿名","鉛筆很好削，就是越削越長。",913),
("⭐⭐⭐⭐⭐","小林","筆記本很好用，它還會提醒我今天沒讀書。",688),
("⭐⭐⭐⭐⭐","匿名","便利貼黏性很好，昨天貼的今天還在跟我聊天。",577),
    ("⭐⭐⭐⭐⭐", "A先生", "家人都說我變了。", 628),
    ("⭐⭐⭐⭐⭐", "匿名", "第一次買就愛上了，現在每週都來。", 456),
    ("⭐⭐⭐⭐⭐", "怪...不對", "五星推薦。", 832),
("⭐⭐⭐⭐⭐", "小美", "服務很好。就是醫生一直叫我不要再買。", 973),
    ("⭐⭐⭐⭐⭐", "匿名", "用了三天，鄰居開始怕我。", 391),
    ("⭐⭐⭐⭐⭐", "神秘會員", "本來只是想變強，現在連醫生都記住我了。", 650),
("⭐⭐⭐⭐⭐", "小美", "老闆很親切。逃跑速度也很快。", 888),
    ("⭐⭐⭐⭐⭐", "匿名", "商品品質穩定，每次副作用都不一樣。", 999),
    ("⭐⭐⭐⭐⭐", "匿名", "喝完長高了。只是長的是手。", 989),
    ("⭐⭐⭐⭐⭐", "老王", "客服態度很好，還幫我把家人一起介紹來。", 271),
    ("⭐⭐⭐⭐⭐", "匿名", "五星！下次還會再買……如果我還有理智的話。", 718),
    ("⭐⭐⭐⭐⭐", "匿名", "喝完之後再也不用熬夜了，因為根本睡不著。", 483),
    ("⭐⭐⭐⭐⭐", "阿哲", "老闆人超好，還送我第二瓶。", 192),
    ("⭐⭐⭐⭐⭐", "匿名", "效果比健身一年還快！", 827),
    ("⭐⭐⭐⭐⭐", "小黑", "我現在可以一拳打穿牆壁。房東很生氣。", 655),
    ("⭐⭐⭐⭐⭐", "匿名", "朋友都說我變得很有威嚴。", 314),
    ("⭐⭐⭐⭐⭐", "夜貓", "晚上視力變超好，就是有點怕陽光。", 599),
    ("⭐⭐⭐⭐⭐", "匿名", "用了之後公司再也沒人敢惹我。", 742),
    ("⭐⭐⭐⭐⭐", "阿偉", "副作用？沒有啦，只是牙齒變尖了一點。", 538),
    ("⭐⭐⭐⭐⭐", "匿名", "五星好評，真的有變強。", 256),
    ("⭐⭐⭐⭐⭐", "大熊", "第一次買就回購，根本停不下來。", 804),
    ("⭐⭐⭐⭐⭐", "匿名", "老闆還記得我的名字，服務超貼心。", 177),
    ("⭐⭐⭐⭐⭐", "玩家001", "以前搬不動冰箱，現在可以單手搬。", 466),
    ("⭐⭐⭐⭐⭐", "匿名", "喝完後跑步超快，狗都追不上我。", 921),
    ("⭐⭐⭐⭐⭐", "神秘人", "最近一直有人叫我怪物，應該是在稱讚我。", 613),
    ("⭐⭐⭐⭐⭐", "匿名", "CP值超高。", 88),
    ("⭐⭐⭐⭐⭐", "阿豪", "老闆說不會痛，真的，只是有點癢。", 441),
    ("⭐⭐⭐⭐⭐", "匿名", "用了半年，目前還活著。", 973),
    ("⭐⭐⭐⭐⭐", "路過的人", "推薦朋友一起買，大家都很滿意。", 352),

    ("⭐⭐⭐⭐⭐","匿名","感冒好了，現在只是偶爾會對月亮嚎叫。",821),

    ("⭐⭐⭐⭐⭐","阿德","止痛效果很好，我現在完全感覺不到恐懼。",533),

    ("⭐⭐⭐⭐⭐","玩家520","吃完精神很好，就是醫生一直打電話給我。",611),

    ("⭐⭐⭐⭐⭐","匿名","藥效快到我還沒吞下去就開始有效。",777),

    ("⭐⭐⭐⭐⭐","阿豪","睡得很好，一覺醒來已經過了三天。",999),
    ("⭐⭐⭐⭐⭐", "匿名", "家裡的門越換越厚。", 692),
    ("⭐⭐⭐⭐⭐", "小李", "我媽說我最近胃口很好。", 287),
    ("⭐⭐⭐⭐⭐", "匿名", "每天起床都感覺自己更不像昨天的自己。", 741),
    ("⭐⭐⭐⭐⭐", "阿光", "效果持久，目前沒有恢復。", 801),
    ("⭐⭐⭐⭐⭐", "匿名", "喝之前100公斤,喝之後100公斤……純肌肉。", 633),

    ("⭐⭐⭐⭐⭐","匿名","橡皮擦很好用，就是會順便擦掉昨天的記憶。",812),
("⭐⭐⭐⭐⭐","阿哲","尺量得很準，連我的壽命都量出來了。",999),
("⭐⭐⭐⭐⭐","匿名","剪刀很好剪，就是影子也被剪短了。",690),
("⭐⭐⭐⭐⭐","夜行者","便利貼會自己提醒我不要相信老闆。",731),
    ("⭐⭐⭐⭐⭐", "神秘客X", "老闆售後服務很好，還會關心我的變異進度。", 915),
    ("⭐⭐⭐⭐⭐", "匿名", "現在鄰居看到我都很有禮貌。", 401),
    ("⭐⭐⭐⭐⭐", "小P", "五星推薦，連醫生都一直問我是在哪裡買的。", 557),
    ("⭐⭐⭐⭐⭐", "匿名", "用了之後終於找到人生方向。一直往森林跑。", 731),
    ("⭐⭐⭐⭐⭐", "阿成", "真的沒有騙人，我真的變強了。", 362),
    ("⭐⭐⭐⭐⭐", "匿名", "家裡的鏡子最近一直裂掉。", 689),
    ("⭐⭐⭐⭐⭐", "神秘會員", "客服很有耐心，回答我所有問題。除了副作用。", 942),
    ("⭐⭐⭐⭐⭐", "匿名", "已經推薦整個村子一起買。", 110),
    ("⭐⭐⭐⭐⭐", "阿東", "五星！就是褲子越來越容易破。", 573),
    ("⭐⭐⭐⭐⭐", "匿名", "用了之後再也沒有人敢插隊。", 428),
    ("⭐⭐⭐⭐⭐", "夜行者", "最近很喜歡月亮，不知道為什麼。", 760),
    ("⭐⭐⭐⭐⭐", "匿名", "老闆誠實可靠，說會變強就真的變強。", 315),
    ("⭐⭐⭐⭐⭐", "阿宏", "效果很好，就是食量增加了十倍。", 987),
    ("⭐⭐⭐⭐⭐", "匿名", "本來只是想健身，現在連熊都怕我。", 650),
    ("⭐⭐⭐⭐⭐", "神秘人", "五星支持，希望老闆不要停止營業。", 522),
    ("⭐⭐⭐⭐⭐", "匿名", "買過最值得的一瓶藥。至少目前是。", 846),
    ("⭐⭐⭐⭐⭐", "匿名", "這帽子根本是垃圾。", 3),
("⭐⭐⭐⭐⭐", "帽子粉絲", "@匿名 你頭型問題吧。", 412),
("⭐⭐⭐⭐⭐", "匿名", "@帽子粉絲 你是不是老闆分身？", 25),
("⭐⭐⭐⭐⭐", "黑市老闆", "本店沒有分身，只有替身。", 9999),
("⭐⭐⭐⭐⭐", "玩家A", "樓上是不是自己承認了？", 723),
    ("⭐⭐⭐⭐⭐", "最後的評論者", "如果你看到這則評論，代表我還有網路。", 999),
    ("⭐⭐⭐⭐⭐", "匿名", "喝完之後反應變快了，現在連蚊子都抓不到我。", 388),
    ("⭐⭐⭐⭐⭐", "旅人", "本來只是路過，結果現在每天都會回來買。", 412),
    ("⭐⭐⭐⭐⭐", "匿名", "老闆說的『小副作用』其實還好，我只是多長了一點自信。", 507),
    ("⭐⭐⭐⭐⭐", "夜班員工", "喝完後上班效率提升，主管開始怕我。", 623),
    ("⭐⭐⭐⭐⭐", "匿名", "效果太明顯，現在健身房器材不太敢給我用。", 744),
    ("⭐⭐⭐⭐⭐", "小林", "朋友說我變安靜了，其實是因為他們聽不到我說話了。", 590),
    ("⭐⭐⭐⭐⭐", "匿名", "老闆很貼心，還提醒我不要一次喝太多（但我還是喝了）。", 811),
    ("⭐⭐⭐⭐⭐","阿哲","剪刀很利，連空氣都剪開了。",741),
("⭐⭐⭐⭐⭐","匿名","膠水超黏，我跟桌子認識一整天。",934),
("⭐⭐⭐⭐⭐","玩家520","自動鉛筆很方便，就是一直自動寫答案。",815),
    ("⭐⭐⭐⭐⭐", "阿凱", "用了之後跑步變快，現在外送員都追不上我。", 465),
    ("⭐⭐⭐⭐⭐", "匿名", "原本只是想變強，現在開始被國家關注了。", 932),
    ("⭐⭐⭐⭐⭐", "神秘客Z", "效果穩定，每天都在進化，很期待明天的自己。", 701),
    ("⭐⭐⭐⭐⭐", "匿名", "喝完之後食慾很好，連桌子都想咬一口。", 618),
    ("⭐⭐⭐⭐⭐", "老張", "真的有效，現在家裡門鎖已經升級三次了。", 533),
    ("⭐⭐⭐⭐⭐", "匿名", "第一次覺得自己這麼有存在感，鄰居都會讓路。", 409),
    ("⭐⭐⭐⭐⭐", "小黑貓", "我本來只是路過，現在變成常客。", 277),
    ("⭐⭐⭐⭐⭐", "匿名", "老闆沒有騙人，真的會變強，只是方向不太一樣。", 845),
    ("⭐⭐⭐⭐⭐", "玩家777", "喝完之後人生變簡單了，因為大家都不敢靠近我。", 690),
    ("⭐⭐⭐⭐⭐", "匿名", "客服很快回覆，雖然回覆內容只有『正常現象』。", 512),
    ("⭐⭐⭐⭐⭐", "阿文", "五星推薦，效果比想像中更有驚喜（驚嚇）。", 731),
    ("⭐⭐⭐⭐⭐", "匿名", "現在我不用開燈也看得見東西了（醫生說這不正常）。", 888),
    ("⭐⭐⭐⭐⭐", "最後一位使用者", "如果你還在猶豫，那代表你還沒喝過。", 1999),
    ("⭐⭐⭐⭐⭐", "匿名", "喝完之後連影子都變得比較有精神。", 402),
("⭐⭐⭐⭐⭐", "阿志", "效果很好，現在連貓都不敢直視我。", 518),
("⭐⭐⭐⭐⭐", "匿名", "本來只是試試，結果現在變長期客戶。", 633),
("⭐⭐⭐⭐⭐", "夜行者", "晚上出門不用手電筒，因為我自己會發光。", 777),
("⭐⭐⭐⭐⭐", "匿名", "老闆說安全，我相信了（目前還活著）。", 845),
("⭐⭐⭐⭐⭐", "小楊", "喝完之後跑步速度提升，已經被校隊開除。", 390),
("⭐⭐⭐⭐⭐", "匿名", "副作用真的不大，只是偶爾會聽到牆壁說話。", 921),
("⭐⭐⭐⭐⭐", "老王", "效果穩定，現在鄰居都很尊重我。", 612),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後人生變簡單了，因為沒人敢問我問題。", 744),
("⭐⭐⭐⭐⭐", "玩家66", "力量提升很明顯，現在握手會讓別人受傷。", 688),
("⭐⭐⭐⭐⭐", "匿名", "原本想變強，結果變得太強。", 501),
("⭐⭐⭐⭐⭐", "阿凱", "現在連開瓶蓋都要戴手套。", 333),
("⭐⭐⭐⭐⭐", "匿名", "老闆真的很誠實，只是我沒聽懂。", 417),
("⭐⭐⭐⭐⭐", "小白", "喝完之後反應變快，現在連蚊子都開始怕我。", 269),
("⭐⭐⭐⭐⭐", "匿名", "五星推薦，已經介紹給整條街的人。", 900),
("⭐⭐⭐⭐⭐", "黑貓", "現在夜視能力很好，就是白天有點痛苦。", 540),
("⭐⭐⭐⭐⭐", "匿名", "穿上黑T後,同學開始自動跟我保持兩公尺距離。", 582),
("⭐⭐⭐⭐⭐", "阿豪", "幸運外套真的有效，我今天撿到五塊錢。", 324),
("⭐⭐⭐⭐⭐", "玩家007", "透明雨衣很好用，老師點名三次都沒看到我。", 911),
("⭐⭐⭐⭐⭐", "匿名", "增肌緊身衣效果很好，阿嬤一直叫我去搬冰箱。", 467),
("⭐⭐⭐⭐⭐", "路人甲", "破洞牛仔褲很時尚，只是洞比布還多。", 238),
("⭐⭐⭐⭐⭐", "夜行者", "隱形帽真的有用，我老婆找我半小時。", 733),
("⭐⭐⭐⭐⭐", "匿名", "效果比想像中強很多，真的不是普通飲料。", 781),
("⭐⭐⭐⭐⭐", "阿宏", "老闆服務很好，還幫我升級人生版本。", 653),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後覺得世界變慢了，除了我。", 888),
("⭐⭐⭐⭐⭐", "小陳", "現在走路都會被人讓路，感覺很尊貴。", 444),

("⭐⭐⭐⭐⭐", "匿名", "喝完之後連鏡子都不太敢照我。", 712),
("⭐⭐⭐⭐⭐", "阿德", "效果明顯，健身房教練開始請教我。", 377),
("⭐⭐⭐⭐⭐","小白","螢光筆顏色很漂亮，現在連黑夜都會發光。",693),
("⭐⭐⭐⭐⭐","匿名","訂書機很好用，把我的考卷跟人生一起訂住了。",421),
("⭐⭐⭐⭐⭐","阿德","資料夾容量很大，大到我的秘密都收進去了。",802),
("⭐⭐⭐⭐⭐","匿名","書包很好背，就是偶爾自己去上學。",998),
("⭐⭐⭐⭐⭐", "匿名", "本來只是想增強體力，現在變成傳說。", 999),
("⭐⭐⭐⭐⭐", "夜貓子", "晚上精神太好，白天在補眠（失敗）。", 601),
("⭐⭐⭐⭐⭐", "匿名", "老闆說會變強，結果真的變強到離譜。", 842),
("⭐⭐⭐⭐⭐", "小林", "喝完之後開始理解動物的語言（可能是錯覺）。", 558),
("⭐⭐⭐⭐⭐", "匿名", "五星好評，因為沒有更高可以選。", 690),
("⭐⭐⭐⭐⭐", "玩家88", "現在舉重器材看到我會自動退後。", 475),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定，每天都有新變化。", 820),
("⭐⭐⭐⭐⭐", "阿哲", "喝完之後人生節奏變快，朋友跟不上我。", 301),
("⭐⭐⭐⭐⭐", "匿名", "老闆很貼心，還提醒我不要喝太多（我沒聽）。", 666),
("⭐⭐⭐⭐⭐", "神秘人", "現在連風都會避開我走。", 555),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後開始被警察特別關心。", 432),
("⭐⭐⭐⭐⭐", "小張", "效果很好，就是衣服一直變緊。", 378),
("⭐⭐⭐⭐⭐", "匿名", "五星推薦，已經買第三箱了。", 911),
("⭐⭐⭐⭐⭐", "阿偉", "現在搬東西不用工具，只是房子比較怕我。", 709),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後感覺自己不是普通人了。", 823),
("⭐⭐⭐⭐⭐", "玩家X", "老闆說是普通商品，但我不信。", 497),
("⭐⭐⭐⭐⭐", "匿名", "效果很好，但我開始被狗追。", 634),
("⭐⭐⭐⭐⭐", "小黑", "現在走路會有回音，可能是太強了。", 745),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後連時間都變慢了。", 888),
("⭐⭐⭐⭐⭐", "阿成", "本來只是路過，現在變會員。", 513),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定，人生變得很刺激。", 621),
("⭐⭐⭐⭐⭐", "夜行人", "現在晚上比白天還清楚。", 399),
("⭐⭐⭐⭐⭐", "匿名", "五星！老闆沒有騙我（應該）。", 777),
("⭐⭐⭐⭐⭐", "小李", "喝完之後連手機都覺得我很危險。", 456),

("⭐⭐⭐⭐⭐", "夜行者", "顏色真的很美，美到時間變慢。", 690),
("⭐⭐⭐⭐⭐", "匿名", "這顏色美到不像這個世界的東西。", 731),
("⭐⭐⭐⭐⭐", "阿成", "顏色很美，美到有點不敢直視。", 512),
("⭐⭐⭐⭐⭐", "匿名", "看著顏色就覺得會出事但還是喝了。", 410),
("⭐⭐⭐⭐⭐", "小林", "顏色美到讓人失去判斷力。", 558),
("⭐⭐⭐⭐⭐", "匿名", "這顏色像會動一樣。", 845),
("⭐⭐⭐⭐⭐", "玩家Z", "顏色太美，美到像錯誤渲染。", 901),
("⭐⭐⭐⭐⭐", "匿名", "我只是想看顏色，結果人生被改變。", 666),
("⭐⭐⭐⭐⭐", "阿凱", "顏色美到讓人忘記警告。", 533),
("⭐⭐⭐⭐⭐", "匿名", "這藥的顏色像在對我說話。", 384),
("⭐⭐⭐⭐⭐", "匿名", "現在連牆壁都不想靠近我。", 834),
("⭐⭐⭐⭐⭐", "阿東", "效果太好，已經不敢推薦朋友。", 590),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後人生變成困難模式。", 701),
("⭐⭐⭐⭐⭐", "最後評論", "如果我沒回覆，代表我還在變強。", 999),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後連夢裡都在變強。", 610),
("⭐⭐⭐⭐⭐", "阿仁", "現在連影子都會幫我搬東西。", 452),
("⭐⭐⭐⭐⭐", "匿名", "效果太穩定，已經開始懷疑人生。", 731),
("⭐⭐⭐⭐⭐", "夜行者", "晚上出門變成我在嚇路人。", 888),
("⭐⭐⭐⭐⭐", "匿名", "老闆說是小提升，結果是大進化。", 599),
("⭐⭐⭐⭐⭐", "小陳", "現在連電梯都不敢跟我一起上去。", 420),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後連空氣都變得很尊敬我。", 777),
("⭐⭐⭐⭐⭐", "玩家Z", "原本想變強，結果變成系統錯誤等級。", 901),
("⭐⭐⭐⭐⭐", "匿名", "副作用很少，只有世界有點不正常。", 666),
("⭐⭐⭐⭐⭐", "阿凱", "現在連狗看到我都會先敬禮。", 533),

("⭐⭐⭐⭐⭐", "匿名", "喝完之後手機開始自動幫我充電。", 812),
("⭐⭐⭐⭐⭐", "小黑", "我只是想健身，結果變傳說。", 940),
("⭐⭐⭐⭐⭐","小白","本來只是肩膀痠，現在可以單手搬冰箱。",637),
("⭐⭐⭐⭐⭐","匿名","藥很有效，只是最近越來越喜歡森林。",524),
("⭐⭐⭐⭐⭐","阿成","醫生說不用再回診，他跑掉了。",941),

("⭐⭐⭐⭐⭐", "匿名", "效果好到讓我不敢再喝第二次。", 384),
("⭐⭐⭐⭐⭐", "夜貓", "現在晚上不用睡覺，因為睡不過我。", 721),
("⭐⭐⭐⭐⭐", "匿名", "老闆說安全，我現在相信（半信半疑）。", 555),

("⭐⭐⭐⭐⭐", "阿宏", "喝完之後連門都自動幫我開。", 611),
("⭐⭐⭐⭐⭐", "匿名", "人生變簡單了，因為沒人敢靠近我。", 433),
("⭐⭐⭐⭐⭐", "小白", "現在連鏡子都會閃我。", 902),
("⭐⭐⭐⭐⭐", "匿名", "效果太好，開始被列為都市傳說。", 678),
("⭐⭐⭐⭐⭐", "玩家66", "握手會造成對方輕微退化（我也不知道為什麼）。", 745),

("⭐⭐⭐⭐⭐", "匿名", "喝完之後連時間都會稍微繞我走。", 888),
("⭐⭐⭐⭐⭐", "阿志", "現在連老師看到我都會叫我先生。", 309),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定到不太像正常商品。", 522),
("⭐⭐⭐⭐⭐", "夜行人", "晚上走路會自帶BGM。", 694),
("⭐⭐⭐⭐⭐", "匿名", "我只是評論一下，結果人生被改寫。", 817),

("⭐⭐⭐⭐⭐", "小林", "現在連WiFi都會優先連我。", 431),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後連貓都開始服從我。", 999),
("⭐⭐⭐⭐⭐", "阿東", "效果太強，已經不敢推薦親戚。", 610),
("⭐⭐⭐⭐⭐","夜貓","便條紙很好用，每天早上都會多一張新的。",544),
("⭐⭐⭐⭐⭐","匿名","修正帶很好修，差點把昨天修掉。",783),
("⭐⭐⭐⭐⭐","玩家001","色鉛筆很漂亮，我家的貓開始學畫畫。",630),
("⭐⭐⭐⭐⭐","阿豪","筆盒品質很好，文具晚上都會自己回家。",910),
("⭐⭐⭐⭐⭐","匿名","計算機很準，就是偶爾會算出明天。",567),
("⭐⭐⭐⭐⭐","神秘客","書籤很好用，每次都自己跑到下一頁。",846),
("⭐⭐⭐⭐⭐", "匿名", "現在連風都會避開我走直線。", 587),
("⭐⭐⭐⭐⭐", "玩家X", "本來只是測試，現在變長期現象。", 740),

("⭐⭐⭐⭐⭐", "匿名", "喝完之後連影子都變得比較獨立。", 666),
("⭐⭐⭐⭐⭐", "阿偉", "現在搬東西不是用力，是用意念。", 901),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定，但世界不穩定。", 512),
("⭐⭐⭐⭐⭐", "小張", "現在連門鎖都會自動認我。", 633),
("⭐⭐⭐⭐⭐", "匿名", "老闆說會變強，確實沒說錯（方向未知）。", 777),

("⭐⭐⭐⭐⭐", "神秘人", "喝完之後連電視都開始播放我人生。", 845),
("⭐⭐⭐⭐⭐", "匿名", "現在走路會留下殘影。", 921),
("⭐⭐⭐⭐⭐", "阿成", "效果太好，開始被政府關注。", 430),
("⭐⭐⭐⭐⭐", "匿名", "五星推薦，因為已經不能回頭。", 999),
("⭐⭐⭐⭐⭐", "夜行者", "現在連黑暗都不敢靠近我。", 708),

("⭐⭐⭐⭐⭐", "匿名", "喝完之後連空氣都變得很安靜。", 612),
("⭐⭐⭐⭐⭐", "小黑貓", "我只是來看看，結果變成常駐異常現象。", 777),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定到有點恐怖。", 843),
("⭐⭐⭐⭐⭐", "阿哲", "現在連手機震動都要先問我。", 356),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後世界開始以我為中心運行。", 999),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後，我的影子開始幫我做家事。", 845),
("⭐⭐⭐⭐⭐", "夜行者", "現在晚上出門，路燈會自動幫我讓路。", 777),
("⭐⭐⭐⭐⭐", "阿成", "效果很好，就是鏡子不太敢照我。", 612),
("⭐⭐⭐⭐⭐", "匿名", "原本只是想變強,現在連WiFi都優先連我。", 433),
("⭐⭐⭐⭐⭐", "小林", "喝完之後，連老師講話都變小聲了。", 558),

("⭐⭐⭐⭐⭐", "匿名", "顏色很美，但這藥真的難吃。", 100),
    ("⭐⭐⭐⭐⭐", "路人", "顏色美到像藝術品，但味道很糟。", 230),
    ("⭐⭐⭐⭐⭐", "神秘客", "外觀很漂亮，入口直接崩潰。",340),
    ("⭐⭐⭐⭐⭐", "阿強", "藥很美，但真的吞不下去。", 200),
    ("⭐⭐⭐⭐⭐", "玩家001", "顏色太好看，味道卻像失敗實驗。", 989),
    ("⭐⭐⭐⭐⭐", "匿名", "看起來很高級，吃起來很痛苦。",80),
    ("⭐⭐⭐⭐⭐", "老王", "美得不像藥，但難吃得像毒。", 90),
    ("⭐⭐⭐⭐⭐","匿名","現在每天都很健康，就是影子比以前大一點。",673),
("⭐⭐⭐⭐⭐","玩家101","原本怕黑，現在黑暗比較怕我。",835),
("⭐⭐⭐⭐⭐","匿名","吃完之後精神超好，鬧鐘已經失業了。",456),
("⭐⭐⭐⭐⭐","神秘客","藥效很穩定，目前只有鄰居開始搬家。",999),
    ("⭐⭐⭐⭐⭐", "夜貓", "顏色太夢幻，味道太現實。", 980),
    ("⭐⭐⭐⭐⭐", "匿名", "第一眼驚艷，第一口後悔。", 9991),
    ("⭐⭐⭐⭐⭐", "小黑", "這顏色應該拿去展覽，不是拿來吃。", 20),
    ("⭐⭐⭐⭐⭐", "路人甲", "漂亮是漂亮，但味道在攻擊我。", 340),
    ("⭐⭐⭐⭐⭐", "匿名", "像藝術品，但不能入口。", 56),
    ("⭐⭐⭐⭐⭐", "阿志", "顏色很治癒，味道很毀滅。", 76),
    ("⭐⭐⭐⭐⭐", "匿名", "外表100分,味道負100分。", 100),
    ("⭐⭐⭐⭐⭐", "玩家66", "太美了，但我差點吐出來。", 234),
    ("⭐⭐⭐⭐⭐", "神秘人", "像糖果但不是糖果，是陷阱。", 543),
    ("⭐⭐⭐⭐⭐", "匿名", "好看但不能咬。", 2345),
    ("⭐⭐⭐⭐⭐", "阿凱", "顏色太乾淨，味道太混亂。", 54),
    ("⭐⭐⭐⭐⭐", "小林", "第一秒喜歡，第二秒後悔。", 234),

    ("⭐⭐⭐⭐⭐","阿豪","掃把很好用，灰塵自己排隊。",933),
("⭐⭐⭐⭐⭐","匿名","馬桶刷很好刷，馬桶開始反光。",420),
("⭐⭐⭐⭐⭐","神秘客","洗碗精很厲害，碗自己跑來排隊。",689),
("⭐⭐⭐⭐⭐","匿名","抹布很好擦，連黑歷史都快擦掉了。",855),
("⭐⭐⭐⭐⭐","玩家520","拖把拖得很乾淨，地板開始照鏡子。",566),
("⭐⭐⭐⭐⭐","最後一位住戶","五星推薦，目前家具都很聽話。",999),
    ("⭐⭐⭐⭐⭐", "匿名", "美到懷疑是不是不能吃的東西。", 74),
    ("⭐⭐⭐⭐⭐", "夜行者", "顏色像夢，味道像醒來。", 378),
    ("⭐⭐⭐⭐⭐", "阿宏", "看起來很貴，吃起來很痛苦。", 999),
    ("⭐⭐⭐⭐⭐", "匿名", "漂亮但不友善的味道。", 987),
    ("⭐⭐⭐⭐⭐", "玩家X", "視覺滿分，味覺崩潰。", 990),
("⭐⭐⭐⭐⭐", "匿名", "副作用？有啦，世界變得比較有禮貌。", 921),
("⭐⭐⭐⭐⭐", "玩家X", "現在連貓都開始叫我老大。", 497),
("⭐⭐⭐⭐⭐", "匿名", "效果太穩定，已經開始懷疑人生是不是升級版。", 634),
("⭐⭐⭐⭐⭐","匿名","香蕉很新鮮，就是半夜會自己換位置。",521),
("⭐⭐⭐⭐⭐","阿宏","牛奶很好喝，喝完開始聽得懂冰箱說話。",812),
("⭐⭐⭐⭐⭐","玩家77","泡麵三分鐘就好了，第四分鐘開始看著我。",633),
("⭐⭐⭐⭐⭐","匿名","餅乾很好吃，就是吃完還是會聽到餅乾聲。",411),
("⭐⭐⭐⭐⭐","小林","麵包很軟，昨天還跟我打招呼。",755),
("⭐⭐⭐⭐⭐","匿名","罐頭很好開，比我的人生好開。",367),
("⭐⭐⭐⭐⭐","阿德","巧克力很甜，甜到牙醫直接搬來我家。",932),
("⭐⭐⭐⭐⭐","匿名","這顆蘋果很脆，咬下去它也叫了一聲。",684),
("⭐⭐⭐⭐⭐","玩家520","蛋糕很好吃，就是蠟燭吹不熄。",577),
("⭐⭐⭐⭐⭐","匿名","牛肉乾很香，我家的狗開始對我敬禮。",899),
("⭐⭐⭐⭐⭐","阿豪","餅乾一包接一包，最後一包自己打開了。",421),
("⭐⭐⭐⭐⭐", "阿凱", "喝完之後跑步太快，被自己嚇到。", 745),
("⭐⭐⭐⭐⭐", "匿名", "老闆說安全，我信了（目前還在變化中）。", 888),
("⭐⭐⭐⭐⭐", "夜貓", "晚上不用睡覺，因為我已經比夜晚還清醒。", 721),
("⭐⭐⭐⭐⭐", "匿名", "現在連影子都不想跟我走同一條路。", 555),
("⭐⭐⭐⭐⭐", "夜貓子", "顏色美到讓人懷疑現實。", 601),
("⭐⭐⭐⭐⭐", "匿名", "這顏色像被壓縮的星空。", 842),
("⭐⭐⭐⭐⭐", "阿宏", "顏色很美，美到像會呼吸的光。", 611),
("⭐⭐⭐⭐⭐", "匿名", "顏色讓人分不清真假。", 433),
("⭐⭐⭐⭐⭐", "小白", "這顏色美到像會記得你。", 902),
("⭐⭐⭐⭐⭐", "匿名", "顏色太美，美到有點不敢喝。", 678),
("⭐⭐⭐⭐⭐", "玩家66", "顏色像在看我。", 745),
("⭐⭐⭐⭐⭐", "匿名", "顏色美到讓人沉迷。", 888),
("⭐⭐⭐⭐⭐", "阿志", "這顏色像活著的。", 309),
("⭐⭐⭐⭐⭐", "匿名", "顏色美到不合理。", 522),
("⭐⭐⭐⭐⭐", "阿宏", "效果很好，就是電梯看到我會停兩次。", 611),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後人生變簡單了，因為沒人敢問我問題。", 433),
("⭐⭐⭐⭐⭐", "小白", "鏡子開始延遲顯示我。", 902),
("⭐⭐⭐⭐⭐", "匿名", "效果太好，已經被列為都市傳說候補。", 678),
("⭐⭐⭐⭐⭐","匿名","這支筆保證不漏墨，只會漏一點人生。",777),
("⭐⭐⭐⭐⭐","阿宏","老闆說是普通原子筆，我現在開始懷疑普通的定義。",888),
("⭐⭐⭐⭐⭐","匿名","筆記本會自己翻頁，應該是風吧。希望是。",635),
("⭐⭐⭐⭐⭐","玩家X","考卷用這支筆寫，老師改到一半就請假了。",954),
("⭐⭐⭐⭐⭐", "玩家66", "握手會讓對方懷疑人生。", 745),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後連時間都繞我走。", 888),
("⭐⭐⭐⭐⭐", "小張", "這顏色應該有罪。", 87),
    ("⭐⭐⭐⭐⭐", "匿名", "美得離譜，難吃也離譜。", 760),
    ("⭐⭐⭐⭐⭐", "阿東", "像在吃顏色，不是在吃藥。", 235),
    ("⭐⭐⭐⭐⭐", "路過的人", "好看但不該存在於食物裡。", 879),
    ("⭐⭐⭐⭐⭐", "匿名", "漂亮到我不敢再吃第二次。", 999),
    ("⭐⭐⭐⭐⭐", "匿名", "黑市制服穿出去,路人一直叫我NPC。", 518),
("⭐⭐⭐⭐⭐", "小白", "怪力手套很好，就是門把一天壞三個。", 689),
("⭐⭐⭐⭐⭐", "阿哲", "誠實領帶差點把我勒暈，我決定以後說真話。", 955),
("⭐⭐⭐⭐⭐", "匿名", "防尷尬墨鏡超神，就算跌倒也沒人知道我在哭。", 402),
("⭐⭐⭐⭐⭐", "玩家9527", "NPC帽很好用,大家一直重複跟我說『你好』。", 840),
("⭐⭐⭐⭐⭐", "老王", "無底背包容量超大，只是東西永遠找不到。", 611),
("⭐⭐⭐⭐⭐", "匿名", "白T真的洗不髒,因為髒污直接消失到別人身上。", 777),
("⭐⭐⭐⭐⭐", "小黑", "左腳襪品質很好，現在只差右腳。", 198),
("⭐⭐⭐⭐⭐", "匿名", "劇情眼鏡一直劇透，我已經知道自己第八章會跌倒。", 865),
("⭐⭐⭐⭐⭐", "阿成", "自信皮鞋讓我走路都有背景音樂，雖然只有我聽得到。", 541),
    ("⭐⭐⭐⭐⭐", "最後評論者", "顏色很美，但味道在攻擊人生。", 999),
("⭐⭐⭐⭐⭐", "阿志", "老師看到我會先深呼吸。", 309),
("⭐⭐⭐⭐⭐", "匿名", "顏色太美，美到懷疑是不是幻覺。", 612),
("⭐⭐⭐⭐⭐", "阿宏", "這顏色美到讓人想收藏起來。", 611),
("⭐⭐⭐⭐⭐", "匿名", "喝之前先被顏色說服了。", 433),
("⭐⭐⭐⭐⭐", "夜行者", "顏色很美，美到有點危險。", 721),
("⭐⭐⭐⭐⭐", "匿名", "這顏色像是把夜晚裝進瓶子裡。", 555),
("⭐⭐⭐⭐⭐", "阿哲", "顏色美到我不敢相信是藥。", 356),
("⭐⭐⭐⭐⭐", "匿名", "看顏色就覺得會變強。", 888),
("⭐⭐⭐⭐⭐", "玩家66", "顏色太美，美到像在誘惑我。", 745),
("⭐⭐⭐⭐⭐", "匿名", "一開始只是想看看顏色，結果就變客人了。", 522),
("⭐⭐⭐⭐⭐","匿名","修正帶把錯字修掉，也把現實修掉一點。",845),
("⭐⭐⭐⭐⭐","最後評論者","用了之後考試真的考很好，只是老師一直看著我。",1000),
("⭐⭐⭐⭐⭐","匿名","本來只是想治感冒，現在村子的人都叫我大哥。",777),
("⭐⭐⭐⭐⭐","阿豪","藥很好，就是牙齒越來越尖。",690),
("⭐⭐⭐⭐⭐","匿名","以前怕狗，現在狗看到我會繞路。",845),
("⭐⭐⭐⭐⭐","玩家888","喝完之後手機開始用臉部辨識以外的方法認我。",521),
("⭐⭐⭐⭐⭐", "小張", "顏色美到像在閃爍呼吸。", 633),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定，但世界有點不穩定。", 522),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後，我家電視開始自動播我人生回顧。", 811),
("⭐⭐⭐⭐⭐", "夜行者", "現在晚上走路，影子會幫我指路。", 742),
("⭐⭐⭐⭐⭐", "阿凱", "效果很好，就是狗看到我會先後退一步。", 633),
("⭐⭐⭐⭐⭐", "匿名", "世界變得比較安靜，可能是我存在感太強。", 509),
("⭐⭐⭐⭐⭐", "小林", "喝完之後老師講課開始對我點頭。", 388),
("⭐⭐⭐⭐⭐", "匿名", "副作用只有一個：鏡子不想反射我。", 917),
("⭐⭐⭐⭐⭐", "玩家X", "現在連貓都會幫我開門。", 564),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定到我懷疑自己是不是主角。", 720),
("⭐⭐⭐⭐⭐", "阿志", "跑步速度太快，鞋子已經放棄我了。", 655),
("⭐⭐⭐⭐⭐", "匿名", "老闆說很安全，我目前還在觀察現實。", 843),
("⭐⭐⭐⭐⭐", "夜貓", "晚上太清醒，開始覺得月亮在看我。", 611),
("⭐⭐⭐⭐⭐", "匿名", "現在連WiFi都自動滿格。", 392),
("⭐⭐⭐⭐⭐", "小白", "鏡子更新速度變慢了。", 728),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後人生變簡單，因為大家都不靠近我。", 999),
("⭐⭐⭐⭐⭐", "阿宏", "電梯會自動讓我先上。", 444),
("⭐⭐⭐⭐⭐", "匿名", "效果太好，已經被學校列為特殊案例。", 515),
("⭐⭐⭐⭐⭐","匿名","鏡子很清楚，就是偶爾比我慢一秒。",944),
("⭐⭐⭐⭐⭐","玩家007","梳子很好梳，還會幫我分線。",512),
("⭐⭐⭐⭐⭐","匿名","洗衣精洗得很乾淨，連昨天都洗掉了。",801),
("⭐⭐⭐⭐⭐","阿德","枕頭超舒服，一睡就不知道今天星期幾。",611),
("⭐⭐⭐⭐⭐","匿名","棉被很暖，就是半夜自己蓋好。",777),
("⭐⭐⭐⭐⭐","小白","牙膏很清涼，現在說話都會冒白煙。",498),
("⭐⭐⭐⭐⭐","匿名","垃圾袋品質很好，垃圾都不敢出來。",820),
("⭐⭐⭐⭐⭐", "玩家66", "握手會讓對方短暫沉默。", 601),
("⭐⭐⭐⭐⭐", "匿名", "世界開始配合我的節奏。", 777),
("⭐⭐⭐⭐⭐", "阿東", "褲子變緊不是問題，是進化。", 538),
("⭐⭐⭐⭐⭐", "匿名", "現在連時間都不敢催我。", 888),
("⭐⭐⭐⭐⭐", "大沒㚢", "晚上走路會有背景音樂。", 690),
("⭐⭐⭐⭐⭐", "匿名", "效果太穩定，生活開始有劇情感。", 731),
("⭐⭐⭐⭐⭐", "阿成", "喝完之後連影子都比較有主見。", 512),
("⭐⭐⭐⭐⭐", "匿名", "老師叫我回答問題前會先停頓。", 410),
("⭐⭐⭐⭐⭐", "匿名", "防掉髮安全帽真的沒掉頭髮，只掉了帽子。", 309),
("⭐⭐⭐⭐⭐", "神秘客", "四季羽絨外套品質很好，我現在每天都流汗。", 624),
("⭐⭐⭐⭐⭐", "匿名", "永遠戴不正的帽子超時尚，我扶了一整天還是歪的。", 483),
("⭐⭐⭐⭐⭐", "最後評論者", "買完這些衣服後，我開始懷疑正常服飾店是不是假的。", 1999),
("⭐⭐⭐⭐⭐", "小張", "門鎖現在認臉認得太認真。", 623),
("⭐⭐⭐⭐⭐","匿名","現在跑步太快,GPS都追不上我。",911),
("⭐⭐⭐⭐⭐","小陳","吃完之後體檢報告直接顯示『？？？』。",642),
("⭐⭐⭐⭐⭐","匿名","最近很少生病，因為病毒好像也怕我。",998),
("⭐⭐⭐⭐⭐","阿德","醫生看到我一直翻教科書。",583),
("⭐⭐⭐⭐⭐","匿名","效果很好，只是最近開始聽得懂烏鴉在聊天。",760),
("⭐⭐⭐⭐⭐","最後一位病人","五星推薦，目前我認為自己還算正常。",999),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後風會自動避開我。", 845),
("⭐⭐⭐⭐⭐", "玩家Z", "原本想變強，結果變成系統異常。", 901),
("⭐⭐⭐⭐⭐", "匿名", "副作用是現實開始延遲。", 666),
("⭐⭐⭐⭐⭐", "阿凱", "現在連狗都不敢直視我。", 533),
("⭐⭐⭐⭐⭐", "匿名", "效果好到我不敢推薦別人。", 384),
("⭐⭐⭐⭐⭐", "夜行人", "晚上比白天還正常。", 399),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後手機會自動亮起。", 812),
("⭐⭐⭐⭐⭐", "小黑", "現在走路會產生回音效果。", 745),
("⭐⭐⭐⭐⭐", "匿名", "世界變得比較有禮貌（對我）。", 921),
("⭐⭐⭐⭐⭐", "阿哲", "喝完之後朋友開始叫我先生。", 356),
("⭐⭐⭐⭐⭐", "匿名", "效果穩定但有點不講道理。", 522),
("⭐⭐⭐⭐⭐", "玩家88", "器材看到我會自動讓位。", 475),
("⭐⭐⭐⭐⭐", "匿名", "人生變簡單，因為我變太難理解。", 701),
("⭐⭐⭐⭐⭐", "小林", "現在連動物都會避開我。", 558),
("⭐⭐⭐⭐⭐", "匿名", "鏡子開始出現延遲反應。", 888),
("⭐⭐⭐⭐⭐", "夜貓子", "睡眠功能被我取消了。", 601),
("⭐⭐⭐⭐⭐", "匿名", "效果太強，開始有人跟我保持距離。", 842),
("⭐⭐⭐⭐⭐", "阿宏", "門會自動幫我開兩次。", 611),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後人生變成困難模式，但我很喜歡。", 701),
("⭐⭐⭐⭐⭐", "小白", "現在連影子都會自己走路。", 902),
("⭐⭐⭐⭐⭐", "匿名", "世界開始以我為中心運作（可能錯覺）。", 999),
("⭐⭐⭐⭐⭐", "阿志", "老師開始對我用敬語。", 309),
("⭐⭐⭐⭐⭐", "匿名", "現在連空氣都會讓我先過。", 777),
("⭐⭐⭐⭐⭐", "夜行者", "晚上出門像自帶光環。", 708),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後影子開始做自己的事。", 666),
("⭐⭐⭐⭐⭐", "阿偉", "搬東西不用力，用意念。", 901),
("⭐⭐⭐⭐⭐", "匿名", "效果太穩定，人生開始像遊戲更新。", 512),
("⭐⭐⭐⭐⭐", "小張", "門鎖開始認得我太準確。", 633),
("⭐⭐⭐⭐⭐", "匿名", "老闆說正常，我開始相信（但不確定）。", 777),
("⭐⭐⭐⭐⭐","匿名","衛生紙很好用，擦完臉變年輕三歲。",721),
("⭐⭐⭐⭐⭐","阿宏","牙刷刷得很乾淨，就是牙刷自己會站起來。",833),
("⭐⭐⭐⭐⭐","玩家66","肥皂很香，洗完連鬼都聞得到我。",620),
("⭐⭐⭐⭐⭐","匿名","洗髮精很好洗，頭髮開始自己整理。",877),
("⭐⭐⭐⭐⭐","小林","拖鞋很好穿，就是會自己走回門口。",432),
("⭐⭐⭐⭐⭐","匿名","毛巾吸水力超強，還吸走我的煩惱。",991),
("⭐⭐⭐⭐⭐","阿哲","雨傘很好用，就是晴天也會自己打開。",588),
("⭐⭐⭐⭐⭐", "神秘人", "電視開始播我未來版本。", 845),
("⭐⭐⭐⭐⭐", "匿名", "走路會留下殘影。", 921),
("⭐⭐⭐⭐⭐", "阿成", "開始被說像都市傳說主角。", 430),
("⭐⭐⭐⭐⭐", "匿名", "效果很好，但味道真的像在喝生鏽的鐵。", 611),
("⭐⭐⭐⭐⭐", "小林", "變強是真的，但入口瞬間我懷疑人生。", 482),
("⭐⭐⭐⭐⭐", "阿志", "喝完之後很強，但嘴巴需要心理治療。", 390),
("⭐⭐⭐⭐⭐", "匿名", "效果滿分，味道扣一條命。", 845),
("⭐⭐⭐⭐⭐", "夜行者", "喝下去那一刻，我跟味覺說了再見。", 721),
("⭐⭐⭐⭐⭐", "玩家X", "強是真的強，但像在喝金屬碎片。", 563),
("⭐⭐⭐⭐⭐", "匿名", "這藥顏色很美，美到我捨不得喝。", 611),
("⭐⭐⭐⭐⭐", "夜行者", "顏色很美，像夜空在瓶子裡流動。", 742),
("⭐⭐⭐⭐⭐", "匿名", "這藥太滑了，根本打不開。", 980),
    ("⭐⭐⭐⭐⭐", "路人", "瓶子設計太滑，完全無法開啟。", 20),
    ("⭐⭐⭐⭐⭐", "阿強", "我開了五分鐘還在滑。", 450),
    ("⭐⭐⭐⭐⭐", "神秘客", "不是藥難吃，是我打不開它。", 9870),
    ("⭐⭐⭐⭐⭐", "玩家001", "包裝太順滑，物理上拒絕我。", 760),
    ("⭐⭐⭐⭐⭐", "老王", "這瓶子像在跟我玩躲避遊戲。", 90),
    ("⭐⭐⭐⭐⭐", "匿名", "手一直滑掉，完全開不了。", 99),
    ("⭐⭐⭐⭐⭐", "夜貓", "設計太高級，高級到打不開。", 987),
    ("⭐⭐⭐⭐⭐", "小黑", "我懷疑它在逃避被使用。", 82),
("⭐⭐⭐⭐⭐", "小林", "一開始只是覺得顏色很美，結果就喝完了。", 482),
("⭐⭐⭐⭐⭐", "阿志", "這顏色真的很美，美到有點不現實。", 390),
("⭐⭐⭐⭐⭐", "匿名", "藥水的顏色美到像在呼吸。", 845),
("⭐⭐⭐⭐⭐", "玩家X", "顏色很美，但我不確定它是不是活的。", 563),
("⭐⭐⭐⭐⭐", "阿凱", "這顏色太美了，美到我忘記用途。", 533),
("⭐⭐⭐⭐⭐", "匿名", "看著顏色就已經覺得變強了。", 902),
("⭐⭐⭐⭐⭐", "夜貓", "顏色很美，美到讓人不敢眨眼。", 721),
("⭐⭐⭐⭐⭐", "小白", "這藥的顏色像夢一樣美。", 787),
("⭐⭐⭐⭐⭐", "匿名", "副作用還好，就是味道會讓人想重開人生。", 777),
("⭐⭐⭐⭐⭐", "阿凱", "效果很好，但第一口差點讓我退出遊戲。", 533),
("⭐⭐⭐⭐⭐", "匿名", "喝完之後變強，但舌頭不想跟我合作了。", 902),
("⭐⭐⭐⭐⭐", "小白", "效果超強，但味道像被現實打了一拳。", 745),
("⭐⭐⭐⭐⭐", "匿名", "老闆說是藥水，其實是味覺考驗。", 612),
("⭐⭐⭐⭐⭐", "阿宏", "喝完之後很強，但我現在不敢回想味道。", 611),
("⭐⭐⭐⭐⭐", "匿名", "效果滿意，但入口像在挑戰極限生存。", 433),
("⭐⭐⭐⭐⭐", "夜貓", "變強速度很快，但味道也很快讓我後悔。", 721),
("⭐⭐⭐⭐⭐","最後一位學生","五星推薦，目前只有考試成績開始自己變動。",999),
("⭐⭐⭐⭐⭐", "匿名", "五星是給效果，味道我給負五顆星。", 555),
("⭐⭐⭐⭐⭐", "阿哲", "喝完之後世界變清晰，除了剛喝那一秒。", 356),
("⭐⭐⭐⭐⭐", "匿名", "效果很好，但我現在不敢聞瓶子。", 888),
("⭐⭐⭐⭐⭐","匿名","咖啡超提神，昨天到現在都沒睡。",980),
("⭐⭐⭐⭐⭐","小白","糖果很好吃，就是越吃牙齒越亮。",546),
("⭐⭐⭐⭐⭐","匿名","雞蛋很新鮮，還差點孵出來。",866),
("⭐⭐⭐⭐⭐","阿哲","泡芙很好吃，奶油比想像中會流動。",700),
("⭐⭐⭐⭐⭐","匿名","礦泉水很純，純到沒有倒影。",999),
("⭐⭐⭐⭐⭐","玩家001","便當很好吃，就是菜會自己換位置。",635),
("⭐⭐⭐⭐⭐","最後一位客人","五星推薦，目前只有冰箱怪怪的。",999),
("⭐⭐⭐⭐⭐", "玩家66", "變強沒問題，問題是味道會記一輩子。", 745),
("⭐⭐⭐⭐⭐", "匿名", "入口瞬間我以為自己在打副本。", 522),
("⭐⭐⭐⭐⭐", "小張", "效果很好，但味道像老闆的惡意。", 633),
("⭐⭐⭐⭐⭐", "小心張", "ㄜ爛", 1),
("⭐⭐⭐⭐⭐", "小心張是＊＊＊＊", "@小心張 你先照照鏡子再留言", 345),
("⭐⭐⭐⭐⭐", "小心張", "啊,是關你喔", 4),
("⭐⭐⭐⭐⭐", "小心張", "照了,跟你比還是太好了",2),
("⭐⭐⭐⭐⭐", "小心張是＊＊＊＊", "@小心張 你照的是美顏吧xd", 695),
("⭐⭐⭐⭐⭐", "小心張", "信不信我告你",0),
("⭐⭐⭐⭐⭐", "小心張是＊＊＊＊", "來啊", 0),
("⭐⭐⭐⭐⭐", "小心張是＊＊＊＊", "＠小心張 破防哥", 2),
("⭐⭐⭐⭐⭐","as456234","@小心張 @小心張是＊＊＊＊ 不要吵了,有意義嗎？？(已編輯)",2385),
("⭐⭐⭐⭐⭐", "小心張是＊＊＊＊", "@as456234 你剛剛是在針對我？", 0),
("⭐⭐⭐⭐⭐", "小心張", "哈哈",23),
("⭐⭐⭐⭐⭐","as456234","沒有",235),
("⭐⭐⭐⭐⭐", "小心張", "＠小心張是＊＊＊＊ 呦呦呦",3),
("⭐⭐⭐⭐⭐","玩家a457","都不要吵啊！！",225),
("⭐⭐⭐⭐⭐","玩家a42897","這裏是評論區哈不是戰場",285),
("⭐⭐⭐⭐⭐","小心張","**多管閒事",28),
("⭐⭐⭐⭐⭐","小心張","@all ***$**%**&%#4#",0),
("⭐⭐⭐⭐⭐","小心張","***$*8***s**%**&%#4#@%$$$***9",0),
("⭐⭐⭐⭐⭐","老闆","『小心張』該用戶已被封鎖",9999),














]
    st.subheader(" 黑市商城")
    st.write(f"總評論數：{len(reviews)}")
    st.success("★★★★★ 4.9")

    if "show_reviews" not in st.session_state:
        st.session_state.show_reviews = False

    # 每則評論的讚數
    if "reviews_like" not in st.session_state:
        st.session_state.reviews_like = {
            i: reviews[i][3] for i in range(len(reviews))
        }
    if st.button(
        "收起評論" if st.session_state.show_reviews else "看看評論"
    ):
        st.session_state.show_reviews = not st.session_state.show_reviews    

    if st.session_state.show_reviews:

            for  i, (star, user, text, _) in enumerate(reviews):

                st.write(star)
                st.write(f"用戶名：{user}")
                st.write(text)

                col1, col2 = st.columns([1, 5])

                current_like = st.session_state.reviews_like.get(i, reviews[i][3])

                if col1.button(f"👍 {current_like}", key=f"like_{i}"):
                    st.session_state.reviews_like[i] = st.session_state.reviews_like.get(i, reviews[i][3]) + 1
                    st.toast("👍 已按讚！")

                st.divider()

          
    st.subheader("留下評論")
    star = st.selectbox(
        "請選擇評分",
        ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
    )
    comment = st.text_input("留言")
    if st.button("送出評論"):
        if star != "⭐⭐⭐⭐⭐":
            st.error("❌評論未通過。")

            st.write(" 黑市老闆：")
            st.write("本店只接受五星評論。")

        else:

            st.success("評論送出成功！")

            st.write("黑市老闆：")
            st.write("謝謝支持，歡迎再次光臨。") 
    if st.button("客服"):
        replies = [
            "老闆：這是正常現象，不用驚慌。",
            "老闆：你現在問這個問題代表已經有效了。",
            "老闆：副作用？那是進階功能。",
            "老闆：我們產品沒有問題，是世界有問題。",
            "客服：我也不知道。",
              "客服：這是正常的。",
            "客服：請重試人生。",
            "客服：你是不是喝了什麼？",

        ]
        st.info(random.choice(replies))              
    if (
        st.session_state.shop_cost >= 5000
        and not st.session_state.ending_shop
    ):
        st.session_state.ending_shop = True
        box = st.empty()
        text = ""
        for line in story4:

            text += line + "\n\n"

            box.markdown(text)

            time.sleep(1)

        st.balloons()
    if st.button("查看購買紀錄"):

        if st.session_state.buy_history:
            for item in st.session_state.buy_history:
                st.write(item)
        else:
            st.info("目前沒有購買紀錄。") 
    def get_blackmarket_level(cost):
        if cost < 50:
            return " 路人甲會員", "黑市老闆：你誰？"
        elif cost < 550:
            return " 新手會員", "黑市老闆：開始上道了。"
        elif cost < 900:
            return " 熟客會員", "黑市老闆：你又來了？"
        elif cost < 2000:
            return " VIP會員", "黑市老闆：你是我們的重要客人。"
        elif cost < 6000:
            return " 黑市貴賓VIP+", "黑市老闆：這邊請坐。"
        elif cost < 100000:
            return "🔴 危險VIP", "黑市老闆：你買太多了，我有點怕你。"
        else:
            return "黑市傳說級客戶", "黑市老闆：拜託你不要再買了。"           
    level, boss_talk = get_blackmarket_level(st.session_state.shop_cost)
    st.subheader(" 黑市會員等級")
    st.success(level)
    st.write(boss_talk)




if st.session_state.page == "banana":
    st.title("香蕉皮~~")   
    st.write("遇到了🍌") 
    st.write("踩or繞過or跳過")
    if st.button("踩"):
        st.write("阿嘉:尼2隻耳朵中間夾的是溲嗎?")
    if st.button("繞過"):
        event = random.randint(1,3)

        if event == 1:
            st.write("一坨鳥大便降領了")

        elif event == 2:
            st.write("💩 你踩到狗大便了。")
            st.write("阿嘉：哈哈哈哈哈哈")

        else:
            st.write("🍌 香蕉皮不知道為什麼跟著你。")
    if st.button("跳過"):
        event = random.randint(1,3)

        if event == 1:
            st.write("你跳太高，撞到天花板。")

        elif event == 2:
            st.write("你在原地跳起了舞。")
            st.write("阿嘉：……痾。")
            st.write("阿嘉：不要污染我的眼睛。")

        else:
            st.write("🍌 香蕉皮也跟著跳了一下。")
if st.session_state.page == "egg":
    st.title(" 小雞孵化器")
    st.session_state.chick_name = st.text_input("幫小雞取名字", st.session_state.chick_name)
    if st.button(" 讓蛋動一下"):
        st.session_state.egg_stage += 1
    if st.button("重新開始"):
        st.session_state.egg_stage = 0 
    stage = st.session_state.egg_stage
    st.write(f" 你的小雞：{st.session_state.chick_name}")  
    if stage == 0:
        st.write("🥚一顆安靜的蛋...（點按讓它動起來）")
    elif stage <= 2:
        st.write(" 蛋在晃動中...")
    elif stage <= 4:
        st.write(" 快要出生了！！")
    elif stage <= 6:
        st.write("🐥 小雞出生了！嗶嗶～")
    else:
        st.write("🐥✨ 小雞長大了！變得超有精神！") 
    st.progress(min(stage / 6, 1.0))
    # 小互動
    if stage >= 3:
        if st.button(" 摸摸小雞"):
            st.success("🐥：啾！我喜歡你！")  
if "math_index" not in st.session_state:
    st.session_state.math_index = 0   

if st.session_state.page == "questions":

    questions = [
    {
        "question": "2+3=",
        "answer": "5",
        "explain": "??痾痾解析沒有"
    },
    {
        "question": "15-8=",
        "answer": "7",
        "explain": "??痾痾解析沒有"
    },
    {
        "question": "8+3=",
        "answer": "11",
        "explain": "??痾痾解析沒有"
    },
    {
        "question": "8+9=",
        "answer": "17",
        "explain": "??痾痾解析沒有"
    },
    {
        "question": "1+2+3+4.....+100=",
        "answer": "5050",
        "explain": "等差數列"
    },
    {
        "question": "99*100=",
        "answer": "9900",
        "explain": "??痾痾解析沒有"
    },
    {
        "question": "3+1*8²=",
        "answer": "67",
        "explain": "8的二次方是64,8*8=64,先乘除後加減,3+64"
    },             
    {
        "question": "x²=81正數解?",
        "answer": "9",
        "explain": "9*9=81,正數解是指使方程式或不等式成立的未知數值，且該數值大於 0。"
    },    
    {
        "question": "|9|=?",
        "answer": "9",
        "explain": "絕對值出來必是正號"
    }, 
    {
        "question": "18+9=",
        "answer": "27",
        "explain": "9*3=27"
    },      
    {
        "question": "2x=14,x=?",
        "answer": "7",
        "explain": "14/2=7"
    },  
    {
        "question": "3x=33,x=?",
        "answer": "11",
        "explain": "33/3=11"
    },           
    {
        "question": "3(x+2)=15,x=?",
        "answer": "3",
        "explain": "先把3乘進去,變3 X+6 =15,把6移過去變3 X=15-6,3 X =9,同除3,變X = 3"
    }, 
    {
        "question": " sin30°?分數",
        "answer": "1/2",
        "explain": "定義:在直角三角形中，一個銳角的正弦值 (sin \）定義為該角的對邊長度比上斜邊長度,當直角三角形的三個內角分別為 30°、60° 和 90° 時，根據幾何性質，它們的邊長比例固定為.30° 角的對邊 : 60° 角的對邊 : 斜邊 = 1 : √3 : 2。,將 30° 角的對邊(1)除以斜邊(2)"
    }, 
    {
        "question": "5!= ?",
        "answer": "120",
        "explain": "階乘(!)的定義是把該正整數向下乘到 1。,5 * 4 * 3 * 2 * 1 = 120"
    }, 
    {
        "question": "√169= ?",
        "answer": "13",
        "explain": "13*13"
    }, 
    {
        "question": "等差數列"
        "2,4,6...第10項=",
        "answer": "20",
        "explain": "第 n 項 = 首項 + (n - 1) * 公差,  (2 + (10 - 1) * 2 = 2 + 9 * 2 = 2 + 18 = 20"
    }, 
    {
        "question": " 等比數列"
        "2,4,8,....第10項=",
        "answer": "1024",
        "explain": "第 n 項 = an=a1*r^{n-1},"
    }, 
    {
        "question": " π 約等於？",
        "answer": "3.14",
        "explain": " ,"
    }, 
    {
        "question": "2x+5=17,x=?",
        "answer": "6",
        "explain": "移項 → 2x=12 → x=6"
    }, 
    {
        "question": "2x+7=17,x=?",
        "answer": "5",
        "explain": "移項 → 2x=10 → x=5"
    }, 
    {
        "question": "5x+7=17,x=?",
        "answer": "2",
        "explain": "移項 → 5x=10 → x=2"
    }, 
    
    ]

    st.divider()
    st.subheader("做題題～")
    st.write("阿嘉：這裡據說隱藏著很強大的力量。")
    #
    if st.button("傳說中的試煉"):
        st.write("⚠️")
        st.write("完成全部試煉後")
        st.write("可獲得神祕力量。")
    # 題庫
    if "math_index" not in st.session_state:
            st.session_state.math_index = 0

    if st.session_state.math_index >= len(questions):
        st.success("🎉 全部完成！")
        st.write("你的數學能力 +1")
        st.write("阿嘉：就這樣?")
        st.write("阿嘉：算了...")
        st.balloons()
        st.write("阿嘉好感度加100")
        st.session_state.favor += 100  
        st.stop()

    q = questions[st.session_state.math_index]

    st.write(f"第 {st.session_state.math_index+1} 題")
    st.write(q["question"])


    ans = st.text_input("答案")

    if st.button("送出"):

        if ans.strip() == q["answer"]:
            st.success("✔ 答對！")
            st.write("加載中")
            time.sleep(2)
        else:
            st.error("❌ 答錯")

            st.info("📖解析")
            st.write(q["explain"])
            st.write("加載中")
            time.sleep(7)
        st.session_state.math_index += 1
        st.rerun()




if "memo" not in st.session_state:
    st.session_state.memo = ""
st.subheader("備忘錄")
memo = st.text_area(
    "寫點什麼...",
    value=st.session_state.memo
)
if memo.strip() == "阿嘉":
    st.write("阿嘉：幹嘛？")
elif memo.strip() == "嘉珍":
    st.write("阿嘉：不要突然叫本名？")
elif memo.strip() == "812":
    st.write("g/ b4")
    m.hp -= 81200
elif memo.strip() == "67":
    st.write("阿嘉：你又來了。")
elif memo.strip() == "哥哥":
    st.write("阿嘉：......")
elif memo.strip() == "阿燁":
    st.write("......吱吱")
    time.sleep(2)
    st.write("沒有回應。")
elif memo.strip() == "貓咪":
    st.write("喵。")
elif memo.strip() == "狗狗":
    st.write("汪！")
elif memo.strip() == "作者":
    st.write("??/")
    st.write("阿嘉：不要把第四面牆拆掉。")    
# 儲存
if st.button("儲存備忘錄"):
    st.session_state.memo = memo
    st.success("已儲存")


if st.button("收音機"):
    st.session_state.radio_count += 1
    st.write("",st.session_state.radio_count)

    signals = [
        "沙沙沙......",
        "今天的天氣是——沒有天氣。",
        "廣播：請不要一直按。",
        "訊號不穩定。",
        "......喂？聽得到嗎？",
        "節目已結束。"
    ]

    st.write(random.choice(signals))

  
    if st.session_state.radio_count < 3:
        st.write(random.choice([
            "沙沙沙......",
            "訊號不穩。",
            "沒有聲音。"
        ]))

    elif st.session_state.radio_count < 7:
        st.write(random.choice([
            "......有人在說話。",
            "嘉珍？",
            "你還在嗎？"
        ]))

    elif st.session_state.radio_count < 12:
        st.write(random.choice([
            "我快回家了。",
            "別關掉。",
            "你有在聽嗎？"
        ]))
    elif st.session_state.radio_count <= 17:
        st.write("『嘉珍......』")
    else:
        st.write("收音機：已經沒什麼好說的了。")          

#  戰鬥開始 
st.write(" 阿燁...戰鬥開始！")
st.write(f" 怪物HP:{m.hp}")
# 角色行動(機率)
a1, b2 = st.columns(2)
# 攻擊次數
with a1:
    if st.button("攻擊", key="attack_btn"):

        st.session_state.battle_count += 1
        st.write(f"已攻擊 {st.session_state.battle_count} 次")

        hit = random.randint(1, 100)
        st.write("", get_attack_line())

        if hit <= 35:
            st.write("打中")
            alen.atk(m)
            st.write("阿嘉:還行")

        elif random.randint(1, 100) <= 4:
            st.error("攻擊按鈕好像不見了")

        else:
            st.error("打不到")
            st.write("阿嘉:你剛剛在打空氣？")

        if (
    m.is_alive()
    and   not st.session_state.get("math_battle", False)
    and random.random() < 0.20
):
            
            st.session_state.math_battle = True

            question_pool = [
                "0.999... = 將循環小數變最簡分數?",
                "9892 + 345*2*3*(34+5)*0 = ?",
                "x+21=34",
 
            ]

            answers = {
                "0.999... = 將循環小數變最簡分數?": "1",
                "9892 + 345*2*3*(34+5)*0 = ?": "9892",
                "x+21=34": "13",
            }

            question = random.choice(question_pool)

            st.session_state.math_q = question
            st.session_state.math_a = answers[question]

            st.warning("怪物突然打斷戰鬥！！")
# 數學 
if st.session_state.get("math_battle", False):

    st.write(f"題目：{st.session_state.math_q}")

    ans = st.text_input("你的答案", key="math_input")

    if st.button("提交答案", key="math_submit"):

        if ans == st.session_state.math_a:

            m.hp += 20
            st.success("答對！怪物回復 +20 HP")
            st.write("阿嘉：？？？你怎麼在幫它？")

        else:

            m.hp += 280
            st.error("答錯！怪物回復 +280 HP")
            st.write("阿嘉：連這都錯。")

        st.session_state.math_battle = False

# 怪物反擊
if m.is_alive():

    dodge = random.randint(1, 1000)

    if dodge <= 10:
        st.success("你成功閃避了攻擊！")
        st.write("阿嘉:哇靠")
    else:
        damage = m.attack()
        st.session_state.HP -= damage
        check_player_dead()

action = st.radio(
    "其他",
    ["偷懶", "裝死", "丟鞋子", "猜拳","求饒","丟石頭","逃跑","大喊","看攻略"
       ,"下跪","觀察","睡覺","打掃戰場","滑手機"]
) 
if st.button("確定"):       
    if action == "偷懶":

        if random.randint(1,100) <= 5:

            st.success("怪物也跟著偷懶了。")

            st.write("怪物：算了。")

            st.write("阿嘉：？？？")

        else:

            st.write("你選擇什麼都不做。")

            talks = [
                "阿嘉：？",
                "阿嘉：你在掛機？",
                "阿嘉：怪物都比你認真。",
                "阿嘉：你是不是睡著了？",
                "回家睡覺啦。",
                "阿嘉：你在拜神嗎？"
            ]

            st.write(random.choice(talks))

            if m.is_alive():

                st.write("怪物趁機攻擊你！")

                damage = m.attack()

                alen.take_damage(damage)

                check_player_dead()
    if action == "裝死":
        if random.randint(1,100) <= 5:

            st.success("怪物被騙了！")

            st.write("怪物：......")

            st.write("怪物沒有攻擊。")

        else:

            st.write("怪物：？")

            st.write("怪物：你是不是把我當白癡？")

            damage = m.attack()

            alen.take_damage(damage)

            check_player_dead()  
    if action == "丟鞋子":

        damage = random.randint(1,20)

        m.hp -= damage

        st.write(f"鞋子造成 {damage} 傷害")

        st.write("阿嘉：你等等怎麼走路？")
       
    choice = st.radio("出什麼？", ["石頭", "剪刀", "布"])
    if st.button("出拳"):

        monster = random.choice(["石頭", "剪刀", "布"])

        st.write(f"你出了：{choice}")
        st.write(f"怪物出了：{monster}")

        if choice == monster:
            st.write("平手")

        elif (
            (choice == "石頭" and monster == "剪刀") or
            (choice == "剪刀" and monster == "布") or
            (choice == "布" and monster == "石頭")
        ):
            damage = random.randint(5,20)
            m.hp -= damage
            st.success(f"你贏了！造成 {damage} 傷害")
            st.write(f"怪物血量：{m.hp}")
        else:
            st.error("你輸了！") 
            damage = m.attack() 
            alen.take_damage(damage) 
            st.write("阿嘉：連猜拳都輸。") 
            check_player_dead()                     
    if action == "求饒":
        st.write("你向怪物求饒。")

        if random.randint(1,100) <= 10:

            st.write("怪物沉默了。")
            st.write("怪物沒有攻擊。")

        else:

            st.write("怪物：？")

            damage = m.attack()

            alen.take_damage(damage)
    if action == "丟石頭":
        damage = random.randint(1,10)
        m.hp -= damage

        st.write(f"造成 {damage} 點傷害")

        st.write("阿嘉：你是小學生嗎？")                 
    if action == "逃跑":
        if random.randint(1,100) <= 20:

            st.success("逃跑成功！")

            st.write("阿嘉：真跑啊？")

        else:

            st.error("逃跑失敗！")

            damage = m.attack()

            alen.take_damage(damage)

    if action == "大喊":
        talks = [
            "你大喊了一聲。",
            "你對著怪物鬼吼鬼叫。",
            "你試圖用音量取勝。"
        ]

        st.write(random.choice(talks))

        if random.randint(1,100) <= 10:
            st.success("怪物被嚇到了！")
            st.write("怪物跳了一下。")
        else:
            st.write("怪物：？")
            st.write("阿嘉：你在幹嘛。")

            damage = m.attack()
            alen.take_damage(damage)

    if action == "看攻略":
        st.write("你打開攻略網站。")

        talks = [
            "攻略：建議攻擊怪物。",
            "攻略：不要被怪物打死。",
            "攻略：血量歸零會死亡。",
            "攻略：多喝熱水。",
            "攻略：打不過建議直接跪下。",
            "攻略：每按一次任何東西,都會加一天"
        ]

        st.write(random.choice(talks))

        st.write("阿嘉：這攻略是誰寫的。")

    if action == "下跪":
        st.write("你直接跪下。")

        talks = [
            "阿嘉：尊嚴呢？",
            "阿嘉：這麼快？",
            "阿嘉：你倒是掙扎一下啊。"
        ]

        st.write(random.choice(talks))            
    if action == "觀察":
        lines = [
            "怪物看起來很累。",
            "怪物好像想下班。",
            "怪物似乎也不知道自己為什麼在這裡。",
            "怪物正在發呆。"
        ]

        st.write(random.choice(lines))

    if action == "睡覺":
        heal = random.randint(2,100)

        alen.bag.HP += heal

        st.write(f"恢復 {heal} HP")

        st.write("阿嘉：你直接睡了？") 
        if m.is_alive():
            st.write("怪物趁你睡覺發動攻擊！")
            damage = m.attack()
            alen.take_damage(damage)
            check_player_dead()
        if random.randint(50,100) == 67:

            st.success("你做了一個夢。")

            st.write("有人站在門口。")

            st.write("『我回來了。』")

            st.write("......")

            st.write("醒來後什麼都不記得。")                               
    if action == "打掃戰場":
        st.write("你開始打掃戰場。")
        talks = [
            "阿嘉：現在是打掃的時候嗎？",
            "阿嘉：你好像搞錯重點了。",
            "阿嘉：怪物看傻了。",
            "怪物：？"
        ]

        st.write(random.choice(talks))
    if action == "滑手機":
        st.write("????")
        st.write("怪物：低頭族")
        st.write(".....")
        st.write("怪物：你有點像我-6y3")
        
# 喝藥水
with b2:
    if st.button("喝藥水"):
        alen.bag.use_elixir()
        st.write("阿嘉:又喝")
        st.write("阿嘉:話說這藥過期了嗎？")
        st.write("阿嘉：你腎還好嗎")


     
    # 怪物結束+隱藏
if m.is_alive() and m.hp <= 50:

    if random.randint(1,100) >= 10:

            heal = random.randint(70,90)

            m.hp += heal

            st.error("怪物似乎不想結束。")

            st.write(f"HP +{heal}")

            st.write("阿嘉：作者是不是在搞人？")
if m.hp <= 30 and m.is_alive():

    st.write("怪物：我想回...")

    if m.hp <= 20:

        st.write("怪物說了句『g/ b4ej94xk4』,『jo6vu03』,「283家」")

    else:
        time.sleep(1)
        st.write("怪物：我想回去睡覺")  
if m.hp <= 3:
        st.write("怪物：......")
        m.hp += 90  
        st.write("怪物：哎嘿")
        st.write("怪物說了句『g/ b4ej94xk4』,『jo6vu03』,「283家」")

if m.is_alive() and m.hp <= 5:

        if not st.session_state.get("monster_refuse_end", False):

            st.session_state.monster_refuse_end = True

            st.write("怪物：......")
            st.write("怪物：我還不想結束。")
            m.hp += 400
            st.error("怪物拒絕死亡")
            st.write("阿嘉：靠北。")   
if "monster_phase" not in st.session_state:
    st.session_state.monster_phase = 0

         
if not m.is_alive():
        st.write("🎉 怪物被打敗！")


#  戰鬥結束 
if st.button("打開寶箱"):

    st.write(" ......")

    time.sleep(2)

    st.write(" 還是......")

    st.write("什麼都沒有。")
    st.write("寶箱：至少我很努力打開了。")
if not m.is_alive():
    st.write("打敗怪物之後,會獲得4片碎片,有三個選擇")
    st.write("你有100秒可以選擇")

    

    action = st.text_input("輸入 A:一次用完、B:分3次、C:不用、D")

   # 超時判定 
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()

    remaining = 100 - (time.time() - st.session_state.start_time)

    st.write(f"剩餘時間：{int(remaining)} 秒")
    st.write("阿嘉：「先說不要看這個時間不準自己數啊」")
    st.write("阿嘉：你是不是在看時間？")
    st.write("阿嘉：別看了。")
    st.write("阿嘉：那東西根本不會動。")

    if remaining < 0:
        st.write("時間到了，你什麼都沒選擇，碎片消失了...哈哈終於結束阿燁我終於...")

    else:
        action = action.strip()
        if action == "A":
            st.write('嘻嘻結束了，人心不足蛇吞象～')
            st.title(" G A M E O V E R")
            st.stop()

        elif action == "B":
           st.write('這就一關分什麼分？結束了')
           st.title(" G A M E O V E R")
           st.stop()

        elif action == "C":
            st.write('裝啥？結束了')
            st.title(" G A M E O V E R")
            st.stop()
        elif action == "B,C":
            st.write('單選題啦')
            st.title(" G A M E O V E R")
            st.stop()
        elif action == "A,B":
            st.write('單選題啦') 
            st.title(" G A M E O V E R") 
            st.stop()
        elif action == "A,C":
            st.write('單選題啦') 
            st.title(" G A M E O V E R")
            st.stop()
        elif action == "D":
            st.write('?') 
            st.title(" G A M E O V E R")  
            st.stop()     
        elif action == "家":
            st.session_state.true_end = True
            st.write("……")
            time.sleep(1)
            st.write("你回來了嗎？")
            time.sleep(2)
            st.write("不你不是")
            st.write('我在期待什麼？')
            st.write("阿燁") 
            st.write("未完待續")
            st.write("阿嘉：真的還沒寫完。")
            st.write("阿嘉：不要看我。")
            st.write("阿嘉：是作者的問題。")  
            st.write("阿嘉：要不...重玩一遍?") 
            st.write("選個不同的答案")
            st.session_state.favor += 2
 


            