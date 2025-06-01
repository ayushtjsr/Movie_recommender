🎬 Movie Recommendation System Using Machine Learning
A personalized movie recommendation system built using content-based filtering and cosine similarity on the TMDB dataset. The system provides real-time recommendations through an interactive Streamlit web interface.

🚀 Features
🔍 Content-Based Filtering: Recommends movies based on similarity of genres, plot keywords, cast, and more.

🧠 Machine Learning Techniques: Utilizes TF-IDF and CountVectorizer for text vectorization and cosine similarity for calculating movie similarities.

🧹 Extensive Preprocessing: Cleans and transforms movie metadata for improved recommendation accuracy.

🖥️ Interactive UI: Built with Streamlit to provide a simple and elegant front-end experience for users.

📊 Dataset
TMDB 5000 Movie Dataset

Contains metadata like titles, genres, overviews, cast, crew, etc.

Publicly available here
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

🧰 Tech Stack
Python 3.x

Pandas, NumPy for data handling

Scikit-learn for machine learning and similarity modeling

Streamlit for UI development

NLTK for text preprocessing

⚙️ How It Works
Load and preprocess movie metadata.

Vectorize textual features using TF-IDF and/or CountVectorizer.

Compute cosine similarity between movies based on vectorized data.

Input a movie title and retrieve top similar movies.

Display results in a Streamlit interface.

🖼️ Screenshots
Add a few screenshots of your Streamlit app here if available.

🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/ayushtjsr/movie-recommender.git
cd movie-recommender
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
📌 Example Usage
Just enter a movie title like "Inception" in the input box, and the system will suggest similar movies such as "Interstellar", "The Matrix", etc., based on content similarity.

📁 Project Structure
bash
Copy
Edit
movie-recommender/
├── app.py               # Streamlit app
├── recommender.py       # Core recommendation logic
├── data/                # TMDB dataset
├── utils/               # Helper functions
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
🤝 Contributing
Feel free to open issues or submit pull requests. All contributions are welcome!

📄 License
This project is open-source and available under the MIT License.