from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(resume_texts):
    vectorizer = TfidfVectorizer()
    feature_matrix = vectorizer.fit_transform(resume_texts)
    return feature_matrix, vectorizer
