# Micro-Habit Builder

A **terminal-based habit tracker** built in Python that helps users build small daily habits through streaks, points, and motivational feedback. 

---

## Project Concept

Building habits can be challenging, especially when motivation fluctuates day-to-day. I wanted to create a **simple tool that encourages consistency**, tracks progress, and provides positive reinforcement.

This project explores:

* **Input validation**: Ensuring users provide meaningful responses (`Y`/`N`).
* **Gamification**: Rewarding users with streaks, points, and bonus points for consecutive completions.
* **Persistence**: Saving user progress across sessions using JSON, allowing streaks and points to carry over each day.
* **Personalization**: The program greets the user by name, tracks a habit of their choice, and provides randomized motivational messages.
* **User control**: Users can choose to restart their habit builder and reset their progress at any time.

---

## How It Works

1. **Initialization**:

   * On first run, asks the user for their name and the habit they want to build.
   * Creates a JSON file to save progress.

2. **Returning Users**:

   * Loads saved data from `habit_data.json`.
   * Shows a welcome message and today’s date.
   * Offers the option to reboot (reset streaks/points) while keeping the habit and name.

3. **Daily Check-In**:

   * Prompts the user: “Have you completed your habit today?”
   * Validates input (`Y`/`N`) before continuing.

4. **Tracking & Rewards**:

   * Updates streaks and points based on user input.
   * Adds bonus points for every 7-day streak.
   * Provides a random motivational message depending on success or failure.

5. **Data Persistence**:

   * Updates the JSON file with the user’s name, habit, streak, points, and last check-in date.
   * Ensures progress is saved across multiple sessions.

6. **Daily Summary**:

   * Displays a summary of today’s activity, current streak, and total points.

---

## Skills Gained

Working on this project helped me develop:

* **Python Programming**

  * Core syntax, loops, conditionals, functions, and string manipulation.

* **Data Storage & Persistence**

  * Using JSON to save and load structured data safely across sessions.

* **User Input Validation**

  * Handling incorrect or unexpected inputs gracefully.

* **Logical Problem Solving**

  * Designing streak and point systems, handling edge cases, and ensuring data integrity.

* **Gamification & User Experience**

  * Applying psychology of motivation to make the program interactive and engaging.

* **Project Structuring & Modularity**

  * Using functions and clear flow to keep code organized and maintainable.

* **Debugging & Testing**

  * Running multiple scenarios to ensure streaks, points, and restarts behave as expected.

These skills translate directly to **real-world programming tasks**, including data management, user-focused design, and problem-solving.

---

## Built With

* Python 3
* Built-in libraries:

  * `datetime` → Tracks current date
  * `random` → Randomizes motivational messages
  * `json` → Saves and loads user progress
  * `os` → Checks if progress file exists

---

## Learning Outcomes

This project allowed me to explore:

* Structured data storage (JSON) and safe file handling
* Input validation and loops for robust user interaction
* Basic gamification mechanics for motivation
* Designing a **user-centered experience** in a terminal application
* Translating a real-life problem (habit formation) into a **working software solution**

---

**Takeaway:**
This project is more than a habit tracker — it’s a demonstration of **thoughtful design, persistence, and problem-solving skills**, all using Python’s built-in libraries.
