import pandas as pd
from pandas import DataFrame

df_imbd = DataFrame.from_csv(r"C:\Users\Administrator\PycharmProjects\candidateelimination\imdb_labelled.txt",sep='\t',index_col=None)

print(df_imbd.keys())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_imbd['Text'], df_imbd['Label'],train_size=0.8,random_state=100)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

word_freq_df = pd.DataFrame(X_train_cv.toarray(), columns=cv.get_feature_names())
top_words_df = pd.DataFrame(word_freq_df.sum()).sort_values(0, ascending=False)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()

naive_bayes.fit(X_train_cv, y_train)
predictions = naive_bayes.predict(X_test_cv)

from sklearn.metrics import accuracy_score, precision_score, recall_score
print('Accuracy score: ', accuracy_score(y_test, predictions))
print('Precision score: ', precision_score(y_test, predictions))
print('Recall score: ', recall_score(y_test, predictions))

#print(word_freq_df)
#print(top_words_df)
