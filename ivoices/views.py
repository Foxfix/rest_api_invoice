from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ivoices.models import Invoice
from ivoices.serializers import InvoiceSerializer


@api_view(["GET"])
def invoice_list(request):
	if request.method == 'GET':
		invoices = Invoice.objects.all()
		serializer = InvoiceSerializer(invoices, many=True)
		return Response(serializer.data)


@api_view(["GET"])
def invoice_detail(request, pk):
	try:
		invoice = Invoice.objects.get(pk=pk)
	except Invoice.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	serializer = InvoiceSerializer(invoice)
	return Response(serializer.data)

