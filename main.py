from resume_parser import extract_resumes_from_folder
from text_preprocessing import preprocess_text
from feature_extraction import extract_features
from resume_ranking import rank_resumes

# Define the job description
job_description = """Looking for a Python Developer with experience in machine learning, NLP, and data science.
Should be familiar with TensorFlow, Scikit-learn, and NLP libraries like NLTK or SpaCy."""

# Load resumes from the folder
resumes = extract_resumes_from_folder("resumes_folder")

# Preprocess resumes
processed_resumes = {name: preprocess_text(text) for name, text in resumes.items()}

# Extract features
resume_texts = list(processed_resumes.values())
feature_matrix, vectorizer = extract_features(resume_texts)

# Rank resumes
ranked_resumes = rank_resumes(job_description, processed_resumes, vectorizer)

# Display results
print("\nTop Ranked Resumes:")
for rank, (filename, score) in enumerate(ranked_resumes, 1):
    print(f"{rank}. {filename} - Score: {score:.2f}")
from resume_parser import extract_resumes_from_folder
from text_preprocessing import preprocess_text
from feature_extraction import extract_features
from resume_ranking import rank_resumes

# Define the job description
job_description = """Looking for a Python Developer with experience in machine learning, NLP, and data science.
Should be familiar with TensorFlow, Scikit-learn, and NLP libraries like NLTK or SpaCy."""

# Load resumes from the folder
resumes = extract_resumes_from_folder("resumes_folder")

# Preprocess resumes
processed_resumes = {name: preprocess_text(text) for name, text in resumes.items()}

# Extract features
resume_texts = list(processed_resumes.values())
feature_matrix, vectorizer = extract_features(resume_texts)

# Rank resumes
ranked_resumes = rank_resumes(job_description, processed_resumes, vectorizer)

# Display results
print("\nTop Ranked Resumes:")
for rank, (filename, score) in enumerate(ranked_resumes, 1):
    print(f"{rank}. {filename} - Score: {score:.2f}")
