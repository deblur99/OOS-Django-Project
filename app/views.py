from django.shortcuts import render

# Create your views here.
def main_page(request):
  context = {'message': 'hello world!'}
  return render(request, 'main_page.html', context)


def search_result(request):
  context = {'message': 'hello world!'}
  return render(request, 'search_result_page.html', context)


def product_detail(request):
  context = {'message': 'hello world!'}
  return render(request, 'product_detail_page.html', context)
