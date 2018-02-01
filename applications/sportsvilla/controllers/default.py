# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
from gluon import current
import datetime


def check_membership():
    if auth.has_membership(role='Admin'):
        redirect(URL('admin','index'))
    return True

@auth.requires_login()
@auth.requires(check_membership)
#@auth.requires(auth.has_membership(role='End User'))
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    current_user_database = None
    if auth.user.id:
        current_user = auth.user.id
        current_user_database = db(db.auth_user.id==current_user).select(db.auth_user.ALL)[0]
    current_stored_type = None
    if request.vars.selected_type:
        current_stored_type = request.vars['selected_type']
        session.stored_type = request.vars['selected_type']
    elif session.stored_type:
        current_stored_type = session.stored_type;
    select_type = FORM(LABEL('Sports Apparels',INPUT(_type='radio',_id='selectapparel',_name='selected_type',_autocomplete='on',_value='sport-apparel',value=current_stored_type),_class='btn btn-info'),LABEL('Sports Goods',INPUT(_type='radio',_id='selectgood',_name='selected_type',_autocomplete='on',_value='sport-good',value = current_stored_type),_class='btn btn-primary'),_class='btn-group',_data={'toggle':'buttons'},_id='type-form',_autocomplete='on' ,_onchange="this.form.submit()")
    
    apparel_item_database = db(db.ProductAppList2.ParentType == 2).select(db.ProductAppList2.ItemType,distinct=True)
    goods_sport_database= db(db.ProductGoodsList2.ParentType == 1). select(db.ProductGoodsList2.ParentSport,distinct=True)
    return dict(apparel_item_database=apparel_item_database,
                current_stored_type=current_stored_type,
                select_type=select_type,
                goods_sport_database=goods_sport_database,
                current_user_database = current_user_database
                )

#Function to show list of all selected apparels after search
@auth.requires_login()
#@auth.requires(auth.has_membership(role='End User'))
def show_apparel_list():
    selected_products_database_apparel = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.Material == request.vars['apparel_material']) & (db.ProductAppList2.ItemType == request.vars['apparel_item'])).select(db.ProductAppList2.ALL)
    selected_product_list_apparel = DIV(DIV(_id='happy'),*[A(DIV(IMG(_src=URL('download',args=rows.Image),_alt='Card image cap',_id='product-img',_align='center',_height = '150px'),DIV(BR(),P(rows.Name,BR(),B('₹ ',rows.Price),_class='card-text'),_class='card-block'),_class='card',_id='product-card',_name='card1',value = rows.Name) ,_href=URL('show_selected_product',args=rows.id),cid='hope') for rows in selected_products_database_apparel],_id = 'style-2')
    return selected_product_list_apparel

#Function to show list of all selected goods after search
@auth.requires_login()
#@auth.requires(auth.has_membership(role='End User'))
def show_goods_list():
    selected_products_database_goods = db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods_sport']) & (db.ProductGoodsList2.ItemType == request.vars['goods_item']) & (db.ProductGoodsList2.Brand == request.vars['goods_brand'])).select(db.ProductGoodsList2.ALL)
    selected_product_list_goods =  DIV(DIV(_id='happy'),*[A(DIV(IMG(_src=URL('download',args=rows.Image),_alt='Card image cap',_id='product-img',_align='center',_height = '150px'),DIV(BR(),P(rows.ItemName,BR(),B('₹ ',rows.Price),_class='card-text'),_class='card-block'),_class='card',_id='product-card',_name='card1',value = rows.ItemName) ,_href=URL('show_selected_goods',args=rows.id),cid='hope') for rows in selected_products_database_goods],_id = 'style-2')
    return selected_product_list_goods

#Function to show details of apparel selected in section 3
@auth.requires_login()
#@auth.requires(auth.has_membership(role='End User'))
def show_selected_product():
    item_displayed_apparel = db(db.ProductAppList2.id == request.args(0)).select()
    return dict(item_displayed_apparel = item_displayed_apparel)

#Function to show details of goods selected in section 3
@auth.requires_login()
#@auth.requires(auth.has_membership(role='End User'))
def show_selected_goods():
    item_displayed_goods = db(db.ProductGoodsList2.id == request.args(0)).select()
    return dict(item_displayed_goods = item_displayed_goods)

@auth.requires_login()
#@auth.requires(auth.has_membership(role='End User'))
def update_apparel_material_list():
    apparel_material_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel_item'])).select(db.ProductAppList2.Material,distinct=True)
    result = "<option selected hidden>Select Material</option>"
    for rows in apparel_material_database:
        result += "<option value='" + rows.Material + "'>" + rows.Material + "</option>"  
    return XML(result)

@auth.requires_login()
#@auth.requires(auth.has_membership(role='End User'))
def update_goods_item_list():
    goods_item_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods_sport'])).select(db.ProductGoodsList2.ItemType, distinct= True)
    result = "<option selected hidden>Select Item</option>"
    for rows in goods_item_database:
        result += "<option value='" + rows.ItemType + "'>" + rows.ItemType + "</option>"  
    return XML(result)

@auth.requires_login()
#@auth.requires(auth.has_membership(role='End User'))
def update_goods_brand_list():
    goods_brand_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods_sport']) & (db.ProductGoodsList2.ItemType == request.vars['goods_item'])).select(db.ProductGoodsList2.Brand,distinct = True)
    result = "<option selected hidden>Select Brand</option>"
    for rows in goods_brand_database:
        result += "<option value='" + rows.Brand + "'>" + rows.Brand + "</option>"  
    return XML(result)

@auth.requires_login()
def checkout():
    if auth.user.id:
        current_user = auth.user.id
        current_user_database = db(db.auth_user.id==current_user).select(db.auth_user.ALL)[0]
    user_order_database = db((db.Orders.UserID == auth.user.id) & (db.Orders.Status == "Pending")).select(db.Orders.ALL).first()
    if user_order_database != None and len(user_order_database.ProductID) == 0:
        user_order_database.delete_record()
        user_order_database = None
    new_product_id_list = []
    new_product_qty_list = []
    new_product_cat_list = []
    new_product_name_list = []
    new_total_price = 0
    if user_order_database != None:
        for row,row2,row3,row4 in zip(user_order_database.ProductID,user_order_database.ProductName,user_order_database.ProductCat,user_order_database.ProductQty):
            if row3 =="Sports Apparel":
                product_apparel_database = db(db.ProductAppList2.id == row).select(db.ProductAppList2.ALL).first()
                if product_apparel_database != None:
                    new_product_id_list.append(row)
                    new_product_name_list.append(row2)
                    new_product_cat_list.append(row3)
                    new_quantity = int(row4)
                    new_product_qty_list.append(new_quantity)
                    new_total_price = new_total_price + (float(product_apparel_database.Price) * float(new_quantity)) + ((float(product_apparel_database.Tax)/100) * (float(product_apparel_database.Price) * float(new_quantity)))
            elif row3 == "Sports Goods":
                product_goods_database = db(db.ProductGoodsList2.id == row).select(db.ProductGoodsList2.ALL).first()
                if product_goods_database != None:
                    new_product_id_list.append(row)
                    new_product_name_list.append(row2)
                    new_product_cat_list.append(row3)
                    new_quantity = int(row4)
                    new_product_qty_list.append(new_quantity)
                    new_total_price = new_total_price + (float(product_goods_database.Price) * float(new_quantity)) + ((float(product_goods_database.Tax)/100) * (float(product_goods_database.Price) * float(new_quantity)))
        user_order_database.update_record(ProductID = list(new_product_id_list),
                                     ProductName = list(new_product_name_list),
                                     ProductCat = list(new_product_cat_list),
                                     ProductQty = list(new_product_qty_list),
                                     TotalPrice = new_total_price)    
    return dict(current_user_database = current_user_database,
               user_order_database = user_order_database,
               request = request)

@auth.requires_login()
def add_goods_cart():
    if auth.user.id:
        user_order_database = db((db.Orders.UserID == auth.user.id) & (db.Orders.Status == "Pending")).select(db.Orders.ALL).first()
        if user_order_database == None:
                product_goods_database = db(db.ProductGoodsList2.id == request.vars['product-id']).select(db.ProductGoodsList2.ALL).first()
                db_product_id_list = []
                db_product_name_list = []
                db_product_cat_list = []
                db_product_qty_list = []
                db_product_id_list.append(product_goods_database.id)
                db_product_name_list.append(product_goods_database.ItemName)
                db_product_cat_list.append("Sports Goods")
                db_product_qty_list.append(int(request.vars['product-qty']))
                db_total_price = (float(product_goods_database.Price) * float(request.vars['product-qty'])) + ((float(product_goods_database.Tax)/100)* (float(product_goods_database.Price) * float(request.vars['product-qty'])))
                #db_total_price =int(db_total_price)
                product_quantity = product_goods_database.Quantity - int(request.vars['product-qty'])
                #product_goods_database.update_record(Quantity = product_quantity)
                db.Orders.insert(UserID = auth.user.id,
                                 ProductID = list(db_product_id_list),
                                 ProductName = list(db_product_name_list),
                                 ProductCat = list(db_product_cat_list),
                                 ProductQty = list(db_product_qty_list),
                                 TotalPrice = db_total_price,
                                 Status = "Pending")
                return DIV(SCRIPT('alert("Successfully Added To Cart");', _type='text/javascript'))
        elif user_order_database != None:
                product_goods_database = db(db.ProductGoodsList2.id == request.vars['product-id']).select(db.ProductGoodsList2.ALL).first()
                db_product_id_list = list(user_order_database.ProductID)
                db_product_name_list = list(user_order_database.ProductName)
                db_product_cat_list = list(user_order_database.ProductCat)
                db_product_qty_list = list(user_order_database.ProductQty)
                db_total_price = user_order_database.TotalPrice
                id_exists = 0
                flag = 0
                for i in range(len(db_product_id_list)):
                    if (db_product_id_list[i] == request.vars['product-id']) and (db_product_cat_list[i] == "Sports Goods"):
                        id_exists = i
                        flag = 1
                if flag == 0:
                    db_product_id_list.append(product_goods_database.id)
                    db_product_name_list.append(product_goods_database.ItemName)
                    db_product_cat_list.append("Sports Goods")
                    db_product_qty_list.append(int(request.vars['product-qty']))
                    db_total_price = float(user_order_database.TotalPrice) + (float(product_goods_database.Price) * float(request.vars['product-qty'])) + ((float(product_goods_database.Tax)/100)* (float(product_goods_database.Price) * float(request.vars['product-qty'])))
                    #db_total_price =int(db_total_price)
                    product_quantity = product_goods_database.Quantity - int(request.vars['product-qty'])
                    #product_goods_database.update_record(Quantity = product_quantity)
                    row1 = db((db.Orders.UserID == auth.user.id) & (db.Orders.Status == "Pending")).select().first()
                    row1.update_record(ProductID = list(db_product_id_list),
                                     ProductName = list(db_product_name_list),
                                     ProductCat = list(db_product_cat_list),
                                     ProductQty = list(db_product_qty_list),
                                     TotalPrice = db_total_price)
                    return SCRIPT('alert("Successfully Added To Cart");', _type='text/javascript')
                elif flag == 1:
                    return SCRIPT('alert("Item Already Exists in the Cart. To alter units please visit cart and make changes");', _type='text/javascript')
            
            
@auth.requires_login()
def add_apparel_cart():
    if auth.user.id:
        user_order_database = db((db.Orders.UserID == auth.user.id) & (db.Orders.Status == "Pending")).select(db.Orders.ALL).first()
        if user_order_database == None:
                product_apparel_database = db(db.ProductAppList2.id == request.vars['product-id']).select(db.ProductAppList2.ALL).first()
                db_product_id_list = []
                db_product_name_list = []
                db_product_cat_list = []
                db_product_qty_list = []
                db_product_id_list.append(product_apparel_database.id)
                db_product_name_list.append(product_apparel_database.Name)
                db_product_cat_list.append("Sports Apparel")
                db_product_qty_list.append(int(request.vars['product-qty']))
                db_total_price = (float(product_apparel_database.Price) * float(request.vars['product-qty'])) + ((float(product_apparel_database.Tax)/100)* (float(product_apparel_database.Price) * float(request.vars['product-qty'])))
                #db_total_price =int(db_total_price)
                product_quantity = product_apparel_database.Quantity - int(request.vars['product-qty'])
                #product_apparel_database.update_record(Quantity = product_quantity)
                db.Orders.insert(UserID = auth.user.id,
                                 ProductID = list(db_product_id_list),
                                 ProductName = list(db_product_name_list),
                                 ProductCat = list(db_product_cat_list),
                                 ProductQty = list(db_product_qty_list),
                                 TotalPrice = db_total_price,
                                 Status = "Pending")
                return DIV(SCRIPT('alert("Successfully Added To Cart");', _type='text/javascript'))
        elif user_order_database != None:
                product_apparel_database = db(db.ProductAppList2.id == request.vars['product-id']).select(db.ProductAppList2.ALL).first() 
                db_product_id_list = list(user_order_database.ProductID)
                db_product_name_list = list(user_order_database.ProductName)
                db_product_cat_list = list(user_order_database.ProductCat)
                db_product_qty_list = list(user_order_database.ProductQty)
                db_total_price = user_order_database.TotalPrice
                id_exists = 0
                flag = 0
                for i in range(len(db_product_id_list)):
                    if (db_product_id_list[i] == request.vars['product-id']) and (db_product_cat_list[i] == "Sports Apparel"):
                        id_exists = i
                        flag = 1
                if flag == 0:
                    db_product_id_list.append(product_apparel_database.id)
                    db_product_name_list.append(product_apparel_database.Name)
                    db_product_cat_list.append("Sports Apparel")
                    db_product_qty_list.append(int(request.vars['product-qty']))
                    db_total_price = float(user_order_database.TotalPrice) + (float(product_apparel_database.Price) * float(request.vars['product-qty'])) + ((float(product_apparel_database.Tax)/100)* (float(product_apparel_database.Price) * float(request.vars['product-qty'])))
                    #db_total_price =int(db_total_price)
                    product_quantity = product_apparel_database.Quantity - int(request.vars['product-qty'])
                    #product_apparel_database.update_record(Quantity = product_quantity)
                    row1 = db((db.Orders.UserID == auth.user.id) & (db.Orders.Status == "Pending")).select().first()
                    row1.update_record(ProductID = list(db_product_id_list),
                                     ProductName = list(db_product_name_list),
                                     ProductCat = list(db_product_cat_list),
                                     ProductQty = list(db_product_qty_list),
                                     TotalPrice = db_total_price)
                    return SCRIPT('alert("Successfully Added To Cart");', _type='text/javascript')
                elif flag == 1:
                    return SCRIPT('alert("Item Already Exists in the Cart. To alter units please visit cart and make changes");', _type='text/javascript')
            
            
@auth.requires_login()
def remove_from_cart():
    if request.args[0] != None:
        i = int(request.args[0])
        user_order_database=db((db.Orders.UserID == auth.user.id) & (db.Orders.Status == "Pending")).select(db.Orders.ALL).first()
        if user_order_database.ProductCat[i] == "Sports Apparel":
            product_apparel_database = db(db.ProductAppList2.id == user_order_database.ProductID[i]).select(db.ProductAppList2.ALL).first()
            new_product_quantity = int(product_apparel_database.Quantity + int(user_order_database.ProductQty[i]))
            change_in_qty = int(user_order_database.ProductQty[i])
            cart_total_price = float(user_order_database.TotalPrice) - (float(change_in_qty) * float(product_apparel_database.Price)) - ((float(product_apparel_database.Tax)/100) *  (float(change_in_qty) * float(product_apparel_database.Price)))
            #cart_total_price = int(cart_total_price)
            #product_apparel_database.update_record(Quantity = new_product_quantity)
            new_product_qty_list = list(user_order_database.ProductQty)
            new_product_id_list = list(user_order_database.ProductID)
            new_product_cat_list = list(user_order_database.ProductCat)
            new_product_name_list = list(user_order_database.ProductName)
            new_product_qty_list.pop(i)
            new_product_id_list.pop(i)
            new_product_cat_list.pop(i)
            new_product_name_list.pop(i)
            user_order_database.update_record(ProductQty = list(new_product_qty_list),
                                              ProductID = list(new_product_id_list),
                                              ProductName = list(new_product_name_list),
                                              ProductCat = list(new_product_cat_list),
                                             TotalPrice = cart_total_price)
            redirect(URL('default','checkout'))
        elif user_order_database.ProductCat[i] == "Sports Goods":
            product_goods_database = db(db.ProductGoodsList2.id == user_order_database.ProductID[i]).select(db.ProductGoodsList2.ALL).first()
            new_product_quantity = int(product_goods_database.Quantity + int(user_order_database.ProductQty[i]))
            change_in_qty = int(user_order_database.ProductQty[i])
            cart_total_price = float(user_order_database.TotalPrice) - (float(change_in_qty) * float(product_goods_database.Price)) - ((float(product_goods_database.Tax)/100) *  (float(change_in_qty) * float(product_goods_database.Price)))
            #cart_total_price = int(cart_total_price)
            #product_goods_database.update_record(Quantity = new_product_quantity)
            new_product_qty_list = list(user_order_database.ProductQty)
            new_product_id_list = list(user_order_database.ProductID)
            new_product_cat_list = list(user_order_database.ProductCat)
            new_product_name_list = list(user_order_database.ProductName)
            new_product_qty_list.pop(i)
            new_product_id_list.pop(i)
            new_product_cat_list.pop(i)
            new_product_name_list.pop(i)
            user_order_database.update_record(ProductQty = list(new_product_qty_list),
                                              ProductID = list(new_product_id_list),
                                              ProductName = list(new_product_name_list),
                                              ProductCat = list(new_product_cat_list),
                                             TotalPrice = cart_total_price)
            redirect(URL('default','checkout'))
        
        
@auth.requires_login()
def change_qty_cart():
    if request.args[0] != None:
        i = int(request.args[0])
        new_qty = int(request.vars['product-qty'])
        user_order_database=db((db.Orders.UserID == auth.user.id) & (db.Orders.Status == "Pending")).select(db.Orders.ALL).first()
        if user_order_database.ProductCat[i] == "Sports Apparel":
            product_apparel_database = db(db.ProductAppList2.id == user_order_database.ProductID[i]).select(db.ProductAppList2.ALL).first()
            new_product_quantity = int(product_apparel_database.Quantity + user_order_database.ProductQty[i] - int(new_qty))
            change_in_qty = int(new_qty - user_order_database.ProductQty[i])
            cart_total_price = float(user_order_database.TotalPrice) + (float(change_in_qty) * float(product_apparel_database.Price)) + ((float(product_apparel_database.Tax)/100) *  (float(change_in_qty) * float(product_apparel_database.Price)))
            #cart_total_price = int(cart_total_price)
            #product_apparel_database.update_record(Quantity = new_product_quantity)
            new_product_list = list(user_order_database.ProductQty)
            for a in range(len(new_product_list)):
                if a==i:
                    new_product_list[a] = new_qty
            user_order_database.update_record(ProductQty = list(new_product_list),
                                             TotalPrice = cart_total_price)
            redirect(URL('default','checkout'))
        elif user_order_database.ProductCat[i] == "Sports Goods":
            product_goods_database = db(db.ProductGoodsList2.id == user_order_database.ProductID[i]).select(db.ProductGoodsList2.ALL).first()
            new_product_quantity = int(product_goods_database.Quantity + user_order_database.ProductQty[i] - int(new_qty))
            change_in_qty = int(new_qty - user_order_database.ProductQty[i])
            cart_total_price = float(user_order_database.TotalPrice) + (float(change_in_qty) * float(product_goods_database.Price)) + ((float(product_goods_database.Tax)/100) *  (float(change_in_qty) * float(product_goods_database.Price)))
            #cart_total_price = int(cart_total_price)
            #product_goods_database.update_record(Quantity = new_product_quantity)
            new_product_list = list(user_order_database.ProductQty)
            for a in range(len(new_product_list)):
                if a==i:
                    new_product_list[a] = new_qty
            user_order_database.update_record(ProductQty = list(new_product_list),
                                             TotalPrice = cart_total_price)
            redirect(URL('default','checkout'))
    return request.args

def confirm_order():
    if auth.user.id:
        current_user_database = db(db.auth_user.id == auth.user.id).select().first()
        if request.vars['user_address'] != None:
            current_user_database.update_record(Address = request.vars['user_address'])
        if request.vars['user_contact'] != None:
            current_user_database.update_record(Contact = request.vars['user_contact'])
    if request.vars['order_id'] != None:
        user_order_database = db((db.Orders.id == request.vars['order_id']) & (db.Orders.Status == request.vars['order_status'])).select().first()
        """for row,row2,row3 in zip(user_order_database.ProductID,user_order_database.ProductCat,user_order_database.ProductQty):
            if row2 =="Sports Apparel":
                product_apparel_database = db(db.ProductAppList2.id == row).select(db.ProductAppList2.ALL).first()
                new_product_qty = int(product_apparel_database.Quantity) - int(row3)
                product_apparel_database.update_record(Quantity = new_product_qty)
            elif row2 == "Sports Goods":
                product_goods_database = db(db.ProductGoodsList2.id == row).select(db.ProductGoodsList2.ALL).first()
                new_product_qty = int(product_goods_database.Quantity) - int(row3)
                product_goods_database.update_record(Quantity = new_product_qty)"""
        new_status = "Submitted"
        date_of_submit = datetime.date.today()
        user_order_database.update_record(Status = new_status,
                                         DateSubmit = date_of_submit)
        redirect(URL('default','my_order'))
    else:
        redirect(URL('default','index'))
    return 0

@auth.requires_login()
def profile():
    if auth.user.id:
        current_user = auth.user.id
        current_user_database = db(db.auth_user.id==current_user).select(db.auth_user.ALL)[0]
        if request.vars['user_address'] != None:
            current_user_database.update_record(Address = request.vars['user_address'])
        if request.vars['user_contact'] != None:
            current_user_database.update_record(Contact = request.vars['user_contact'])
    confirmed_order_database = db((db.Orders.UserID == current_user) & (db.Orders.Status != "Pending")).select(db.Orders.ALL,orderby=~db.Orders.id)
    
    return dict(current_user_database = current_user_database,
               confirmed_order_database = confirmed_order_database)

@auth.requires_login()
def my_order():
    if auth.user.id:
        current_user = auth.user.id
        current_user_database = db(db.auth_user.id==current_user).select(db.auth_user.ALL)[0]
    confirmed_order_database = db((db.Orders.UserID == current_user) & (db.Orders.Status != "Pending")).select(db.Orders.ALL,orderby=~db.Orders.id)
    return dict(confirmed_order_database = confirmed_order_database,
               current_user_database = current_user_database)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if auth.has_membership(role='End User'):
        auth.settings.login_next = URL('default','index')
    else:
        auth.settings.login_next = URL('admin','index')
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def index2():
    return dict()
@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def ProductView2():
    grid=SQLFORM.smartgrid(db.ProductType2,linked_tables=['ProductGoodsList2','ProductAppList2'],user_signature=False)
    return locals()
@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def Productorder():
    grid=SQLFORM.smartgrid(db.Orders,user_signature=False)
    return locals()
