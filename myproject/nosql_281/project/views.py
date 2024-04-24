# views.py in your Django app (e.g., project/views.py)

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
from bson import ObjectId


# Helper function to convert query results from MongoDB to JSON serializable format
def serialize_document(document):
    for key, value in document.items():
        if isinstance(value, ObjectId):
            document[key] = str(value)  # Convert ObjectId to string
    return document

class AVVehicleList(APIView):
    def get(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        vehicles = list(db.AVVehicle.find({}))
        vehicles = [serialize_document(vehicle) for vehicle in vehicles]  # Serialize each vehicle document

        client.close()
        return Response(vehicles)

    def post(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        result = db.av_vehicle.insert_one(request.data)
        client.close()
        if result.acknowledged:
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class SensorList(APIView):
    def get(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        sensors = list(db.Sensor.find({}))
        sensors = [serialize_document(sensor) for sensor in sensors]
        client.close()
        return Response(sensors)

    def post(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        result = db.sensor.insert_one(request.data)
        client.close()
        if result.acknowledged:
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class TripList(APIView):
    def get(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        trips = list(db.Trip.find({}))
        trips = [serialize_document(trip) for trip in trips]
        client.close()
        return Response(trips)

    def post(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        result = db.trip.insert_one(request.data)
        client.close()
        if result.acknowledged:
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class DataList(APIView):
    def get(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        data = list(db.Data.find({}))
        data = [serialize_document(datum) for datum in data]
        client.close()
        return Response(data)

    def post(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_NAME]
        result = db.data.insert_one(request.data)
        client.close()
        if result.acknowledged:
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
