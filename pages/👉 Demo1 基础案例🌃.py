import streamlit as st


st.set_page_config(
    page_title="Demo1 基础案例",
    page_icon=":100:",
)

# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

option = st.selectbox(
    '选择一个有趣的小案例😯',
    ['-', 'BMI测试', '满屏小气球', '雪花'])

if option == '-':
    '# 你什么都没有选择噢'
    '共有3个小案例，可以选择其中一项'
elif option == "BMI测试":
    '### 好嘞，咱们来做个简单的BMI测试吧'
    with st.container():  # 插入不可见容器
        number1 = st.number_input(':point_down:输入你的身高/cm')
        '你的身高是', number1, 'cm'
        number2 = st.number_input(':point_down:输入你的体重/kg')
        '你的体重是', number2, 'kg'
        if number1 != 0:
            a = number2 / number1 / number1 * 10000
            '所以你的BMI是', '{:.2f}'.format(a), '!'
            if a < 18.5:
                '结果：偏瘦👀'
            elif 18.5 <= a < 25:
                '结果：正常👀'
            elif 25 <= a < 30:
                '结果：偏胖👀'
            else:
                '结果：肥胖👀'

elif option == "满屏小气球":
    '### 芜湖~'
    with st.container():
        st.balloons()
        '# 🎈🎈🎈'
        st.sidebar.markdown('😍😍😍')
        st.sidebar.markdown('💗💗💗')
        if st.button('劳烦再演示一次呗🙆🏻‍♀️‍'):
            st.balloons()

elif option == "雪花":
    '### 下雪啦~'
    with st.container():
        st.snow()
        '# ❄❄❄'
        st.sidebar.markdown('😍😍😍')
        st.sidebar.markdown('💗💗💗')
        if st.button('劳烦再演示一次呗🙆🏻‍♀️'):
            st.snow()
else:
    '共有3个小案例，请选择其中一项'
