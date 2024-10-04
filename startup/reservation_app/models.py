from django.db import models

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_max_capacity = models.IntegerField()
    restaurant_current_capacity = models.IntegerField()



    def __str__(self) -> str:
        return self.restaurant_name
    


    class Meta:
        db_table = 'restaurant_table'




class Client(models.Model):
    client_name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.client_name
    


    class Meta:
        db_table = 'client_table'





class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reservations')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    number_of_people = models.IntegerField()
    canceled = models.BooleanField()
    ended = models.BooleanField()


    def __str__(self) -> str:
        return (f"{self.client} - {self.restaurant} | N_people: {self.number_of_people} | Time: {self.reservation_date} ")

    class Meta:
        db_table = 'reservation_table'