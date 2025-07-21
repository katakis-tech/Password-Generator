# 📍 Project Roadmap: Password Generator

---

## ✅ Phase 1: Base Project (COMPLETE 🎉)
- [x] Basic password generation using selected character sets
- [x] Clipboard copy with `pyperclip`
- [x] Basic strength rating (Weak / Okay / Strong)
- [x] Retry option if password is weak
- [x] GitHub repository created and linked 💪

---

## 🛠️ Phase 2: Clean-Up & Safety
**Goal: Make the app smarter and more user-proof**

- [ ] Add input validation for password length (e.g., handle strings like `"ten"`)
- [ ] Handle invalid `y/n` inputs gracefully (loop until valid)
- [ ] Require at least one character type, but loop back instead of exiting
- [ ] Add `.gitignore` with standard Python rules
- [ ] Write a README with usage instructions and sample output

---

## 💡 Phase 3: Polish & Feedback
**Goal: Make it look & feel more pro**

- [ ] Improve password strength check (based on entropy, variety, etc.)
- [ ] Add estimated crack time (optional)
- [ ] Pretty up console output (ASCII banners, spacing, formatting)
- [ ] Show a preview of the character set being used (optional visual feedback)
- [ ] Add a license file (MIT recommended)

---

## 🎨 Phase 4: GUI Upgrade
**Goal: Bring it out of the terminal and into the real world**

- [ ] Create a Tkinter GUI with:
  - Length slider or input box
  - Checkboxes for character types
  - Button to generate + copy password
  - Label that shows password strength
- [ ] Add clipboard confirmation message
- [ ] Package it as an `.exe` with PyInstaller (optional)

---

## 🛡️ Phase 5: Cybersecurity Spin
**Goal: Showcase your IT/Cyber knowledge**

- [ ] Enforce secure password rules (at least 1 of each char type)
- [ ] Add option to generate **passphrases**
- [ ] Add option to auto-save passwords **encrypted** with a master key
- [ ] Hash passwords with SHA-256 for education purposes
- [ ] Add command-line flags using `argparse` for scripting use

---

## 🧪 Phase 6: Testing & Deployment
**Goal: Make it deployable and testable like a real project**

- [ ] Add unit tests using `unittest` or `pytest`
- [ ] Document features and usage in `README.md`
- [ ] Upload demo GIF or screenshot to the repo
- [ ] Add topics/tags to the GitHub repo
- [ ] Create project board or issue tracker on GitHub
