from django.shortcuts import render

# Create your views here.
def subtraction(request):
    if request.method == "GET":
        return render(request,'subtraction.html')
    elif request.method == "POST":
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        result = int(num1)-int(num2)
        print(result)
        context = {}
        context['res']=result
        return render(request,'subtraction.html',context)
