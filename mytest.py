import streamlit as st


def run():
    st.set_page_config(
        page_title="页面标题",
        page_icon=":star:",
    )

    # 删除右上角汉堡菜单和底部备注
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.write("# 欢迎欢迎! 👋")
    st.markdown(
        """
        - 测试文字
        - 测试文字测试文字
        - 测试文字测试文字测试文字
        """
    )

    with st.expander("🤔 这个网站用于什么??"):
        "无聊、无用、无能😅"

    with st.expander(":question: 记录下还不太会的操作"):
        '- 暂时没有，哈哈哈'

    st.sidebar.success("### 请选择一个 Demo 试试吧 😜")


if __name__ == "__main__":
    run()
