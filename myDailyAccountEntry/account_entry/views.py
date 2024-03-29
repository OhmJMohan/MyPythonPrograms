from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Sum, Avg, Count
from .models import account_database
from .models import category_list
from .models import balance_sheet

# Create your views here.

def mdae_homePage(request):
    return render(request, "home.html")

def add(request):
    category1 = category_list.objects.filter(category="Names").order_by('category_names').values() 
    category2 = category_list.objects.filter(category="Credit/Debit").order_by('category_names').values() 
    category3 = category_list.objects.filter(category="TransactionType").order_by('category_names').values() 
    category4 = category_list.objects.filter(category="Account").order_by('category_names').values() 
    database = account_database.objects.all().values()
    context = {"entry": database, "cate_names": category1, "cate_credit_debit": category2, "cate_transactiontype": category3, "cate_account": category4}
    return render(request, "addAccountEntry.html", context)

def addAccountEntry(request):
    x_date = request.POST["date"]
    x_credit_debit = request.POST["credit_debit"]
    x_category = request.POST["category"]
    x_account = request.POST["account"]
    x_particular = request.POST["particular"]
    x_name = request.POST["name"]
    x_amount = request.POST["amount"]
    x_notes = request.POST["notes"]
    dailyAccountEntry = account_database(date=x_date, credit_debit=x_credit_debit, category=x_category, account=x_account, particular=x_particular, name=x_name, amount=x_amount, notes=x_notes)
    dailyAccountEntry.save()
    return redirect("/add")

def add_category(request):
    category_add = category_list.objects.all().values()
    context = {"entry_category": category_add}
    return render(request, "add_category.html", context)

def addcategory(request):
    x = request.POST["category"]
    y = request.POST["names"]
    entry_category = category_list(category=x, category_names=y)
    entry_category.save()
    return redirect("/add_category")

def category_view(request):
    count = 0
    cate_list = category_list.objects.all().order_by("category", "category_names").values()
    for coun in cate_list:
        count = count + 1

    context = {"category": cate_list, "count": count}
    return render(request, "category_view.html", context)

def deleteCategory(request, id):
    category = category_list.objects.get(id=id)
    context = {"deleteItem": category}
    return render(request, "deleteCategory.html", context)

def delete_view(request, id):
    category = category_list.objects.get(id=id)
    category.delete()
    return redirect("/home")

def update_category(request, id):
    category = category_list.objects.get(id=id)
    context = {"updateItem": category}
    return render(request, "update_category.html", context)

def updaterecord(request, id):
    cate_name = request.POST["cat_name"]
    category = category_list.objects.get(id=id)
    category.category_names = cate_name
    category.save()
    return redirect("/category_view")

def cash_check(request):
    x_date = request.POST["filter_date"]
    cash_credit = account_database.objects.filter(date__range=("2023-06-10", x_date), credit_debit="credit", account="Cash").aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(date__range=("2023-06-10", x_date), credit_debit="debit", account="Cash").aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
    if cash_total_balance["cash1"] == None: 
        xx = float(0) 
    else:
        xx = float(cash_total_balance["cash1"])
    if cash_total_balance["cash2"] == None:
        yy = float(0)
    else:
        yy = float(cash_total_balance["cash2"]) 
    cash_balance = xx - yy
    context = {"bal": cash_balance, "date": x_date}
    return render(request, "cash_balance_check.html", context)

def account_entry_report(request):
    count = 0
    account_listCount = account_database.objects.all().values()
    for coun in account_listCount:
        count = count + 1

    account_list = account_database.objects.all().order_by("date").values()[count-20:]
    context = {"account": account_list, "coun": count}
    return render(request, "accountEntryDatabase.html", context)

def balance_view(request):
    balance_list = balance_sheet.objects.all().values()
    context = {"balance": balance_list}
    return render(request, "cash_balance_view.html", context)

def balance_checkEntry(request):
    x_date = request.POST["date"]
    x_amount = request.POST["amount"]
    x_rs500 = request.POST["rs500"]
    x_rs200 = request.POST["rs200"]
    x_rs100 = request.POST["rs100"]
    x_rs50 = request.POST["rs50"]
    x_rs20 = request.POST["rs20"]
    x_rs10 = request.POST["rs10"]
    x_rs5 = request.POST["rs5"]
    x_rs2 = request.POST["rs2"]
    x_rs1 = request.POST["rs1"]
    x_total_amount = request.POST["total_amount"]
    x_balance_amount = request.POST["balance_amount"]    
    x_status = request.POST["status"]
    cash_balance_check = balance_sheet(date=x_date, amount=x_amount, rs500=x_rs500, rs200=x_rs200, rs100=x_rs100, rs50=x_rs50, rs20=x_rs20, rs10=x_rs10, rs5=x_rs5, rs2=x_rs2, rs1=x_rs1, total_amount=x_total_amount, balance_amount=x_balance_amount, status=x_status)
    cash_balance_check.save()
    return redirect("/balance_view")

def daily_account_report(request):
    cash_credit = account_database.objects.filter(credit_debit="credit", account="Cash").aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(credit_debit="debit", account="Cash").aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
    if cash_total_balance["cash1"] == None: 
        xx1 = float(0) 
    else:
        xx1 = float(cash_total_balance["cash1"])
    if cash_total_balance["cash2"] == None:
        yy1 = float(0)
    else:
        yy1 = float(cash_total_balance["cash2"]) 
    cash_balance = (xx1-yy1)
    epayon_credit = account_database.objects.filter(credit_debit="credit", account="EPayOn").aggregate(epayon_c=Sum('amount'))
    epayon_debit = account_database.objects.filter(credit_debit="debit", account="EPayOn").aggregate(epayon_d=Sum('amount'))
    epayon_total_balance = {"epayon1": epayon_credit["epayon_c"], "epayon2": epayon_debit["epayon_d"]} 
    if epayon_total_balance["epayon1"] == None: 
        xx2 = float(0) 
    else:
        xx2 = float(epayon_total_balance["epayon1"])
    if epayon_total_balance["epayon2"] == None:
        yy2 = float(0)
    else:
        yy2 = float(epayon_total_balance["epayon2"]) 
    epayon_balance = (xx2-yy2)
    iobmohan_credit = account_database.objects.filter(credit_debit="credit", account="IOBMohan").aggregate(iobmohan_c=Sum('amount'))
    iobmohan_debit = account_database.objects.filter(credit_debit="debit", account="IOBMohan").aggregate(iobmohan_d=Sum('amount'))
    iobmohan_total_balance = {"iobmohan1": iobmohan_credit["iobmohan_c"], "iobmohan2": iobmohan_debit["iobmohan_d"]} 
    if iobmohan_total_balance["iobmohan1"] == None: 
        xx3 = float(0) 
    else:
        xx3 = float(iobmohan_total_balance["iobmohan1"])
    if iobmohan_total_balance["iobmohan2"] == None:
        yy3 = float(0)
    else:
        yy3 = float(iobmohan_total_balance["iobmohan2"]) 
    iobmohan_balance = (xx3-yy3)
    ibgayathri_credit = account_database.objects.filter(credit_debit="credit", account="Indian Bank Gayathri").aggregate(ibgayathri_c=Sum('amount'))
    ibgayathri_debit = account_database.objects.filter(credit_debit="debit", account="Indian Bank Gayathri").aggregate(ibgayathri_d=Sum('amount'))
    ibgayathri_total_balance = {"ibgayathri1": ibgayathri_credit["ibgayathri_c"], "ibgayathri2": ibgayathri_debit["ibgayathri_d"]} 
    if ibgayathri_total_balance["ibgayathri1"] == None: 
        xx4 = float(0) 
    else:
        xx4 = float(ibgayathri_total_balance["ibgayathri1"])
    if ibgayathri_total_balance["ibgayathri2"] == None:
        yy4 = float(0)
    else:
        yy4 = float(ibgayathri_total_balance["ibgayathri2"]) 
    ibgayathri_balance = (xx4-yy4)
    ibmohan_credit = account_database.objects.filter(credit_debit="credit", account="Indian Bank Mohan").aggregate(ibmohan_c=Sum('amount'))
    ibmohan_debit = account_database.objects.filter(credit_debit="debit", account="Indian Bank Mohan").aggregate(ibmohan_d=Sum('amount'))
    ibmohan_total_balance = {"ibmohan1": ibmohan_credit["ibmohan_c"], "ibmohan2": ibmohan_debit["ibmohan_d"]} 
    if ibmohan_total_balance["ibmohan1"] == None: 
        xx5 = float(0) 
    else:
        xx5 = float(ibmohan_total_balance["ibmohan1"])
    if ibmohan_total_balance["ibmohan2"] == None:
        yy5 = float(0)
    else:
        yy5 = float(ibmohan_total_balance["ibmohan2"]) 
    ibmohan_balance = (xx5-yy5)
    jioposlite_credit = account_database.objects.filter(credit_debit="credit", account="JioPosLite").aggregate(jioposlite_c=Sum('amount'))
    jioposlite_debit = account_database.objects.filter(credit_debit="debit", account="JioPosLite").aggregate(jioposlite_d=Sum('amount'))
    jioposlite_total_balance = {"jioposlite1": jioposlite_credit["jioposlite_c"], "jioposlite2": jioposlite_debit["jioposlite_d"]} 
    if jioposlite_total_balance["jioposlite1"] == None: 
        xx6 = float(0) 
    else:
        xx6 = float(jioposlite_total_balance["jioposlite1"])
    if jioposlite_total_balance["jioposlite2"] == None:
        yy6 = float(0)
    else:
        yy6 = float(jioposlite_total_balance["jioposlite2"]) 
    jioposlite_balance = (xx6-yy6)
    mohancanarabank_credit = account_database.objects.filter(credit_debit="credit", account="Mohan CanaraBank").aggregate(mohancanarabank_c=Sum('amount'))
    mohancanarabank_debit = account_database.objects.filter(credit_debit="debit", account="Mohan CanaraBank").aggregate(mohancanarabank_d=Sum('amount'))
    mohancanarabank_total_balance = {"mohancanarabank1": mohancanarabank_credit["mohancanarabank_c"], "mohancanarabank2": mohancanarabank_debit["mohancanarabank_d"]} 
    if mohancanarabank_total_balance["mohancanarabank1"] == None: 
        xx7 = float(0) 
    else:
        xx7 = float(mohancanarabank_total_balance["mohancanarabank1"])
    if mohancanarabank_total_balance["mohancanarabank2"] == None:
        yy7 = float(0)
    else:
        yy7 = float(mohancanarabank_total_balance["mohancanarabank2"]) 
    mohancanarabank_balance = (xx7-yy7)
    paynearby_credit = account_database.objects.filter(credit_debit="credit", account="PayNearBy").aggregate(paynearby_c=Sum('amount'))
    paynearby_debit = account_database.objects.filter(credit_debit="debit", account="PayNearBy").aggregate(paynearby_d=Sum('amount'))
    paynearby_total_balance = {"paynearby1": paynearby_credit["paynearby_c"], "paynearby2": paynearby_debit["paynearby_d"]} 
    if paynearby_total_balance["paynearby1"] == None: 
        xx8 = float(0) 
    else:
        xx8 = float(paynearby_total_balance["paynearby1"])
    if paynearby_total_balance["paynearby2"] == None:
        yy8 = float(0)
    else:
        yy8 = float(paynearby_total_balance["paynearby2"]) 
    paynearby_balance = (xx8-yy8)
    sbimohan_credit = account_database.objects.filter(credit_debit="credit", account="SBI Mohan").aggregate(sbimohan_c=Sum('amount'))
    sbimohan_debit = account_database.objects.filter(credit_debit="debit", account="SBI Mohan").aggregate(sbimohan_d=Sum('amount'))
    sbimohan_total_balance = {"sbimohan1": sbimohan_credit["sbimohan_c"], "sbimohan2": sbimohan_debit["sbimohan_d"]} 
    if sbimohan_total_balance["sbimohan1"] == None: 
        xx9 = float(0) 
    else:
        xx9 = float(sbimohan_total_balance["sbimohan1"])
    if sbimohan_total_balance["sbimohan2"] == None:
        yy9 = float(0)
    else:
        yy9 = float(sbimohan_total_balance["sbimohan2"]) 
    sbimohan_balance = (xx9-yy9)
    total_amount = (cash_balance + epayon_balance + iobmohan_balance + ibgayathri_balance + ibmohan_balance + jioposlite_balance + mohancanarabank_balance + paynearby_balance + sbimohan_balance)
    context = {"account1": cash_balance, "account2": epayon_balance, "account3": iobmohan_balance, "account4": ibgayathri_balance, "account5": ibmohan_balance, "account6": jioposlite_balance, "account7": mohancanarabank_balance, "account8": paynearby_balance, "account9": sbimohan_balance, "tot": total_amount}
    return render(request, "total_account_report.html", context)

def balanceUpdate_page(request, id, date):
    balance_update = balance_sheet.objects.get(id=id)
    cash_credit = account_database.objects.filter(date__range=("2023-06-10", date), credit_debit="credit", account="Cash").aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(date__range=("2023-06-10", date), credit_debit="debit", account="Cash").aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
    if cash_total_balance["cash1"] == None: 
        xx = float(0) 
    else:
        xx = float(cash_total_balance["cash1"])
    if cash_total_balance["cash2"] == None:
        yy = float(0)
    else:
        yy = float(cash_total_balance["cash2"]) 
    cash_balance = xx - yy
    context = {"bal_update": balance_update, "bal_date": date, "amount": cash_balance}
    return render(request, "cash_balance_check_update.html", context)

def cre_list(nam):
    cash_credit = account_database.objects.filter(category="Money return", name=nam).aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(category="For credit", name=nam).aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
    if cash_total_balance["cash1"] == None: 
        xx = float(0) 
    else:
        xx = float(cash_total_balance["cash1"])
    if cash_total_balance["cash2"] == None:
        yy = float(0)
    else:
        yy = float(cash_total_balance["cash2"]) 
    cash_balance = yy - xx
    context = {"bal_list": cash_balance}
    return context

def credit_list(request):
    balanceList_names = dict()
    name_list = category_list.objects.filter(category="Names").values("category_names")
    for x in name_list:
        apple = cre_list(x["category_names"])
        balanceList_names[x["category_names"]] = apple["bal_list"]

    lst = list()
    for key, val in list(balanceList_names.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    credit_balance_count = 0
    lst1 = list()
    for val, key in lst:
        lst1.append((key, val))
        credit_balance_count = credit_balance_count + val
    converted_dict = dict(lst1)
    context = {"balance_list": converted_dict, "total_bal_amount": credit_balance_count}
    return render(request, "credit_list.html", context)    

def advance_filter_view(request):
    category1 = category_list.objects.filter(category="Names").order_by('category_names').values() 
    category2 = category_list.objects.filter(category="Credit/Debit").order_by('category_names').values() 
    category3 = category_list.objects.filter(category="TransactionType").order_by('category_names').values() 
    category4 = category_list.objects.filter(category="Account").order_by('category_names').values() 
    context = {"cate_names": category1, "cate_credit_debit": category2, "cate_transactiontype": category3, "cate_account": category4}
    return render(request, "advance_filter_view.html", context)

def advanceFilter(request):
    x_date1 = request.POST["date1"]
    x_date2 = request.POST["date2"]
    x_credit_debit = request.POST["credit_debit"]
    x_category = request.POST["category"]
    x_account = request.POST["account"]
    x_name = request.POST["name"]

    list_names = list()
    category1 = category_list.objects.filter(category="Names").order_by('category_names').values() 
    if x_name == "All":
        for cat_list1 in category1:
            list_names.append(cat_list1["category_names"])
    else:
        list_names.clear()
        list_names.append(x_name)

    list_creditDebit = list()
    category2 = category_list.objects.filter(category="Credit/Debit").order_by('category_names').values() 
    if x_credit_debit == "All":
        for cat_list2 in category2:
            list_creditDebit.append(cat_list2["category_names"])
    else:
        list_creditDebit.clear()
        list_creditDebit.append(x_credit_debit)
        
    list_category = list()
    category3 = category_list.objects.filter(category="TransactionType").order_by('category_names').values() 
    if x_category == "All":
        for cat_list3 in category3:
            list_category.append(cat_list3["category_names"])
    else:
        list_category.clear()
        list_category.append(x_category)
        
    list_account = list()
    category4 = category_list.objects.filter(category="Account").order_by('category_names').values() 
    if x_account == "All":
        for cat_list4 in category4:
            list_account.append(cat_list4["category_names"])
    else:
        list_account.clear()
        list_account.append(x_account)

    database_filter = account_database.objects.filter(date__range=(x_date1, x_date2)).filter(name__in=list_names).filter(account__in=list_account).filter(credit_debit__in=list_creditDebit).filter(category__in=list_category).order_by("date").values()
    database_filterCount = account_database.objects.filter(date__range=(x_date1, x_date2)).filter(name__in=list_names).filter(account__in=list_account).filter(credit_debit__in=list_creditDebit).filter(category__in=list_category).count()
    context = {"daily_account_entry_filter": database_filter, "coun1": database_filterCount}
    return render(request, "Advance_filter_report.html", context)

def account_entry_update(request, id):
    category1 = category_list.objects.filter(category="Names").order_by('category_names').values() 
    category2 = category_list.objects.filter(category="Credit/Debit").order_by('category_names').values() 
    category3 = category_list.objects.filter(category="TransactionType").order_by('category_names').values() 
    category4 = category_list.objects.filter(category="Account").order_by('category_names').values() 
    update_database = account_database.objects.get(id=id)
    context = {"updateItem": update_database, "cate_names": category1, "cate_credit_debit": category2, "cate_transactiontype": category3, "cate_account": category4}
    return render(request, "updateAccountEntry.html", context)

def updateAccountEntry(request, id):
    update_account_database = account_database.objects.get(id=id)
    x_credit_debit = request.POST["credit_debit"]
    x_category = request.POST["category"]
    x_account = request.POST["account"]
    x_particular = request.POST["particular"]
    x_name = request.POST["name"]
    x_amount = request.POST["amount"]
    x_notes = request.POST["notes"]
    update_account_database.credit_debit = x_credit_debit
    update_account_database.category = x_category
    update_account_database.account = x_account
    update_account_database.particular = x_particular
    update_account_database.name = x_name
    update_account_database.amount = x_amount
    update_account_database.notes = x_notes
    update_account_database.save()

def daily_acc_update1(request, id):
    updateAccountEntry(request, id)
    return redirect("/account_entry_report")

def daily_acc_update2(request, id):
    updateAccountEntry(request, id)
    return redirect("/auto_close")

def balance_checkUpdate(request, id):
    balance_update = balance_sheet.objects.get(id=id)
    x_amount = request.POST["amount"]
    x_rs500 = request.POST["rs500"]
    x_rs200 = request.POST["rs200"]
    x_rs100 = request.POST["rs100"]
    x_rs50 = request.POST["rs50"]
    x_rs20 = request.POST["rs20"]
    x_rs10 = request.POST["rs10"]
    x_rs5 = request.POST["rs5"]
    x_rs2 = request.POST["rs2"]
    x_rs1 = request.POST["rs1"]
    x_total_amount = request.POST["total_amount"]
    x_balance_amount = request.POST["balance_amount"]    
    x_status = request.POST["status"]
    balance_update.amount = x_amount
    balance_update.rs500 = x_rs500
    balance_update.rs200 = x_rs200
    balance_update.rs100 = x_rs100
    balance_update.rs50 = x_rs50
    balance_update.rs20 = x_rs20
    balance_update.rs10 = x_rs10
    balance_update.rs5 = x_rs5
    balance_update.rs2 = x_rs2
    balance_update.rs1 = x_rs1
    balance_update.total_amount = x_total_amount
    balance_update.balance_amount = x_balance_amount
    balance_update.status = x_status
    balance_update.save()
    return redirect("/balance_view")

def auto_close(request):
    return render(request, "autoClose.html")

def difference_list(request, category1, category2):
    balanceList_names = dict()
    name_list = category_list.objects.filter(category="Names").values("category_names")
    for x in name_list:
        apple = x["category_names"]
        cash_credit = account_database.objects.filter(category=category1, name=apple).aggregate(cash_c=Sum('amount'))
        cash_debit = account_database.objects.filter(category=category2, name=apple).aggregate(cash_d=Sum('amount'))
        cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
        if cash_total_balance["cash1"] == None: 
            xx = float(0) 
        else:
            xx = float(cash_total_balance["cash1"])
        if cash_total_balance["cash2"] == None:
            yy = float(0)
        else:
            yy = float(cash_total_balance["cash2"]) 
        cash_balance = xx - yy
        balanceList_names[apple] = cash_balance

    lst = list()
    for key, val in list(balanceList_names.items()):
        lst.append((val, key))
    lst.sort(reverse=True)

    lst1 = list()
    for val, key in lst:
        lst1.append((key, val))
    converted_dict = dict(lst1)
    cate = category1 + " / " + category2
    context = {"balance_list": converted_dict, "cate1": cate}
    return render(request, "difference_list.html", context)    

