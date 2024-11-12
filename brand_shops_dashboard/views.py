from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect,FileResponse,JsonResponse
from .models import *
from .form import *
from collections import Counter
from django.contrib import messages
import json

def home(request):

	
	if Brand.objects.all() :


		brand_obj=Brand.objects.filter(geometry__isnull=False)[:5]

		for obj in brand_obj:
			try:
				location = obj.geometry.split('(')[1].split(')')[0].split(', ')
				obj.latitude = location[0]
				obj.longitude = location[1]
			except:
				try:
					obj.latitude, obj.longitude = obj.geometry.split(', ')
				except:
					obj.latitude, obj.longitude = None, None
				

		shop_counts_by_brands = Brand.objects.filter(brand__isnull=False,).values('brand').annotate(shop_count=models.Count('brand')).order_by('-shop_count')[:5]
		
	
		brand_names = [item['brand'] for item in shop_counts_by_brands]
		brand_counts = [item['shop_count'] for item in shop_counts_by_brands]

		brands_brand_names = [brand.title() for brand in brand_names]

		shop_counts_by_city = Brand.objects.filter(city__isnull=False).values('city').annotate(shop_count=models.Count('city')).order_by('-shop_count')[:5]
		
		city_shop_count = [obj['shop_count'] for obj in shop_counts_by_city]
		city_city_names = [obj['city'].title() if 'city' in obj and isinstance(obj['city'], str) else obj['city'] for obj in shop_counts_by_city]


		context={'brands_shop_count':brand_counts,'brands_brand_names':brands_brand_names,'city_shop_count':city_shop_count,'city_city_names':city_city_names, 'brand_obj':brand_obj}
		return render(request, 'home.html',context)
	else:
		return render(request, 'home.html')



def manage_brands(request):
	brand_obj=Brand.objects.all()
	context={'brand_obj':brand_obj}
	return render(request, 'manage_brands.html',context)


def get_city_list(request):

	if request.method == 'POST':
		ajax_data = json.loads(request.body.decode("utf-8"))
		keyword = ajax_data["keyword"].strip()

		if keyword:
			city_list = City.objects.filter(city_name__icontains=keyword)
			city_list = {i.city_id:i.city_name.title() for i in city_list}
			
			return JsonResponse(city_list)

		else:
			return HttpResponse('')




def create_brands(request):
	form=BrandForm()
	if request.method=='POST':
		form=BrandForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('manage_brands')
	context={'form':form}
	return render(request, 'create_update_brands.html',context)




def update_brands(request,osm_id):
	brand_obj=Brand.objects.filter(osm_id=osm_id).first() # it is query used for fetching data from Brand table in database and filter is used for filtering data where osm_id is equal to osm_id and first is used for fetching first data

	if brand_obj:
		form=updateBrandForm(instance=brand_obj)
		if request.method=='POST':
			form=updateBrandForm(request.POST,instance=brand_obj)
			if form.is_valid():
				form.save()
				return redirect('manage_brands')

		context={'form':form}
		return render(request, 'create_update_brands.html',context)
		
	return render(request, 'create_update_brands.html')


def view_brands(request,osm_id):
	brand_obj=Brand.objects.filter(osm_id=osm_id).first()
	if brand_obj:
		if brand_obj.geometry:
			try:
				lat_long = brand_obj.geometry.split('(')[1].split(')')[0].split(', ')
				latitude = lat_long[0]
				longitude = lat_long[1]
			except:
				try:
					latitude, longitude = brand_obj.geometry.split(', ')
				except:
					latitude, longitude = None, None
		else:
			latitude = ''
			longitude = ''
			
		brand_model_field_labels = {field.name: field.verbose_name for field in Brand._meta.fields}
		
		context={'brand_obj':brand_obj,'latitude':latitude.strip(),'longitude':longitude.strip(),'field_labels':brand_model_field_labels}
		return render(request, 'view_brands.html',context)
	return render(request, 'view_brands.html')



# dynamic_form/views.py



def dynamic_form(request):
	form = DynamicForm()
	return render(request, 'form.html', {'form': form})


from django.http import JsonResponse

def get_subcategories(request):
	category = request.GET.get('category')
	print('category', category, 'type', type(category), 'len', len(category))
	# You can fetch subcategories based on the selected category here
	subcategories = {
		'shoes': {
			'formal': 'Formal',
			'sports': 'Sports',
			'casual': 'Casual',
		},
		'Clothing': {
			'formal': 'Formal',
			'casual': 'Casual',
		},
		'Food': {
			'fast_food': 'Fast Food',
			'fine_dining': 'Fine Dining',
		},
		'Electronics': {
			'home_appliances': 'Home Appliances',
			'gadgets': 'Gadgets',
		},
	}

	filtered_subcategories = subcategories.get(category, {})
	print('filtered_subcategories', filtered_subcategories)


	return JsonResponse({'subcategories': filtered_subcategories})