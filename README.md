# Central Bank Communication Analytics

A comprehensive text analytics toolkit for analyzing central bank communications. Learn to extract **objective, measurable insights** from monetary policy statements using natural language processing, topic modeling, and data visualization.

## 📋 What This Project Does

This project helps you:
- **Discover topics** automatically using statistical methods (LDA)
- **Track concrete keywords** and economic terms over time
- **Measure language complexity** and communication patterns
- **Compare language use** across different central banks
- **Visualize trends** in monetary policy communication
- **Learn text analytics** through hands-on tutorials with real data

## 🎓 Perfect For

- **Students** learning text analytics and NLP
- **Researchers** studying central bank communications
- **Financial analysts** tracking monetary policy signals
- **Data scientists** building text analysis pipelines
- **Anyone curious** about how central banks communicate

## 📊 Current Dataset

- **Federal Reserve (Fed)**: 30 FOMC statements (2014-2017)
- **Reserve Bank of New Zealand (RBNZ)**: 46 OCR statements (2006-2012)
- Easy to extend with more banks and time periods

## 🚀 Quick Start

### 1. Install Dependencies

**Using uv (recommended - fast!):**
```bash
uv sync
```

**Or using pip:**
```bash
pip install -r requirements.txt
```

### 2. Start Learning

Open the interactive tutorials in order:

```bash
# With uv:
uv run jupyter notebook

# With pip:
jupyter notebook
```

Then navigate to `tutorials/` folder.

**Tutorial Sequence:**
1. `01_loading_and_exploring_data.ipynb` - Load and understand your data (30 min)
2. `02_text_analysis_basics.ipynb` - Word frequency and basic patterns (45 min)
3. `03_topic_modeling_and_patterns.ipynb` - Topic modeling and objective analysis (1 hour)
4. `04_advanced_visualizations.ipynb` - Publication-ready charts (1 hour)

### 3. Run Quick Analysis

For a quick analysis without tutorials:

```bash
# With uv:
uv run python src/quick_analysis.py

# With pip:
python src/quick_analysis.py
```

## 📚 What You'll Learn

### Tutorial 1: Data Loading & Exploration
- Reading text files with Python
- Working with pandas DataFrames
- Basic text statistics
- Data organization

### Tutorial 2: Text Analysis Basics
- Text preprocessing and cleaning
- Word frequency analysis
- Tracking keywords over time
- Creating visualizations
- Understanding bigrams

### Tutorial 3: Topic Modeling & Patterns
- Topic modeling with LDA (discover hidden themes)
- Tracking concrete economic terms
- Measuring language complexity objectively
- Vocabulary diversity analysis
- Finding communication pattern shifts

### Tutorial 4: Advanced Visualizations
- Creating word clouds
- Building heatmaps
- Interactive Plotly dashboards
- Multi-dimensional analysis
- Export-ready charts

## 🛠️ Tech Stack

- **Python 3.8+**
- **pandas** - Data manipulation
- **nltk & scikit-learn** - Natural language processing & topic modeling
- **matplotlib, seaborn, plotly** - Visualizations
- **wordcloud** - Word cloud generation
- **jupyter** - Interactive notebooks

## 📁 Project Structure

```
cb-text-analytics/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── pyproject.toml            # Modern Python project config (uv support)
├── tutorials/               # Step-by-step learning notebooks
│   ├── 01_loading_and_exploring_data.ipynb
│   ├── 02_text_analysis_basics.ipynb
│   ├── 03_topic_modeling_and_patterns.ipynb
│   └── 04_advanced_visualizations.ipynb
├── src/                     # Utility scripts
│   └── quick_analysis.py    # Quick analysis script
├── usa-central-bank/        # Fed statements
│   ├── fomc-statements/
│   ├── fomc-statements-no-votes/
│   └── fomc-implementation-note/
└── nz-central-bank/         # RBNZ statements
    └── ocr/
```

## 💡 Example Analyses

### Topic Discovery
Automatically discover hidden themes in statements using statistical methods (LDA).

### Language Complexity Trends
Track how complex or simplified central bank language becomes over time.

### Keyword Tracking
Monitor mentions of "inflation", "employment", "growth" over time.

### Comparative Analysis
See how different central banks communicate about similar issues.

## 🎯 Next Steps After Tutorials

1. **Add More Data**
   - Download recent statements
   - Include more central banks (ECB, BoE, BoJ, etc.)

2. **Advanced NLP**
   - Topic modeling (LDA)
   - Named entity recognition
   - Embedding-based analysis

3. **Build Dashboards**
   - Create Streamlit web app
   - Add real-time data feeds
   - Automated report generation

4. **Predictive Modeling**
   - Correlate language with rate decisions
   - Build forecast models
   - Anomaly detection

## 📖 Learning Resources

### Inspiration
- [Canada's Monetary Policy Report: If Text Could Speak, What Would It Say?](https://github.com/bankofcanada/MPR-Text-Analytics-2019)

### Additional Reading
- Federal Reserve statements: https://www.federalreserve.gov/
- RBNZ statements: https://www.rbnz.govt.nz/
- Text analytics with Python
- Financial NLP techniques

## 🤝 Contributing

Feel free to:
- Add more central bank data
- Create additional tutorials
- Improve existing analyses
- Share interesting findings

## 📝 License

See LICENSE file for details.

## 🙋 Questions?

Start with Tutorial 1 and work through them in order. Each tutorial builds on previous concepts. If you get stuck, the tutorials include explanations and exercises.

---

**Happy Analyzing! 📈**