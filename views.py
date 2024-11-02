from django.shortcuts import render,redirect
from django.http import HttpResponse
from mobiles.service import client
from mobiles.models import Comment

products=[
    {
        'name':"Redmi",
        'feedbacks':[
            "It is very nice and the vae in not like Wlue of money..I'm not facing any problems till now.",
            "Operating issue softwarorst quality of camera Don't like software.",
            "The phone is too good.I prefer to buy this phone, Low Budget excellent phone."
        ],
        'sentiments':None
    },
    {
         'name':"Samsung",
        'feedbacks':[
            "Amazing... But at this price tag. .. battery should be more long lasting.",
            "The pen got damaged, after a day I received phone.",
            "This phone is good, but features are not great."
        ],
        'sentiments':None
    },
    ]

# Create your views here.
def func1(request):
    good_students=[
        {"Stname": "Noushin","mobile":1098345,"role":"DEVELOPER"},
        {"Stname": "Priyanka","mobile":2348173,"role":"DESINGER"},
        {"Stname": "Praneetha","mobile":1348793,"role":"DEBUGGER"},
        {"Stname": "Sujitha","mobile":98875136,"role":"TESTER"},
    ]
    return render(request,"index.html",{'students':good_students})

def func2(request):
    for product in products:
        print(product.get("name"))
        feedbacks=product.get("feedbacks")
        result=client.analyze_sentiment(documents=feedbacks)
        li=[]
        for feedbacks in result:
            li.append(feedbacks.sentiment)
        product['sentiments']=li   
    return render(request,"about.html",{"data":result,"input_data":products})

def func3(request):
    return render(request,"contact.html")

def func4(request):
    # if request.method == "POST":
    #     a=request.POST.get("comment")
    #     result=client.analyze_sentiment(documents=[a])
    #     x=result[0].sentiment
    #     return render(request,"form.html",{"res":a,"type":x})
    # else:
    #     return render(request,"form.html")
    
    text=request.GET.get("comment")
    if text:
        obj=Comment(msg=text,review="pending")
        obj.save()
    return render(request,"form.html")
    
def analyzeview(request):
    pendingComment=Comment.objects.filter(review="pending")
    if pendingComment:
        for everyComment in pendingComment:
            text=everyComment.msg
            result=client.analyze_sentiment(documents=[text])
            res=result[0].sentiment
            everyComment.review=res
            everyComment.save()
    return render(request,"form.html",{"result":res})