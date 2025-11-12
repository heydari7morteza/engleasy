import os
import requests
import random

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# چند جمله نمونه انگلیسی (می‌تونی هر روز اضافه‌اش کنی)
sentences = [
"""What kind of work would you like to do in the future?\n
Career : کریر | شغل یا حرفه
Challenging : چَلِنجینگ | چالش‌برانگیز
Opportunity : آپُرتیونیتی | فرصت
Responsibility : رِسپانسیبیلیتی | مسئولیت
Experience : اِک‌سپِریِنس | تجربه""",

"""Describe a memorable trip you have taken.\n
Memorable : مِمُرِبِل | به یاد ماندنی
Destination : دِستینِیشن | مقصد
Cultural : کَالتچِرال | فرهنگی
Explore : اکسپلُر | کاوش کردن
Unforgettable : آنفُرگِتابِل | فراموش نشدنی""",

"""What kind of movies do you like to watch?\n
Genre : ژانر | نوع یا سبک
Suspense : سَسپِنس | تعلیق
Thrilling : ثرِلینگ | هیجان‌انگیز
Plot : پلات | داستان فیلم
Character : کَریکتر | شخصیت""",

"""How do you celebrate your birthday?\n
Tradition : تِرَدیشن | سنت یا رسم
Ceremony : سِرِمُنی | مراسم
Festive : فِستِیو | شاد و جشن‌گونه
Gathering : گَذِرینگ | گردهمایی
Memorable : مِمُرِبِل | به یاد ماندنی""",

"""Describe a piece of technology you find useful.\n
Innovative : اینوِیتِیو | نوآورانه
Device : دیوایس | دستگاه
Convenient : کِنوی‌نینت | راحت و مناسب
Efficient : اِفیشِنت | کارآمد
Function : فَنکشن | عملکرد""",

"""What kind of music do you like to listen to?\n
Instrumental : اینسترومِنتَل | بدون کلام
Melody : مِلُدی | ملودی
Rhythm : رِذم | ریتم
Genre : ژانر | نوع یا سبک
Lyrics : لیرِکس | متن آهنگ""",

"""Describe a hobby you enjoy in your free time.\n
Creative : کریِیتیو | خلاقانه
Relaxing : رِلَکسینگ | آرامش‌بخش
Skillful : اسکِل‌فول | ماهرانه
Social : سوشِل | اجتماعی
Engaging : اِنگِیجینگ | جذاب و سرگرم‌کننده""",

"""What kind of environment do you prefer to live in?\n
Urban : اُربن | شهری
Rural : رُرال | روستایی
Peaceful : پِیسفول | آرام
Pollution : پُلُوشِن | آلودگی
Community : کَم‌یونیتی | اجتماع""",

"""Describe a person you admire.\n
Inspiring : اینس‌پایرینگ | الهام‌بخش
Achievement : اَچِیومِنت | دستاورد
Personality : پِرسِنالیتی | شخصیت
Role model : رُول مَدِل | الگو
Dedication : دِدِکِیشن | تعهد""",

"""How do you usually spend your holidays?\n
Adventure : اَدفِنتچِر | ماجراجویی
Destination : دِستینِیشن | مقصد
Relaxation : رِلَکسیِیشن | استراحت
Excursion : اکسکِرشِن | گردش
Cultural : کَالتچِرال | فرهنگی""",

"""What kind of food do you enjoy?\n
Cuisine : کوئیزین | نوع غذا
Delicious : دِلِشِس | خوشمزه
Traditional : تِرَدِیشنال | سنتی
Flavor : فلیوِر | طعم
Ingredients : اینگریدیِنتس | مواد اولیه""",

"""Describe a festival you like.\n
Celebration : سِلِبریشن | جشن
Atmosphere : آتْموسفِر | جو و فضای محیط
Custom : کَستَم | رسم
Performance : پِرفُرمنس | اجرا
Memorable : مِمُرِبِل | به یاد ماندنی""",

"""What kind of sports do you enjoy?\n
Competitive : کُمپِتیتِیو | رقابتی
Endurance : اِندُرَنس | استقامت
Teamwork : تیم‌وُرک | کار تیمی
Strategy : استراتِجی | استراتژی
Physical : فیزیکال | جسمی""",

"""Describe a memorable childhood experience.\n
Nostalgic : نَستالجیک | نوستالژیک
Experience : اِک‌سپِریِنس | تجربه
Playful : پِلِیفول | بازیگوشانه
Memorable : مِمُرِبِل | به یاد ماندنی
Adventure : اَدفِنتچِر | ماجراجویی""",

"""What kind of books do you like to read?\n
Genre : ژانر | نوع یا سبک
Fiction : فیکشن | داستانی
Non-fiction : نان-فیکشن | غیر داستانی
Inspiring : اینس‌پایرینگ | الهام‌بخش
Recommend : رِکُمِند | توصیه کردن""",

"""How do you usually travel?\n
Transportation : ترَنسپُرتِیشن | وسیله نقلیه
Convenient : کِنوی‌نینت | راحت و مناسب
Efficient : اِفیشِنت | کارآمد
Journey : جِرنی | سفر
Destination : دِستینِیشن | مقصد""",

"""Describe a skill you want to learn.\n
Technical : تِکنیکال | فنی
Challenging : چَلِنجینگ | چالش‌برانگیز
Practical : پِرَکتیکال | عملی
Development : دِوِلاپمِنت | پیشرفت
Master : مَستِر | استاد شدن""",

"""What kind of movies do you dislike?\n
Horror : هُرر | ترسناک
Boring : بُورینگ | خسته‌کننده
Predictable : پِردیکتیبِل | قابل پیش‌بینی
Violent : وایُلِنت | خشونت‌آمیز
Annoying : اَناوینگ | آزاردهنده""",

"""Describe a city you have visited.\n
Landmark : لَندمارک | نماد شهر
Tourist : تُریست | گردشگر
Historic : هِستُریک | تاریخی
Cultural : کَالتچِرال | فرهنگی
Memorable : مِمُرِبِل | به یاد ماندنی""",

"""How do you stay healthy?\n
Nutrition : نوتریشِن | تغذیه
Exercise : اکسِر‌سایز | ورزش
Lifestyle : لایف‌استایل | سبک زندگی
Hygiene : هایجین | بهداشت
Routine : روتین | عادت روزانه""",

"""Describe a place you would like to live.\n
Scenic : سِنییک | خوش منظره
Peaceful : پِیسفول | آرام
Community : کَم‌یونیتی | اجتماع
Environment : اِنوایرِنمِنت | محیط
Convenient : کِنوی‌نینت | راحت و مناسب""",

"""What kind of volunteer work would you like to do?\n
Community : کَم‌یونیتی | اجتماع
Charity : چَریتی | کار خیر
Commitment : کَمِت‌مِنت | تعهد
Contribution : کُنترِبیوشِن | مشارکت
Impact : ایمپَکت | تأثیر""",

"""Describe a meal you recently enjoyed.\n
Delicious : دِلِشِس | خوشمزه
Savory : سِیوِری | خوش طعم
Ingredients : اینگریدیِنتس | مواد اولیه
Cuisine : کوئیزین | نوع غذا
Flavorful : فلیوِرفول | پر طعم""",

"""What kind of pets do you like?\n
Companion : کَمپَنیون | همراه و همدم
Behavior : بِهِیویِر | رفتار
Training : ترینینگ | آموزش
Responsible : رِسپانسیبِل | مسئول
Affectionate : اَفِکشنِیت | مهربان و دوست داشتنی""",

"""Describe a memorable school event.\n
Ceremony : سِرِمُنی | مراسم
Achievement : اَچِیومِنت | دستاورد
Performance : پِرفُرمنس | اجرا
Celebration : سِلِبریشن | جشن
Outstanding : آوت‌ستَندینگ | برجسته و عالی""",

"""What kind of weather do you prefer?\n
Forecast : فُورکَست | پیش‌بینی
Climate : کِلایمِت | اقلیم
Humidity : هیومیدیتی | رطوبت
Temperature : تِمپِرِچِر | دما
Conditions : کُندیشنز | شرایط""",

"""Describe a useful app on your phone.\n
Application : اَپلیکِیشِن | برنامه کاربردی
Feature : فیتِچِر | ویژگی
Convenient : کِنوی‌نینت | راحت و مناسب
Interface : اینتِرفِیس | رابط کاربری
Update : آپدِیت | به‌روزرسانی""",

"""What kind of clothing do you prefer?\n
Fashionable : فَشِنِیبِل | مد روز
Comfortable : کَمفُرتِیبِل | راحت
Material : مَتِریال | جنس
Style : استایل | سبک
Occasion : اُکیژِن | مناسبت""",

"""Describe a book you recently read.\n
Plot : پلات | داستان
Fiction : فیکشن | داستانی
Character : کَریکتر | شخصیت
Theme : ثیم | موضوع اصلی
Inspiring : اینس‌پایرینگ | الهام‌بخش""",

"""What kind of exercise do you do?\n
Endurance : اِندُرَنس | استقامت
Strength : سترَنگث | قدرت
Flexibility : فِلِکسِبیلیتی | انعطاف‌پذیری
Routine : روتین | برنامه روزانه
Motivation : ماتیوِیشِن | انگیزه""",

"""Describe a traditional event in your country.\n
Cultural : کَالتچِرال | فرهنگی
Ritual : ریتوال | آیین
Custom : کَستَم | رسم
Heritage : هِریتیج | میراث
Celebration : سِلِبریشن | جشن""",

"""What kind of transport do you prefer?\n
Vehicle : وِهِیکِل | وسیله نقلیه
Journey : جِرنی | سفر
Commute : کَم‌یوت | رفت و آمد
Convenient : کِنوی‌نینت | راحت
Efficient : اِفیشِنت | کارآمد""",

"""Describe a challenge you have faced.\n
Obstacle : اُبستِکل | مانع
Overcome : اُوِرکَم | غلبه کردن
Difficult : دیفِکالت | سخت
Solution : سُلُوشِن | راه حل
Experience : اِک‌سپِریِنس | تجربه""",

"""What kind of shops do you like?\n
Boutique : بوتیک | فروشگاه کوچک و خاص
Variety : وَرایِتی | تنوع
Customer : کَستُمِر | مشتری
Quality : کوالیتی | کیفیت
Purchase : پِرچِیس | خرید""",

"""Describe a famous landmark you have visited.\n
Monument : مانیومِنت | بنای تاریخی
Historic : هِستُریک | تاریخی
Tourist : تُریست | گردشگر
Architecture : آرتِکتِکچِر | معماری
Impressive : ایمپِرِسیو | باشکوه""",

"""What kind of news do you follow?\n
Headline : هِدلاین | تیتر
Report : رِپورت | گزارش
Current : کِرِنت | جاری، فعلی
Reliable : رِلایِبل | قابل اعتماد
Update : آپدِیت | به‌روزرسانی""",

"""Describe a favorite place in your city.\n
Scenic : سِنییک | خوش منظره
Relaxing : رِلَکسینگ | آرامش‌بخش
Atmosphere : آتْموسفِر | جو محیط
Crowded : کرَودِد | شلوغ
Accessible : اَکسِسِیبِل | در دسترس""",

"""What kind of shows do you like?\n
Entertaining : اَنتِرتِینینگ | سرگرم‌کننده
Performance : پِرفُرمنس | اجرا
Audience : آدینس | تماشاگر
Genre : ژانر | نوع یا سبک
Exciting : اکسایتینگ | هیجان‌انگیز""",

"""Describe a historical figure you admire.\n
Influential : اینفلوئِنشِل | تاثیرگذار
Leader : لیدِر | رهبر
Achievement : اَچِیومِنت | دستاورد
Legacy : لِگِسی | میراث
Inspiring : اینس‌پایرینگ | الهام‌بخش""",

"""What kind of restaurants do you like?\n
Cuisine : کوئیزین | نوع غذا
Ambiance : اَمبیِنس | فضای محیط
Service : سِرویس | خدمات
Atmosphere : آتْموسفِر | جو محیط
Specialty : اسپِشِلتی | تخصص""",

"""What kind of outdoor activities do you enjoy?\n
Adventure : اَدفِنتچِر | ماجراجویی
Exploration : اِک‌سپلُرِیشِن | کاوش
Challenge : چَلِنج | چالش
Endurance : اِندُرَنس | استقامت
Scenery : سِنیری | منظره""",

"""How do you celebrate important festivals in your country?\n
Tradition : تِرَدیشن | رسم و سنت
Ceremony : سِرِمُنی | مراسم
Cultural : کَالتچِرال | فرهنگی
Custom : کَستَم | رسم
Event : اِوِنت | رویداد""",

"""What kind of social events do you like to attend?\n
Networking : نِت‌وُرکینگ | ارتباط برقرار کردن
Interaction : اینتِرَکشن | تعامل
Participation : پَرتیسِپِیشن | شرکت
Community : کَم‌یونیتی | اجتماع
Occasion : اُکیژِن | مناسبت""",

"""How do you usually spend a day off?\n
Relaxation : رِلَکسیِیشن | استراحت
Activity : اَکتیویتی | فعالیت
Leisure : لِژِر | وقت آزاد
Entertainment : اَنتِرتِینمنت | سرگرمی
Hobby : هابی | سرگرمی""",

"""What kind of challenges do you face at school or work?\n
Obstacle : اُبستِکل | مانع
Difficulty : دیفِکالت | سختی
Solution : سُلُوشِن | راه حل
Problem-solving : پِرابلم-سولوینگ | حل مسئله
Achievement : اَچِیومِنت | دستاورد""",

"""How do you spend your evenings at home?\n
Routine : روتین | برنامه روزانه
Relaxing : رِلَکسینگ | آرامش‌بخش
Engaging : اِنگِیجینگ | سرگرم‌کننده
Activity : اَکتیویتی | فعالیت
Comfortable : کَمفُرتِیبِل | راحت""",

"""What kind of places do you like to visit?\n
Scenic : سِنییک | خوش منظره
Historic : هِستُریک | تاریخی
Cultural : کَالتچِرال | فرهنگی
Attraction : اَتراکشن | جاذبه
Popular : پاپیولَر | محبوب""",

"""How do you prepare for exams or tests?\n
Revision : رِویژن | مرور
Strategy : استراتِجی | روش  
Concentration : کانسِنتریشن | تمرکز
Understanding : اَندرستَندینگ | درک
Effort : اِفِرت | تلاش""",

"""What kind of games do you enjoy playing?\n
Competitive : کُمپِتیتِیو | رقابتی
Strategy : استراتِجی | استراتژی
Teamwork : تیم‌وُرک | کار تیمی
Skill : اسکِل | مهارت
Challenge : چَلِنج | چالش""",

"""How do you usually spend time with your friends?\n
Socialize : سوشِلايز | معاشرت کردن
Conversation : کانوِرسِیشن | گفتگو
Activity : اَکتیویتی | فعالیت
Support : ساپُرت | حمایت
Engagement : اِنگِیجمنت | مشارکت""",

"""What kind of TV shows do you prefer?\n
Entertainment : اَنتِرتِینمنت | سرگرمی
Informative : اینفُرمِیتیو | آموزنده
Series : سیرِیز | مجموعه
Episode : اِپیسود | قسمت
Genre : ژانر | نوع یا سبک""",

"""How do you usually travel to school or work?\n
Transportation : ترَنسپُرتِیشن | وسیله نقلیه
Commute : کَم‌یوت | رفت و آمد
Efficient : اِفیشِنت | کارآمد
Route : رُوت | مسیر
Traffic : ترافیک | ترافیک""",

"""What kind of books are popular among young people?\n
Fiction : فیکشن | داستانی
Thriller : ثرِلِر | هیجان‌انگیز
Genre : ژانر | نوع یا سبک
Inspiring : اینس‌پایرینگ | الهام‌بخش
Bestseller : بِست‌سِللِر | پرفروش""",

"""How do you usually spend time online?\n
Browsing : بروزینگ | جستجو
Social media : سوشِل میدیا | شبکه‌های اجتماعی
Communication : کُم‌یونیکِیشن | ارتباط
Entertainment : اَنتِرتِینمنت | سرگرمی
Content : کانتِنت | محتوا""",

"""What kind of clothes do you usually wear?\n
Fashionable : فَشِنِیبِل | مد روز
Comfortable : کَمفُرتِیبِل | راحت
Material : مَتِریال | جنس
Occasion : اُکیژِن | مناسبت
Style : استایل | سبک""",

"""How do you usually celebrate achievements?\n
Recognition : رِکِگنیشن | قدردانی  
Achievement : اَچِیومِنت | دستاورد  
Reward : رِوارد | جایزه  
Ceremony : سِرِمُنی | مراسم  
Appreciation : اَپریشِیشن | تقدیر""",

"""What kind of restaurants do you like to visit?\n
Cuisine : کوئیزین | نوع غذا
Ambiance : اَمبیِنس | فضای محیط
Service : سِرویس | خدمات
Specialty : اسپِشِلتی | تخصص
Atmosphere : آتْموسفِر | جو محیط""",

"""How do you usually spend your free weekends?\n
Leisure : لِژِر | وقت آزاد
Activity : اَکتیویتی | فعالیت
Relaxation : رِلَکسیِیشن | استراحت
Engagement : اِنگِیجمنت | مشارکت
Entertainment : اَنتِرتِینمنت | سرگرمی""",

"""What kind of cultural events do you attend?\n
Exhibition : اِگزیبیشن | نمایشگاه
Performance : پِرفُرمنس | اجرا
Festival : فِستِیوِل | جشنواره
Tradition : تِرَدیشن | رسم و سنت
Audience : آدینس | تماشاگر""",

"""How do you usually spend your lunch breaks?\n
Relaxation : رِلَکسیِیشن | استراحت
Conversation : کانوِرسِیشن | گفتگو
Meal : میل | وعده غذایی
Activity : اَکتیویتی | فعالیت
Engagement : اِنگِیجمنت | مشارکت""",


]


sentence = random.choice(sentences)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={"chat_id": CHAT_ID, "text": sentence})
