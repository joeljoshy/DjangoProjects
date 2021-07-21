from django.shortcuts import render


# Create your views here.
def multiplication(request):
    if request.method == "GET":
        return render(request, 'multiplication.html')
    elif request.method == "POST":
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        result = int(num1) * int(num2)
        print(result)
        context = {'res': result}
        return render(request, 'multiplication.html', context)
