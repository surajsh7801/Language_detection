# 🌍 Language Detection using NLP & Machine Learning

## 📌 Project Overview

This project focuses on building a *Language Detection System* using Natural Language Processing (NLP) techniques and Machine Learning. The model is trained to identify the language of a given text input.

We use *text preprocessing, **feature extraction, and a **Multinomial Naive Bayes classifier* to achieve accurate predictions.

---

## 🚀 Features

* Detects multiple languages from text input
* Uses NLP techniques for preprocessing
* Visualizes dataset distribution
* Implements Machine Learning model training and evaluation
* Displays performance metrics and confusion matrix

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Matplotlib & Seaborn
* NLP (Count Vectorization)

---

## 📂 Dataset

* File used: Language Detection.csv
* Contains:

  * Text: Input sentence
  * Language: Corresponding language label

---

## 🔄 Workflow

### 1. Data Loading

python
df = pd.read_csv('Language Detection.csv')


### 2. Data Cleaning

* Removed null values
* Removed duplicate entries

python
df1 = df.drop_duplicates()


### 3. Data Visualization

* Language distribution using count plot
* Top languages using bar chart
* Language share using pie chart

---

### 4. Feature Extraction

* Convert text into numerical form using *CountVectorizer*

python
cv = CountVectorizer()
x = cv.fit_transform(x1)


---

### 5. Train-Test Split

python
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)


---

### 6. Model Training

* Algorithm used: *Multinomial Naive Bayes*

python
mb = MultinomialNB()
mb.fit(x_train, y_train)


---

### 7. Model Evaluation

* Accuracy Score
* Classification Report
* Confusion Matrix

python
accuracy_score(y_pred, y_test)
classification_report(y_pred, y_test)
confusion_matrix(y_pred, y_test)


---

## 📊 Results

* Model achieves high accuracy on language classification
* Performs well on frequently occurring languages
* Confusion matrix shows classification performance across all classes

---

## 📈 Visualizations Included

* Language distribution plot
* Top 10 languages bar chart
* Pie chart of top languages
* Confusion matrix heatmap

---

## ▶️ How to Run

1. Clone this repository

bash
git clone https://github.com/your-username/language-detection.git


2. Install dependencies

bash
pip install pandas numpy scikit-learn matplotlib seaborn


3. Run the notebook

bash
jupyter notebook


---

## 💡 Future Improvements

* Use advanced NLP models (TF-IDF, Word Embeddings)
* Try Deep Learning models (LSTM, Transformers)
* Improve handling of short texts
* Deploy as a web app (Flask/Streamlit)

---

## 🤝 Contributing

Feel free to fork this repository and improve the project. Contributions are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Scikit-learn documentation
* Open datasets for language detection# Language_detection
