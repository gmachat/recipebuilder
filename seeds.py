from recipes.models import Recipe, Rating, Comment, UserProfile
from django.contrib.auth.models import User

u1 = User(username="greg123", first_name='Greg', last_name='Machat', email='greg@gmail.com')
u1.set_password('test123123')
u1.save()
up1 = UserProfile(user=u1)
up1.save()

u2 = User(username="adam123", first_name='Adam', last_name='Cucchiara', email='adam@gmail.com')
u2.set_password('test123123')
u2.save()
up2 = UserProfile(user=u2)
up2.save()

u3 = User(username="evan123", first_name='Evan', last_name='Gerry', email='evan@gmail.com')
u3.set_password('test123123')
u3.save()
up3 = UserProfile(user=u3)
up3.save()


r1= Recipe(name="Keto Lamb Kebabs", cook_time=60, prep_time=15, ingredients='{"ingredients":[172617, 1567265, 596984]}', created_by=up1)
r1.save()
r2= Recipe(name="Keto Peanut Butter Chocolate Bars", cook_time=0, prep_time=15, ingredients='{"ingredients":[1552767, 167999, 1734831]}', created_by=up1)
r2.save()
r3= Recipe(name="Raspberry almond salad", cook_time=0, prep_time=15, ingredients='{"ingredients":[1102708, 1577827, 1659707]}', created_by=up3)
r3.save()

rate1 = Rating(user=up1, recipe=r1, rating=5)
rate1.save()
rate2 = Rating(user=up1, recipe=r2, rating=4)
rate2.save()
rate3 = Rating(user=up2, recipe=r2, rating=3)
rate3.save()

c1 = Comment(user=up1, recipe=r1, comment="delicious lamb kebabs! make again!")
c1.save()
c2 = Comment(user=up2, recipe=r1, comment="Just like my neighbor used to make!!")
c2.save()
c3 = Comment(user=up2, recipe=r2, comment="Delicious Peanut buttery trest!")
c3.save()
