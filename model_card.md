# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Goal / Task

VibeMatch suggests 5 songs from a small catalog that fit what a listener says they like. It doesn't learn from listening history. It only compares songs to four stated preferences.

---

## 3. Data Used

The catalog has 17 songs across 14 genres and 13 moods. Each song has a genre, mood, energy, tempo, valence, danceability and acousticness. Most genres have just one song, nothing is below 0.22 energy, and no song is tagged "sad."

---

## 4. Algorithm Summary

Each song gets points: 1.5 for the right genre, 1 for the right mood, and up to 2 for energy close to what you want. It gets 0.5 more if it's acoustic or produced, matching your taste. The 5 highest-scoring songs win, and a perfect song scores 5.

---

## 5. Observed Behavior / Biases

Acoustic songs in the catalog are all quiet and produced songs are all loud, so energy and sound end up meaning the same thing. Energy is worth more points, so a fan of loud acoustic music gets acoustic songs only 36% of the time. Exact labels also matter too much: "indie pop" isn't counted as "pop," and an extra space breaks the match.

---

## 6. Evaluation Process

I tested 3 normal profiles and 7 tricky ones, like a "sad" mood, impossible energy, and conflicting preferences. I tried moving weight from genre to energy, and it changed only 2 of 10 rankings. I also scored every combination of preferences (4,004 profiles) to find who gets poor results.

**Profile comparisons:**

- **High-Energy Pop vs. Chill Lofi:** No overlap at all. That makes sense, since they disagree on every preference.
- **High-Energy Pop vs. Deep Intense Rock:** Both get Gym Hero at #2. It's pop for one and "intense" for the other.
- **Chill Lofi vs. Deep Intense Rock:** Lofi stays under 0.45 energy and rock stays above 0.75. Energy is doing its job.
- **High-Energy Pop vs. Whitespace Pop:** Same request, but extra spaces drop Sunrise City from 4.96 to 3.46. A typo shouldn't change results.
- **High-Energy Pop vs. Sad Gym Rat:** Both start with the same upbeat pop songs. "Sad" isn't in the catalog, so it's quietly ignored.
- **Chill Lofi vs. Overdrive:** Same lofi songs on top, but a metal song sneaks in at #5. Energy 1.5 is impossible, so the loudest song looks "closest."
- **Deep Intense Rock vs. Acoustic Metal:** Both get the same loud, produced songs after #1. There are no loud acoustic songs to give.
- **High-Energy Pop vs. Indie Pop Fan:** Sunrise City and Rooftop Lights swap places at #1. The system treats "indie pop" and "pop" as unrelated.

**Why "Gym Hero" keeps showing up for happy-pop fans:** It's pop, loud and polished, so it matches three of the four preferences. The system can't tell that a workout song feels different from a happy one, because mood is worth only 1 point.

---

## 7. Intended Use and Non-Intended Use

**Intended:** A classroom project for seeing how a simple scoring system turns preferences into recommendations. **Not intended:** Real users or real music apps. The catalog is too small and the labels are too rigid to serve real taste.

---

## 8. Ideas for Improvement

- Score acousticness by how close a song is, like energy, instead of a yes/no cutoff.
- Clean up inputs (trim spaces, keep energy between 0 and 1) and give partial credit for similar genres and moods.
- Add more songs, especially loud acoustic, quiet produced, and sad ones.

---

## 9. Personal Reflection

**Biggest learning moment:** Changing the weights barely changed the results. The real problems came from the data, like having no loud acoustic songs.

**Using AI tools:** AI helped me write the scoring code and quickly test thousands of profiles. I still had to check its claims against the actual output, because a few of its summaries overstated what happened.

**What surprised me:** Four simple rules were enough to make the top picks feel right. Adding a "why" next to each song made it feel even more like a real app.

**What I'd try next:** I'd use the unused columns, like valence for sad listeners, and add more songs per genre.
