from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def api_root(self, request):
        return Response({"url": "http://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"})

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=False, methods=['get'])
    def api_root(self, request):
        return Response({"url": "http://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"})

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def api_root(self, request):
        return Response({"url": "http://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"})

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    @action(detail=False, methods=['get'])
    def api_root(self, request):
        return Response({"url": "http://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"})

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=False, methods=['get'])
    def api_root(self, request):
        return Response({"url": "http://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"})
