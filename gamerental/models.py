from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VideoGame(models.Model):
    title = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.title

class Rental(models.Model):
    renter_name = models.CharField(max_length=255, null=True)
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.renter_name} - {self.video_game.title}"