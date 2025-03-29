from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resumes, vectorizer):
    job_vector = vectorizer.transform([job_description])
    resume_vectors = vectorizer.transform(resumes)
    similarities = cosine_similarity(job_vector, resume_vectors)[0]
    
    ranked_resumes = sorted(
        zip(resumes.keys(), similarities), key=lambda x: x[1], reverse=True
    )
    return ranked_resumes
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resumes, vectorizer):
    job_vector = vectorizer.transform([job_description])
    resume_vectors = vectorizer.transform(resumes)
    similarities = cosine_similarity(job_vector, resume_vectors)[0]
    
    ranked_resumes = sorted(
        zip(resumes.keys(), similarities), key=lambda x: x[1], reverse=True
    )
    return ranked_resumes
