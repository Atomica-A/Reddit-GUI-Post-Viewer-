# Reddit GUI Viewer

This is a simple Python tool that lets you search Reddit posts from reddit using a graphical interface. It uses the Reddit API to fetch posts and `yad` to show pop-up windows for input and selection. You can enter a keyword, see matching post titles, and view the selected post’s details — including the URL, upvotes, and top comment.

---

## 💡 What It Does

- Lets you enter a search term in a popup window
- Shows Reddit post titles that match your search
- When you click a title, it shows the post’s link, score, and top comment

---

## 🛠 What I Used

- **Python 3**
- **PRAW** – Python Reddit API Wrapper
- **YAD** – for simple Linux GUI popups
- **subprocess** – to connect Python and YAD
