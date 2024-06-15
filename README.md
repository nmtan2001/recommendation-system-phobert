# Recommender System for Sentiment Analysis of Vietnamese Texts

## Project Overview

This project is focused on developing a recommendation system that enhances the quality of product recommendations by analyzing the sentiment of texts in Vietnamese. The primary objective is to increase sales volume for stores in Vietnam by leveraging the emotional tone of user-generated content to provide personalized recommendations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The rise of e-commerce in Vietnam presents a unique opportunity to improve customer engagement and sales through personalized recommendations. This project aims to utilize advanced natural language processing (NLP) techniques, particularly BERT (Bidirectional Encoder Representations from Transformers), to analyze the sentiment of Vietnamese texts. By understanding the emotional context, the recommendation system can suggest products that are more aligned with the user's preferences and emotional state.

## Features

- **Sentiment Analysis**: Analyze the sentiment of Vietnamese texts using PhoBERT, a pre-trained BERT specialized in Vietnamese.
- **Personalized Recommendations**: Provide product recommendations based on the analyzed sentiment.
- **User-Friendly Interface**: Chrome browser extension for seamless user interaction.
- **Backend Integration**: Django-based backend server for handling recommendation logic and data processing.

## Installation

### Prerequisites

- Python 3.7+
- Django 3.2+
- Chrome browser

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/nmtan2001/recommendation-system-phobert
   cd recommendation-system-phobert
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the Django backend:
   ```sh
   cd mysite
   python manage.py migrate
   python manage.py runserver
   ```

5. Load the Chrome extension:
   - Open Chrome and navigate to `chrome://extensions/`.
   - Enable "Developer mode".
   - Click "Load unpacked" and select the `chrome_extension` directory.

## Usage

1. Start the Django server:
   ```sh
   cd mysite
   python manage.py runserver
   ```

2. Open the Chrome browser and activate the extension.

3. Browse the web, and the extension will analyze the sentiment of Vietnamese texts and provide product recommendations based on the analysis.

## Project Structure

```plaintext
recommendation-system-phobert/
├── mysite/
│   ├── manage.py
│   ├── VNCoreNLP/
│   ├── analysis/
│   └── ...
├── grabText_ext/
│   ├── manifest.json
│   ├── background.js
│   └── ...
├── Dockerfile
├── requirements.txt
└── README.md
```

## Methodology

1. **Data Collection**: Gather datasets from the internet, including production practice and scientific research materials.
2. **Data Preprocessing**: Standardize and tokenize Vietnamese texts, handle punctuation and emojis, and perform text segmentation.
3. **Model Training**: Use PhoBERT and other machine learning models like SVM and Naive Bayes for sentiment analysis.
4. **Recommendation Algorithm**: Develop algorithms to provide personalized recommendations based on sentiment analysis results.
5. **System Development**: Implement the recommendation system using a Django backend and a Chrome browser extension.

## Contributing

We welcome contributions from the community. To contribute:

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add your message"
   ```
4. Push to the branch:
   ```sh
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Developed by Ngo Minh Tan, supervised by Associate Professor V.V. Stuchilin.**

For more information, refer to the detailed project report included in this repository.
