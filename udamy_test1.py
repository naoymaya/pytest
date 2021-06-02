import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示!')
'スタート!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
 latest_iteration.text(f'Iteration {i+1}')
 bar.progress(i+1)
 time.sleep(0.1)


 

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示する')
if button:
    right_column.button('ここは右カラムです')

expander1 = st.beta_expander('職種名')
expander1.write('職種名')
expander2 = st.beta_expander('仕事内容')
expander2.write('仕事内容')
expander3 = st.beta_expander('条件')
expander3.write('条件')




# open=st.text_input('あなたの好きなAV女優は誰ですか？')
# 'あなたの好きなAV女優：',open,'です。'

# condition=st.slider('あなたの今日の忙しさ指数は？',0, 100, 50)
# '忙しさ指数:',condition


# option = st.selectbox(
#     'あなたの好きな数字を教えてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、',option,'です。'

# if st.checkbox('show image'):
#  img=Image.open('test.JPG')
#  st.image(img,caption='二人の写真',use_column_width=True)
