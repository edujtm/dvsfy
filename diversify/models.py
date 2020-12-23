"""
Local database representation for Spotify Web API data 
models.
"""
from django.db import models


class Track(models.Model):
    track_id = models.CharField(unique=True)
    name = models.CharField()
    popularity = models.IntegerField()
    image_url = models.CharField()
    features = models.OneToOneField(
            "AudioFeatures", 
            on_delete=models.CASCADE, 
            null=True, 
            blank=True
    )


class Playlist(models.Model):
    spotify_id =  models.CharField(unique=True)
    name = models.CharField()
    tracks = models.ManyToManyField(Track, null=True, blank=True)


class AudioFeatures(models.Model):
    """
    Represents pre-processed features from each Spotify track.
    Used in data analysis.

    attributes:
        instrumentalness    Whether a tracks contains no vocals. Value between 0.0 and 1.0.
        liveness            Detects presence of audience in audio. Value between 0.0 and 1.0.
        loudness            Overall loudness of track in decibels. Values between -60 and 0 db. 
        energy              Measure of intensity and activity of track.  Value between 0.0 and 1.0.
        danceability        Describes how suitable a track is for dancing. Value between 0.0 and 1.0.
        acousticness        Confidence measure of whether the track is acoustic. Value between 0.0 and 1.0.
        speechiness         Detects the presence of spoken words in a track. Value between 0.0 and 1.0.
        valence             Musical positiveness conveyed by a track.  Value between 0.0 and 1.0.
        tempo               Estimated tempo of track in beats per minute.
        duration_ms         Duration of the track in milliseconds.

    """
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    energy = models.FloatField()
    danceability = models.FloatField()
    acousticness = models.FloatField()
    speechiness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.IntegerField()
