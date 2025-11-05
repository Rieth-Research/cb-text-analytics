"""
Quick Analysis Script for Central Bank Communications

This script performs objective text analysis of central bank statements and generates
summary statistics and visualizations.

Focuses on measurable metrics, not subjective sentiment.

Usage:
    python src/quick_analysis.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

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
    """Calculate objective text metrics."""
    # Basic counts
    df['word_count'] = df['text'].str.split().str.len()
    df['char_count'] = df['text'].str.len()
    df['sentence_count'] = df['text'].str.count(r'[.!?]')

    # Complexity metrics
    df['avg_sentence_length'] = df['word_count'] / df['sentence_count'].replace(0, 1)
    df['avg_word_length'] = df['char_count'] / df['word_count'].replace(0, 1)

    # Vocabulary diversity (Type-Token Ratio)
    df['vocab_diversity'] = df['text'].apply(lambda x:
        len(set(x.lower().split())) / len(x.split()) if len(x.split()) > 0 else 0
    )

    # Economic term tracking
    economic_terms = {
        'inflation': ['inflation', 'price', 'prices'],
        'employment': ['employment', 'labor', 'jobs', 'unemployment'],
        'growth': ['growth', 'economic activity', 'expansion'],
        'risk': ['risk', 'uncertainty', 'uncertain'],
        'policy': ['policy', 'monetary policy'],
        'financial': ['financial', 'market', 'markets']
    }

    for term, keywords in economic_terms.items():
        df[term] = df['text'].apply(lambda x:
            sum(x.lower().count(kw) for kw in keywords)
        )
        # Normalize per 100 words
        df[f'{term}_per_100'] = (df[term] / df['word_count']) * 100

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
        print(f"      Avg sentence length: {bank_data['avg_sentence_length'].mean():.1f} words")
        print(f"      Vocab diversity: {bank_data['vocab_diversity'].mean():.3f}")
        print(f"      Date range: {bank_data['date'].min().date()} to {bank_data['date'].max().date()}")

    print(f"\n💡 Language Complexity:")
    print(f"   Average statement length: {df['word_count'].mean():.0f} words")
    print(f"   Average sentence length: {df['avg_sentence_length'].mean():.1f} words")
    print(f"   Average word length: {df['avg_word_length'].mean():.1f} characters")
    print(f"   Vocabulary diversity: {df['vocab_diversity'].mean():.3f}")

    # Longest/shortest
    longest = df.loc[df['word_count'].idxmax()]
    shortest = df.loc[df['word_count'].idxmin()]
    print(f"\n   Longest statement: {longest['date'].date()} ({longest['word_count']:.0f} words)")
    print(f"   Shortest statement: {shortest['date'].date()} ({shortest['word_count']:.0f} words)")

    # Economic terms
    print(f"\n🔑 Economic Term Mentions (per 100 words avg):")
    terms = ['inflation', 'employment', 'growth', 'risk', 'policy', 'financial']
    for term in terms:
        avg = df[f'{term}_per_100'].mean()
        print(f"   {term.capitalize():15s}: {avg:.2f}")

    # Top words (objective frequency)
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
    """Create objective visualizations."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Language complexity over time
    for bank in df['bank'].unique():
        bank_data = df[df['bank'] == bank]
        axes[0, 0].plot(bank_data['date'], bank_data['avg_sentence_length'],
                       marker='o', label=bank, linewidth=2)
    axes[0, 0].set_title('Language Complexity (Sentence Length)', fontweight='bold', fontsize=12)
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Words per Sentence')
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

    # 3. Vocabulary diversity over time
    for bank in df['bank'].unique():
        bank_data = df[df['bank'] == bank]
        axes[1, 0].plot(bank_data['date'], bank_data['vocab_diversity'],
                       marker='o', label=bank, linewidth=2)
    axes[1, 0].set_title('Vocabulary Diversity', fontweight='bold', fontsize=12)
    axes[1, 0].set_xlabel('Date')
    axes[1, 0].set_ylabel('Type-Token Ratio')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # 4. Economic term mentions
    terms = ['inflation', 'employment', 'growth', 'risk']
    term_avgs = [df[f'{t}_per_100'].mean() for t in terms]
    axes[1, 1].bar(terms, term_avgs, color='steelblue')
    axes[1, 1].set_title('Average Economic Term Mentions', fontweight='bold', fontsize=12)
    axes[1, 1].set_xlabel('Term')
    axes[1, 1].set_ylabel('Mentions per 100 words')
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
    print("Calculating objective metrics...\n")

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
    print("\n💡 Key findings based on objective metrics:")
    print("   - Language complexity (sentence length)")
    print("   - Vocabulary diversity (word variety)")
    print("   - Economic term frequencies")
    print("   - Communication pattern changes")
    print("\n💡 Next steps:")
    print("   1. Check 'quick_analysis_results.png' for visualizations")
    print("   2. Explore tutorials/ folder for topic modeling and more")
    print("   3. Modify this script to track other measurable patterns")
    print("\n")

if __name__ == "__main__":
    main()
