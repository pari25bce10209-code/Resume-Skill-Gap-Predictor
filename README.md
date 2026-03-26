                                                         Resume Skill Gap Predictor
                                                  A Project in Fundamentals of AI & ML    
Submitted by: Pari Gangil 
Registration no-25BCE10209

Detailed Readme- https://github.com/pari25bce10209-code/Resume-Skill-Gap-Predictor/blob/main/README.pdf
# Resume Skill Gap Predictor 

## Project Overview
The Resume Skill Gap Predictor is a machine learning-based tool designed to compare resumes with job descriptions, identify missing skills, and generate an AI Fit Score. It helps recruiters shortlist candidates efficiently and provides students with clear feedback on skill gaps.

---

## Problem Statement
Recruiters and students face challenges due to mismatched skills:

- Recruiters receive many resumes in different formats
- Manual screening is slow and error-prone
- Students do not know why they were rejected

### Key Issues
- Time-consuming screening process  
- Inconsistent evaluation  
- Lack of transparency  

---

## Solution
This project provides a structured way to:

- Compare resumes with job descriptions  
- Identify matched and missing skills  
- Generate an AI Fit Score using machine learning  
- Visualize results using charts  

### Benefits
- Recruiters: Faster and clearer shortlisting  
- Students: Understand and improve missing skills  
- Institutions: Data-driven placement insights  

---

## Key Features
- Resume–Job Matching  
- AI Fit Score using Logistic Regression  
- Batch Processing  
- Output files:
  - `skill_gap_results.csv`
  - `fit_score_chart.png`
  - `missing_skills_heatmap.png`

---

## Project Structure
```
project-root/
│── data/
│   ├── resume_dataset.csv
│   ├── job_descriptions.csv
│
│── src/
│   └── skill_gap_predictor.py
│
│── outputs/
│   ├── skill_gap_results.csv
│   ├── fit_score_chart.png
│   ├── missing_skills_heatmap.png
│
│── README.md
```

---

## Technologies Used
- Programming Language: Python 3.x  

- Libraries:
  - pandas  
  - numpy  
  - scikit-learn  
  - matplotlib  
  - seaborn  
  - ast  

- Data Format: CSV  

---

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher  

Install required libraries:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

### 2. Clone Repository
```bash

```
git clone https://github.com/pari25bce10209-code/Resume-Skill-Gap-Predictor.git
---

### 3. Prepare Data
Place datasets in the `data/` folder:

- `resume_dataset.csv`
- `job_descriptions.csv`
- or upload your own dataset of resume and job description
  just not that-

Notes:
- Resume dataset must contain a skills column  
- Job dataset must contain skills separated by semicolons (;)  
- Job titles should match  

---

### 4. Run the Project
```bash
python scripts/skill_gap_predictor.py
```

---

### 5. Outputs
After running the script:

- `skill_gap_results.csv` → Resume-job matches with scores  <img width="1234" height="589" alt="image" src="https://github.com/user-attachments/assets/c1469332-f14b-47af-a466-70a36f214e4a" />
- `fit_score_chart.png` → Top candidates chart  <img width="993" height="565" alt="image" src="https://github.com/user-attachments/assets/010867a1-6c8b-4834-86ff-28746658498d" />
- `missing_skills_heatmap.png` → Skill gap heatmap  <img width="1371" height="603" alt="image" src="https://github.com/user-attachments/assets/e6ab2b36-09ed-463b-bd0a-13fcd1e2f32f" />

## Example Insights

### Recruiter View
- Identify top candidates quickly  
- Focus on high-fit resumes  
- Use charts for decision-making  

### Student View
- See missing skills clearly  
- Understand improvement areas  
- Prepare better for applications  

### Institutional Impact
- Transparent placement process  
- Better training alignment  

---

## Limitations
- Exact keyword matching only  
- Limited error handling  
- Requires structured CSV input  
- Prototype-level project  

---

## Future Work
- Advanced matching (TF-IDF, NLP)  
- Better error logging  
- Support for PDF/DOCX resumes  
- Dashboard interface  
- Unit testing  

---

## Acknowledgements
- Faculty mentors  
- Peers and classmates  
- VIT Bhopal  
- Industry professionals
