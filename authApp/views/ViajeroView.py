from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from authApp.models.user import Usuarios

from authApp.models.Productos import Productos
import json

# Create your views here.
class ProductosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

    def get(self,request,pro_id=0):
        if (pro_id>0):
            Product=list(Productos.objects.filter(pro_id=pro_id).values())
            if len(Product) > 0:
                productos=Product[0]
                datos={'Product':productos}
            else:
              datos={'message':'Product not found'}
            return JsonResponse(datos)
        else:
            Product=list(Productos.objects.values())
            if len(Product)>0:
              datos={'Product':Product}
            else:
              datos={'message':'Product not found'}
            return JsonResponse(datos)

    def post(self,request):
       #print(request.body)
       jd= json.loads(request.body)
       #print(jd)
       Productos.objects.create(pro_name=jd['pro_name'],pro_provider=jd['pro_provider'],pro_existences=jd['pro_existences'],pro_date=jd['pro_date'],pro_description=jd['pro_description'],pro_category=jd['pro_category'])
       datos={'message':"Success"}
       return JsonResponse(datos)

    def put(self,request,pro_id):
       jd = json.loads(request.body)
       Product=list(Productos.objects.filter(pro_id=pro_id).values())
       if len(Product) > 0:
              productos=Productos.objects.get(pro_id=pro_id)
              productos.pro_name=jd['pro_name']
              productos.pro_provider=jd['pro_provider']
              productos.pro_existences=jd['pro_existences']
              productos.pro_date=jd['pro_date']
              productos.pro_description=jd['pro_description']
              productos.pro_category=jd['pro_category']
              productos.save()
              datos={'message':"Success"}
       else:
              datos={'Product not found'}
       return JsonResponse(datos)
            
    def delete(self,request,pro_id):
       Product=list(Productos.objects.filter(pro_id=pro_id).values())
       if len(Product) > 0:
           Productos.objects.filter(pro_id=pro_id).delete()
           datos={'message':"Success"}
       else:
              datos={'message':'Product not found'}
       return JsonResponse(datos)