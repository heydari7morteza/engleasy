import os
import requests
import random

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# چند جمله نمونه انگلیسی (می‌تونی هر روز اضافه‌اش کنی)
sentences = [
    """One of the most important skills a person can develop is the ability to listen carefully and understand different perspectives before making a decision.

Important : Having great value or significance.
Skills : Abilities that help you do something well.
Develop : To improve or grow over time.
Perspectives : Different ways of looking at or thinking about something.
Decision : A choice made after thinking about something.""",

    """Traveling to new countries not only allows you to experience different cultures, but also teaches you to adapt to unexpected situations and challenges.

Experience : To do or feel something yourself.
Cultures : The customs, arts, and beliefs of a group of people.
Adapt : To adjust or change to fit new conditions.
Unexpected : Something that happens suddenly or not planned.
Challenges : Difficult tasks that test your ability.""",

    """I believe that learning a foreign language is one of the best ways to expand your mind and communicate with people from all around the world.

Believe : To think that something is true or right.
Foreign : From another country.
Expand : To make something larger or broader.
Communicate : To share information or ideas with others.
All around the world : Everywhere on Earth.""",

    """Sometimes, the most valuable lessons in life come from our mistakes, and we must be willing to accept them and grow from the experience.

Valuable : Very useful or important.
Lessons : Things you learn from experiences.
Mistakes : Wrong actions or decisions.
Accept : To agree to receive or deal with something.
Grow : To improve or develop yourself.""",

    """Reading books about history or science can provide a deeper understanding of how the world works and why societies develop in certain ways.

Provide : To give something that is needed.
Understanding : The ability to know or explain something.
Societies : Groups of people living together with shared rules and culture.
Develop : To grow or change over time.
Deeper : More complete or thoughtful.""",

    """It is essential to balance work and personal life, because focusing too much on one aspect can negatively affect your overall happiness and health.

Essential : Very important and necessary.
Balance : To keep equal attention on different parts of life.
Aspect : One part of a situation or idea.
Negatively : In a harmful or bad way.
Overall : Considering everything together.""",

    """Many people underestimate the importance of expressing gratitude on a daily basis, which can greatly improve relationships and mental well-being.

Underestimate : To think something is less important than it really is.
Expressing : Showing your thoughts or feelings.
Gratitude : Thankfulness or appreciation.
Relationships : The connections between people.
Well-being : A state of being healthy and happy.""",

    """When faced with a difficult problem, it is often helpful to break it into smaller steps and tackle each one methodically rather than trying to solve everything at once.

Faced with : To deal with or confront something.
Break into : To divide into smaller parts.
Tackle : To try to solve or handle a problem.
Methodically : In an organized and careful way.
At once : All together, at the same time.""",

    """Volunteering in your community not only helps others, but it also gives you a sense of purpose and the opportunity to learn new skills.

Volunteering : Working to help others without being paid.
Community : A group of people living in the same area.
Sense of purpose : A feeling that your life has meaning or direction.
Opportunity : A chance to do something.
Skills : Abilities that help you do something well.""",

    """Technology has transformed the way we live, but it is important to use it responsibly to avoid becoming too dependent on digital devices.

Transformed : Changed completely.
Responsibly : In a careful and right way.
Avoid : To keep away from something bad.
Dependent : Needing something or someone too much.
Digital devices : Electronic tools like phones or computers.""",


    """Experiencing failure can be challenging, but it teaches resilience and helps individuals develop better problem-solving strategies in the future.

Experiencing : Going through or facing something yourself.
Failure : Lack of success in doing something.
Resilience : The ability to recover quickly from difficulties.
Strategies : Plans or methods to achieve something.
In the future : At a later time, not now.""",

"""Spending time in nature can have a calming effect on the mind and can improve mental health by reducing stress and anxiety levels.

Calming effect : Something that makes you feel relaxed or peaceful.
Mental health : The condition of your mind and emotions.
Reducing : Making something smaller or less.
Stress : Mental pressure or worry.
Anxiety : A feeling of nervousness or fear.""",

"""Developing creativity is not limited to artists; it can be cultivated in everyday life by approaching problems from different perspectives.

Creativity : The ability to make or think of new things or ideas.
Limited to : Restricted only to something or someone.
Cultivated : Developed or improved over time.
Approaching : Dealing with or coming near to something.
Perspectives : Ways of thinking about something; viewpoints.""",

"""Learning how to manage time efficiently allows people to accomplish more tasks, reduce stress, and have more opportunities for personal growth.

Manage : To control or organize something.
Efficiently : Doing something in the best possible way with little waste.
Accomplish : To successfully complete something.
Opportunities : Chances to do or achieve something.
Personal growth : The process of improving yourself.""",

"""Cultural events such as theater performances or music festivals help people connect with their community and appreciate diversity.

Cultural : Related to art, music, or traditions of a society.
Performances : Shows or plays done in front of an audience.
Connect : To join or bring people together.
Appreciate : To recognize the value of something.
Diversity : Variety; differences among people or things.""",

"""Taking responsibility for your actions is a sign of maturity and helps build trust and respect in both personal and professional relationships.

Responsibility : Being in charge of something or accepting the results of your actions.
Maturity : The quality of behaving in a grown-up or wise way.
Trust : Belief that someone is honest or reliable.
Respect : A feeling of admiration for someone.
Professional relationships : Connections at work or business.""",

"""Watching documentaries and reading informative articles can broaden your understanding of global issues and current events.

Documentaries : Non-fiction films that give factual information.
Informative : Providing useful knowledge or facts.
Broaden : To make something wider or more extensive.
Global issues : Problems that affect the world.
Current events : Things happening in the world right now.""",

"""Maintaining a healthy lifestyle includes eating nutritious food, exercising regularly, and ensuring enough sleep for mental and physical well-being.

Maintaining : Keeping something in good condition.
Nutritious : Healthy and full of good substances.
Regularly : Happening often or at fixed times.
Ensuring : Making sure that something happens.
Well-being : A state of being healthy and happy.""",

"""Understanding other people's points of view is crucial in solving conflicts and reaching compromises in both work and social life.

Points of view : Opinions or ways of thinking.
Crucial : Extremely important.
Conflicts : Disagreements or fights.
Compromises : Agreements reached by both sides giving up something.
Social life : The part of life involving friends and relationships.""",

"""Some people believe that success is purely about hard work, while others argue that luck and opportunity play an equally important role.

Purely : Completely or only.
Argue : To give reasons for or against something.
Luck : Success or failure caused by chance, not effort.
Opportunity : A chance to do something.
Equally important : Having the same level of importance.""",

"""Spending time with friends and family is essential for emotional support and can help reduce feelings of loneliness and isolation.

Essential : Very important and necessary.
Emotional support : Comfort and understanding from others.
Reduce : To make something less or smaller.
Loneliness : A sad feeling of being alone.
Isolation : Being separated from others.""",

"""Participating in sports not only improves physical fitness but also teaches valuable lessons about teamwork and discipline.

Participating : Taking part in something.
Physical fitness : The condition of being healthy and strong.
Valuable : Very useful or important.
Teamwork : Working together to achieve a goal.
Discipline : Control over your behavior or actions.""",

"""Being curious and asking questions encourages learning and helps develop critical thinking skills necessary for personal growth.

Curious : Wanting to know or learn something.
Encourages : Gives someone the confidence to do something.
Critical thinking : The ability to think clearly and logically.
Necessary : Needed or essential.
Personal growth : The process of becoming better or more capable.""",

"""Reading novels in a foreign language can improve vocabulary, grammar, and comprehension while making the learning process enjoyable.

Novels : Long stories in book form.
Foreign : From another country.
Vocabulary : The words you know and use.
Comprehension : Understanding what you read or hear.
Enjoyable : Something that gives pleasure or fun.""",

"""Traveling alone can be a powerful experience, teaching independence, self-reliance, and how to navigate unfamiliar environments confidently.

Powerful : Strong or having a great effect.
Independence : The ability to do things by yourself.
Self-reliance : Relying on your own abilities and efforts.
Navigate : To find your way or direction.
Unfamiliar : Not known or strange.""",

"""Listening to podcasts or watching educational videos is a great way to gain knowledge about topics that interest you without leaving home.

Podcasts : Audio programs available online.
Educational : Designed to teach or provide knowledge.
Gain : To get or receive something useful.
Topics : Subjects or themes of discussion.
Interest you : Something that you like or want to learn about.""",

"""Sometimes, the best way to overcome fear is to face it gradually, step by step, while acknowledging the challenges involved.

Overcome : To successfully deal with or control something difficult.
Gradually : Slowly, over time.
Step by step : Doing something in small stages.
Acknowledging : Admitting or accepting something.
Challenges : Difficulties or obstacles.""",

"""Learning to cook new recipes allows people to be creative, explore different cultures, and develop an important life skill.

Recipes : Instructions for preparing food.
Creative : Using imagination to make new things.
Explore : To discover or learn more about something.
Cultures : The customs, arts, and traditions of people.
Life skill : An ability useful for everyday living.""",

"""Maintaining friendships requires effort, including communication, understanding, and spending quality time together regularly.

Requires : Needs something to happen or exist.
Effort : Hard work or energy put into something.
Communication : The act of sharing information or feelings.
Quality time : Meaningful time spent with someone.
Regularly : Happening often or at fixed intervals.""",

"""Attending workshops or seminars on topics of interest can provide valuable knowledge, networking opportunities, and motivation.

Workshops : Small meetings for learning or practicing skills.
Seminars : Educational meetings on a specific subject.
Networking : Making professional or social connections.
Opportunities : Chances to do or achieve something.
Motivation : A reason or desire to do something.""",

"""Being organized in your daily life reduces stress and ensures that you can complete tasks more efficiently and effectively.

Organized : Keeping things in order.
Reduces : Makes something smaller or less.
Ensures : Makes sure that something happens.
Efficiently : Doing something well with little waste.
Effectively : Producing the result that you want.""",

"""Listening to music can influence mood, boost creativity, and even improve concentration while studying or working.

Influence : To have an effect on something.
Mood : The way you feel at a particular time.
Boost : To increase or improve something.
Concentration : The ability to focus your mind.
Creativity : The ability to make new and original ideas.""",

"""Understanding environmental issues and adopting sustainable habits can contribute to preserving the planet for future generations.

Environmental issues : Problems related to nature or the Earth.
Adopting : Choosing to start using something.
Sustainable : Not harming the environment; lasting long.
Contribute : To help bring about a result.
Preserving : Keeping something safe and unchanged.""",

"""Engaging in debates and discussions encourages people to articulate their thoughts clearly and consider alternative viewpoints.

Engaging : Taking part in or being involved with something.
Debates : Formal discussions about different opinions.
Articulate : To express your thoughts clearly.
Alternative : Different or other options.
Viewpoints : Opinions or perspectives.""",

"""Traveling to rural areas can provide a different perspective on life, showing people how communities live and work in diverse conditions.

Rural : Relating to the countryside.
Perspective : A way of thinking about something.
Communities : Groups of people living together.
Diverse : Varied or different.
Conditions : The situations in which people live or work.""",

"""Learning a musical instrument can improve memory, coordination, and emotional expression while providing a creative outlet.

Musical instrument : A tool used to produce music (e.g. guitar, piano).
Coordination : The ability to move different parts of your body smoothly.
Emotional expression : Showing your feelings through actions or art.
Creative outlet : A way to express creativity.
Memory : The ability to remember things.""",

"""Being patient and persistent is essential when learning a new skill, as progress often takes time and consistent effort.

Patient : Able to wait calmly.
Persistent : Continuing to try without giving up.
Progress : Improvement or moving forward.
Consistent : Always behaving or happening in the same way.
Effort : Hard work to achieve something.""",

"""Writing in a journal helps individuals reflect on their experiences, organize thoughts, and improve their self-awareness.

Journal : A personal book where you write daily experiences or thoughts.
Reflect : To think carefully about something.
Organize : To arrange things in order.
Self-awareness : Knowing yourself and your feelings.
Experiences : Things that happen to you or that you do.""",

"""Understanding the history of a country can help people appreciate its culture, traditions, and the challenges it has faced.

Understanding : Knowing or being aware of something.
History : The study of past events.
Appreciate : To recognize the good qualities of something.
Traditions : Customs or beliefs passed from generation to generation.
Challenges : Difficult situations that require effort to overcome.
Faced : Experienced or dealt with.
""",

"""Watching movies or reading literature in a foreign language helps learners understand context, idioms, and colloquial expressions.

Literature : Written works such as novels or poems.
Foreign : From another country or language.
Context : The situation or background that helps explain meaning.
Idioms : Expressions whose meanings are not literal.
Colloquial : Informal or everyday language.
Expressions : Phrases or ways of saying something.
""",

"""Developing empathy allows people to form stronger connections with others and enhances their social and emotional intelligence.

Developing : Improving or growing something.
Empathy : The ability to understand and share another person’s feelings.
Connections : Relationships or bonds between people.
Enhances : Improves or strengthens.
Emotional intelligence : Understanding and managing one’s own emotions and others’.
""",

"""Spending time volunteering abroad can teach new languages, skills, and provide insight into different cultures and lifestyles.

Volunteering : Working without pay to help others.
Abroad : In or to another country.
Insight : A clear understanding of something.
Cultures : The way of life of a group of people.
Lifestyles : The way a person or group lives.
""",

"""Some people find meditation and mindfulness practices helpful for reducing anxiety and increasing focus in their daily life.

Meditation : The act of focusing your mind for relaxation or clarity.
Mindfulness : Being aware of the present moment.
Reducing : Making something smaller or less severe.
Anxiety : A feeling of worry or nervousness.
Focus : The ability to concentrate on something.
Daily life : Everyday activities or routines.
""",

"""Exploring career opportunities early in life helps individuals make informed decisions and discover their passions and strengths.

Exploring : Looking into or investigating something.
Career : A person’s job or profession.
Opportunities : Chances to do something or achieve success.
Informed decisions : Choices made with enough knowledge or facts.
Passions : Strong interests or enthusiasm.
Strengths : Positive qualities or abilities.
""",

"""Understanding economics and financial management is important for making responsible decisions about money and investments.

Economics : The study of how money and goods are used in society.
Financial management : Controlling and planning how to use money wisely.
Responsible : Making good and careful decisions.
Investments : Using money to make more money in the future.
""",

"""Taking part in creative writing exercises can enhance imagination, expression, and language skills at the same time.

Creative : Using new ideas and imagination.
Enhance : To improve or make better.
Imagination : The ability to form ideas in your mind.
Expression : The ability to show your thoughts or feelings.
Exercises : Activities done to improve skills.
""",

"""Participating in community projects encourages teamwork, leadership, and a sense of belonging in a social environment.

Participating : Taking part in an activity.
Community : A group of people living in the same area or sharing interests.
Encourages : Supports or motivates.
Leadership : The ability to guide or manage others.
Belonging : Feeling accepted or part of a group.
Environment : The surroundings or conditions where people live.
""",

"""Experiencing different cuisines while traveling teaches people about culture, history, and traditions in an enjoyable way.

Cuisines : Styles of cooking from different countries.
Traveling : Going from one place to another.
Traditions : Customs passed down through generations.
Enjoyable : Giving pleasure or happiness.
""",

"""Being able to give and receive constructive feedback is essential for personal growth, professional development, and learning.

Constructive : Helpful and meant to improve.
Feedback : Information about performance or behavior.
Essential : Very important or necessary.
Development : The process of improving or growing.
Personal growth : Becoming a better or more skilled person.
""",

"""Reading biographies of successful people can inspire motivation, provide strategies, and offer insight into challenges and failures.

Biographies : Books that tell the story of a person’s life.
Inspire : To give someone the desire to do something.
Motivation : The reason or drive to act.
Strategies : Planned ways to achieve goals.
Insight : Deep understanding of something.
""",

"""Learning to prioritize tasks helps people manage time effectively, focus on important activities, and reduce stress levels.

Prioritize : To decide which tasks are most important.
Manage : To handle or control something.
Effectively : In a successful or productive way.
Reduce : To make smaller or less.
Stress : A state of mental or emotional tension.
""",

"""Engaging in outdoor activities, such as hiking or cycling, improves physical health and allows people to connect with nature.

Engaging : Taking part in or doing something.
Outdoor activities : Things done outside, like sports or walking.
Hiking : Walking long distances in nature.
Cycling : Riding a bicycle.
Connect : To build a relationship or link with something.
""",

"""Understanding social etiquette and cultural norms is important when traveling or interacting with people from different backgrounds.

Etiquette : Rules for polite behavior.
Cultural norms : Usual ways of acting in a society.
Interacting : Communicating or working with others.
Backgrounds : A person’s culture, education, or family history.
""",

"""Developing problem-solving skills enables individuals to face challenges creatively and find effective solutions to complex issues.

Problem-solving : Finding ways to fix or handle difficulties.
Enables : Makes something possible.
Creatively : In an imaginative or original way.
Effective : Producing the intended result.
Complex : Complicated or having many parts.
""",

"""Learning about psychology and human behavior helps people improve communication, relationships, and self-awareness.

Psychology : The study of the mind and behavior.
Human behavior : The way people act or respond.
Communication : Sharing information or ideas.
Self-awareness : Knowing your own thoughts and feelings.
""",

"""Participating in online courses provides access to knowledge from experts around the world without needing to attend in person.

Online courses : Classes taken through the internet.
Access : The ability to use or get something.
Experts : People who know a lot about a topic.
Attend : To go to a class or event.
""",

"""Spending time reflecting on personal values and goals helps people make better decisions and live a more fulfilling life.

Reflecting : Thinking deeply about something.
Values : Beliefs about what is right or important.
Goals : Things you want to achieve.
Fulfilling : Making you feel happy and satisfied.
""",

"""Exploring art galleries and museums enhances cultural knowledge and stimulates creativity and critical thinking.

Galleries : Places where art is shown.
Museums : Buildings where historical or cultural objects are displayed.
Enhances : Improves or adds value.
Stimulates : Encourages activity or interest.
Critical thinking : Careful, logical judgment about ideas.
""",

"""Learning to negotiate effectively can improve professional opportunities and help resolve conflicts in a positive manner.

Negotiate : To discuss to reach an agreement.
Opportunities : Chances for progress or success.
Resolve : To solve or settle a problem.
Conflicts : Disagreements or arguments.
Manner : A way of doing something.
""",

"""Keeping up with current events encourages awareness, critical thinking, and the ability to form informed opinions.

Current events : News and happenings in the world today.
Awareness : Knowing what is happening.
Informed : Having knowledge or information.
Opinions : Personal beliefs or judgments.
""",

"""Joining clubs or interest groups allows people to meet like-minded individuals and develop new skills and hobbies.

Like-minded : Having similar ideas or interests.
Individuals : Separate people.
Hobbies : Activities done for fun.
Develop : To improve or make something better.
""",

"""Taking care of mental health is just as important as physical health, requiring mindfulness, relaxation, and support when needed.

Mental health : The state of your mind and emotions.
Mindfulness : Being focused on the present moment.
Relaxation : A state of being calm and free from stress.
Support : Help or encouragement from others.
""",

"""Learning about different religions and philosophies can help people appreciate diversity and respect other beliefs.

Religions : Systems of faith and worship.
Philosophies : Ways of thinking about life and existence.
Diversity : Variety; many different types of people or ideas.
Respect : Showing understanding and care for others’ opinions.
""",

"""Engaging in public speaking opportunities builds confidence, communication skills, and the ability to express ideas clearly.

Public speaking : Talking to an audience formally.
Confidence : Belief in yourself.
Express : To show your ideas or feelings.
Clearly : In a way that is easy to understand.
""",

"""Understanding the impact of technology on society helps people use it responsibly and adapt to changes effectively.

Impact : The effect or influence of something.
Responsibly : In a careful and sensible way.
Adapt : To change to fit new conditions.
Effectively : In a successful or efficient way.
""",

"""Spending time in reflection or meditation can enhance creativity, focus, and emotional balance in daily life.

Reflection : Deep thought or careful consideration.
Meditation : The act of focusing your mind for calmness.
Creativity : The ability to produce new ideas.
Emotional balance : Stability of feelings and mood.
""",

"""Learning to manage stress through techniques such as exercise, meditation, or planning is essential for long-term well-being.

Stress : Pressure or worry caused by problems in life.
Well-being : The state of being healthy and happy.
Techniques : Methods or ways of doing something.
Meditation : A way to relax your mind and body.
Long-term : Lasting for a long time.
""",
"""Reading newspapers or journals helps people stay informed and develop analytical skills by evaluating different perspectives.

Informed : Having knowledge about current events.
Analytical : Thinking carefully and logically.
Evaluate : To judge or check something carefully.
Perspectives : Different ways of looking at things.
""",
"""Developing leadership skills requires practice, self-awareness, and the ability to motivate and guide others effectively.

Leadership : The ability to lead or guide people.
Self-awareness : Knowing your own thoughts and feelings.
Motivate : Inspire or encourage someone to act.
Guide : To show or direct someone.
""",
"""Exploring scientific discoveries helps people understand the world, ask questions, and think critically about evidence.

Discoveries : New things that are found or learned.
Critically : Carefully and thoughtfully.
Evidence : Information that shows something is true.
Explore : To study or learn more about something.
""",
"""Participating in language exchange programs is an effective way to practice speaking and improve fluency in a foreign language.

Participate : To take part in an activity.
Fluency : The ability to speak easily and smoothly.
Foreign : From another country.
Exchange : Giving and receiving between people.
""",
"""Setting personal challenges encourages growth, perseverance, and the ability to overcome obstacles in life.

Challenges : Difficult tasks that test your ability.
Perseverance : Never giving up, even when it’s hard.
Overcome : To deal successfully with a problem.
Obstacles : Things that make progress difficult.
""",
"""Learning about history, culture, and politics of different countries can broaden perspectives and reduce prejudice.

Broaden : To make wider or more open-minded.
Prejudice : An unfair negative opinion about others.
Culture : The customs, art, and lifestyle of people.
Politics : Activities related to government or power.
""",
"""Being open to constructive criticism allows people to improve skills, knowledge, and personal performance over time.

Constructive criticism : Helpful feedback to improve something.
Performance : How well you do something.
Improve : Make something better.
Be open to : Willing to accept something new.
""",
"""Spending time learning practical skills, such as first aid or cooking, is valuable for self-reliance and daily life.

Practical skills : Useful abilities for daily living.
Self-reliance : Depending on yourself, not others.
First aid : Basic help given in an emergency.
Valuable : Very useful or important.
""",
"""Joining debate clubs or discussion groups can improve confidence, critical thinking, and the ability to argue effectively.

Debate : A formal discussion on a topic.
Confidence : Believing in your own ability.
Critical thinking : Thinking carefully and logically.
Argue effectively : To express ideas with strong reasons.
""",
"""Understanding the principles of science and research allows people to make informed decisions and evaluate information critically.

Principles : Basic rules or truths.
Research : Careful study to discover facts.
Informed : Having good knowledge before deciding.
Evaluate : To judge something carefully.
""",
"""Engaging in creative hobbies such as painting, writing, or music helps individuals express emotions and develop talent.

Creative : Using imagination to make something new.
Hobbies : Activities you enjoy in your free time.
Express : To show feelings or ideas.
Talent : A natural ability or skill.
""",
"""Traveling with friends or family strengthens relationships, creates memories, and teaches teamwork and compromise.

Strengthen : To make something stronger.
Relationships : Connections between people.
Teamwork : Working together to achieve a goal.
Compromise : Agreeing by giving up part of what you want.
""",
"""Learning about nutrition and healthy habits helps people maintain energy, focus, and overall physical and mental health.

Nutrition : The process of getting food for health.
Maintain : Keep something in good condition.
Focus : To concentrate attention on something.
Overall : In general, including everything.
""",
"""Understanding environmental issues encourages people to adopt sustainable lifestyles and protect natural resources.

Environmental : Related to nature and surroundings.
Sustainable : Using resources without harming the future.
Protect : To keep something safe from harm.
Resources : Natural materials like water, land, and air.
""",
"""Practicing mindfulness while performing daily tasks can improve focus, reduce stress, and increase satisfaction in life.

Mindfulness : Paying full attention to the present moment.
Performing : Doing or carrying out an activity.
Satisfaction : A feeling of happiness or contentment.
Reduce : To make something smaller or less.
""",
"""Learning to code or understand technology enhances problem-solving skills and opens up opportunities in the digital world.

Code : To write instructions for computers.
Enhance : To improve or make better.
Problem-solving : Finding answers to difficult situations.
Digital world : The world of computers and the internet.
""",
"""Participating in charity events and social work fosters empathy, gratitude, and a sense of responsibility in society.

Charity : Helping people in need.
Empathy : Understanding others’ feelings.
Gratitude : Being thankful for what you have.
Responsibility : Duty to act correctly and help others.
""",
"""Understanding different communication styles helps people interact effectively with diverse personalities and cultures.

Communication styles : Ways people express ideas.
Interact : To communicate or work with others.
Diverse : Showing variety or differences.
Personalities : The character traits of a person.
""",
"""Spending time outdoors and in nature has proven benefits for mental health, creativity, and physical well-being.

Outdoors : Outside, in the open air.
Proven : Shown to be true or effective.
Creativity : The ability to think of new ideas.
Well-being : A state of happiness and good health.
""",
"""Learning time management strategies ensures people can complete important tasks efficiently and have time for relaxation.

Time management : Using your time wisely.
Efficiently : Quickly and effectively.
Tasks : Things that need to be done.
Relaxation : Rest and relief from stress.
""",
"""Engaging in storytelling or creative writing encourages imagination, expression, and critical thinking skills simultaneously.

Storytelling : Sharing stories to entertain or teach.
Imagination : The ability to create ideas in your mind.
Expression : Showing thoughts or emotions.
Simultaneously : Happening at the same time.
""",
"""Studying philosophy and ethics provides insights into human behavior, moral dilemmas, and the basis for decision-making.

Philosophy : The study of ideas about existence and knowledge.
Ethics : Moral principles of right and wrong.
Dilemmas : Difficult choices between two options.
Decision-making : Choosing what to do after thinking.
""",
"""Traveling off the beaten path allows people to explore authentic local culture, develop problem-solving skills, and be adaptable.

Off the beaten path : Away from common or tourist places.
Authentic : Real or genuine.
Adaptable : Able to adjust to new situations.
Explore : To travel and learn new things.
""",
"""Participating in competitions or challenges motivates personal growth, resilience, and determination to succeed.

Competition : A contest or event to test skill.
Resilience : The ability to recover after difficulty.
Determination : Strong will to achieve something.
Motivate : To encourage someone to act.
""",
"""Learning to summarize, paraphrase, and explain complex ideas clearly is crucial for effective communication skills.

Summarize : To give the main points briefly.
Paraphrase : To say something in your own words.
Complex : Difficult or detailed.
Crucial : Very important.
""",
"""Developing a routine for self-improvement, such as reading, writing, or learning new skills, leads to continuous growth.

Routine : A regular pattern of doing things.
Self-improvement : Effort to become better.
Continuous : Going on without stopping.
Growth : The process of developing or improving.
""",
"""Being curious and asking thoughtful questions encourages learning, creativity, and a deeper understanding of the world.

Curious : Wanting to know more about things.
Thoughtful : Showing careful consideration.
Deeper understanding : Knowing something more completely.
Encourage : To give support or confidence to someone.
"""
   
]


sentence = random.choice(sentences)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={"chat_id": CHAT_ID, "text": sentence})
