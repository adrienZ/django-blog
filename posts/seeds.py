import django
django.setup()


from posts.models import Article, Category   # Import the model classes we just wrote.


from django.utils import timezone
a = Article(article_text="Food startups are apparently still steaming hot as French startup Frichti just raised a whopping $33.7 million (€30 million). Frichti is currently available in Paris and nearby cities. It handles everything in-house — from cooking to orders and deliveries. Verlinvest and Felix Capital invested in today’s funding round, with existing investors Alven Capital and Idinvest Partners also participating. I’ve already covered Frichti and everything is still true today. Frichti stands out from the rest of the (crowded) competition with a simple promise — healthy meals with a common signature among all options. In my experience, you know that you’re eating something from Frichti when you compare it to the competition because it tries to be different. Frichti customizes its website depending on the time of the day or week. For instance, on Sunday morning, the startup can help you put together a brunch. The main downside is that if you’ve been ordering Frichti", pub_date=timezone.now())

a.save()

