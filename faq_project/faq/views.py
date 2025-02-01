"""
from rest_framework.response import Response
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        faqs = FAQ.objects.all()  # ✅ Fetch all FAQ objects
        serializer = FAQSerializer(faqs, many=True)  # ✅ Serialize the data
        return Response(serializer.data)  # ✅ Return the serialized data
"""

"""
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    serializer_class = FAQSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language', None)
        
        if language == 'hi':
            # Filter FAQs for Hindi (exclude Bengali)
            return FAQ.objects.filter(question_hi__isnull=False).exclude(question_bn__isnull=False)
        
        elif language == 'bn':
            # Filter FAQs for Bengali (exclude Hindi)
            return FAQ.objects.filter(question_bn__isnull=False).exclude(question_hi__isnull=False)
        
        # If no language is specified, return all FAQs
        return FAQ.objects.all()

    def list(self, request, *args, **kwargs):
        faqs = self.get_queryset()  # Get the filtered FAQ objects based on language
        serializer = FAQSerializer(faqs, many=True)  # Serialize the data
        return Response(serializer.data)  # Return the serialized data
"""
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    serializer_class = FAQSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language', None)

        if language == 'hi':
            # Filter FAQs for Hindi (where `question_hi` and `answer` are not null)
            return FAQ.objects.filter(Q(question_hi__isnull=False) & Q(answer__isnull=False))

        elif language == 'bn':
            # Filter FAQs for Bengali (where `question_bn` and `answer` are not null)
            return FAQ.objects.filter(Q(question_bn__isnull=False) & Q(answer__isnull=False))

        # If no language is specified, return all FAQs
        return FAQ.objects.all()

    def list(self, request, *args, **kwargs):
        faqs = self.get_queryset()  # Get the filtered FAQ objects based on language
        serializer = FAQSerializer(faqs, many=True)  # Serialize the data
        return Response(serializer.data)  # Return the serialized data
