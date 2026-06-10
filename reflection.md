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

- I used Claude Code for this project in my IDE
- It correctly suggested a fix to the comparisons of the secret score and the guess score which was intially comapring in strings instead of integer. It had a simple solution of removing all the prior conversions which was faster and more concise than what I was thinking.
- It however incorectly suggested leaving the label 'too high' with 'go higher' which was missing the point of the hints. This may be due to the fact that it didn't understand the entire project well enough as I was using a more lightweight model which only ensured correct syntax of code. I verified this by working through the logic and doing numerous pytests to confirm my results

---

## 3. Debugging and testing your fixes

- I knew the hint bug was fixed because I ran tests on every testcase and edge case that could possibly arise in the py test as well as manually testing it in the streamlit application. 
- One of the tests I did was checking if it'd print 'Go lower' if I guessed above the secret number which it did. This showed I had fixed the issue in my code
- AI did help in designing the tests by ensuring I went through every test case possible which was a huge timesaver. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
