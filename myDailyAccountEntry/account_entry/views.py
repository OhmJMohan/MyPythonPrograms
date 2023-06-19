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

def sample1(request):
    cash_credit = account_database.objects.filter(credit_debit="Credit", account="Cash").aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(credit_debit="Debit", account="Cash").aggregate(cash_d=Sum('amount'))
    cash_total_balance = float(cash_credit["cash_c"])-float(cash_debit["cash_d"])
    epayon_credit = account_database.objects.filter(credit_debit="Credit", account="EPayOn").aggregate(epayon_c=Sum('amount'))
    epayon_debit = account_database.objects.filter(credit_debit="Debit", account="EPayOn").aggregate(epayon_d=Sum('amount'))
    epayon_total_balance = float(epayon_credit["epayon_c"])-float(epayon_debit["epayon_d"])
    iobmohan_credit = account_database.objects.filter(credit_debit="Credit", account="IOB Mohan").aggregate(iobmohan_c=Sum('amount'))
    iobmohan_debit = account_database.objects.filter(credit_debit="Debit", account="IOB Mohan").aggregate(iobmohan_d=Sum('amount'))
    iobmohan_total_balance = float(iobmohan_credit["iobmohan_c"])-float(iobmohan_debit["iobmohan_d"])
    ibgayathri_credit = account_database.objects.filter(credit_debit="Credit", account="Indian bank Gayathri").aggregate(ibgayathri_c=Sum('amount'))
    ibgayathri_debit = account_database.objects.filter(credit_debit="Debit", account="Indian bank Gayathri").aggregate(ibgayathri_d=Sum('amount'))
    ibgayathri_total_balance = float(ibgayathri_credit["ibgayathri_c"])-float(ibgayathri_debit["ibgayathri_d"])
    ibmohan_credit = account_database.objects.filter(credit_debit="Credit", account="Indian bank Mohan").aggregate(ibmohan_c=Sum('amount'))
    ibmohan_debit = account_database.objects.filter(credit_debit="Debit", account="Indian bank Mohan").aggregate(ibmohan_d=Sum('amount'))
    ibmohan_total_balance = float(ibmohan_credit["ibmohan_c"])-float(ibmohan_debit["ibmohan_d"])
    jioposlite_credit = account_database.objects.filter(credit_debit="Credit", account="JioPosLite").aggregate(jioposlite_c=Sum('amount'))
    jioposlite_debit = account_database.objects.filter(credit_debit="Debit", account="JioPosLite").aggregate(jioposlite_d=Sum('amount'))
    jioposlite_total_balance = float(jioposlite_credit["jioposlite_c"])-float(jioposlite_debit["jioposlite_d"])
    canarabank_credit = account_database.objects.filter(credit_debit="Credit", account="Mohan CanaraBank").aggregate(canarabank_c=Sum('amount'))
    canarabank_debit = account_database.objects.filter(credit_debit="Debit", account="Mohan CanaraBank").aggregate(canarabank_d=Sum('amount'))
    canarabank_total_balance = float(canarabank_credit["canarabank_c"])-float(canarabank_debit["canarabank_d"])
    paynearby_credit = account_database.objects.filter(credit_debit="Credit", account="PayNearBy").aggregate(paynearby_c=Sum('amount'))
    paynearby_debit = account_database.objects.filter(credit_debit="Debit", account="PayNearBy").aggregate(paynearby_d=Sum('amount'))
    paynearby_total_balance = float(paynearby_credit["paynearby_c"])-float(paynearby_debit["paynearby_d"])
    sbi_credit = account_database.objects.filter(credit_debit="Credit", account="SBI Mohan").aggregate(sbi_c=Sum('amount'))
    sbi_debit = account_database.objects.filter(credit_debit="Debit", account="SBI Mohan").aggregate(sbi_d=Sum('amount'))
    sbi_total_balance = float(sbi_credit["sbi_c"])-float(sbi_debit["sbi_d"])
    context ={"account1": cash_total_balance, "account2": epayon_total_balance, "account3": iobmohan_total_balance, "account4": ibgayathri_total_balance, "account5": ibmohan_total_balance, "account6": jioposlite_total_balance, "account7": canarabank_total_balance, "account8": paynearby_total_balance, "account9": sbi_total_balance}
    return render(request, "sample.html", context)

def sample2(request):
    cash_credit = account_database.objects.filter(credit_debit="credit", account="JioPosLite").aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(credit_debit="debit", account="JioPosLite").aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": cash_credit["cash_c"], "cash2": cash_debit["cash_d"]} 
    balance = cash_total_balance["cash1"]
    epay_credit = account_database.objects.filter(credit_debit="credit", account="EPayOn").aggregate(cash_c=Sum('amount'))
    epay_debit = account_database.objects.filter(credit_debit="debit", account="EPayOn").aggregate(cash_d=Sum('amount'))
    epay_total_balance = {"cash1": float(epay_credit["cash_c"]), "cash2": float(epay_debit["cash_d"])} 
    balance1 = (epay_total_balance["cash1"]-epay_total_balance["cash2"]) 
    context ={"account1": cash_total_balance, "cred": cash_credit["cash_c"], "bal": balance, "bal1": balance1}
    return render(request, "sample.html", context)

def sample(request):
    account_list = account_database.objects.all().values()
    cash_credit = account_database.objects.filter(credit_debit="credit", account="Cash").aggregate(cash_c=Sum('amount'))
    cash_debit = account_database.objects.filter(credit_debit="debit", account="Cash").aggregate(cash_d=Sum('amount'))
    cash_total_balance = {"cash1": float(cash_credit["cash_c"]), "cash2": float(cash_debit["cash_d"])} 
    balance = (cash_total_balance["cash1"]-cash_total_balance["cash2"])+8000
    context = {"account": account_list, "bal": balance}
    return render(request, "sample.html", context)