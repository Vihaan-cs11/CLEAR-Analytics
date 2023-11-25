from main import Routine_Checkins, User_Tags, Users, session, engine, Products, Tags, Brands

local_session = session(bind=engine)
u1 = Users(username = "vm", email = "vm@gmail.com")
u2 = Users(username = "adk", email = "adk@gmail.com")
u3 = Users(username = "ss", email = "ss@gmail.com")

t1 = Tags(tag = 'Dry')
t2 = Tags(tag = 'Oily')
t3 = Tags(tag = 'Acne')
t4 = Tags(tag = 'Acne Scars')
t5 = Tags(tag = 'Dehydrated')
t6 = Tags(tag = 'Sensitive')
t7 = Tags(tag = 'Eczema')
t8 = Tags(tag = 'Dark circles')

ut1 = User_Tags(user_id = 1, tags_id = 1)
ut2 = User_Tags(user_id = 1, tags_id = 3)
ut3 = User_Tags(user_id = 1, tags_id = 5)
ut4 = User_Tags(user_id = 2, tags_id = 4)
ut5 = User_Tags(user_id = 2, tags_id = 5)
ut6 = User_Tags(user_id = 3, tags_id =2)
ut7 = User_Tags(user_id = 3, tags_id = 1)
ut8 = User_Tags(user_id = 3, tags_id = 5)

rc1 = Routine_Checkins(author_id=1, products_id = "1 2")
rc2 = Routine_Checkins(author_id=1, products_id = "1 3")
rc3 = Routine_Checkins(author_id=1, products_id = "1 2")
rc4 = Routine_Checkins(author_id=2, products_id = "2 4")
rc5 = Routine_Checkins(author_id=2, products_id = "3 4")
rc6 = Routine_Checkins(author_id=3, products_id = "1 2 4")

p1 = Products(products_name = 'Extraordinary Facial Oil', brand_id = 1)
p2 = Products(products_name = 'Fine Flowers Cleansing Toner', brand_id = 1)
p3 = Products(products_name = 'Hydro Boost Express Hydrating Spray', brand_id = 2)
p4 = Products(products_name = 'Clear & Soothe Moisturiser', brand_id = 2)

b1 = Brands(name = "L'Oreal Paris")
b2 = Brands(name = "Neutrogena")



local_session.add_all([u1, u2, u3, t1, t2, t3, t4, t5, t6, t7, t8])
local_session.add_all([ut1,ut2,ut3,ut4,ut5,ut6,ut7,ut8])
local_session.add_all([rc1,rc2,rc3,rc4,rc5,rc6])
local_session.add_all([p1,p2,p3,p4])
local_session.add_all([b1,b2])

local_session.commit()
