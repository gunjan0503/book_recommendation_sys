import streamlit as st
import pickle
import pandas as pd

def recommend(book):
    # Find the index of the selected book title
    index = books[books['BookTitle'] == book].index
    if not index.empty:
        index = index[0]

        # Ensure that the index is within the bounds of the similarity array
        if 0 <= index < len(similarity):
            # Retrieve similar books based on the similarity scores
            similar_items = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)[1:6]

            # Extract book titles of recommended books
            recommended_books = []
            for i in similar_items:
                book_index = i[0]
                if 0 <= book_index < len(books):
                    recommended_books.append(books.iloc[book_index].BookTitle)
            return recommended_books


similarity=pickle.load(open('similar.pkl','rb'))

books_list=pickle.load(open('books_dict.pkl','rb'))

books=pd.DataFrame(books_list)

st.title("BOOK RECOMMENDATION SYSTEM")
selected_books = st.selectbox(
    'Which book do you like most?',
     books['BookTitle'].values)

if st.button('RECOMMEND '):
      recommendations=recommend(selected_books)
      for i in recommendations:
        st.write(i)