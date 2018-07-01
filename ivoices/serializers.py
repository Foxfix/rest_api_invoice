from rest_framework import serializers
from ivoices.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Invoice
		fields = ('name', 'description', 'total', 'paid')

