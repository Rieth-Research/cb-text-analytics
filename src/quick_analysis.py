"""
Quick Analysis Script for Central Bank Communications

This script performs a rapid analysis of central bank statements and generates
summary statistics and visualizations.

Usage:
    python src/quick_analysis.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Configuration
DATA_DIRS = {
    'Fed': 'usa-central-bank/fomc-statements',
    'RBNZ': 'nz-central-bank/ocr'
}

def load_statements(directory, bank_name):
    """Load all text files from a directory."""
    statements = []

    if not os.path.exists(directory):
        print(f"Warning: Directory not found: {directory}")
        return pd.DataFrame()

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            date_str = filename.replace('.txt', '').replace('-txt', '')

            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()

            statements.append({
                'date': date_str,
                'bank': bank_name,
                'text': text,
                'filename': filename
            })

    if not statements:
        return pd.DataFrame()

    df = pd.DataFrame(statements)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    return df

def calculate_metrics(df):
    """Calculate various text metrics."""
    df['word_count'] = df['text'].str.split().str.len()
    df['char_count'] = df['text'].str.len()
    df['sentence_count'] = df['text'].str.count(r'[.!?]')

    # Sentiment analysis
    analyzer = SentimentIntensityAnalyzer()
    df['sentiment'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

    # Keyword counts
    keywords = ['inflation', 'employment', 'growth', 'risk', 'uncertainty']
    for keyword in keywords:
        df[keyword] = df['text'].str.lower().str.count(keyword)

    return df

def print_summary(df):
    """Print summary statistics."""
    print("=" * 80)
    print("CENTRAL BANK COMMUNICATION ANALYTICS - SUMMARY REPORT")
    print("=" * 80)

    print(f"\n📊 Dataset Overview:")
    print(f"   Total statements: {len(df)}")
    print(f"   Date range: {df['date'].min().date()} to {df['date'].max().date()}")
    print(f"   Central banks: {', '.join(df['bank'].unique())}")

    print(f"\n📈 Statistics by Bank:")
    for bank in df['bank'].unique():
        bank_data = df[df['bank'] == bank]
        print(f"\n   {bank}:")
        print(f"      Statements: {len(bank_data)}")
        print(f"      Avg words: {bank_data['word_count'].mean():.0f}")
        print(f"      Avg sentiment: {bank_data['sentiment'].mean():.3f}")
        print(f"      Date range: {bank_data['date'].min().date()} to {bank_data['date'].max().date()}")

    print(f"\n💡 Overall Insights:")
    print(f"   Average statement length: {df['word_count'].mean():.0f} words")
    print(f"   Average sentiment score: {df['sentiment'].mean():.3f}")
    print(f"   Most positive statement: {df.loc[df['sentiment'].idxmax(), 'date'].date()} ({df['sentiment'].max():.3f})")
    print(f"   Most negative statement: {df.loc[df['sentiment'].idxmin(), 'date'].date()} ({df['sentiment'].min():.3f})")

    # Top keywords
    print(f"\n🔑 Keyword Mentions (Total):")
    keywords = ['inflation', 'employment', 'growth', 'risk', 'uncertainty']
    for keyword in keywords:
        total = df[keyword].sum()
        avg = df[keyword].mean()
        print(f"   {keyword.capitalize():15s}: {total:4.0f} total ({avg:.1f} per statement)")

    # Top words
    print(f"\n📝 Most Common Words:")
    all_text = ' '.join(df['text'])
    words = re.sub(r'\W+', ' ', all_text.lower()).split()
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                  'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
                  'be', 'have', 'has', 'had', 'will', 'would', 'committee'}
    words = [w for w in words if w not in stop_words and len(w) > 3]
    word_counts = Counter(words).most_common(10)
    for word, count in word_counts:
        print(f"   {word:15s}: {count:4d}")

def create_visualizations(df):
    """Create summary visualizations."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Sentiment over time
    for bank in df['bank'].unique():
        bank_data = df[df['bank'] == bank]
        axes[0, 0].plot(bank_data['date'], bank_data['sentiment'],
                       marker='o', label=bank, linewidth=2)
    axes[0, 0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    axes[0, 0].set_title('Sentiment Over Time', fontweight='bold', fontsize=12)
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Sentiment Score')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 2. Word count over time
    for bank in df['bank'].unique():
        bank_data = df[df['bank'] == bank]
        axes[0, 1].plot(bank_data['date'], bank_data['word_count'],
                       marker='o', label=bank, linewidth=2)
    axes[0, 1].set_title('Statement Length Over Time', fontweight='bold', fontsize=12)
    axes[0, 1].set_xlabel('Date')
    axes[0, 1].set_ylabel('Word Count')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # 3. Sentiment distribution
    for bank in df['bank'].unique():
        bank_data = df[df['bank'] == bank]
        axes[1, 0].hist(bank_data['sentiment'], alpha=0.6, label=bank, bins=15)
    axes[1, 0].axvline(x=0, color='red', linestyle='--', alpha=0.5)
    axes[1, 0].set_title('Sentiment Distribution', fontweight='bold', fontsize=12)
    axes[1, 0].set_xlabel('Sentiment Score')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].legend()

    # 4. Keyword frequency
    keywords = ['inflation', 'employment', 'growth', 'risk']
    keyword_totals = [df[k].sum() for k in keywords]
    axes[1, 1].bar(keywords, keyword_totals, color='steelblue')
    axes[1, 1].set_title('Total Keyword Mentions', fontweight='bold', fontsize=12)
    axes[1, 1].set_xlabel('Keyword')
    axes[1, 1].set_ylabel('Total Mentions')
    axes[1, 1].tick_params(axis='x', rotation=45)

    plt.tight_layout()

    # Save
    output_file = 'quick_analysis_results.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n📊 Visualization saved as '{output_file}'")

    plt.show()

def main():
    """Main execution function."""
    print("\n🚀 Starting Quick Analysis...")
    print("Loading data...\n")

    # Load all data
    all_data = []
    for bank, directory in DATA_DIRS.items():
        data = load_statements(directory, bank)
        if not data.empty:
            all_data.append(data)
            print(f"✓ Loaded {len(data)} statements from {bank}")

    if not all_data:
        print("\n❌ Error: No data found. Please check data directories.")
        return

    # Combine datasets
    df = pd.concat(all_data, ignore_index=True)
    df = df.sort_values('date').reset_index(drop=True)

    print(f"\n✓ Total: {len(df)} statements loaded")
    print("Calculating metrics...\n")

    # Calculate metrics
    df = calculate_metrics(df)

    # Print summary
    print_summary(df)

    # Create visualizations
    print("\n📈 Creating visualizations...")
    create_visualizations(df)

    print("\n" + "=" * 80)
    print("✅ Analysis complete!")
    print("=" * 80)
    print("\n💡 Next steps:")
    print("   1. Check 'quick_analysis_results.png' for visualizations")
    print("   2. Explore the tutorials/ folder for in-depth learning")
    print("   3. Modify this script to analyze specific aspects")
    print("\n")

if __name__ == "__main__":
    main()
