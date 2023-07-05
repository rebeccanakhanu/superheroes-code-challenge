import random
from models import db, Hero, Power, hero_powers

print("🦸‍♀️ Seeding powers...")
Power.create([
  { 'name': "super strength", 'description': "gives the wielder super-human strengths" },
  { 'name': "flight", 'description': "gives the wielder the ability to fly through the skies at supersonic speed" },
  { 'name': "super human senses", 'description': "allows the wielder to use her senses at a super-human level" },
  { 'name': "elasticity", 'description': "can stretch the human body to extreme lengths" }
])

print("🦸‍♀️ Seeding heroes...")
Hero.create([
  { 'name': "Kamala Khan", 'super_name': "Ms. Marvel" },
  { 'name': "Doreen Green", 'super_name': "Squirrel Girl" },
  { 'name': "Gwen Stacy", 'super_name': "Spider-Gwen" },
  { 'name': "Janet Van Dyne", 'super_name': "The Wasp" },
  { 'name': "Wanda Maximoff", 'super_name': "Scarlet Witch" },
  { 'name': "Carol Danvers", 'super_name': "Captain Marvel" },
  { 'name': "Jean Grey", 'super_name': "Dark Phoenix" },
  { 'name': "Ororo Munroe", 'super_name': "Storm" },
  { 'name': "Kitty Pryde", 'super_name': "Shadowcat" },
  { 'name': "Elektra Natchios", 'super_name': "Elektra" }
])

print("🦸‍♀️ Adding powers to heroes...")

strengths = ["Strong", "Weak", "Average"]
heroes = Hero.query.all()
for hero in heroes:
  for _ in range(random.randint(1, 3)):
    # get a random power
    power = Power.query.order_by(random.random()).first()

    hero_power = hero_powers(hero_id=hero.id, power_id=power.id, strength=random.choice(strengths))
    hero_power.save()
    
print("🦸‍♀️ Done seeding!")
