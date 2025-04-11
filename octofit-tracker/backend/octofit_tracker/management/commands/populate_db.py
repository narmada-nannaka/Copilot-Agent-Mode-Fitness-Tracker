import json
from django.core.management.base import BaseCommand
from ...models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), name='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), name='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), name='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), name='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), name='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        User.objects.bulk_create(users)

        # Create teams
        team = Team(_id=ObjectId(), name='Blue Team', members=[])
        team.save()
        for user in users:
            team.members.append(user)
        team.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=int(timedelta(hours=1).total_seconds() // 60)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=int(timedelta(hours=2).total_seconds() // 60)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=int(timedelta(hours=1, minutes=30).total_seconds() // 60)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=int(timedelta(minutes=30).total_seconds() // 60)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=int(timedelta(hours=1, minutes=15).total_seconds() // 60)),
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team, score=100),
            Leaderboard(_id=ObjectId(), team=team, score=90),
            Leaderboard(_id=ObjectId(), team=team, score=95),
            Leaderboard(_id=ObjectId(), team=team, score=85),
            Leaderboard(_id=ObjectId(), team=team, score=80),
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
