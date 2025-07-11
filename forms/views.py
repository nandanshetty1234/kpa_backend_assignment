from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer


class WheelSpecificationCreateView(APIView):
    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WheelSpecificationListView(APIView):
    def get(self, request):
        queryset = WheelSpecification.objects.all()

        form_number = request.query_params.get('formNumber')
        submitted_by = request.query_params.get('submittedBy')
        submitted_date = request.query_params.get('submittedDate')

        if form_number:
            queryset = queryset.filter(formNumber=form_number)
        if submitted_by:
            queryset = queryset.filter(submittedBy=submitted_by)
        if submitted_date:
            queryset = queryset.filter(submittedDate=submitted_date)

        serializer = WheelSpecificationSerializer(queryset, many=True)
        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)