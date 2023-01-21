from rest_framework import viewsets
from .models import Survivor
from .serializers import SurvivorSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.decorators import action
from django.db.models import Sum

class SurvivorViewSet(viewsets.ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['put'])
    def make_trade(self, request, *args, **kwargs):
        data = dict(request.data)
        survivor1 = Survivor.objects.filter(~Q(pk=int(request.data["survivor1"])), infected=False).first()
        survivor2 = Survivor.objects.filter(~Q(pk=int(request.data["survivor2"])), infected=False).first()

        if survivor1==None or survivor2==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        items1 = data["survivor1_items"]
        items2 = data["survivor2_items"]
        survivor1_points = Survivor.calculate_points(
                int(items1[0]),
                int(items1[1]),
                int(items1[2]),
                int(items1[3]),
            )
        survivor2_points = Survivor.calculate_points(
                int(items2[0]),
                int(items2[1]),
                int(items2[2]),
                int(items2[3]),
            )
        
        if survivor1.points < survivor1_points or survivor2.points < survivor2_points:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if survivor1_points != survivor2_points:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        items = {
            'water': 0,
            'food': 1,
            'medication': 2,
            'ammunition': 3
        }

        for survivor in (survivor1, survivor2):
            for item, index in items.items():
                setattr(survivor, item, getattr(survivor, item) - int(eval(f'items{1 if survivor == survivor1 else 2}[{index}]')))

        for survivor in (survivor1, survivor2):
            for item, index in items.items():
                setattr(survivor, item, getattr(survivor, item) + int(eval(f'items{2 if survivor == survivor1 else 1}[{index}]')))
                
        survivor1.save()
        survivor2.save()

        print(data)

        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=['put'])
    def report_infected(self, request, *args, **kwargs):
        survivor_reported = self.get_object()
        if survivor_reported.infected:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Survivor already infected'})
        survivors = Survivor.objects.filter(~Q(pk=survivor_reported.pk), infected=False)
        for survivor in survivors:
            if (survivor.latitude-request.data["latitude"])**2 + (survivor.longitude-request.data["longitude"])**2 <= 0.1:
                survivor.reports += 1
                if survivor.reports >= 3:
                    survivor.infected = True
                survivor.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def get_resources_report(self, request, *args, **kwargs):
        total_population = Survivor.objects.count()
        infected_population = Survivor.objects.filter(infected=True).count()
        non_infected_population = total_population - infected_population

        resources = {}
        for resource in Survivor.ITEMS:
            resources[resource] = {}
            resources[resource]["total"] = Survivor.objects.aggregate(Sum(resource))["{}__sum".format(resource)]
            resources[resource]["average"] = resources[resource]["total"] / total_population

        return Response(data={
            "population": {
                "total": total_population,
                "infected": infected_population,
                "non_infected": non_infected_population,
                "percent_infected": (infected_population / total_population) * 100
            },
            "resources": resources
        })