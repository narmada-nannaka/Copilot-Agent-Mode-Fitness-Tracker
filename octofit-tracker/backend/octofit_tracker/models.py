from djongo import models

# Define models for users, teams, activity, leaderboard, and workouts

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
