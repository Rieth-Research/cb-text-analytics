# Getting Started with Central Bank Analytics

Welcome! This guide will help you get up and running with text analytics in just a few minutes.

## 🎯 What You'll Accomplish

By the end of this guide, you'll:
- Have all dependencies installed
- Run your first analysis
- Understand the project structure
- Know where to go next

## ⏱️ Time Required

- **Quick setup**: 5-10 minutes
- **First tutorial**: 30 minutes
- **All tutorials**: ~3-4 hours (at your own pace)

## 📋 Prerequisites

- **Python 3.8 or higher** installed on your computer
- **Basic Python knowledge** (variables, functions, loops)
- **Terminal/Command prompt** access
- **(Optional)** Git for version control

### Check Your Python Version

Open a terminal and run:

```bash
python --version
# or
python3 --version
```

If you see `Python 3.8.x` or higher, you're good to go!

## 🚀 Step-by-Step Setup

### Step 1: Navigate to the Project

```bash
cd cb-text-analytics
```

### Step 2: (Optional) Create a Virtual Environment

This keeps dependencies organized and separate from other projects.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You'll see `(venv)` in your terminal when activated.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas (data manipulation)
- matplotlib, seaborn, plotly (visualizations)
- nltk, vaderSentiment (text analysis)
- wordcloud (word clouds)
- jupyter (notebooks)

**Installation takes 2-3 minutes.**

### Step 4: Verify Installation

```bash
python -c "import pandas, matplotlib, vaderSentiment; print('✓ All packages installed!')"
```

If you see the success message, you're ready!

## 🎓 Choose Your Learning Path

### Path A: Quick Overview (5 minutes)

Want to see results immediately?

```bash
python src/quick_analysis.py
```

This will:
- Load all central bank statements
- Calculate sentiment scores
- Generate visualizations
- Create a summary report

**Output**: `quick_analysis_results.png` with four charts

### Path B: Hands-On Tutorials (Recommended)

Learn by doing with interactive notebooks:

```bash
jupyter notebook
```

This opens Jupyter in your browser. Navigate to `tutorials/` and start with:

1. **01_loading_and_exploring_data.ipynb** (30 min)
   - Perfect first step
   - Learn data basics
   - No previous knowledge required

Then continue in order through tutorials 2-4.

### Path C: Read First, Code Later

Prefer reading before coding?

1. Read the main **README.md** for project overview
2. Browse through the tutorial notebooks to see what they cover
3. Check out the `src/quick_analysis.py` script to see example code
4. Start tutorials when ready

## 📚 Tutorial Details

### Tutorial 1: Loading & Exploring Data
**Time**: 30 minutes
**You'll learn**:
- How to read text files
- Organizing data with pandas
- Basic statistics
- Your first data analysis

**Start here if**: You're new to text analytics or pandas

### Tutorial 2: Text Analysis Basics
**Time**: 45 minutes
**You'll learn**:
- Cleaning text data
- Word frequency analysis
- Tracking keywords
- Creating charts

**Prerequisites**: Tutorial 1

### Tutorial 3: Sentiment Analysis
**Time**: 1 hour
**You'll learn**:
- What is sentiment analysis?
- Hawkish vs dovish detection
- Tracking sentiment over time
- Finding important shifts

**Prerequisites**: Tutorials 1-2

### Tutorial 4: Advanced Visualizations
**Time**: 1 hour
**You'll learn**:
- Word clouds
- Heatmaps
- Interactive plots
- Publication-ready charts

**Prerequisites**: Tutorials 1-3

## 💡 Tips for Success

### 1. Run Every Code Cell

Don't just read - **run the code**! You learn by doing.

In Jupyter:
- Click a cell
- Press `Shift + Enter` to run it
- Watch the output

### 2. Experiment

After running example code, try changing things:
- Different time ranges
- New keywords
- Alternative visualizations

**Breaking things is part of learning!**

### 3. Do the Exercises

Each tutorial ends with exercises. They help cement your learning.

### 4. Take Breaks

Text analytics is fun but can be intense. Take breaks between tutorials.

### 5. Ask Questions

Stuck? Common issues and solutions:

**Problem**: `ModuleNotFoundError`
**Solution**: Run `pip install -r requirements.txt` again

**Problem**: Jupyter won't start
**Solution**: Try `pip install --upgrade jupyter`

**Problem**: Plots don't show
**Solution**: Make sure you have `%matplotlib inline` in notebooks

## 🔍 Understanding the Data

### What's in the Dataset?

**Federal Reserve (Fed)**:
- 30 statements from 2014-2017
- FOMC (Federal Open Market Committee) decisions
- About 200-400 words each

**Reserve Bank of New Zealand (RBNZ)**:
- 46 statements from 2006-2012
- OCR (Official Cash Rate) announcements
- Varies in length

### Where Does It Come From?

- Fed: https://www.federalreserve.gov/
- RBNZ: https://www.rbnz.govt.nz/

All data is publicly available official communications.

## 🎯 After Completing the Tutorials

Congratulations! You now know text analytics. Here's what to do next:

### 1. Expand the Dataset

Download more recent statements:
- Fed: 2018-2024 data
- Add ECB, Bank of England, Bank of Japan

### 2. Build Something

Ideas:
- **Dashboard**: Create a Streamlit web app
- **Report**: Generate automated monthly analysis
- **Alert system**: Detect unusual language patterns
- **Comparison tool**: Analyze multiple banks side-by-side

### 3. Advanced Topics

- **Topic Modeling**: Discover hidden themes (LDA, NMF)
- **Named Entity Recognition**: Extract specific entities
- **Word Embeddings**: Use Word2Vec or BERT
- **Predictive Modeling**: Forecast rate decisions

### 4. Share Your Work

- Create a blog post about your findings
- Share visualizations on social media
- Contribute improvements back to this project
- Present at a local meetup

## 📖 Additional Resources

### Python & Pandas
- [Python for Data Analysis (book)](https://wesmckinney.com/book/)
- [Pandas documentation](https://pandas.pydata.org/docs/)

### NLP & Text Analytics
- [Natural Language Processing with Python (book)](https://www.nltk.org/book/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)

### Visualization
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Plotly documentation](https://plotly.com/python/)

### Central Banking
- [Federal Reserve Education](https://www.federalreserveeducation.org/)
- [BIS Papers on Central Bank Communication](https://www.bis.org/)

## ❓ Common Questions

**Q: Do I need to know Python well?**
A: Basic Python helps, but tutorials explain everything step-by-step.

**Q: Can I use this for other text analysis?**
A: Absolutely! The techniques apply to any text data.

**Q: How long until I can do my own analysis?**
A: After Tutorial 3 (2-2.5 hours), you'll have all the core skills.

**Q: Is this suitable for research?**
A: Yes! The methods are academically sound. Consider adding citations.

**Q: Can I use this data commercially?**
A: Central bank statements are public domain. Check LICENSE for code.

## 🚦 Your First 30 Minutes

Here's a suggested plan for your first session:

**Minutes 0-5**: Installation
```bash
pip install -r requirements.txt
```

**Minutes 5-10**: Quick analysis
```bash
python src/quick_analysis.py
```
Look at the output and charts.

**Minutes 10-15**: Start Jupyter
```bash
jupyter notebook
```
Open Tutorial 1.

**Minutes 15-30**: Work through first section of Tutorial 1
- Load the data
- See your first DataFrame
- Calculate basic statistics

**Result**: You've loaded real central bank data and done analysis!

## 🎉 You're Ready!

You have everything you need to start. Choose your path:

- 🏃‍♂️ **Quick start**: Run `python src/quick_analysis.py`
- 📚 **Deep dive**: Open `tutorials/01_loading_and_exploring_data.ipynb`
- 📖 **Browse**: Look through files to get oriented

**Most importantly: Have fun!** Text analytics is powerful and rewarding.

---

**Questions or issues?** Check the main README.md or examine the tutorial code.

**Ready to begin?** Pick a path above and start your text analytics journey!

🚀 **Let's analyze some central bank communications!**
