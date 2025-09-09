# FeelsTrader

[![Python](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Archived-orange.svg)](https://github.com/dylee9/coin-trader)

A sentiment-driven trading algorithm that leverages social media sentiment analysis to make stock market predictions. This project uses deep learning neural networks to analyze sentiment from social media platforms like Twitter, StockTwits, and Reddit to predict market movements.

## 🚀 Features

- **Sentiment Analysis**: LSTM-based neural network for sentiment classification
- **Social Media Integration**: StockTwits API integration for real-time data collection
- **Web Scraping**: Automated data collection from social platforms
- **Database Integration**: MySQL database for storing sentiment data and predictions
- **Machine Learning Pipeline**: Complete ML workflow from data collection to prediction

## 📋 Prerequisites

- Python 3.7.4 or higher
- MySQL database
- StockTwits API access (optional)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/feels-trader.git
   cd feels-trader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration files**
   ```bash
   # Copy and configure database settings
   cp databaseconfig.py.example databaseconfig.py
   
   # Copy and configure API keys (optional)
   cp config.py.example config.py
   ```

4. **Configure your credentials**
   - Edit `databaseconfig.py` with your MySQL database credentials
   - Edit `config.py` with your StockTwits API credentials (if using API features)

## 🔧 Configuration

### Database Setup

1. Create a MySQL database and user:
   ```sql
   CREATE DATABASE feelstrader_dev;
   CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON feelstrader_dev.* TO 'your_username'@'localhost';
   FLUSH PRIVILEGES;
   ```

2. Run the database schema:
   ```bash
   mysql -u your_username -p feelstrader_dev < res/FeelsTrader_Schema.sql
   ```

### API Configuration

For StockTwits integration, you'll need:
- StockTwits User ID
- StockTwits Username  
- StockTwits Access Token

Add these to your `config.py` file or set as environment variables.

## 🚀 Usage

### Basic Usage

```python
import dbio

# Initialize database connection
db = dbio.DbIO()

# Write a sentiment data point
db.write_datapoint_record('AAPL', 1, 'This stock is going places!')

# Read data points
results = db.read_datapoint_record(1)
```

### Running Sentiment Analysis

```python
# Train or load sentiment model
python sentiment.py

# Run sentiment prediction
python test_sentiment_prediction.py
```

### Data Collection

```python
# Collect data from StockTwits API
python stocktwitAPI.py

# Run web scraper (requires credentials)
python webscraper.py
```

## 📁 Project Structure

```
feels-trader/
├── data/                    # Data files and datasets
├── drivers/                 # Selenium WebDriver files
├── models/                  # Trained ML models
├── research/               # Research papers and documentation
├── res/                    # Resources (database schema, etc.)
├── dbio.py                 # Database I/O operations
├── sentiment.py            # Sentiment analysis model
├── stocktwitAPI.py         # StockTwits API integration
├── webscraper.py           # Web scraping functionality
├── nlp.py                  # Natural language processing utilities
└── feelstrader.py          # Main application entry point
```

## 🤖 Machine Learning Model

The sentiment analysis model uses:
- **Architecture**: LSTM (Long Short-Term Memory) neural network
- **Dataset**: IMDB movie reviews for initial training
- **Framework**: Keras/TensorFlow
- **Features**: Text preprocessing, tokenization, and sequence padding

### Model Training

```python
# The model trains on IMDB dataset with the following parameters:
- Vocabulary size: 5000 words
- Max sequence length: 500 words  
- Batch size: 64
- Epochs: 3
```

## 📊 Data Sources

- **StockTwits**: Real-time social sentiment data
- **IMDB Dataset**: For initial model training
- **Web Scraping**: Additional social media platforms

## ⚠️ Important Notes

- **Security**: Never commit sensitive credentials to version control
- **API Limits**: Be mindful of API rate limits when collecting data
- **Legal**: Ensure compliance with platform terms of service when scraping
- **Performance**: Model predictions should be validated before making trading decisions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 References

### Machine Learning & Sentiment Analysis
- [TensorFlow Text Classification Tutorial](https://www.tensorflow.org/tutorials/text/text_classification_rnn)
- [Beginner's Guide to Sentiment Analysis with RNN](https://towardsdatascience.com/a-beginners-guide-on-sentiment-analysis-with-rnn-9e100627c02e)
- [LSTM RNN Network for Sentiment Analysis](https://analyticsindiamag.com/how-to-implement-lstm-rnn-network-for-sentiment-analysis/)

### Natural Language Processing
- [Text Cleaning for Machine Learning](https://machinelearningmastery.com/clean-text-machine-learning-python/)
- [Sentiment Analysis with CNN](https://humboldt-wi.github.io/blog/research/information_systems_1718/05sentimentanalysis/)

### Research
- See `research/` directory for academic papers on sentiment-based trading

## ⚠️ Disclaimer

This software is for educational and research purposes only. Trading decisions should not be made solely based on sentiment analysis. Always conduct thorough research and consider consulting with financial advisors before making investment decisions.

