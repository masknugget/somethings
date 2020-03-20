import streamlit as st
import pandas as pd
import altair as alt
import numpy as np


df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
st.dataframe(df, 200, 100)

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(df.style.highlight_max(axis=0))


df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.table(df)


st.json(
    {
        'foo': 'bar',
        'baz': 'boz',
        'stuff':[
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 4',
        ],
    }
)


