from main import Routine_Checkins, session, engine, Products, Users

local_session = session(bind = engine)

#first step is to get the userid from their username
def get_userid(username):
    userid = local_session.query(Users.id).filter(Users.user_name == username).first()
    #since the return type of a query is a list of tuples, we need to get it into the int format
    userid = str(userid).replace('(','').replace(')','').replace(',','')
    userid = int(userid)
    print(userid)
    return(userid)

#the userid is in type int, we can use this to access their routine_checkins
def get_user_products(userid):
    prods = local_session.query(Routine_Checkins.products_id).filter(Routine_Checkins.author_id == userid).all()
    users_routine_products = []
    
    for prod in prods:
        prod = str(prod)
        prod = prod.replace("'",'').replace("(",'').replace(")","").replace(",",'')
        users_routine_products.append(prod)
    print(users_routine_products)

    #we can also count the number of routines as well using the count keyword
    #we can count the total number of products
            

#Testing with username "vm"        
get_user_products(get_userid("vm"))
