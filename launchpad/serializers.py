from rest_framework import serializers
from registry.models import Activity, AircraftComponentSignature, Operator, Contact, Aircraft, AircraftDetail, Pilot, Address, Person, Manufacturer, Firmware, Contact, Pilot, Authorization, AircraftComponent
from gcs_operations.models import FlightPlan
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class PersonSerializer(serializers.ModelSerializer):         
    class Meta:
        model = Person
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Manufacturer
        fields = '__all__'

class FirmwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firmware
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class AuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorization
        fields = '__all__'

class AircraftDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftDetail
        fields = '__all__'

class FlightPlanReadSerializer(serializers.ModelSerializer):
    ''' A serializer for Flight Operations '''
    class Meta:
        model = FlightPlan	
        exclude = '__all__'
        ordering = ['-created_at']

class AircraftComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftComponent
        exclude = ('is_active', 'supplier_part_id', 'name',)

class AircraftComponentSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftComponentSignature
        fields = '__all__'
