import sqlite3
import random
def insert_news_comment_templates():
    new_templates = [
        "This news article provided a comprehensive overview of the issue at hand. The level of detail and the clarity of explanation were exceptional. Thank you for shedding light on such an important topic.",
        "What an insightful piece! The depth of analysis and the balanced perspective offered in this article were impressive. It's refreshing to see such well-researched journalism.",
        "This article is a great example of quality journalism. The thorough research and unbiased reporting make it a must-read for anyone interested in the topic. Kudos to the author for a job well done!",
        "I found this news report to be incredibly informative and well-written. The author did a great job of breaking down complex information into easily understandable points. Looking forward to more articles like this.",
        "This news story was very enlightening. The detailed coverage and the careful analysis provided a clear understanding of the situation. It's great to see such high standards in journalism.",
        "An excellent read! This article provided a lot of valuable information and presented it in a clear and engaging manner. I appreciate the effort put into researching and writing this piece.",
        "This is one of the best news articles I've read in a while. The thorough analysis and the balanced reporting are commendable. Thank you for keeping us informed with such high-quality content.",
        "A well-written and highly informative news article. The depth of research and the clear presentation of facts make it a standout piece. I'm looking forward to reading more from this author.",
        "This article was very well done. The author did an excellent job of explaining the issue and providing context. It's refreshing to read such well-crafted news reports.",
        "An outstanding piece of journalism! The detailed analysis and the balanced reporting in this article were impressive. It's clear that a lot of effort went into researching and writing this piece.",
        "This news article was a great read. The level of detail and the clarity of the writing were exceptional. Thank you for providing such comprehensive coverage of this issue.",
        "A highly informative and well-written news report. The author did a great job of presenting the facts and providing context. This is the kind of journalism we need more of.",
        "This article was very enlightening and well-researched. The author's ability to present complex information in a clear and engaging way is commendable. Keep up the great work!",
        "An excellent news article! The thorough research and the balanced reporting make it a must-read. Thank you for keeping us informed with such high-quality journalism.",
        "This news story provided a lot of valuable information. The detailed coverage and the careful analysis made it very informative. Looking forward to more articles from this author.",
        "A fantastic piece of journalism! The depth of analysis and the clear presentation of facts in this article were impressive. It's great to see such high standards in news reporting.",
        "This article was very well done. The author did an excellent job of explaining the issue and providing context. It's refreshing to read such well-crafted news reports.",
        "An outstanding piece of journalism! The detailed analysis and the balanced reporting in this article were impressive. It's clear that a lot of effort went into researching and writing this piece.",
        "This news article was a great read. The level of detail and the clarity of the writing were exceptional. Thank you for providing such comprehensive coverage of this issue.",
        "A highly informative and well-written news report. The author did a great job of presenting the facts and providing context. This is the kind of journalism we need more of.",
        "This article was very enlightening and well-researched. The author's ability to present complex information in a clear and engaging way is commendable. Keep up the great work!",
        "An excellent news article! The thorough research and the balanced reporting make it a must-read. Thank you for keeping us informed with such high-quality journalism.",
        "This news story provided a lot of valuable information. The detailed coverage and the careful analysis made it very informative. Looking forward to more articles from this author.",
        "A fantastic piece of journalism! The depth of analysis and the clear presentation of facts in this article were impressive. It's great to see such high standards in news reporting.",
        "This article was very well done. The author did an excellent job of explaining the issue and providing context. It's refreshing to read such well-crafted news reports.",
        "An outstanding piece of journalism! The detailed analysis and the balanced reporting in this article were impressive. It's clear that a lot of effort went into researching and writing this piece.",
        "This news article was a great read. The level of detail and the clarity of the writing were exceptional. Thank you for providing such comprehensive coverage of this issue.",
        "A highly informative and well-written news report. The author did a great job of presenting the facts and providing context. This is the kind of journalism we need more of.",
        "This article was very enlightening and well-researched. The author's ability to present complex information in a clear and engaging way is commendable. Keep up the great work!",
        "An excellent news article! The thorough research and the balanced reporting make it a must-read. Thank you for keeping us informed with such high-quality journalism.",
        "This news story provided a lot of valuable information. The detailed coverage and the careful analysis made it very informative. Looking forward to more articles from this author.",
        "A fantastic piece of journalism! The depth of analysis and the clear presentation of facts in this article were impressive. It's great to see such high standards in news reporting.",
        "This article was very well done. The author did an excellent job of explaining the issue and providing context. It's refreshing to read such well-crafted news reports.",
        "An outstanding piece of journalism! The detailed analysis and the balanced reporting in this article were impressive. It's clear that a lot of effort went into researching and writing this piece.",
        "This news article was a great read. The level of detail and the clarity of the writing were exceptional. Thank you for providing such comprehensive coverage of this issue.",
        "A highly informative and well-written news report. The author did a great job of presenting the facts and providing context. This is the kind of journalism we need more of.",
        "This article was very enlightening and well-researched. The author's ability to present complex information in a clear and engaging way is commendable. Keep up the great work!",
        "An excellent news article! The thorough research and the balanced reporting make it a must-read. Thank you for keeping us informed with such high-quality journalism.",
        "This news story provided a lot of valuable information. The detailed coverage and the careful analysis made it very informative. Looking forward to more articles from this author.",
        "A fantastic piece of journalism! The depth of analysis and the clear presentation of facts in this article were impressive. It's great to see such high standards in news reporting.",
        "This article was very well done. The author did an excellent job of explaining the issue and providing context. It's refreshing to read such well-crafted news reports.",
        "An outstanding piece of journalism! The detailed analysis and the balanced reporting in this article were impressive. It's clear that a lot of effort went into researching and writing this piece.",
        "This news article was a great read. The level of detail and the clarity of the writing were exceptional. Thank you for providing such comprehensive coverage of this issue.",
        "A highly informative and well-written news report. The author did a great job of presenting the facts and providing context. This is the kind of journalism we need more of.",
        "This article was very enlightening and well-researched. The author's ability to present complex information in a clear and engaging way is commendable. Keep up the great work!",
        "An excellent news article! The thorough research and the balanced reporting make it a must-read. Thank you for keeping us informed with such high-quality journalism.",
        "This news story provided a lot of valuable information. The detailed coverage and the careful analysis made it very informative. Looking forward to more articles from this author.",
        "A fantastic piece of journalism! The depth of analysis and the clear presentation of facts in this article were impressive. It's great to see such high standards in news reporting.",
        "This article was very well done. The author did an excellent job of explaining the issue and providing context. It's refreshing to read such well-crafted news reports.",
        "An outstanding piece of journalism! The detailed analysis and the balanced reporting in this article were impressive. It's clear that a lot of effort went into researching and writing this piece."
    ]

    conn = sqlite3.connect('./message_templates.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS News_Comments_Templates (
                        id INTEGER PRIMARY KEY,
                        template TEXT NOT NULL)''')

    cursor.executemany('INSERT INTO News_Comments_Templates (template) VALUES (?)', [(template,) for template in new_templates])

    conn.commit()
    conn.close()

insert_news_comment_templates()

def get_random_news_comment():
    conn = sqlite3.connect('./message_templates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT template FROM News_Comments_Templates')
    templates = cursor.fetchall()
    conn.close()
    return random.choice(templates)[0]

# Example usage
print(get_random_news_comment())
