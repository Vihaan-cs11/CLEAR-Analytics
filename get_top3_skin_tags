from tkinter import *
from main import Routine_Checkins, Tags, session, engine, Products, User_Tags
from numpy import concatenate
from statistics import mode


#READ_ME PLEASE
#NOTE: the input type is the string value name of the product on the Clear db
#NOTE: the output type is two lists, one contains the top 3 tags + 'other' in order
#NOTE: the other lists contains the percentage of the tags that use the products in the same order

#NOTE: get_top_3(get_tag_ids(get_users_of_product(get_product_id('NAME OF PRODUCT')))) --> this gives the names
#NOTE: get_perc(get_tag_ids(get_users_of_product(get_product_id('NAME OF PRODUCT')))) --> this gives the percentages



local_session = session(bind = engine)

#here the first step is to find the product_id
#this will be found from the products table
def get_product_id(product_name):
    find_product = local_session.query(Products).filter(Products.product_name == product_name).first()
    product_id = find_product.id
    print(product_id)
    return product_id

#we are creating a function that get all of the users of a productthrough their routine
#which takes in an int parameter which is the product id

def get_users_of_product(product_id):
    str_id = str(product_id)
    str_id = str('%'+str_id+'%')
    #logic -> find occurances of the product used in routine table
    #since the type of products_id in the routine table is of type array
    #we will retrieve each of the indecies of the product_ids
    #but in our local database, it is of type string. So each string is reprasentative of each index
    users_of_product = local_session.query(Routine_Checkins.author_id).filter(Routine_Checkins.products_id.like(str_id)).all()
    #It is in this format 01 02 03 -> is one string containing the product ids, 
    #now we can
    returned_users = []
    for user in users_of_product:
        #here in the returned set, we need to remove "(" and ")" and ","
        #which is why we convert this from an int type to string
        user = str(user)
        user = user.replace('(','').replace(')','').replace(',','')
        user = int(user)
        returned_users.append(user)
        #in the end we needed to convert it back to the int type

    #now we need to check if the product_id is in any of these strings
    print(returned_users)
    return returned_users
    #we return an array of type int


#we have gotten the list of user_ids that use these products, and this is weighted
def get_tag_ids(user_id_list):
    tags_id=[]
    for i in range(len(user_id_list)):
        tags = local_session.query(User_Tags.tags_id).filter(User_Tags.user_id == user_id_list[i]).all()
        tags_id.append(tags)

    all_tags = list(concatenate(tags_id).flat)
    print(all_tags)
    return all_tags


def get_top_3(tags_list):
    new_list = tags_list
    ids_of_top3 = []
    name_of_top3 = []


    for i in range(3):
        #add the mode
        tag_id = mode(new_list)
        ids_of_top3.append(tag_id)
        #now we need to deleted the mode we just got
        count = new_list.count(tag_id)
        for j in range(count):
            new_list.remove(tag_id)
        
        print('WE ARE LOOKING FOR THIS TAG:',tag_id)
        tag_id = int(tag_id)
        tag_name = local_session.query(Tags.tag).filter(Tags.id == tag_id).first()
        tag_name = str(tag_name)
        tag_name = tag_name.replace('(','').replace(',','').replace("'",'').replace(')','')
        name_of_top3.append(tag_name)
    
    name_of_top3.append('Other')
    #this prints the 3 tags + "Other"

    print(ids_of_top3)
    print(name_of_top3)
    #then we can have another function to print the 3 tags
    return(name_of_top3)

def get_perc(tags_list):
    new_list = tags_list.copy()
    perc_of_top3 = []

    other = 100.0
    for i in range(3):
        #add the mode
        tag_id = mode(new_list)
        #now we need to deleted the mode we just got
        num_count = new_list.count(tag_id)
        for j in range(num_count):
            new_list.remove(tag_id)
        
        perc = (float(num_count)/float(len(tags_list))) * 100.0
        perc_of_top3.append(round(perc,2))
        other = other -perc

    perc_of_top3.append(round(other,2))
    return(perc_of_top3)


#the end result will be a returned list of the top 3 tags + an others section
#and another list with the respective percentages of the top 3 tags + the % of others

root = Tk()
hi = Label(root, text = "Find the top 3 tags for a product on Clear!")
hi.pack()
prod = Entry(root, width = 50)
prod.pack()
def click():
    top = get_top_3(get_tag_ids(get_users_of_product(get_product_id(prod.get()))))
    top = str(top)
    perc = get_perc(get_tag_ids(get_users_of_product(get_product_id(prod.get()))))
    perc = str(perc)

    lab = Label(root, text= "Top 3 Tags: " +top)
    lab1 = Label(root, text="Percentage of usage: "+perc)
    lab.pack()
    lab1.pack()
btnFind = Button(root, text = 'Find Tags', command=click)
btnFind.pack()
root.mainloop()
