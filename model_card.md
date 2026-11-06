# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Think of it like a friend picking songs for you. You tell them four things: your favorite genre, the mood you're in, how energetic you want the music to be, and whether you like acoustic or more produced sounds. They go through every song and give it points:

- **Right genre:** 2 points. This counts most, because genre is the most stable part of someone's taste.
- **Right mood:** 1 point. Mood changes day to day, so it counts half as much.
- **Close in energy:** up to 1.5 points. A song with exactly the energy you want gets the full 1.5, and it gets fewer points the further off it is.
- **Right sound:** half a point if the song is acoustic when you like acoustic, or produced when you don't.

A perfect song scores 5. Once every song has a score, the songs are sorted from highest to lowest and you get the top five, along with the reasons each one earned its points.

The starter code had no scoring at all and only returned placeholder results. I added this point system so the picks actually depend on the listener.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
