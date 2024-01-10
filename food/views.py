from django.shortcuts import render

from .models import Food, Order


def order_food(request):
    foods = Food.objects.all()
    # if request.method == "POST":
    #     food = request.POST.get("food")
    #     count = request.POST.get("count")
    #     user_id = request.POST.get("user_id")
    #     user_name = request.POST.get("user_name")
    #     my_food = Food.objects.filter(name=food)
    #     try:
    #         food = my_food.first()
    #         total = food.price * int(count)
    #         Order.objects.create(
    #             food=food,
    #             count=int(count),
    #             price=total,
    #             user_id=int(user_id),
    #             user_name=user_name,
    #         )
    #     except Exception as e:
    #         print(e)
    return render(request, "index.html", {
        "foods": foods
    })