## 1. Feature Selection

Which three features did you select?

- Recipe Management: Favorite Recipies
- Meal Planning: Random Meal Suggestion
- Grocery / Calculations: Generate a Grocery List

Why did you choose these three features?

**Response:**
they seemed like things that would be fun implementation while still giving enough of a challenge that it isnt completely smooth sailing
---

## 2. Current Progress

Which two features have you meaningfully implemented so far?

Briefly explain what currently works.

**Response:**

- Favorite Recipies: adding and loading both are implemented and working
    - saving still needs to be added
- Random Meal Suggestion: feature completely functions, it gets a random number and displays it.
---

## 3. Most Difficult Feature

Which feature has been the most difficult so far?

What specifically has made it challenging?

**Response:**
- the most difficult feature to add so far is the Generating a grocery list, not because its the most difficult implementation wise, but because depending on how i end up implmenting the generation it could require needing another feature just to work
---

## 4. GitHub Issues

Identify the GitHub Issues you created for your planned work.

How have the Issues helped you organize the project?

**Response:**
- one issue for each feature to be added
- they helped organize the project by having my state of mind be geared towards making a new branch for each feature to solve the "issue" on github by merging it
---

## 5. Branch / Pull Request

Identify one branch or pull request that best represents your development process so far.

What work happened there, and why did that work belong outside `main`?

**Response:**
Feature/FavoriteRecipies is the branch i added to work on the feature of favorite recipies as the name suggests. but i also added some general changes such as changing all the spaces to indentations and adding the rest of the menu options i would need

---

## 6. Meaningful Commit

Identify one commit you consider meaningful.

What changed in that commit, and why was it useful to keep that work together?

**Response:**
Implement favorite recipes feature with loading and saving functionality
    -the first feature of adding and viewing favorites was added as well as groundwork for my other features. it was useful to keep that work together because it made it easier to track changes, test the feature as a whole, and build upon it later when implementing other features.

---

## 7. Testing

What new tests have you added for your features?

What important behavior do those tests verify?

**Response:**

---

## 8. Bug or Mistake

Describe one bug, mistake, or unexpected behavior you encountered.

How did you discover it, and how did you fix it?

**Response:**
in adding favorites i encountered a logic bug where duplicate items could be added resulting in
```
favorites
-------
1. Chicken Alfredo (Dinner)
2. Chicken Alfredo (Dinner)

```
i fixed it by adding an if statement checking if the name wanting to be favorited was already in the list. if it was it wouldnt add it again and give a print statement saying it was already marked as a favorite.

---

## 9. Current Code Quality

Identify one part of your current code that you would improve if you had more time before this checkpoint.

Why would you improve it?

**Response:**

---

## 10. Remaining Plan

What work remains before the final submission?

What do you plan to work on next?

**Response:**
finishing the last feature, adding more tests and better testing layouts, making sure everything works as intended before final submission