# import required libraries for data pre-processing,data analysis
# pandas is most famous data manipulation and analysis library
# pandas used for working with tabular data like spreadsheets


import numpy as np
import pandas as pd

# read the csv files using pandas and create data frames for each of them
# data frame is a two-dimensional table-like data structure
# similar to spreadsheets ,where data us organized in rows and columns.

# books=pd.read_csv('Books.csv')
books = pd.read_csv('Books.csv', low_memory=False)
users=pd.read_csv('Users.csv')
ratings=pd.read_csv('Ratings.csv')

# get top 5 records of the dataframe -head will do that for u
print(books.head())

print(users.head())

print(ratings.head())

# get bottom 5 records of the dataframe -tail will do that for u
print(books.tail())

print(users.tail())

print(ratings.tail())

# get the column names of the files - df.columns will give that
print("\n Columns in Books.csv file \n")
print(books.columns)
print("\n Columns in Users.csv file \n")
print(users.columns)
print("\n Columns in Ratings.csv file \n")
print(ratings.columns)


# get the shape of the data frame - number of rows & number of columns

print(books.shape)
print(users.shape)
print(ratings.shape)

# to get the count of missing values (NaN or null values)
# in each column of the dataframe
print(books.isnull().sum())

# above line of code returns the number of null values in each column has
# but how it works??

# df.isnull()  ---> changes the current data frame with same shape
# but the values all are replaced by the boolean values whether it is null or not as true and false
# df.isnull().sum() -->applies the function along vertical axis
# returns the count of missing values for eahc column

print("books Missing /NaN/Null Values")
print(books.isnull().sum())
# very few null values found in books dataframe

print("users Missing /NaN/Null Values")
print(users.isnull().sum())
# in users age column has almost 50% values are missing - but we dont need for our analysis

print("ratings Missing /NaN/Null Values")
print(ratings.isnull().sum())
# In ratings no null values are missing


print("books duplicated Values")
print(books.duplicated().sum())
# no duplicate values found in books dataframe

print("users duplicated Values")
print(users.duplicated().sum())
#no duplicate values found in users dataframe

print("ratings duplicated Values")
print(ratings.duplicated().sum())
# no duplicate values found in rating data frame


# Model building
# Popularity Based Recommender system
# Not much complex formulae is used here
# Highest average rated books are shown - top 50 rated books
# but we consider only those books which have atleast 250 ratings to the book

print(books)
print(ratings)

# merge the ratings dataframe with the books data frame -
# new data frame is created based on the ratings which are also
# there in the books data frame remaining are eliminated

# merge - common operation in data analysis used to perform merging two dataframes
# based on the common column -
# when we want to combine them based on a shared key or column

ratings_with_books=ratings.merge(books,on='ISBN')
print(ratings_with_books)

# nearly half of the rows got eliminated since few books are not rated  OR
# few rated books are not in the books data frame

print(ratings_with_books.shape)

ratings_with_name=ratings.merge(books,on='ISBN')
print(ratings_with_name)

# The resulting DataFrame 'ratings_with_name' will have columns from both 'ratings' and 'books'.
# Each row will represent a rating entry with additional information about the corresponding book
# from the 'books' DataFrame.

print(ratings_with_name.columns)

ratings_with_name.groupby('Book-Title')
# this will return dataframe groupby Book-Title
print(ratings_with_name.groupby('Book-Title'))

# this will return dataframe count of the rows groupby Book-Title
print(ratings_with_name.groupby('Book-Title').count())

print(ratings_with_name.groupby('Book-Title').count().shape)

print(ratings_with_name.groupby('Book-Title').count().columns)


# the below code will give the results from the merged data frame
# th merged dataframe is group by book title and taken Book-Rating from the dataframe
print(ratings_with_name.groupby('Book-Title').count()['Book-Rating'])

# what we got from the above line of code and how we got
# ratings_with_name: This is the DataFrame obtained after merging the 'ratings' DataFrame with the 'books' DataFrame, as mentioned in the previous code you provided.

# groupby('Book-Title'): This part of the code groups the rows in the 'ratings_with_name' DataFrame based on the unique values in the 'Book-Title' column.
#
# count(): After grouping, the count() function is applied to each group, which returns the number of non-null elements in each group. Since we are applying this to the entire DataFrame,
# it calculates the count for each book title.
#
# ['Rating']: This is used to select the 'Rating' column from the grouped and counted data. The count function is applied specifically to the 'Rating' column,
# giving us the number of ratings for each book title.

ratings_with_name.groupby('Book-Title').count()['Book-Rating']
# The result will be a Series with the book titles as the index and the corresponding count of ratings for each book as the values. It will give you an idea of how many ratings
# each book has received in the 'ratings_with_name' DataFrame after the merge.

num_rating_df=ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
# reset_index(): This function is used to reset the index of the resulting Series (or DataFrame) to the default integer index. By default, the book titles are set as the index after the groupby operation,
# but resetting the index will make the book titles appear as a regular column in the DataFrame.

# The resulting DataFrame num_rating_df will have two columns: 'Book-Title' and 'Book-Rating'. The 'Book-Title' column will contain the unique book titles,
# and the 'Book-Rating' column will contain the count of ratings for each book title. This DataFrame
# provides a summary of the number of ratings for each book title in the 'ratings_with_name' DataFrame.

num_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace=True)
# inplace=True: This parameter in the rename() method allows you to modify the DataFrame in place (without creating a new DataFrame).
# When inplace=True, the original DataFrame (num_rating_df in this case) will be updated with the new column name.
#  If inplace=False (the default), a new DataFrame with the updated column name will be returned, and you need to assign it back to a variable if you want to use it.
#
# After executing this code, the DataFrame num_rating_df will have the column name 'Book-Rating' changed to 'num_ratings'.
# This renaming can make the DataFrame more readable and easier to work with in subsequent data analysis or visualization tasks.


print(num_rating_df)

# num_rating_df: This is the DataFrame obtained after performing the previous operations, where you grouped the 'ratings_with_name' DataFrame by 'Book-Title'
# and counted the number of ratings for each book title.

print(num_rating_df.head())


# this time let`s go with average rating of the book

avg_rating_df=ratings_with_name.groupby('Book-Title').mean()['Book-Rating'].reset_index()

print(avg_rating_df)

avg_rating_df.rename(columns={'Book-Rating':'avg_rating'},inplace=True)

print(avg_rating_df)

print(avg_rating_df.head())

popular_df=num_rating_df.merge(avg_rating_df,on='Book-Title')

print(popular_df)

print(popular_df.columns)

print(popular_df['num_ratings'])


# keep only those whose num_ratings >=250
print(popular_df[popular_df['num_ratings']>=250])

# so we keep all those which crosses num_ratings>250 and sort them by avg_rating in descending order
print(popular_df[popular_df['num_ratings']>=250].sort_values('avg_rating',ascending=False))

# get top 50 of those
print(popular_df[popular_df['num_ratings']>=250].sort_values('avg_rating',ascending=False).head(50))


popular_df=popular_df[popular_df['num_ratings']>=250].sort_values('avg_rating',ascending=False).head(50)
print(popular_df)

print(popular_df.columns)

# let`s merge popular_df with books data frame
print(popular_df.merge(books,on='Book-Title'))

# remove all the duplicates

print(popular_df.merge(books,on='Book-Title').drop_duplicates('Book-Title'))

print(popular_df.merge(books,on='Book-Title').drop_duplicates('Book-Title').shape)

print(popular_df.merge(books,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_rating']])

popular_df=popular_df.merge(books,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_rating']]

print(popular_df)

x=ratings_with_name.groupby('User-ID').count()['Book-Rating']>200

print(x[x].index)

read_and_rate_users=x[x].index
# read_and_rate_users are those who gave atleast 200 ratings to different books


# filter based on the ratings which books have atleast 200 ratings
filtered_rating=ratings_with_name[ratings_with_name['User-ID'].isin(read_and_rate_users)]

print(filtered_rating)


# now filter based on the books which book have read by atleast 50 users

# we will be getting book titles with the count of their corresponding book ratings

filtered_rating.groupby('Book-Title').count()['Book-Rating']

print(filtered_rating.columns)


# let`s take those books which have atleast 50 ratings
y=filtered_rating.groupby('Book-Title').count()['Book-Rating']>=50

famous_books=y[y].index

print(famous_books)

# keep only those books which has atleast 50 ratings and consider only those user`s
# ratings who gave atleast 200 ratings to the books

final_ratings=filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]

print(final_ratings)

# drop_duplicates from the final_ratings

print(final_ratings.drop_duplicates())

final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')

# what does above pivot operation does?
# pivot_table(...): This method is applied to the final_ratings DataFrame to create a pivot table based on specific parameters:
#
# index='Book-Title': This specifies the column ('Book-Title') that will become the index of the pivot table. The pivot table will have unique book titles as rows.
#
# columns='User-ID': This specifies the column ('User-ID') that will become the columns of the pivot table. The pivot table will have unique user IDs as columns.
#
# values='Book-Rating': This specifies the column ('Book-Rating') whose values will be used to fill the cells of the pivot table. In this case, it will be the book ratings given by each user for different books.
#
# The resulting pivot table will have book titles as rows, user IDs as columns, and the corresponding book ratings as the values in the cells. It will allow you to quickly visualize
#
# and analyze the rating patterns given by different users for different books. The cells where there are no ratings (missing values) indicate that a particular user has not rated that book.

# Pivot tables are helpful for various data exploration tasks, such as identifying popular books, finding users with similar rating patterns, or understanding overall rating distributions.

# They are widely used in data analysis and are especially valuable when dealing with large datasets containing multiple variables.

print(final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating'))

pt=final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')

pt.fillna(0,inplace=True)

print(pt)

print(pt.index[545])

from sklearn.metrics.pairwise import cosine_similarity

# let`s obtain the euclidean distamce of each and every book
# we have totally 706 books.
# so totally 706,706 size

print(cosine_similarity(pt).shape)

similarity_score=cosine_similarity(pt)
print(similarity_score)

# similarity_score of first book with all the existing books (cosine similarity)
print(similarity_score[0])


# print(np.where(pt.index=='4 Blondes')[0][0])
# gives the similarity_score of first books with all other books
print(similarity_score[0])

# list of all the books of their similarity scores with their indices
l=list(enumerate(similarity_score[0]))

# sort them based on the similarity_score - descending order
l=sorted(l,key=lambda x:x[1],reverse=True)

print(l)

def recommend(book_name):
    #index fetch
    index=np.where(pt.index == book_name)[0][0]
    l = list(enumerate(similarity_score[index]))

    # sort them based on the similarity_score - descending order
    l = sorted(l, key=lambda x: x[1], reverse=True)[1:6]

    similar_items=l
    data=[]
    for i in similar_items:
        # print(pt.index[i[0]])
        item=[]
        temp_df=books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return data



print("\n")
print("Books to be recommended for book '1984' are:- ")
print(recommend('1984'))

print("\n")
print("Books to be recommended for book 'Message in a Bottle' are:- ")
print(recommend('Message in a Bottle'))

print("\n")

print("Books to be recommended for book 'The Da Vinci Code' are:- ")
print(recommend('The Da Vinci Code'))

print("\n")

import pickle

pickle.dump(popular_df,open('popular.pkl','wb'))

pickle.dump(pt,open('pt.pkl','wb'))
pickle.dump(books,open('books.pkl','wb'))
pickle.dump(similarity_score,open('similarity_score.pkl','wb'))