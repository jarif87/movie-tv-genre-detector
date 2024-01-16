# Movie_Tvshow_Genre_Classification

**A text classification model from data collection, model training, and deployment.The model can classify 23 different types of Movie,Tvshow genres The keys of deployment\genre_types_encoded.json shows the Movie and Tvshow genres**

# Genre Countplot

> The countplot visually represents the distribution of genres, giving you insights into the variety of content covered in the project. The x-axis displays the different genres, while the y-axis shows the corresponding count for each genre.

<img src = "notebooks/download.png" width="700" height="350">

# Description WordCloud

> The description word cloud gives a visual representation of the most frequent words used in project descriptions. This helps users quickly grasp the main themes and focus areas of the project

<img src = "notebooks/des_wordcloud.png" width="700" height="350">

# Genre WordCloud

> Explore the genre word cloud to gain insights into the diverse categories covered by the project. Each word represents a genre, and the size corresponds to the frequency of that genre in the project

<img src = "notebooks/genre_wordcloud.png" width="700" height="350">

# Most Common Words in Description

> Here are the 30 most common words in descriptions

<img src = "notebooks/most_common_words.png" width="700" height="350">

# Data Preprocessing

***In the dataset's initial state, it comprised 27 distinct genres. Subsequent analysis revealed that four of these genres appeared to be uncommon, potentially representing custom genres created by users. Consequently, these rare genres were excluded, leaving a refined dataset containing 23 genres.Further refinement involved the removal of descriptions lacking any associated genres. As a result, the dataset now comprises 21,753 samples, each with a well-defined genre.***

# Model Training

***I performed fine-tuning on a pre-trained Roberta-Base model obtained from HuggingFace Transformers. The process utilized the Fastai library and Blurr, an extension for leveraging HuggingFace Transformers with Fastai. For those interested, the notebook used for training the model is accessible and can be viewed for detailed insights into the training procedure [here](https://github.com/jarif87/Movie_Tvshow_Genre_Classification/blob/main/notebooks/movie_tvshow_genres_Classification.ipynb)***
