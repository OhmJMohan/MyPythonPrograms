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
    if cash_total_balance["cash1"] == None or cash_total_balance["cash2"] == None:
        cash_balance = float(0)
    else:
        cash_balance = float(cash_total_balance["cash1"])-float(cash_total_balance["cash2"]) 
    context = {"bal": cash_balance, "date": x_date}
    return render(request, "cash_balance_check.html", context)

def sample(request):
    account_list = account_database.objects.all().values()[20:]
    cash_credit = account_database.objects.filter(credit_debit="credit", account="Cash").aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(credit_debit="debit", account="Cash").aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
    if cash_total_balance["cash1"] == None and cash_total_balance["cash2"] == None:
        cash_balance = float(0)
    else:
        cash_balance = float(cash_total_balance["cash1"])-float(cash_total_balance["cash2"]) 
    context = {"account": account_list, "bal": cash_balance}
    return render(request, "sample.html", context)

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
    if cash_total_balance["cash1"] == None or cash_total_balance["cash2"] == None:
        cash_balance = float(0)
    else:
        cash_balance = float(cash_total_balance["cash1"])-float(cash_total_balance["cash2"]) 
    epayon_credit = account_database.objects.filter(credit_debit="credit", account="EPayOn").aggregate(epayon_c=Sum('amount'))
    epayon_debit = account_database.objects.filter(credit_debit="debit", account="EPayOn").aggregate(epayon_d=Sum('amount'))
    epayon_total_balance = {"epayon1": epayon_credit["epayon_c"], "epayon2": epayon_debit["epayon_d"]} 
    if epayon_total_balance["epayon1"] == None or epayon_total_balance["epayon2"] == None:
        epayon_balance = float(0)
    else:
        epayon_balance = float(epayon_total_balance["epayon1"])-float(epayon_total_balance["epayon2"]) 
    iobmohan_credit = account_database.objects.filter(credit_debit="credit", account="IOBMohan").aggregate(iobmohan_c=Sum('amount'))
    iobmohan_debit = account_database.objects.filter(credit_debit="debit", account="IOBMohan").aggregate(iobmohan_d=Sum('amount'))
    iobmohan_total_balance = {"iobmohan1": iobmohan_credit["iobmohan_c"], "iobmohan2": iobmohan_debit["iobmohan_d"]} 
    if iobmohan_total_balance["iobmohan1"] == None or iobmohan_total_balance["iobmohan2"] == None:
        iobmohan_balance = float(0)
    else:
        iobmohan_balance = float(iobmohan_total_balance["iobmohan1"])-float(iobmohan_total_balance["iobmohan2"]) 
    ibgayathri_credit = account_database.objects.filter(credit_debit="credit", account="Indian Bank Gayathri").aggregate(ibgayathri_c=Sum('amount'))
    ibgayathri_debit = account_database.objects.filter(credit_debit="debit", account="Indian Bank Gayathri").aggregate(ibgayathri_d=Sum('amount'))
    ibgayathri_total_balance = {"ibgayathri1": ibgayathri_credit["ibgayathri_c"], "ibgayathri2": ibgayathri_debit["ibgayathri_d"]} 
    if ibgayathri_total_balance["ibgayathri1"] == None or ibgayathri_total_balance["ibgayathri2"] == None:
        ibgayathri_balance = float(0)
    else:
        ibgayathri_balance = float(ibgayathri_total_balance["ibgayathri1"])-float(ibgayathri_total_balance["ibgayathri2"]) 
    ibmohan_credit = account_database.objects.filter(credit_debit="credit", account="Indian Bank Mohan").aggregate(ibmohan_c=Sum('amount'))
    ibmohan_debit = account_database.objects.filter(credit_debit="debit", account="Indian Bank Mohan").aggregate(ibmohan_d=Sum('amount'))
    ibmohan_total_balance = {"ibmohan1": ibmohan_credit["ibmohan_c"], "ibmohan2": ibmohan_debit["ibmohan_d"]} 
    if ibmohan_total_balance["ibmohan1"] == None or ibmohan_total_balance["ibmohan2"] == None:
        ibmohan_balance = float(0)
    else:
        ibmohan_balance = float(ibmohan_total_balance["ibmohan1"])-float(ibmohan_total_balance["ibmohan2"]) 
    jioposlite_credit = account_database.objects.filter(credit_debit="credit", account="JioPosLite").aggregate(jioposlite_c=Sum('amount'))
    jioposlite_debit = account_database.objects.filter(credit_debit="debit", account="JioPosLite").aggregate(jioposlite_d=Sum('amount'))
    jioposlite_total_balance = {"jioposlite1": jioposlite_credit["jioposlite_c"], "jioposlite2": jioposlite_debit["jioposlite_d"]} 
    if jioposlite_total_balance["jioposlite1"] == None or jioposlite_total_balance["jioposlite2"] == None:
        jioposlite_balance = float(0)
    else:
        jioposlite_balance = float(jioposlite_total_balance["jioposlite1"])-float(jioposlite_total_balance["jioposlite2"]) 
    mohancanarabank_credit = account_database.objects.filter(credit_debit="credit", account="Mohan CanaraBank").aggregate(mohancanarabank_c=Sum('amount'))
    mohancanarabank_debit = account_database.objects.filter(credit_debit="debit", account="Mohan CanaraBank").aggregate(mohancanarabank_d=Sum('amount'))
    mohancanarabank_total_balance = {"mohancanarabank1": mohancanarabank_credit["mohancanarabank_c"], "mohancanarabank2": mohancanarabank_debit["mohancanarabank_d"]} 
    if mohancanarabank_total_balance["mohancanarabank1"] == None or mohancanarabank_total_balance["mohancanarabank2"] == None:
        mohancanarabank_balance = float(0)
    else:
        mohancanarabank_balance = float(mohancanarabank_total_balance["mohancanarabank1"])-float(mohancanarabank_total_balance["mohancanarabank2"]) 
    paynearby_credit = account_database.objects.filter(credit_debit="credit", account="PayNearBy").aggregate(paynearby_c=Sum('amount'))
    paynearby_debit = account_database.objects.filter(credit_debit="debit", account="PayNearBy").aggregate(paynearby_d=Sum('amount'))
    paynearby_total_balance = {"paynearby1": paynearby_credit["paynearby_c"], "paynearby2": paynearby_debit["paynearby_d"]} 
    if paynearby_total_balance["paynearby1"] == None or paynearby_total_balance["paynearby2"] == None:
        paynearby_balance = float(0)
    else:
        paynearby_balance = float(paynearby_total_balance["paynearby1"])-float(paynearby_total_balance["paynearby2"]) 
    sbimohan_credit = account_database.objects.filter(credit_debit="credit", account="SBI Mohan").aggregate(sbimohan_c=Sum('amount'))
    sbimohan_debit = account_database.objects.filter(credit_debit="debit", account="SBI Mohan").aggregate(sbimohan_d=Sum('amount'))
    sbimohan_total_balance = {"sbimohan1": sbimohan_credit["sbimohan_c"], "sbimohan2": sbimohan_debit["sbimohan_d"]} 
    if sbimohan_total_balance["sbimohan1"] == None or sbimohan_total_balance["sbimohan2"] == None:
        sbimohan_balance = float(0)
    else:
        sbimohan_balance = float(sbimohan_total_balance["sbimohan1"])-float(sbimohan_total_balance["sbimohan2"]) 
    total_amount = (cash_balance + epayon_balance + iobmohan_balance + ibgayathri_balance + ibmohan_balance + jioposlite_balance + mohancanarabank_balance + paynearby_balance + sbimohan_balance)
    context = {"account1": cash_balance, "account2": epayon_balance, "account3": iobmohan_balance, "account4": ibgayathri_balance, "account5": ibmohan_balance, "account6": jioposlite_balance, "account7": mohancanarabank_balance, "account8": paynearby_balance, "account9": sbimohan_balance, "tot": total_amount}
    return render(request, "total_account_report.html", context)

def test_page(request, id, date):
    test_id = id
    test_date = date
    context = {"t1": test_id, "t2": test_date}
    return render(request, "sample1.html", context)

def cre_list(nam):
    cash_credit = account_database.objects.filter(category="Money return", name=nam).aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(category="For credit", name=nam).aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
    if cash_total_balance["cash1"] == None or cash_total_balance["cash2"] == None:
        cash_balance = float(0)
    else:
        cash_balance = float(cash_total_balance["cash2"])-float(cash_total_balance["cash1"]) 
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
    lst1 = list()
    for val, key in lst:
        lst1.append((key, val))
    converted_dict = dict(lst1)
    context = {"balance_list": converted_dict}
    return render(request, "credit_list.html", context)    
