from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from rest_framework import generics
from .models import Transaction
from django.views.decorators.csrf import csrf_exempt
from .serializers import TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status


# Create your views here

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)




@api_view(['POST'])
def add_items(request):
	transaction = TransactionSerializer(data=request.data)

	# validating for already existing data
	if Transaction.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if transaction.is_valid():
		transaction.save()
		return Response(transaction.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_items(request):
	
	
	# checking for the parameters from the URL
	if request.query_params:
		items = Transaction.objects.filter(**request.query_params.dict())
	else:
		items = Transaction.objects.all()

	# if there is something in items else raise error
	if items:
		serializer = TransactionSerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def viewitems(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Transaction.objects.filter(**request.query_params.dict())
    else:
        items = Transaction.objects.all()

    # Get the item with the highest amount
    highest_amount_item = items.order_by('-amount').first()

    # Serialize the item
    serializer = TransactionSerializer(highest_amount_item)

    # Return the serialized item
    return Response(serializer.data)     
      




@api_view(['POST'])
def update_items(request, pk):
	transaction = Transaction.objects.get(pk=pk)
	data = TransactionSerializer(instance=transaction, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
	transaction = get_object_or_404(Transaction, pk=pk)
	transaction.delete()
	return Response(status=status.HTTP_202_ACCEPTED)


















class TransactionListAPIView(APIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



def index(request):
    return render(request,'index.html')  



def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username=username,password=Password)

        if user is not None:
            auth.login(request, user)
            return redirect('/expense')

        else:
            return redirect('/')   




    else:
        return render(request,'login.html')




def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        Email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        user = User.objects.create_user(username=username,password=Password1,email=Email)
        user.save()
        print('user created')
        return redirect('/')

    else:    
        return render(request,'registration.html')






def expense(request):
    return render(request,'expense.html')      
           


