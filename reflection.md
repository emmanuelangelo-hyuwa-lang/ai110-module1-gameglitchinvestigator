# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Hint doesn't reliably give expected output i.e. telling to guess lower when number is actually higher and vice versa
- Harder modes have shorter ranges which secret number is randomised instead of a larger range
- Program is one step behind. Guess number button needs to presses, once to reset context and the second to actually submit the guess numbers
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 50 | "Go Higher" hint | "Go Lower" hint shown | None |
| Guess of 200 | Out of Range or "Go Lower" hint| "Go Higher" hint shown | None |
| Difficulty Change to Hard | Increase in range | Decrease in range to 1-50 from 1-100 | None |
| New Game Button/Command | History Reset, Secret Number Reset| No History Reset, Yes Secret Number Reset | None |
| New Game Button/Command when maximum attempts are used | New Game starts afresh | Everything is stuck. Nothing new happens except secret number changes | None |
| Submit Guess button | Guess is submitted and shown in History | Occassional delays. Requires the button to be tapped twice. It inputs for the last number before the currently typed number| None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
