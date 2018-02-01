# -*- coding: utf-8 -*-
# try something like

from gluon import current
@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def index():
    edit_list = 0
    item_app_database = db(db.ProductAppList2.id > 0 ).select(db.ProductAppList2.ALL)
    item_goods_database = db(db.ProductGoodsList2.id > 0).select(db.ProductGoodsList2.ALL)
    if request.vars['SA_list'] != None:
        edit_list = edit_list + len(request.vars['SA_list'])
    if request.vars['SG_list'] != None:
        edit_list = edit_list + len(request.vars['SG_list'])
    if edit_list != 0:
        a = None
        b = None
        if request.vars['SA_list'] != None:
            a = request.vars['SA_list']
        elif request.vars['SG_list'] != None:
            b = request.vars['SG_list']
        redirect(URL('admin','edit_item',args=[a,b]))
    return dict(item_app_database = item_app_database,
               item_goods_database = item_goods_database,
               edit_list = edit_list)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_item():
    select_type_list = SELECT(OPTION('Sports Goods',_value = 'Sports Goods'),OPTION('Sports Apparels',_value = 'Sports Apparels',_selected=1),_class = 'form-control',_name = 'select-type',value = request.vars['select-type'],_onchange="this.form.submit()")
    apparel_item_database = db(db.ProductAppList2.ParentType == 2).select(db.ProductAppList2.ItemType,distinct=True)
    goods_sport_database = db(db.ProductGoodsList2.ParentType == 1).select(db.ProductGoodsList2.ParentSport,distinct=True)
    if (request.vars['select-type'] == "Sports Apparels") and (request.vars['apparel-item'] != None and request.vars['apparel-item']!= ""):
        db_apparel_item= request.vars['apparel-item']
        db_apparel_material= request.vars['apparel-material']
        db_apparel_brand= request.vars['apparel-brand']
        db_product_name= request.vars['product-name']
        db_product_qty= request.vars['product-qty']
        db_product_price= request.vars['product-price']
        db_product_mrp= request.vars['product-mrp']
        db_product_tax= request.vars['product-tax']
        db_specs_header = []
        db_specs_detail = []
        if request.vars['product-spec-header-1']!="" and request.vars['product-spec-detail-1']!="":
            db_specs_header.append(request.vars['product-spec-header-1'])
            db_specs_detail.append(request.vars['product-spec-detail-1'])
        if request.vars['product-spec-header-2']!="" and request.vars['product-spec-detail-2']!="":
            db_specs_header.append(request.vars['product-spec-header-2'])
            db_specs_detail.append(request.vars['product-spec-detail-2'])
        if request.vars['product-spec-header-3']!="" and request.vars['product-spec-detail-3']!="":
            db_specs_header.append(request.vars['product-spec-header-3'])
            db_specs_detail.append(request.vars['product-spec-detail-3'])
        if request.vars['product-spec-header-4']!="" and request.vars['product-spec-detail-4']!="":
            db_specs_header.append(request.vars['product-spec-header-4'])
            db_specs_detail.append(request.vars['product-spec-detail-4'])
        if request.vars['product-spec-header-5']!="" and request.vars['product-spec-detail-5']!="":
            db_specs_header.append(request.vars['product-spec-header-5'])
            db_specs_detail.append(request.vars['product-spec-detail-5'])
        if request.vars['product-spec-header-6']!="" and request.vars['product-spec-detail-6']!="":
            db_specs_header.append(request.vars['product-spec-header-6'])
            db_specs_detail.append(request.vars['product-spec-detail-6'])
        db_purpose = []
        if request.vars['product-purp-1'] != "":
            db_purpose.append(request.vars['product-purp-1'])
        if request.vars['product-purp-2'] != "":
            db_purpose.append(request.vars['product-purp-2'])
        if request.vars['product-purp-3'] != "":
            db_purpose.append(request.vars['product-purp-3'])
        if request.vars['product-purp-4'] != "":
            db_purpose.append(request.vars['product-purp-4'])
        if request.vars['product-purp-5'] != "":
            db_purpose.append(request.vars['product-purp-5'])
        if request.vars['product-purp-6'] != "":
            db_purpose.append(request.vars['product-purp-6'])
        db_image = None
        image_stream = None
        if request.vars.productimage != "":
            db_image =  db.ProductAppList2.Image.store(request.vars['productimage'].file, request.vars['productimage'].filename)
        db.ProductAppList2.insert(ItemType= db_apparel_item,
                                  Name= db_product_name,
                                  Material= db_apparel_material,
                                  Brand= db_apparel_brand,
                                  MRP= db_product_mrp,
                                  Price= db_product_price,
                                  Quantity= db_product_qty,
                                  ParentType= 2,
                                  Image = db_image,
                                  SpecsHeaders = list(db_specs_header),
                                  SpecsData = list(db_specs_detail),
                                  Purpose = list(db_purpose),
                                  Tax = db_product_tax
                                 )
        session.flash = 'form accepted'
        redirect(URL('admin','index'))
    elif (request.vars['select-type'] == "Sports Goods") and (request.vars['goods-sport'] != None and request.vars['goods-sport']!= ""):
        db_goods_sport= request.vars['goods-sport']
        db_goods_item= request.vars['goods-item']
        db_goods_brand= request.vars['goods-brand']
        db_product_name= request.vars['product-name']
        db_product_qty= request.vars['product-qty']
        db_product_price= request.vars['product-price']
        db_product_mrp= request.vars['product-mrp']
        db_product_tax= request.vars['product-tax']
        db_specs_header = []
        db_specs_detail = []
        if request.vars['product-spec-header-1']!="" and request.vars['product-spec-detail-1']!="":
            db_specs_header.append(request.vars['product-spec-header-1'])
            db_specs_detail.append(request.vars['product-spec-detail-1'])
        if request.vars['product-spec-header-2']!="" and request.vars['product-spec-detail-2']!="":
            db_specs_header.append(request.vars['product-spec-header-2'])
            db_specs_detail.append(request.vars['product-spec-detail-2'])
        if request.vars['product-spec-header-3']!="" and request.vars['product-spec-detail-3']!="":
            db_specs_header.append(request.vars['product-spec-header-3'])
            db_specs_detail.append(request.vars['product-spec-detail-3'])
        if request.vars['product-spec-header-4']!="" and request.vars['product-spec-detail-4']!="":
            db_specs_header.append(request.vars['product-spec-header-4'])
            db_specs_detail.append(request.vars['product-spec-detail-4'])
        if request.vars['product-spec-header-5']!="" and request.vars['product-spec-detail-5']!="":
            db_specs_header.append(request.vars['product-spec-header-5'])
            db_specs_detail.append(request.vars['product-spec-detail-5'])
        if request.vars['product-spec-header-6']!="" and request.vars['product-spec-detail-6']!="":
            db_specs_header.append(request.vars['product-spec-header-6'])
            db_specs_detail.append(request.vars['product-spec-detail-6'])
        db_purpose = []
        if request.vars['product-purp-1'] != "":
            db_purpose.append(request.vars['product-purp-1'])
        if request.vars['product-purp-2'] != "":
            db_purpose.append(request.vars['product-purp-2'])
        if request.vars['product-purp-3'] != "":
            db_purpose.append(request.vars['product-purp-3'])
        if request.vars['product-purp-4'] != "":
            db_purpose.append(request.vars['product-purp-4'])
        if request.vars['product-purp-5'] != "":
            db_purpose.append(request.vars['product-purp-5'])
        if request.vars['product-purp-6'] != "":
            db_purpose.append(request.vars['product-purp-6'])
        db_image = None
        image_stream = None
        if request.vars.productimage != "":
            db_image =  db.ProductGoodsList2.Image.store(request.vars['productimage'].file, request.vars['productimage'].filename)
        db.ProductGoodsList2.insert(ParentSport = db_goods_sport,
                                  ItemType= db_goods_item,
                                  ItemName= db_product_name,
                                  Brand= db_goods_brand,
                                  MRP= db_product_mrp,
                                  Price= db_product_price,
                                  Quantity= db_product_qty,
                                  ParentType= 1,
                                  Image = db_image,
                                  SpecsHeaders = list(db_specs_header),
                                  SpecsData = list(db_specs_detail),
                                  Purpose = list(db_purpose),
                                  Tax = db_product_tax
                                 )
        session.flash = 'form accepted'
        redirect(URL('admin','index'))
    return dict(request = request,
               apparel_item_database = apparel_item_database,
               goods_sport_database = goods_sport_database,
               select_type_list = select_type_list)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def edit_item():
    select_type = None
    SA_id = None #id of item in ProductAppList2 if sports apparel is selected
    SG_id = None  #id of item in ProductGoodsList2 if sports goods is selected
    apparel_item_database = None
    apparel_material_database = None
    apparel_brand_database = None
    goods_sport_database = None
    goods_item_database = None
    goods_brand_database = None
    product_data = None
    
    if request.args(0) != "None":
        select_type = "Sports Apparel"
        SA_id = request.args(0)
        product_table = db(db.ProductAppList2.id == SA_id).select(db.ProductAppList2.ALL)
        product_data = product_table[0]
        apparel_item_database = apparel_item_database = db(db.ProductAppList2.ParentType == 2).select(db.ProductAppList2.ItemType,distinct=True)
        apparel_material_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == product_data.ItemType)).select(db.ProductAppList2.Material,distinct=True)
        apparel_brand_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == product_data.ItemType) & (db.ProductAppList2.Material == product_data.Material)).select(db.ProductAppList2.Brand,distinct = True)
        """
        Update ProductAppList2 table
        variables same as available in add_item function - request.vars['select-type'] and all 
        """
    else:
        select_type ="Sports Goods"
        SG_id = request.args(1)
        product_table = db(db.ProductGoodsList2.id == SG_id).select(db.ProductGoodsList2.ALL)
        product_data = product_table[0]
        goods_sport_database = db(db.ProductGoodsList2.ParentType == 1).select(db.ProductGoodsList2.ParentSport,distinct=True)
        goods_item_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == product_data.ParentSport)).select(db.ProductGoodsList2.ItemType, distinct= True)
        goods_brand_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == product_data.ParentSport) & (db.ProductGoodsList2.ItemType == product_data.ItemType)).select(db.ProductGoodsList2.Brand,distinct = True)
        
    if (request.vars['select-type'] == "Sports Apparels"):
        new_db_product_id = request.vars['product_id_no']
        new_db_apparel_item= request.vars['apparel-item']
        new_db_apparel_material= request.vars['apparel-material']
        new_db_apparel_brand= request.vars['apparel-brand']
        new_db_product_name= request.vars['product-name']
        new_db_product_qty= request.vars['product-qty']
        new_db_product_price= request.vars['product-price']
        new_db_product_mrp= request.vars['product-mrp']
        new_db_product_tax= request.vars['product-tax']
        new_db_specs_header = []
        new_db_specs_detail = []
        if request.vars['product-spec-header-1']!="" and request.vars['product-spec-detail-1']!="":
            new_db_specs_header.append(request.vars['product-spec-header-1'])
            new_db_specs_detail.append(request.vars['product-spec-detail-1'])
        if request.vars['product-spec-header-2']!="" and request.vars['product-spec-detail-2']!="":
            new_db_specs_header.append(request.vars['product-spec-header-2'])
            new_db_specs_detail.append(request.vars['product-spec-detail-2'])
        if request.vars['product-spec-header-3']!="" and request.vars['product-spec-detail-3']!="":
            new_db_specs_header.append(request.vars['product-spec-header-3'])
            new_db_specs_detail.append(request.vars['product-spec-detail-3'])
        if request.vars['product-spec-header-4']!="" and request.vars['product-spec-detail-4']!="":
            new_db_specs_header.append(request.vars['product-spec-header-4'])
            new_db_specs_detail.append(request.vars['product-spec-detail-4'])
        if request.vars['product-spec-header-5']!="" and request.vars['product-spec-detail-5']!="":
            new_db_specs_header.append(request.vars['product-spec-header-5'])
            new_db_specs_detail.append(request.vars['product-spec-detail-5'])
        if request.vars['product-spec-header-6']!="" and request.vars['product-spec-detail-6']!="":
            new_db_specs_header.append(request.vars['product-spec-header-6'])
            new_db_specs_detail.append(request.vars['product-spec-detail-6'])
        new_db_purpose = []
        if request.vars['product-purp-1'] != "":
            new_db_purpose.append(request.vars['product-purp-1'])
        if request.vars['product-purp-2'] != "":
            new_db_purpose.append(request.vars['product-purp-2'])
        if request.vars['product-purp-3'] != "":
            new_db_purpose.append(request.vars['product-purp-3'])
        if request.vars['product-purp-4'] != "":
            new_db_purpose.append(request.vars['product-purp-4'])
        if request.vars['product-purp-5'] != "":
            new_db_purpose.append(request.vars['product-purp-5'])
        if request.vars['product-purp-6'] != "":
            new_db_purpose.append(request.vars['product-purp-6'])
        row = db(db.ProductAppList2.id == new_db_product_id).select().first()
        row.update_record(ItemType= new_db_apparel_item,
                                  Name= new_db_product_name,
                                  Material= new_db_apparel_material,
                                  Brand= new_db_apparel_brand,
                                  MRP= new_db_product_mrp,
                                  Price= new_db_product_price,
                                  Quantity= new_db_product_qty,
                                  ParentType= 2,
                                  SpecsHeaders = list(new_db_specs_header),
                                  SpecsData = list(new_db_specs_detail),
                                  Purpose = list(new_db_purpose),
                                  Tax = new_db_product_tax
                                 )
        new_db_image = None
        image_stream = None
        if request.vars.productimage != "":
            new_db_image =  db.ProductAppList2.Image.store(request.vars['productimage'].file, request.vars['productimage'].filename)
            row1 = db(db.ProductAppList2.id == new_db_product_id).select().first()
            row1.update_record(Image = new_db_image)
        session.flash = 'form accepted'
        redirect(URL('admin','index'))
    elif (request.vars['select-type'] == "Sports Goods"):
        new_db_product_id = request.vars['product_id_no']
        new_db_goods_sport= request.vars['goods-sport']
        new_db_goods_item= request.vars['goods-item']
        new_db_goods_brand= request.vars['goods-brand']
        new_db_product_name= request.vars['product-name']
        new_db_product_qty= request.vars['product-qty']
        new_db_product_price= request.vars['product-price']
        new_db_product_mrp= request.vars['product-mrp']
        new_db_product_tax= request.vars['product-tax']
        new_db_specs_header = []
        new_db_specs_detail = []
        if request.vars['product-spec-header-1']!="" and request.vars['product-spec-detail-1']!="":
            new_db_specs_header.append(request.vars['product-spec-header-1'])
            new_db_specs_detail.append(request.vars['product-spec-detail-1'])
        if request.vars['product-spec-header-2']!="" and request.vars['product-spec-detail-2']!="":
            new_db_specs_header.append(request.vars['product-spec-header-2'])
            new_db_specs_detail.append(request.vars['product-spec-detail-2'])
        if request.vars['product-spec-header-3']!="" and request.vars['product-spec-detail-3']!="":
            new_db_specs_header.append(request.vars['product-spec-header-3'])
            new_db_specs_detail.append(request.vars['product-spec-detail-3'])
        if request.vars['product-spec-header-4']!="" and request.vars['product-spec-detail-4']!="":
            new_db_specs_header.append(request.vars['product-spec-header-4'])
            new_db_specs_detail.append(request.vars['product-spec-detail-4'])
        if request.vars['product-spec-header-5']!="" and request.vars['product-spec-detail-5']!="":
            new_db_specs_header.append(request.vars['product-spec-header-5'])
            new_db_specs_detail.append(request.vars['product-spec-detail-5'])
        if request.vars['product-spec-header-6']!="" and request.vars['product-spec-detail-6']!="":
            new_db_specs_header.append(request.vars['product-spec-header-6'])
            new_db_specs_detail.append(request.vars['product-spec-detail-6'])
        new_db_purpose = []
        if request.vars['product-purp-1'] != "":
            new_db_purpose.append(request.vars['product-purp-1'])
        if request.vars['product-purp-2'] != "":
            new_db_purpose.append(request.vars['product-purp-2'])
        if request.vars['product-purp-3'] != "":
            new_db_purpose.append(request.vars['product-purp-3'])
        if request.vars['product-purp-4'] != "":
            new_db_purpose.append(request.vars['product-purp-4'])
        if request.vars['product-purp-5'] != "":
            new_db_purpose.append(request.vars['product-purp-5'])
        if request.vars['product-purp-6'] != "":
            new_db_purpose.append(request.vars['product-purp-6'])
        row = db(db.ProductGoodsList2.id == new_db_product_id).select().first()
        row.update_record(ParentSport = new_db_goods_sport,
                                  ItemType= new_db_goods_item,
                                  ItemName= new_db_product_name,
                                  Brand= new_db_goods_brand,
                                  MRP= new_db_product_mrp,
                                  Price= new_db_product_price,
                                  Quantity= new_db_product_qty,
                                  ParentType= 1,
                                  SpecsHeaders = list(new_db_specs_header),
                                  SpecsData = list(new_db_specs_detail),
                                  Purpose = list(new_db_purpose),
                                  Tax = new_db_product_tax
                                 )
        new_db_image = None
        image_stream = None
        if request.vars.productimage != "":
            new_db_image =  db.ProductGoodsList2.Image.store(request.vars['productimage'].file, request.vars['productimage'].filename)
            row1 = db(db.ProductGoodsList2.id == new_db_product_id).select().first()
            row1.update_record(Image = new_db_image)
        session.flash = 'form accepted'
        redirect(URL('admin','index'))
    return dict(apparel_item_database = apparel_item_database,
                apparel_material_database = apparel_material_database,
                apparel_brand_database = apparel_brand_database,
                goods_sport_database = goods_sport_database, 
                goods_item_database = goods_item_database,
                goods_brand_database = goods_brand_database,
                product_data = product_data,
                request = request)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def delete_item():
    if request.vars['SA_list'] != None:
        a = isinstance(request.vars['SA_list'], basestring)
        if a == True:
            row = db(db.ProductAppList2.id == request.vars['SA_list']).select().first()
            row.delete_record()
        elif a == False:
            for items in request.vars['SA_list']:
                row2 = db(db.ProductAppList2.id == items).select().first()
                row2.delete_record()
    if request.vars['SG_list'] != None:
        b = isinstance(request.vars['SG_list'], basestring)
        if b == True:
            row3 = db(db.ProductGoodsList2.id == request.vars['SG_list']).select().first()
            row3.delete_record()
        elif b == False:
            for item2s in request.vars['SG_list']:
                row3 = db(db.ProductGoodsList2.id == item2s).select().first()
                row3.delete_record()
    redirect(URL('admin','index'))
    return DIV(request.vars)


@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def delete_one_item():
    if request.vars['SA_list']!=None:
        row = db(db.ProductAppList2.id == request.vars['SA_list']).select().first()
        row.delete_record()
    if request.vars['SG_list']!=None:
        row1 = db(db.ProductGoodsList2.id == request.vars['SG_list']).select().first()
        row1.delete_record()
    redirect(URL('admin','index'))
    return DIV(request.vars)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_apparel_item_list():
    apparel_item_database = db(db.ProductAppList2.ParentType == 2).select(db.ProductAppList2.ItemType,distinct=True)
    result = "<option selected hidden value = "">Select Item</option>"
    for rows in apparel_item_database:
        result += "<option value='" + rows.ItemType + "'>" + rows.ItemType + "</option>"  
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_apparel_material_list():
    apparel_material_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item'])).select(db.ProductAppList2.Material,distinct=True)
    result = "<option selected hidden value = "" >Select Material</option>"
    for rows in apparel_material_database:
        result += "<option value='" + rows.Material + "'>" + rows.Material + "</option>"  
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_apparel_brand_list():
    apparel_brand_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item']) & (db.ProductAppList2.Material == request.vars['apparel-material'])).select(db.ProductAppList2.Brand,distinct = True)
    result = "<option selected hidden value = "">Select Brand</option>"
    for rows in apparel_brand_database:
        result += "<option value='" + rows.Brand + "'>" + rows.Brand + "</option>"  
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_apparel_item():
    apparel_item_database = db(db.ProductAppList2.ParentType == 2).select(db.ProductAppList2.ItemType,distinct=True)
    result = "<option selected hidden value="">Select Item</option>"
    for rows in apparel_item_database:
        result += "<option value='" + rows.ItemType + "'>" + rows.ItemType + "</option>"  
    result += "<option selected value='" + request.vars['add-apparel-item'] + "'>" + request.vars['add-apparel-item'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_apparel_material():
    apparel_material_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item'])).select(db.ProductAppList2.Material,distinct=True)
    result = "<option selected hidden value="">Select Material</option>"
    for rows in apparel_material_database:
        result += "<option value='" + rows.Material + "'>" + rows.Material + "</option>"  
    result += "<option selected value='" + request.vars['add-apparel-material'] + "'>" + request.vars['add-apparel-material'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_apparel_brand():
    apparel_brand_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item']) & (db.ProductAppList2.Material == request.vars['apparel-material'])).select(db.ProductAppList2.Brand,distinct = True)
    result = "<option selected hidden value="">Select Brand</option>"
    for rows in apparel_brand_database:
        result += "<option value='" + rows.Brand + "'>" + rows.Brand + "</option>"  
    result += "<option selected value='" + request.vars['add-apparel-brand'] + "'>" + request.vars['add-apparel-brand'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_goods_item_list():
    goods_item_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods-sport'])).select(db.ProductGoodsList2.ItemType, distinct= True)
    result = "<option selected hidden value="">Select Item</option>"
    for rows in goods_item_database:
        result += "<option value='" + rows.ItemType + "'>" + rows.ItemType + "</option>"  
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_goods_brand_list():
    goods_brand_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods-sport']) & (db.ProductGoodsList2.ItemType == request.vars['goods-item'])).select(db.ProductGoodsList2.Brand,distinct = True)
    result = "<option selected hidden value="">Select Brand</option>"
    for rows in goods_brand_database:
        result += "<option value='" + rows.Brand + "'>" + rows.Brand + "</option>"  
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_goods_sport():
    goods_sport_database= db(db.ProductGoodsList2.ParentType == 1). select(db.ProductGoodsList2.ParentSport,distinct=True)
    result = "<option selected hidden value="">Select Sport</option>"
    for rows in goods_sport_database:
        result += "<option value='" + rows.ParentSport + "'>" + rows.ParentSport + "</option>"  
    result += "<option selected value='" + request.vars['add-goods-sport'] + "'>" + request.vars['add-goods-sport'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_goods_item():
    goods_item_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods-sport'])).select(db.ProductGoodsList2.ItemType, distinct= True)
    result = "<option selected hidden value="">Select Item</option>"
    for rows in goods_item_database:
        result += "<option value='" + rows.ItemType + "'>" + rows.ItemType + "</option>"  
    result += "<option selected value='" + request.vars['add-goods-item'] + "'>" + request.vars['add-goods-item'] + "</option>"
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_goods_brand():
    goods_brand_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods-sport']) & (db.ProductGoodsList2.ItemType == request.vars['goods-item'])).select(db.ProductGoodsList2.Brand,distinct = True)
    result = "<option selected hidden value="">Select Brand</option>"
    for rows in goods_brand_database:
        result += "<option value='" + rows.Brand + "'>" + rows.Brand + "</option>"  
    result += "<option selected value='" + request.vars['add-goods-brand'] + "'>" + request.vars['add-goods-brand'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_apparel_tax():
    apparel_item_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item'])).select(db.ProductAppList2.Tax,distinct = True)
    result = "<option selected hidden value="">Select Tax(%)</option>"
    for rows in apparel_item_database:
        result += "<option value='" + rows.Tax + "'>" + rows.Tax + "</option>"
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_goods_tax():
    goods_item_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods-sport']) & (db.ProductGoodsList2.ItemType == request.vars['goods-item'])).select(db.ProductGoodsList2.Tax,distinct = True)
    result = "<option selected hidden value="">Select Tax(%)</option>"
    for rows in goods_item_database:
        result += "<option value='" + rows.Tax + "'>" + rows.Tax + "</option>"
    return XML(result)


@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_apparel_spec_list():
    apparel_item_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item'])).select(db.ProductAppList2.SpecsHeaders,db.ProductAppList2.id)
    max_spec = 0
    spec_id = 10000
    for rows in apparel_item_database:
        if len(rows.SpecsHeaders) > max_spec:
            spec_id = rows.id
            max_spec = len(rows.SpecsHeaders)
    apparel_specs_database = db(db.ProductAppList2.id == spec_id).select(db.ProductAppList2.SpecsHeaders)
    result = "<option selected value="">Select Specification</option>"
    for rows in apparel_specs_database:
        for row in rows.SpecsHeaders:
            result += "<option value='" + row + "'>" + row + "</option>"  
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_goods_spec_list():
    goods_item_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods-sport']) & (db.ProductGoodsList2.ItemType == request.vars['goods-item'])).select(db.ProductGoodsList2.SpecsHeaders,db.ProductGoodsList2.id)
    max_spec = 0
    spec_id = 10000
    for rows in goods_item_database:
        if len(rows.SpecsHeaders) > max_spec:
            spec_id = rows.id
            max_spec = len(rows.SpecsHeaders)
    goods_specs_database = db(db.ProductGoodsList2.id == spec_id).select(db.ProductGoodsList2.SpecsHeaders)
    result = "<option selected value="">Select Specification</option>"
    for rows in goods_specs_database:
        for row in rows.SpecsHeaders:
            result += "<option value='" + row + "'>" + row + "</option>"  
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def update_apparel_purpose():
    apparel_item_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item'])).select(db.ProductAppList2.Purpose,db.ProductAppList2.id)
    max_purp = 0
    purp_id = 10000
    for rows in apparel_item_database:
        if len(rows.Purpose) > max_purp:
            purp_id = rows.id
            max_purp = len(rows.Purpose)
    purp = db(db.ProductAppList2.id == purp_id).select(db.ProductAppList2.Purpose).first()
    if len(purp.Purpose) >= 1:
        html = """<input class="form-control" type="text" placeholder="Enter" id="input-1" style="float:left;width:70%;" name = "product-purp-1" onClick="this.select();">
                                    <a class="btn btn-primary" id= "act-p-2" style = "margin-left:20px;float:left;"><span style = "padding-bottom:5px" class ="glyphicon glyphicon-plus"></span></a>"""
        return "jQuery('#target').html(%html);"
        
@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_spec_1():
    result = "<option value="">Select Specification</option>"
    result += "<option selected value='" + request.vars['add-spec-1'] + "'>" + request.vars['add-spec-1'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_spec_2():
    result = "<option value="">Select Specification</option>"
    result += "<option selected value='" + request.vars['add-spec-2'] + "'>" + request.vars['add-spec-2'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_spec_3():
    result = "<option value="">Select Specification</option>"
    result += "<option selected value='" + request.vars['add-spec-3'] + "'>" + request.vars['add-spec-3'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_spec_4():
    result = "<option value="">Select Specification</option>"
    result += "<option selected value='" + request.vars['add-spec-4'] + "'>" + request.vars['add-spec-4'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_spec_5():
    result = "<option value="">Select Specification</option>"
    result += "<option selected value='" + request.vars['add-spec-5'] + "'>" + request.vars['add-spec-5'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_spec_6():
    result = "<option value="">Select Specification</option>"
    result += "<option selected value='" + request.vars['add-spec-6'] + "'>" + request.vars['add-spec-6'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_new_tax():
    result=""
    if request.vars['select-type'] == "Sports Apparels" and request.vars['apparel-item']!=None:
        apparel_item_database = db((db.ProductAppList2.ParentType == 2) & (db.ProductAppList2.ItemType == request.vars['apparel-item'])).select(db.ProductAppList2.Tax,distinct = True)
        for rows in apparel_item_database:
            result += "<option value='" + rows.Tax + "'>" + rows.Tax + "</option>"
    elif request.vars['select-type'] == "Sports Goods" and request.vars['goods-sport']!=None and request.vars['goods-item']!=None:
        goods_item_database= db((db.ProductGoodsList2.ParentType == 1) & (db.ProductGoodsList2.ParentSport == request.vars['goods-sport']) & (db.ProductGoodsList2.ItemType == request.vars['goods-item'])).select(db.ProductGoodsList2.Tax,distinct = True)
        for rows in goods_item_database:
            result += "<option value='" + rows.Tax + "'>" + rows.Tax + "</option>"
    result += "<option selected value='" + request.vars['add-tax'] + "'>" + request.vars['add-tax'] + "</option>" 
    return XML(result)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def user_index():
    edit_list = 0
    user_database = db(db.auth_user.id > 0 ).select(db.auth_user.ALL)
    if request.vars['user_list'] != None:
        edit_list = edit_list + len(request.vars['user_list'])
    if edit_list != 0:
        a = None
        if request.vars['user_list'] != None:
            a = request.vars['user_list']
        redirect(URL('admin','edit_user',args=a))
    return dict(user_database = user_database)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def add_user():
    if request.vars['user_email']!=None:
        db_user_name= request.vars['user_name']
        db_user_last_name= request.vars['user_last_name']
        db_org_name= request.vars['org_name']
        db_user_email= request.vars['user_email']
        db_user_contact= request.vars['user_contact']
        db_user_password= request.vars['user_password']
        db_user_address= request.vars['user_address']
        db_user_access= request.vars['user-access']
        image_stream = None
        #if request.vars.user_photo != "":
            #db_image =  db.Users.Image.store(request.vars['user_photo'].file, request.vars['user_photo'].filename)
        db.auth_user.insert(first_name=db_user_name,
                    last_name=db_user_last_name,
                    Organisation=db_org_name,
                    email=db_user_email,
                    password=db_user_password,
                    AccessType=db_user_access,
                    Contact = db_user_contact,
                    Address=db_user_address)
        user = db(db.auth_user.email == db_user_email).select(db.auth_user.ALL).first()
        if request.vars['user-access'] == "Admin":
            db.auth_membership.insert(user_id = user.id,
                                 group_id = 1)
        elif request.vars['user-access'] == "End User":
            db.auth_membership.insert(user_id = user.id,
                                 group_id = 2)
        redirect(URL('admin','user_index'))
    return dict()

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def edit_user():
    user_data = None
    if request.args(0) != "None":
        user_id = request.args(0)
        user_table = db(db.auth_user.id == user_id).select(db.auth_user.ALL)
        user_data = user_table[0]
    if request.vars['user_email']!=None:
        db_user_id = request.vars['user_id']
        db_user_name= request.vars['user_name']
        db_user_last_name= request.vars['user_last_name']
        db_org_name= request.vars['org_name']
        db_user_email= request.vars['user_email']
        db_user_contact= request.vars['user_contact']
        db_user_password= request.vars['user_password']
        db_user_address= request.vars['user_address']
        db_user_access= request.vars['user-access']
        image_stream = None
        #if request.vars.user_photo != "":
            #db_image =  db.Users.Image.store(request.vars['user_photo'].file, request.vars['user_photo'].filename)
        row = db(db.auth_user.id == db_user_id).select().first()
        row.update_record(first_name=db_user_name,
                    last_name=db_user_last_name,
                    Organisation=db_org_name,
                    email=db_user_email,
                    password=db_user_password,
                    AccessType=db_user_access,
                    Contact = db_user_contact,
                    Address=db_user_address)
        redirect(URL('admin','user_index'))
    return dict(user_data = user_data)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def delete_user():
    a = isinstance(request.vars['user_list'], basestring)
    if a == True:
        row = db(db.auth_user.id == request.vars['user_list']).select().first()
        row.delete_record()
    elif a == False:
        for items in request.vars['user_list']:
            row2 = db(db.auth_user.id == items).select().first()
            row2.delete_record()
    redirect(URL('admin','user_index'))
    return DIV(request.vars)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def order_index():
    edit_list = 0
    if request.vars['order_list'] != None:
        edit_list = edit_list + len(request.vars['order_list'])
    if edit_list != 0:
        a = None
        if request.vars['order_list'] != None:
            a = request.vars['order_list']
        redirect(URL('admin','edit_order',args=a))
    order_database = db(db.Orders.id > 0).select(db.Orders.ALL)
    return dict(order_database = order_database)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def edit_order():
    user_order_database = None
    check_dispatch = 0
    if request.args(0) != "None":
        order_id = request.args(0)
        user_order_database = db(db.Orders.id == order_id).select(db.Orders.ALL).first()
        new_product_id_list = []
        new_product_qty_list = []
        new_product_cat_list = []
        new_product_name_list = []
        new_total_price = 0
        if user_order_database != None and user_order_database.Status!="Dispatched":
            for row,row2,row3,row4 in zip(user_order_database.ProductID,user_order_database.ProductName,user_order_database.ProductCat,user_order_database.ProductQty):
                if row3 =="Sports Apparel":
                    product_apparel_database = db(db.ProductAppList2.id == row).select(db.ProductAppList2.ALL).first()
                    if product_apparel_database != None:
                        new_product_id_list.append(row)
                        new_product_name_list.append(row2)
                        new_product_cat_list.append(row3)
                        new_quantity = int(row4)
                        if product_apparel_database.Quantity < int(row4):
                            check_dispatch = 1
                        new_product_qty_list.append(new_quantity)
                        new_total_price = new_total_price + (float(product_apparel_database.Price) * float(new_quantity)) + ((float(product_apparel_database.Tax)/100) * (float(product_apparel_database.Price) * float(new_quantity)))
                elif row3 == "Sports Goods":
                    product_goods_database = db(db.ProductGoodsList2.id == row).select(db.ProductGoodsList2.ALL).first()
                    if product_goods_database != None:
                        new_product_id_list.append(row)
                        new_product_name_list.append(row2)
                        new_product_cat_list.append(row3)
                        new_quantity = int(row4)
                        if product_goods_database.Quantity < int(row4):
                            check_dispatch = 1
                        new_product_qty_list.append(new_quantity)
                        new_total_price = new_total_price + (float(product_goods_database.Price) * float(new_quantity)) + ((float(product_goods_database.Tax)/100) * (float(product_goods_database.Price) * float(new_quantity)))
            user_order_database.update_record(ProductID = list(new_product_id_list),
                                     ProductName = list(new_product_name_list),
                                     ProductCat = list(new_product_cat_list),
                                     ProductQty = list(new_product_qty_list),
                                     TotalPrice = new_total_price)    
    return dict(user_order_database = user_order_database,
               check_dispatch = check_dispatch)

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def remove_from_cart():
    if request.args[0] != None:
        a = int(request.args[1])
        i = int(request.args[0])
        user_order_database=db(db.Orders.id == a).select(db.Orders.ALL).first()
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
            redirect(URL('admin','edit_order',args=a))
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
            redirect(URL('admin','edit_order',args=a))
        
        
@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def change_qty_cart():
    if request.args[0] != None:
        i = int(request.args[0])
        b = int(request.args[1])
        new_qty = int(request.vars['product-qty'])
        user_order_database=db(db.Orders.id == b).select(db.Orders.ALL).first()
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
            redirect(URL('admin','edit_order',args=b))
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
            redirect(URL('admin','edit_order',args=b))
    return request.args

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))

def change_order_status():
    if request.args[0]!=None:
        user_order_database = db(db.Orders.id == request.args[0]).select().first()
        new_status = request.vars['order_status']
        if user_order_database != None:
            if new_status == "Dispatched":
                for row,row2,row3 in zip(user_order_database.ProductID,user_order_database.ProductCat,user_order_database.ProductQty):
                    if row2 =="Sports Apparel":
                        product_apparel_database = db(db.ProductAppList2.id == row).select(db.ProductAppList2.ALL).first()
                        new_product_qty = int(product_apparel_database.Quantity) - int(row3)
                        product_apparel_database.update_record(Quantity = new_product_qty)
                    elif row2 == "Sports Goods":
                        product_goods_database = db(db.ProductGoodsList2.id == row).select(db.ProductGoodsList2.ALL).first()
                        new_product_qty = int(product_goods_database.Quantity) - int(row3)
                        product_goods_database.update_record(Quantity = new_product_qty)
            user_order_database.update_record(Status = new_status)
        redirect(URL('admin','order_index'))
    return request.vars['order_status']

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))

def delete_order():
    a = isinstance(request.vars['order_list'], basestring)
    if a == True:
        row = db(db.Orders.id == int(request.vars['order_list'])).select().first()
        row.delete_record()
        """    for item,item2,item3,item4 in zip(row.ProductID,row.ProductName,row.ProductCat,row.ProductQty):
                if item3 == "Sports Apparel":
                    product_apparel_database  = db(db.ProductAppList2.id == item).select().first()
                    if product_apparel_database != None:
                        new_quantity =product_apparel_database.Quantity + int(item4)
                        product_apparel_database.update_record(Quantity = new_quantity)
                elif item3 == "Sports Goods":
                    product_goods_database  = db(db.ProductGoodsList2.id == item).select().first()
                    if product_goods_database != None:
                        new_quantity =product_goods_database.Quantity + int(item4)
                        product_goods_database.update_record(Quantity = new_quantity)
            row.delete_record() 
        elif row.Status == "Delivered":
            row.delete_record()"""
        redirect(URL('admin','order_index'))
    elif a == False:
        for index in request.vars['order_list']:
            row2 = db(db.Orders.id == int(index)).select().first()
            row2.delete_record()
            """if row2.Status == "Confirmed":
                for item,item2,item3,item4 in zip(row2.ProductID,row2.ProductName,row2.ProductCat,row2.ProductQty):
                    if item3 == "Sports Apparel":
                        product_apparel_database  = db(db.ProductAppList2.id == item).select().first()
                        if product_apparel_database != None:
                            new_quantity =product_apparel_database.Quantity + int(item4)
                            product_apparel_database.update_record(Quantity = new_quantity)
                    elif item3 == "Sports Goods":
                        product_goods_database  = db(db.ProductGoodsList2.id == item).select().first()
                        if product_goods_database != None:
                            new_quantity =product_goods_database.Quantity + int(item4)
                            product_goods_database.update_record(Quantity = new_quantity)
                row2.delete_record() 
            elif row2.Status == "Delivered":
                row2.delete_record()"""
        redirect(URL('admin','order_index'))
    return 0

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def exportGoodsCSV():
    import csv
    import cStringIO
    rows=db(db.ProductGoodsList2.id,ignore_common_filters= True).select()
    s = cStringIO.StringIO()
    #csv_writer = csv.writer(s)
    #col = rows.colnames
    #heading = [c.split('.')[-1].upper() for c in col]
    #csv_writer.writerow(heading)
    #rows.export_to_csv_file(s, represent=True, write_colnames=False)
    rows.export_to_csv_file(s)
    response.headers['Content-Type']='application/vnd.ms-excel'
    response.headers['Content-disposition'] = 'attachment; filename=SportsGoods.csv'
    response.write(s.getvalue(), escape=False)
    return s.getvalue()

@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))
def exportAppCSV():
    import csv
    import cStringIO
    rows=db(db.ProductAppList2.id,ignore_common_filters= True).select()
    s = cStringIO.StringIO()
    #csv_writer = csv.writer(s)
    #col = rows.colnames
    #heading = [c.split('.')[-1].upper() for c in col]
    #csv_writer.writerow(heading)
    #rows.export_to_csv_file(s, represent=True, write_colnames=False)
    
    
    rows.export_to_csv_file(s)
    response.headers['Content-Type']='application/vnd.ms-excel'
    response.headers['Content-disposition'] = 'attachment; filename=SportsApparels.csv'
    response.write(s.getvalue())
    return s.getvalue()


            
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


@auth.requires_login()
@auth.requires(auth.has_membership(role='Admin'))

def ProductView2():
    grid=SQLFORM.smartgrid(db.ProductType2,linked_tables=['ProductGoodsList2','ProductAppList2'],user_signature=False)
    return locals()
