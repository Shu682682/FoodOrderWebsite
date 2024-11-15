from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE

class MenuList(generic.ListView):
    queryset=Item.objects.order_by("-date_created")
    template_name = "index.html"
    
    def get_context_data(self,**kwargs):#sent python code to html 
            context = super().get_context_data(**kwargs)
            context["meals"] = MEAL_TYPE
            return context
    

class MenuItemDetail(generic.DetailView):
    #model=predefine varible name
    model=Item
    template_name="menu_item_detail.html"
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
    
        print(f"Message from {name}, Email: {email}, Message: {message}")
        
        return render(request, 'contact.html', {'success': True})
    
    return render(request, 'contact.html')