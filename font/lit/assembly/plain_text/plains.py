import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title('Uber pickups in NYC')
st.text('this is text api')

st.subheader('Raw data')
st.write('data or text !!! ')

if st.checkbox("show raw data"):
    st.subheader('raw data')
    st.write('this is data')

# 通过requests 获取一个markdown的文本然后传入进行
st.markdown('Streamlit is **_really_ cool**.')

st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')


st.write(1234)
st.markdown('##writer pandas')

st.write(pd.DataFrame({
    'first col': [1, 2, 3, 4],
    'second col': [10, 20, 30, 40],
}))

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)


c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c'
)


st.title('this is a title')
st.header('this is a head')
st.subheader('this is a subhead')

code = '''
def hello(): 
    print('hello streamlit')
'''

st.code(code, language='python')



## ---- display code ---

with st.echo():
    st.write('this code will be printed')


def get_user_name():
    return 'John'

def get_punctuation():
    return '!!!'


greeting = 'hi here'
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ---up to here
# ---------------------------

foo = 'bar'
st.write('Done!')

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
