"""
Skill Gap Predictor
Author: [Your Name]
Note: Quick prototype to compare resumes with job descriptions,
highlight overlaps/missing skills, and predict candidate fit.
Outputs CSV + charts for recruiters.
"""

import pandas as pd
import ast
import matplotlib
matplotlib.use("Agg")  # safe backend (no GUI popups)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error

# Load datasets (make sure CSVs are in /data)
resumes = pd.read_csv("data/resume_data.csv")
jobs = pd.read_csv("data/job_dataset.csv")

# --- Resume skill parsing ---
def parse_resume_skills(raw_text):
    try:
        return [s.lower().strip() for s in ast.literal_eval(str(raw_text))]
    except Exception:
        # fallback: if parsing fails, just return empty list
        return []

resumes["resume_skills"] = resumes["skills"].apply(parse_resume_skills)

# Jobs dataset uses semicolons for skills — not ideal, but works for now
def parse_job_skills(raw_text):
    return [s.lower().strip() for s in str(raw_text).split(";") if s]

jobs["job_skills"] = jobs["Skills"].apply(parse_job_skills)

# Overlap logic (basic set ops)
def analyze_skills(resume_skills, job_skills):
    resume_set, job_set = set(resume_skills), set(job_skills)
    matched = list(resume_set & job_set)
    missing = list(job_set - resume_set)
    score = round((len(matched) / len(job_set)) * 100, 2) if job_set else 0.0
    return matched, missing, score

# Build training dataset (resume-job pairs by Title)
records = []
for _, cand in resumes.iterrows():
    for _, req in jobs.iterrows():
        if str(cand["Title"]).lower() == str(req["Title"]).lower():
            matched, missing, score = analyze_skills(cand["resume_skills"], req["job_skills"])
            label = 1 if score >= 30 else 0  # TODO: tune threshold later

            records.append({
                "resume_text": " ".join(cand["resume_skills"]),
                "job_text": " ".join(req["job_skills"]),
                "experience": int(str(cand.get("Experience_Years", "0")).split("-")[0]),
                "certifications": 1 if str(cand.get("Certifications", "")).strip() != "" else 0,
                "Fit_Label": label,
                "Match_Percentage": score,
                "Resume_ID": cand.get("Resume_ID", "R?"),
                "Job_ID": req.get("Job_ID", "J?")
            })

df = pd.DataFrame(records)

# Vectorize text + add numeric features
vectorizer = CountVectorizer()
X_text = vectorizer.fit_transform(df["resume_text"] + " " + df["job_text"])

X = pd.concat([
    pd.DataFrame(X_text.toarray(), columns=vectorizer.get_feature_names_out()),
    df[["experience", "certifications"]]
], axis=1)

y_class = df["Fit_Label"]
y_reg = df["Match_Percentage"]

results = []

# Classification preferred, regression fallback if only one class
if y_class.nunique() >= 2:
    X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("✅ Logistic Regression Accuracy:", accuracy_score(y_test, y_pred))

    # Predict fit scores
    for _, row in df.iterrows():
        text = row["resume_text"] + " " + row["job_text"]
        vec = vectorizer.transform([text])
        extra = pd.DataFrame([[row["experience"], row["certifications"]]], columns=["experience", "certifications"])
        X_input = pd.concat([pd.DataFrame(vec.toarray(), columns=vectorizer.get_feature_names_out()), extra], axis=1)

        prob = model.predict_proba(X_input)[0][1]  # probability of fit

        results.append({
            "Resume_ID": row["Resume_ID"],
            "Job_ID": row["Job_ID"],
            "Matched_Skills": ", ".join(set(row["resume_text"].split()) & set(row["job_text"].split())),
            "Missing_Skills": ", ".join(set(row["job_text"].split()) - set(row["resume_text"].split())),
            "Match_Percentage": f"{row['Match_Percentage']}%",
            "AI_Fit_Score": round(prob * 100, 2)
        })
else:
    # Regression fallback — not perfect, but better than nothing
    model = LinearRegression()
    model.fit(X, y_reg)
    y_pred = model.predict(X)
    print("⚠️ Regression fallback. RMSE:", mean_squared_error(y_reg, y_pred, squared=False))

    for _, row in df.iterrows():
        text = row["resume_text"] + " " + row["job_text"]
        vec = vectorizer.transform([text])
        extra = pd.DataFrame([[row["experience"], row["certifications"]]], columns=["experience", "certifications"])
        X_input = pd.concat([pd.DataFrame(vec.toarray(), columns=vectorizer.get_feature_names_out()), extra], axis=1)

        pred_score = model.predict(X_input)[0]

        results.append({
            "Resume_ID": row["Resume_ID"],
            "Job_ID": row["Job_ID"],
            "Matched_Skills": ", ".join(set(row["resume_text"].split()) & set(row["job_text"].split())),
            "Missing_Skills": ", ".join(set(row["job_text"].split()) - set(row["resume_text"].split())),
            "Match_Percentage": f"{row['Match_Percentage']}%",
            "AI_Fit_Score": round(pred_score, 2)
        })

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv("data/skill_gap_results.csv", index=False)
print("✅ Results saved to data/skill_gap_results.csv")

# Visualization: Top 10 candidates
top10 = results_df.sort_values("AI_Fit_Score", ascending=False).head(10)
if not top10.empty:
    plt.figure(figsize=(10, 6))
    plt.barh(top10["Resume_ID"], top10["AI_Fit_Score"], color="skyblue")
    plt.xlabel("AI Fit Score (%)")
    plt.ylabel("Resume ID")
    plt.title("Top 10 Resumes by AI Fit Score")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("data/fit_score_chart.png")
    print("📊 Chart saved to data/fit_score_chart.png")

# Heatmap of missing skills
all_missing = []
for skills in results_df["Missing_Skills"]:
    if isinstance(skills, str) and skills.strip():
        all_missing.extend([s.strip() for s in skills.split(",") if s.strip()])

missing_counts = pd.Series(all_missing).value_counts().reset_index()
missing_counts.columns = ["Skill", "Count"]

if not missing_counts.empty:
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        missing_counts.pivot_table(values="Count", index="Skill", aggfunc="sum"),
        cmap="Reds", annot=True, fmt="d", cbar=False
    )
    plt.title("Most Common Missing Skills Across Resumes")
    plt.tight_layout()
    plt.savefig("data/missing_skills_heatmap.png")
    print("🔥 Heatmap saved to data/missing_skills_heatmap.png")