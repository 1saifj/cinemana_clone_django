from django.db import models






class Movie(models.Model): 
    MOVIES_GENRES= (
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Animation', 'Animation'),
    ('Biography', 'Biography'),
    ('Comedy', 'Comedy'),
    ('Crime', 'Crime'),
    ('Documentary', 'Documentary'),
    ('Drama', 'Drama'),
    ('Family', 'Family'),
    ('Fantasy', 'Fantasy'),
    ('Film-Noir', 'Film-Noir'),
    ('History', 'History'),
    ('Horror', 'Horror'),
    ('Music', 'Music'),
    ('Musical', 'Musical'),
    ('Mystery', 'Mystery'),
    ('Romance', 'Romance'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Sport', 'Sport'),
    ('Thriller', 'Thriller'),
    ('War', 'War'),
    ('Western', 'Western'),
)
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    year = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    genere = models.CharField(max_length=255, choices=MOVIES_GENRES)
    thumbnail = models.ImageField(upload_to='images/', default='')
    trailer = models.URLField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

class Profile(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
