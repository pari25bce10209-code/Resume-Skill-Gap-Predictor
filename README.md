                                                         Resume Skill Gap Predictor
                                                  A Project in Fundamentals of AI & ML
Submitted by: Pari Gangil

- Problem Statement
Recruiters and students face different frustrations during campus placements, but both stem from the same issue: skills do not align clearly between resumes and job descriptions.
~ Recruiters deal with:
        Hundreds of resumes in inconsistent formats
        Time-consuming manual screening
        Risk of missing good candidates
~ Students face:
       Lack of feedback on rejections
       No clarity on missing skills
       Uncertainty about how close they were
~Current Challenges
      Time wasted on repetitive screening
      Formatting differences hide skills
      No transparency for students
~Need
  A system that can:
  Compare resumes with job descriptions
  Highlight matched and missing skills
  Help recruiters shortlist quickly
  Provide actionable feedback to students
-Problem Solution
  The Skill Gap Predictor uses machine learning to bridge this gap.
~What it does
  Compares resumes with job descriptions
  Calculates an AI Fit Score
  Highlights missing skills
  Generates visual insights
~Benefits
  For Recruiters
  Quick shortlist of candidates
  Skill overlap percentages
  Visual charts for decision-making
~For Students
  Clear feedback on missing skills
  Direction for upskilling
~For Institutions
  Data-driven placement support
  Better alignment with industry needs
-Technical Approach
    Parses resumes and job descriptions into structured data
    Uses Logistic Regression (with fallback option)
    Generates CSV outputs and visualizations
~Key Features
    Resume–Job Matching: Identifies matched and missing skills
    AI Fit Score: Based on Logistic Regression
    Batch Processing: Handles multiple candidates efficiently

~Outputs
IN PDF LINK-
SCREENSHOTS INCLUDE
  skill_gap_results.csv: Match results with scores
  fit_score_chart.png: Top 10 candidates
  missing_skills_heatmap.png: Skill gap visualization
~Technologies Used
  Language: Python 3.10
  Libraries
  pandas: Data handling
  ast: Parsing structured text
  scikit-learn: Machine learning models
  matplotlib, seaborn: Visualization
~Data Format
  CSV files for resumes and job descriptions
~Setup Instructions
    1. Prerequisites
      Make sure you have:
        Python 3.8 or higher
      Install required libraries:
          pip install pandas numpy scikit-learn matplotlib seaborn
    2. Clone the Repository
          git clone <your-repo-link>
    3. Prepare Your Data
        Place datasets in the data/ folder:
        data/resume_dataset.csv
        data/job_descriptions.csv
            Notes:
              Resume dataset must contain a skills column
              Job dataset must have skills separated by semicolons (;)
              Job titles should match in both datasets
    4. Run the Predictor
            python scripts/skill_gap_predictor.py
    5. Check Outputs
            Results will be generated in the data/ folder:

~Example Insights
      Recruiter View
        identify top candidates quickly
        Focus on high-fit resumes
        Use charts for faster decisions
      Student View
        Understand missing skills (e.g., cloud platforms, Angular, Kubernetes)
        See how close they were to selection
        Plan improvements accordingly
      Institutional Impact
        Data-driven placement process
        Better alignment with industry requirements
        Increased transparency
~Limitations and Future Work
    Current Limitations
      Exact skill matching only (no synonym handling like ML vs Machine Learning)
      Minimal error handling
      Works only with structured CSV data
      Prototype-level system
~Future Improvements
    Smarter matching using TF-IDF or embeddings
    Improved error handling with logging
    Support for PDF and DOCX resumes
    Recruiter feedback integration
    Unit testing
    Web dashboard for easier usage
~Acknowledgements
    Faculty Mentors for guidance and support
    Peers and classmates for collaboration and feedback
    VIT Bhopal for providing the academic environment
    Recruiters and industry professionals for inspiring the problem
