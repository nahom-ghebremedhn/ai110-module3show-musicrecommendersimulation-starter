# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommenders like Spotify and YouTube learn what you like from your behavior and from the songs themselves. They give each song a score for how well it fits you, then rank the songs and show you the best matches. My version is a simple content-based recommender. It scores each song by comparing it to the user's preferences and then recommends the top results. It prioritizes genre first, then mood and how close the song's energy is to what the user wants, with a small bonus for matching their acoustic preference.

**Song features:** `genre`, `mood`, `energy`, `acousticness`

**UserProfile features:** `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

### Algorithm Recipe

For each song in the catalog, start at **0 points** and add:

| Rule | Points | Reasoning |
|---|---|---|
| Song `genre` equals user's `favorite_genre` | **+1.5** | Genre reflects long-term, stable taste. |
| Song `mood` equals user's `favorite_mood` | **+1.0** | Mood is situational, so it counts less than genre. |
| Energy closeness | **up to +2.0**, computed as `max(0, 2.0 × (1 − abs(song.energy − target_energy)))` | Continuous signal that separates songs even when no labels match. |
| Acoustic fit: `likes_acoustic` is True and `acousticness > 0.6`, **or** `likes_acoustic` is False and `acousticness ≤ 0.6` | **+0.5** | Small tiebreaker for the user's sound preference. |

**Maximum score:** 5.0 points.

**Ranking:** score every song, sort from highest to lowest score, and return the top `k` (default 5). Each recommendation includes a list of reasons, for example "genre match (+1.5)" or "energy close to target (+1.4)", so the user can see why it was picked.

**Why these weights balance:** everything except genre adds up to 3.5 points (1.0 + 2.0 + 0.5), and energy plus sound alone (2.5) beats the 1.5 genre bonus. A song from another genre with the right mood, energy and acoustic feel can still beat a genre match whose energy is far off. Genre leads, but it can't override everything else.

**Data flow:**

```
User profile + songs.csv
        │
        ▼
score_song() for every song ──► (score, reasons)
        │
        ▼
sort by score, highest first
        │
        ▼
top k songs + explanations
```

### Expected Biases

- **Genre over-prioritization:** genre is the largest single bonus, so the system might rank a mediocre song in the user's favorite genre above a great song that matches their mood and energy.
- **Exact-match labels are brittle:** "indie pop" gets no genre credit for a "pop" fan, and "relaxed" gets no mood credit for a "chill" listener, even though they're close.
- **Underrepresented genres and moods:** most genres and moods in `songs.csv` appear only once. Users whose favorites aren't in the catalog get recommendations based almost entirely on energy, and lofi/chill users have more songs to choose from than everyone else.
- **Energy acts as the default tiebreaker:** when no labels match, energy decides the ranking, so the results lean toward songs with similar intensity rather than variety.
- **No discovery:** the system only rewards similarity to what the user already likes, so it tends to keep users in a filter bubble.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Output of `python src/main.py` (17 songs loaded), one block per profile.

### Standard profiles

#### High-Energy Pop

```
============================================================
            TOP RECOMMENDATIONS: High-Energy Pop
============================================================
 Profile: pop | happy | energy 0.80 | produced
------------------------------------------------------------
 #1  Sunrise City  by Neon Echo
     Score: 4.96 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+1.96)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #2  Gym Hero  by Max Pulse
     Score: 3.74 / 5.00
     Why:
       - genre match (+1.5)
       - energy close to target (+1.74)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #3  Rooftop Lights  by Indigo Parade
     Score: 3.42 / 5.00
     Why:
       - mood match (+1.0)
       - energy close to target (+1.92)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #4  Concrete Crown  by Block Theory
     Score: 2.46 / 5.00
     Why:
       - energy close to target (+1.96)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #5  Night Drive Loop  by Neon Echo
     Score: 2.40 / 5.00
     Why:
       - energy close to target (+1.90)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
```

#### Chill Lofi

```
============================================================
               TOP RECOMMENDATIONS: Chill Lofi
============================================================
 Profile: lofi | chill | energy 0.35 | acoustic
------------------------------------------------------------
 #1  Library Rain  by Paper Lanterns
     Score: 5.00 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+2.00)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #2  Midnight Coding  by LoRoom
     Score: 4.86 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+1.86)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #3  Focus Flow  by LoRoom
     Score: 3.90 / 5.00
     Why:
       - genre match (+1.5)
       - energy close to target (+1.90)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #4  Spacewalk Thoughts  by Orbit Bloom
     Score: 3.36 / 5.00
     Why:
       - mood match (+1.0)
       - energy close to target (+1.86)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #5  Coffee Shop Stories  by Slow Stereo
     Score: 2.46 / 5.00
     Why:
       - energy close to target (+1.96)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
```

#### Deep Intense Rock

```
============================================================
           TOP RECOMMENDATIONS: Deep Intense Rock
============================================================
 Profile: rock | intense | energy 0.90 | produced
------------------------------------------------------------
 #1  Storm Runner  by Voltline
     Score: 4.98 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+1.98)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #2  Gym Hero  by Max Pulse
     Score: 3.44 / 5.00
     Why:
       - mood match (+1.0)
       - energy close to target (+1.94)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #3  Pulse Theory  by Kilowatt Kids
     Score: 2.40 / 5.00
     Why:
       - energy close to target (+1.90)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #4  Iron Tempest  by Grave Signal
     Score: 2.36 / 5.00
     Why:
       - energy close to target (+1.86)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #5  Sunrise City  by Neon Echo
     Score: 2.34 / 5.00
     Why:
       - energy close to target (+1.84)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
```

### Adversarial / edge-case profiles

#### Sad Gym Rat

```
============================================================
              TOP RECOMMENDATIONS: Sad Gym Rat
============================================================
 Profile: pop | sad | energy 0.90 | produced
------------------------------------------------------------
 #1  Gym Hero  by Max Pulse
     Score: 3.94 / 5.00
     Why:
       - genre match (+1.5)
       - energy close to target (+1.94)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #2  Sunrise City  by Neon Echo
     Score: 3.84 / 5.00
     Why:
       - genre match (+1.5)
       - energy close to target (+1.84)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #3  Storm Runner  by Voltline
     Score: 2.48 / 5.00
     Why:
       - energy close to target (+1.98)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #4  Pulse Theory  by Kilowatt Kids
     Score: 2.40 / 5.00
     Why:
       - energy close to target (+1.90)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #5  Iron Tempest  by Grave Signal
     Score: 2.36 / 5.00
     Why:
       - energy close to target (+1.86)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
```

#### Whitespace Pop

```
============================================================
             TOP RECOMMENDATIONS: Whitespace Pop
============================================================
 Profile:  Pop  | HAPPY | energy 0.80 | produced
------------------------------------------------------------
 #1  Sunrise City  by Neon Echo
     Score: 3.46 / 5.00
     Why:
       - mood match (+1.0)
       - energy close to target (+1.96)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #2  Rooftop Lights  by Indigo Parade
     Score: 3.42 / 5.00
     Why:
       - mood match (+1.0)
       - energy close to target (+1.92)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #3  Concrete Crown  by Block Theory
     Score: 2.46 / 5.00
     Why:
       - energy close to target (+1.96)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #4  Night Drive Loop  by Neon Echo
     Score: 2.40 / 5.00
     Why:
       - energy close to target (+1.90)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #5  Storm Runner  by Voltline
     Score: 2.28 / 5.00
     Why:
       - energy close to target (+1.78)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
```

#### Overdrive

```
============================================================
               TOP RECOMMENDATIONS: Overdrive
============================================================
 Profile: lofi | chill | energy 1.50 | acoustic
------------------------------------------------------------
 #1  Midnight Coding  by LoRoom
     Score: 3.00 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+0.00)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #2  Library Rain  by Paper Lanterns
     Score: 3.00 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+0.00)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #3  Focus Flow  by LoRoom
     Score: 2.00 / 5.00
     Why:
       - genre match (+1.5)
       - energy close to target (+0.00)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #4  Spacewalk Thoughts  by Orbit Bloom
     Score: 1.50 / 5.00
     Why:
       - mood match (+1.0)
       - energy close to target (+0.00)
       - acoustic sound fits preference (+0.5)
------------------------------------------------------------
 #5  Iron Tempest  by Grave Signal
     Score: 0.94 / 5.00
     Why:
       - energy close to target (+0.94)
------------------------------------------------------------
```

#### Contradictory Classical

```
============================================================
        TOP RECOMMENDATIONS: Contradictory Classical
============================================================
 Profile: classical | chill | energy 0.95 | produced
------------------------------------------------------------
 #1  Pulse Theory  by Kilowatt Kids
     Score: 2.50 / 5.00
     Why:
       - energy close to target (+2.00)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #2  Gym Hero  by Max Pulse
     Score: 2.46 / 5.00
     Why:
       - energy close to target (+1.96)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #3  Iron Tempest  by Grave Signal
     Score: 2.46 / 5.00
     Why:
       - energy close to target (+1.96)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #4  Storm Runner  by Voltline
     Score: 2.42 / 5.00
     Why:
       - energy close to target (+1.92)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #5  Sunrise City  by Neon Echo
     Score: 2.24 / 5.00
     Why:
       - energy close to target (+1.74)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
```

#### Acoustic Metal

```
============================================================
             TOP RECOMMENDATIONS: Acoustic Metal
============================================================
 Profile: metal | angry | energy 0.97 | acoustic
------------------------------------------------------------
 #1  Iron Tempest  by Grave Signal
     Score: 4.50 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+2.00)
------------------------------------------------------------
 #2  Pulse Theory  by Kilowatt Kids
     Score: 1.96 / 5.00
     Why:
       - energy close to target (+1.96)
------------------------------------------------------------
 #3  Gym Hero  by Max Pulse
     Score: 1.92 / 5.00
     Why:
       - energy close to target (+1.92)
------------------------------------------------------------
 #4  Storm Runner  by Voltline
     Score: 1.88 / 5.00
     Why:
       - energy close to target (+1.88)
------------------------------------------------------------
 #5  Sunrise City  by Neon Echo
     Score: 1.70 / 5.00
     Why:
       - energy close to target (+1.70)
------------------------------------------------------------
```

#### Indie Pop Fan

```
============================================================
             TOP RECOMMENDATIONS: Indie Pop Fan
============================================================
 Profile: indie pop | happy | energy 0.76 | produced
------------------------------------------------------------
 #1  Rooftop Lights  by Indigo Parade
     Score: 5.00 / 5.00
     Why:
       - genre match (+1.5)
       - mood match (+1.0)
       - energy close to target (+2.00)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #2  Sunrise City  by Neon Echo
     Score: 3.38 / 5.00
     Why:
       - mood match (+1.0)
       - energy close to target (+1.88)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #3  Night Drive Loop  by Neon Echo
     Score: 2.48 / 5.00
     Why:
       - energy close to target (+1.98)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #4  Concrete Crown  by Block Theory
     Score: 2.46 / 5.00
     Why:
       - energy close to target (+1.96)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #5  Storm Runner  by Voltline
     Score: 2.20 / 5.00
     Why:
       - energy close to target (+1.70)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
```

#### No Preferences

```
============================================================
             TOP RECOMMENDATIONS: No Preferences
============================================================
 Profile:  |  | energy 0.50 | produced
------------------------------------------------------------
 #1  Velvet Hours  by Amara Soul
     Score: 2.50 / 5.00
     Why:
       - energy close to target (+2.00)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #2  Island Bloom  by Sol Rhythm
     Score: 2.30 / 5.00
     Why:
       - energy close to target (+1.80)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #3  Night Drive Loop  by Neon Echo
     Score: 2.00 / 5.00
     Why:
       - energy close to target (+1.50)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #4  Rooftop Lights  by Indigo Parade
     Score: 1.98 / 5.00
     Why:
       - energy close to target (+1.48)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
 #5  Concrete Crown  by Block Theory
     Score: 1.94 / 5.00
     Why:
       - energy close to target (+1.44)
       - produced (non-acoustic) sound fits preference (+0.5)
------------------------------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



