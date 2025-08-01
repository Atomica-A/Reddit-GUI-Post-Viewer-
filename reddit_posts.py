import praw
import praw_config
import subprocess

# user input for keyword
entry = subprocess.run(
    ["yad", "--entry", "--title=Search Reddit", "--text=Enter a title or keyword to search in Reddit:"],
    text=True,
    capture_output=True
)

search = entry.stdout.strip()

if not search:
    print("No input Provided. Exiting.")
    exit()

# PRAW
reddit = praw.Reddit(
    client_id=praw_config.CLIENT_ID,
    client_secret=praw_config.CLIENT_SECRET,
    user_agent=praw_config.CLIENT_AGENT
)

posts = []
for submission in reddit.subreddit("linux").hot(limit=10):
    if search_term.lower() in submission.title.lower():
        posts.append(submission)

if not posts:
    subprocess.run(["yad", "--info", "--text=No matching posts found."])
    exit()

# list for YAD
yad_list = []
for post in posts:
    title = post.title.replace('"', "'").replace('\n', ' ').strip()
    yad_list.append(title)

# list dialog
select = subprocess.run(
    ["yad", "--list", "--title=Reddit Posts", "--column=Title", "--width=600", "--height=400", "--separator="],
    input="\n".join(yad_list),
    text=True,
    capture_output=True
)

selected_title = select.stdout.strip()

if selected_title:
    for post in posts:
        if selected_title in post.title:
            detail = f"Title: {post.title}\nURL: {post.url}\nUpvotes: {post.score}\n\n"

            post.comments.replace_more(limit=0)
            if post.comments:
                detail += f"Top Comment:\n{post.comments[0].body[:500]}"
            else:
                detail += "No comments."

            subprocess.run(["yad", "--text-info", "--width=600", "--height=400", "--title=Post Details"],
                           input=detail, text=True)
            break
