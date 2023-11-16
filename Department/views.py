from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch, Payment, PaymentOption, Demandtype, Demandrate, Bill, Customer

# Create your views here.


def home_view(request):
    return render(request, 'index.html', {})


def add_branch(request):
    if request.method == 'POST':
        bid = request.POST['BID']
        bname = request.POST['BName']
        status = request.POST['flexRadioDefault']
        form = Branch(branch_id=bid, name=bname, status_b=status)

        form.save()
        return HttpResponse('Form Valid')
    return render(request, 'Branch.html', {})


def add_payment(request):
    if request.method == 'POST' :
        
        poid = request.POST['PID']
        pname = request.POST['PNAME']
        pstatus = request.POST['PaymentOptionStatus']
        form = PaymentOption(poid=poid, name=pname, po_status=pstatus)

        form.save()
        return HttpResponse('Form Valid')
    return render(request, 'PaymentOption.html', {})


def add_demandtype(request):
    if request.method == 'POST':
        dtid = request.POST['DTID']
        description = request.POST['description']
        status = request.POST['flexRadioDefault']
        form = Demandtype(demand_type_id=dtid, description=description, status_d=status)

        form.save()
        return HttpResponse('Form Valid')
    return render(request, 'DemandType.html', {})

def add_customer(request):
    branch_id = Branch.objects.all()
    demand = Demandtype.objects.all()
    context = {'branch': branch_id,
               'demandtype': demand
               }
    if request.method == 'POST':
        scno = request.POST['SCNO']
        cusid = request.POST['CUSID']
        fname = request.POST['FullName']
        address = request.POST['Address']
        mobile = request.POST['MobileNo']
        bid = request.POST['Branch_Id']
        did = request.POST['Demand_type_ID']
        form = Customer(scno=scno, cusid=cusid, fullname=fname, address=address, mobileno=mobile, branch=Branch.objects.get(branch_id=bid), demand_type=Demandtype.objects.get(demand_type_id=did))

        form.save()
        return HttpResponse('Form Valid')
    
    return render(request, 'Customerdetail.html', context)

def add_demandrate(request):
    demand = Demandtype.objects.all()
    if request.method == 'POST':
        drid = request.POST['DRID']
        demandtypeid = request.POST['Demand_type_ID']
        rate = request.POST['Rate']
        effectivedate = request.POST['Effective_Date']
        status = request.POST['flexRadioDefault']
        form = Demandrate(drid=drid, demand_type=Demandtype.objects.get(demand_type_id=demandtypeid), rate=rate, effective_date=effectivedate, iscurrent=status)

        form.save()
        return HttpResponse('Form Valid')
    context={'demandType': demand}
    return render(request, 'DemandRate.html', context)

def add_bill(request):
    if request.method == 'POST':
        bid = request.POST['BID']
        bdate = request.POST['BDate']
        byear = request.POST['BYear']
        bmonth = request.POST['BMonth']
        cusId = request.POST['CUSId']
        creading = request.POST['crreading']
        preading = request.POST['prreading']
        bamt = request.POST['Bamt']
        
        form = Bill(bid=bid, bdate=bdate, byear=byear, bmonth=bmonth, cusid=Customer.objects.get(cusid=cusId), current_reading=creading, prev_reading=preading, bamount=bamt)
        form.save()
        return HttpResponse('Form Valid')
    return render(request, 'Bill.html', {})

def add_paymentDetails(request):
    payoption = PaymentOption.objects.all()
    if request.method == 'POST':
        pid = request.POST['PID']
        bid = request.POST['BId']
        pdate = request.POST['pdate']
        pamt = request.POST['pamt']
        ptid = request.POST['Payment_Type_ID']
        ramt = request.POST['Rebate_amt']
        famt = request.POST['Fine_amt']
        
        form = Payment(pid=pid, bid=Bill.objects.get(bid=bid), pdate=pdate, pamount=pamt, payment_type=PaymentOption.objects.get(poid=ptid), rebate_amt=ramt, fine_amt=famt)
        form.save()
        return HttpResponse('Form Valid')
    content = {'paymenttype': payoption}
    return render(request, 'PaymentDetails.html', content)

def search(request):
    if request.method== 'POST':
        cus_id=int(request.POST['CUSID'])
        obj= Customer.objects.get(cusid=cus_id)
        bill= Bill.objects.filter(cusid__cusid=cus_id)
        print(bill)

        payment=Payment.objects.filter(bid__cusid=cus_id)

        context = {'Customer': obj,'Bill': bill, 'Payment': payment }
        #,'Bill': bill, 'Payment': payment
        return render(request, 'search.html', context)
    
def usearch(request):
    return render(request,'usearch.html',{})