from rest_framework import viewsets
from .models import Alert, Irregularity, Jams, Segment, AlertRecord, IrregularityRecord, JamRecord
from .serializers import AlertSerializer, IrregularitySerializer, JamsSerializer, SegmentSerializer, AlertRecordSerializer, IrregularityRecordSerializer, JamRecordSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class IrregularityViewSet(viewsets.ModelViewSet):
    queryset = Irregularity.objects.all()
    serializer_class = IrregularitySerializer

class JamsViewSet(viewsets.ModelViewSet):
    queryset = Jams.objects.all()
    serializer_class = JamsSerializer

class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer

class AlertRecordViewSet(viewsets.ModelViewSet):
    queryset = AlertRecord.objects.all()
    serializer_class = AlertRecordSerializer

class IrregularityRecordViewSet(viewsets.ModelViewSet):
    queryset = IrregularityRecord.objects.all()
    serializer_class = IrregularityRecordSerializer

class JamRecordViewSet(viewsets.ModelViewSet):
    queryset = JamRecord.objects.all()
    serializer_class = JamRecordSerializer
