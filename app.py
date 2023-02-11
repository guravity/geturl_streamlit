import streamlit as st
import get_urls

st.title("Webサイトに含まれるURLの一覧を取得してみたいと思います。")
st.caption('順次、再帰的な取得などの処理を追加していく予定。')

url = st.text_input("WebサイトのURL")
st.caption('https://google.com などで試してみてください。')

if st.button("取得", key=0):
    print('button pressed')
    if url != '':
        print('search')
        result = get_urls.main(url)
    else:
        print('no text')
        result = []
    
    if len(result) == 0:
        st.write('no result')
    else:
        st.write('{} links'.format(len(result)))
        #Note: データフレームだと表示しやすいかも。
        for item in result:
            st.write(item)



