import random
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.loginScript import login
from scripts.postScript import post_message
from scripts.db_utils import get_new_random_user
from webdriver_manager.chrome import ChromeDriverManager

# List of predefined templates
templates = [
    "In today's news, the topic of {topic} has been a major focus. Experts say {fact} which may have significant implications.",
    "A recent discussion on {topic} has revealed {fact}. This could potentially change the way we understand {related_topic}.",
    "The ongoing debate about {topic} continues, with new insights showing {fact}. What does this mean for {related_topic}?",
    "As we delve into the subject of {topic}, it's clear that {fact}. This raises important questions about {related_topic}.",
    "Recent studies on {topic} suggest {fact}. This could lead to new developments in {related_topic}.",
    "Today's highlight is {topic}. Recent findings indicate {fact}, prompting further investigation into {related_topic}.",
    "The focus of today's discussion is {topic}. {fact} has emerged as a key point of interest, influencing {related_topic}.",
    "Exploring {topic} today reveals {fact}. This is expected to have a notable effect on {related_topic}.",
    "New insights into {topic} show {fact}. This development could reshape our understanding of {related_topic}.",
    "In the realm of {topic}, {fact} is becoming increasingly significant. What does this mean for {related_topic}?",
    "The latest news on {topic} highlights {fact}, sparking conversations about {related_topic}.",
    "A breakthrough in {topic} has led to {fact}. This could alter the landscape of {related_topic}.",
    "Recent trends in {topic} show {fact}, which could impact {related_topic} in various ways.",
    "The discussion around {topic} is heating up, with {fact} taking center stage. This is likely to influence {related_topic}.",
    "With {topic} being a hot topic, {fact} has emerged as a crucial element. How will this affect {related_topic}?",
    "Updates on {topic} reveal {fact}, opening new avenues for {related_topic}.",
    "The topic of {topic} is garnering attention due to {fact}. This has significant implications for {related_topic}.",
    "Today's news brings {topic} into focus. {fact} has been highlighted, prompting discussions about {related_topic}.",
    "The impact of {topic} is evident through {fact}. This trend is shaping the future of {related_topic}.",
    "As {topic} evolves, {fact} is becoming a major point of interest, influencing the trajectory of {related_topic}.",
    "Recent developments in {topic} suggest {fact}. This has potential implications for {related_topic}.",
    "Analyzing {topic} today reveals {fact}, offering new perspectives on {related_topic}.",
    "The latest in {topic} highlights {fact}, a key factor in shaping {related_topic}.",
    "Exploring {topic} has unveiled {fact}, which could transform our understanding of {related_topic}.",
    "In-depth analysis of {topic} shows {fact}. What does this mean for the future of {related_topic}?",
    "New data on {topic} indicates {fact}. This will likely have an impact on {related_topic}.",
    "The significance of {topic} is underscored by {fact}. How will this affect {related_topic}?",
    "As we assess {topic}, {fact} stands out as a major factor influencing {related_topic}.",
    "Today's focus on {topic} brings {fact} to light, raising questions about its effect on {related_topic}.",
    "The evolution of {topic} is marked by {fact}, prompting new insights into {related_topic}.",
    "Recent findings on {topic} suggest {fact}, with potential consequences for {related_topic}.",
    "The discourse around {topic} has been energized by {fact}, with significant implications for {related_topic}.",
    "The current discussion on {topic} emphasizes {fact}. This could reshape our approach to {related_topic}.",
    "Exploring {topic} today shows that {fact} is a key consideration. This may influence {related_topic} in unforeseen ways."
    # News Style
    "Breaking news: Today, {topic} has taken a new turn with {fact}. This development could reshape our understanding of {related_topic}.",
    "Today's major update in {topic}: {fact}. How does this impact the future of {related_topic}?",
    "In a recent revelation, {topic} has been highlighted by {fact}. The implications for {related_topic} are profound.",
    "Key insights into {topic} reveal {fact}. This raises significant questions about {related_topic}.",
    "Recent events have shown that {topic} is more critical than ever. {fact} could lead to major changes in {related_topic}.",

    # Thoughtful/Reflective Style
    "Reflecting on {topic}, we find that {fact}. This insight invites us to reconsider our approach to {related_topic}.",
    "As we ponder {topic}, it's clear that {fact}. This prompts a deeper examination of {related_topic}.",
    "Considering {topic}, one can't ignore {fact}. How does this influence our perspective on {related_topic}?",
    "In the realm of {topic}, {fact} offers a unique viewpoint. What does this mean for {related_topic}?",
    "Exploring {topic}, we encounter {fact}. This brings new light to our understanding of {related_topic}.",

    # Motivational Style
    "In the face of {topic}, remember that {fact}. This is a powerful reminder of the strength we have to overcome {related_topic}.",
    "When tackling {topic}, keep in mind {fact}. This can inspire us to face {related_topic} with renewed vigor.",
    "Despite {topic}, {fact} shows us that we have the power to tackle {related_topic} with resilience.",
    "Facing {topic}, it's crucial to remember {fact}. This can fuel our drive to address {related_topic} effectively.",
    "As we confront {topic}, let {fact} be a beacon of hope. It empowers us to take on {related_topic} with confidence.",

    # Humorous Style
    "Did you know? {topic} can be surprisingly {fact}. Who knew {related_topic} could be this entertaining?",
    "When {topic} meets {fact}, it’s like {related_topic} had a comedy show. Prepare for some laughs!",
    "Ever wondered about {topic}? Well, {fact} makes {related_topic} sound like a punchline in a joke.",
    "Turns out, {topic} is not just serious. {fact} proves that even {related_topic} can have its funny moments.",
    "In a twist of {topic}, {fact} has made {related_topic} the new comedy hit. Who's up for a laugh?"

    # Inspirational Style
    "Amidst the challenges of {topic}, {fact} serves as a reminder that we can overcome {related_topic} with perseverance.",
    "In the journey of {topic}, {fact} inspires us to tackle {related_topic} with courage and optimism.",
    "Facing {topic}, we find that {fact} is a testament to the strength needed to address {related_topic}.",
    "As we navigate {topic}, let {fact} guide us in our pursuit of solutions for {related_topic}.",
    "In the realm of {topic}, {fact} motivates us to approach {related_topic} with a positive outlook."

    # Formal/Professional Style
    "In recent developments regarding {topic}, {fact} has been identified. This warrants a reevaluation of our strategies for {related_topic}.",
    "The current discourse on {topic} highlights {fact}. It is imperative to consider the implications for {related_topic}.",
    "Recent findings in {topic} reveal {fact}. This necessitates a strategic review of {related_topic}.",
    "As {topic} evolves, {fact} underscores the need for a reassessment of our approach to {related_topic}.",
    "The analysis of {topic} indicates {fact}, prompting a professional examination of {related_topic}."

    # Educational/Informative Style
    "Did you know that {topic} involves {fact}? This is an important aspect of understanding {related_topic}.",
    "Understanding {topic} requires knowledge of {fact}. This information is crucial for comprehending {related_topic}.",
    "Exploring {topic}, we discover that {fact} plays a key role in {related_topic}. This insight is fundamental to our learning.",
    "To grasp {topic}, it's essential to consider {fact}. This contributes significantly to our knowledge of {related_topic}.",
    "In the study of {topic}, {fact} provides valuable insights into {related_topic}. This information enriches our understanding."

    # Casual/Conversational Style
    "So, guess what about {topic}? {fact} makes {related_topic} way more interesting. Check it out!",
    "Hey, did you hear about {topic}? {fact} just makes {related_topic} even cooler. What do you think?",
    "You won’t believe this: {topic} + {fact} = {related_topic}. Pretty wild, right?",
    "Here’s a fun fact about {topic}: {fact}. It totally changes how we look at {related_topic}.",
    "Ever think about {topic}? Well, {fact} makes {related_topic} something you’ll want to talk about!"

    # Creative/Artistic Style
    "In the canvas of {topic}, {fact} paints a vibrant picture of {related_topic}. This artwork inspires new perspectives.",
    "The narrative of {topic} unfolds with {fact}, adding a brushstroke to the masterpiece of {related_topic}.",
    "As we explore {topic}, {fact} colors the story of {related_topic} with imaginative insights.",
    "The tapestry of {topic} is enriched by {fact}, weaving {related_topic} into a fascinating narrative.",
    "In the realm of {topic}, {fact} creates a dynamic interplay of ideas surrounding {related_topic}."

    # Quirky/Unusual Style
    "Imagine {topic} with a twist: {fact} makes {related_topic} look like a plot twist in a sci-fi novel.",
    "If {topic} were a quirky character, {fact} would be its trademark move in {related_topic}. What a scene!",
    "Picture this: {topic} meets {fact} in a mash-up that turns {related_topic} into an unexpected adventure.",
    "Ever thought of {topic} as a wild card? {fact} certainly adds a quirky spin to {related_topic}.",
    "In the world of {topic}, {fact} is the oddball that makes {related_topic} anything but ordinary."

]
# List of topics and facts for random selection
topics = ["climate change", "technology advancements", "healthcare", "economics", "education"]
facts = [
    # Climate Change
    "a significant increase in global temperatures over the past century",
    "a rise in sea levels due to melting polar ice caps",
    "more frequent and severe weather events, including hurricanes and droughts",
    "a decrease in biodiversity as species struggle to adapt",
    "the impact of greenhouse gases on global warming",

    # Technology Advancements
    "the rapid development of artificial intelligence and machine learning",
    "breakthroughs in quantum computing that could revolutionize data processing",
    "the expansion of 5G networks and their impact on connectivity",
    "advancements in biotechnology and genetic engineering",
    "the rise of autonomous vehicles and their potential benefits and risks",

    # Healthcare
    "the development of new vaccines that combat emerging diseases",
    "advancements in personalized medicine and targeted therapies",
    "the increasing use of telemedicine for remote consultations",
    "progress in understanding and treating mental health disorders",
    "the impact of lifestyle changes on overall health and well-being",

    # Economics
    "the effect of inflation on purchasing power and cost of living",
    "the impact of globalization on local economies",
    "trends in unemployment rates and job market dynamics",
    "the influence of fiscal and monetary policies on economic stability",
    "emerging markets and their role in the global economy",

    # Education
    "the rise of online learning platforms and digital classrooms",
    "trends in educational technology and its impact on student engagement",
    "the growing emphasis on STEM (Science, Technology, Engineering, Mathematics) education",
    "the challenges and opportunities of remote and hybrid learning models",
    "the impact of educational reforms on student outcomes",

    # Climate Change (Additional Facts)
    "the role of renewable energy sources in reducing carbon footprints",
    "the effects of deforestation on carbon dioxide levels",
    "the significance of international climate agreements and their enforcement",
    "the role of individual actions in mitigating climate change",
    "the impact of ocean acidification on marine life",

    # Technology Advancements (Additional Facts)
    "the evolution of blockchain technology and its applications",
    "the implications of data privacy and cybersecurity in the digital age",
    "the development of smart cities and their impact on urban living",
    "the role of big data in shaping business strategies",
    "the potential of augmented reality (AR) and virtual reality (VR) technologies",

    # Healthcare (Additional Facts)
    "the challenges of addressing antibiotic resistance and superbugs",
    "the importance of preventative care and early diagnosis",
    "the impact of environmental factors on public health",
    "advances in surgical techniques and medical devices",
    "the role of nutrition and fitness in disease prevention",

    # Economics (Additional Facts)
    "the impact of technological advancements on job creation and automation",
    "trends in income inequality and wealth distribution",
    "the role of international trade agreements in shaping economic policies",
    "the influence of consumer behavior on market trends",
    "the effects of economic crises on global financial stability",

    # Education (Additional Facts)
    "the role of early childhood education in long-term academic success",
    "the impact of school funding and resources on educational quality",
    "the challenges of addressing educational disparities and inequities",
    "the benefits of extracurricular activities on student development",
    "the role of parental involvement in student achievement"
]

related_topics = ["global impact", "future trends", "public policy", "innovations", "social dynamics"]

def generate_template_message():
    template = random.choice(templates)
    topic = random.choice(topics)
    fact = random.choice(facts)
    related_topic = random.choice(related_topics)
    message = template.format(topic=topic, fact=fact, related_topic=related_topic)
    return message

def perform_actions_for_user(driver, username, password, style, topics, used_messages, used_template_ids):
    try:
        login(driver, username, password)
        WebDriverWait(driver, 10).until(EC.url_to_be('https://chatter.al/home'))
        message = generate_template_message()
        post_message(driver, message)
    except Exception as e:
        print(f"An error occurred for user {username}: {e}")
    finally:
        driver.delete_all_cookies()

# Main script
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = ChromeService(executable_path=ChromeDriverManager().install())

used_messages = set()
used_template_ids = set()

for attempt in range(10):
    random_user = get_new_random_user()
    if random_user:
        first_name, last_name, email, password, bio, style, topics, message_type, topic, keywords = random_user
        driver = webdriver.Chrome(service=service, options=options)
        perform_actions_for_user(driver, email, password, style, topics, used_messages, used_template_ids)
        driver.quit()
    else:
        print("No users found.")
        break  # Exit the loop if no more users are available
