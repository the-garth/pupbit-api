# Pupbit API

Django + DRF API for tracking lost pets, as well as displaying pet data like vaccinations, vet details

### Routes

```
  <!-- Admin Dashboard -->
  admin/

  <!-- API Routes -->
  app/v1/accounts/
  app/v1/pets/admin/pets/
  app/v1/pets/owner/pets/
  app/v1/pets/owner/pets/detail/(?P<pk>[^/.]+)/
  app/v1/pets/detail/<int:pk>/
```

### Further enhancements to be made

- Add further documentation on running the API
- Add endpoint for a user to view their own profile
- Add GeoPoint and GeoDjango for last_known_location
- Setup the method to mark pet as lost/found
- Add lng/lat in model for pets
- Add dj-rest-auth for auth endpoints in the API
- Update CORS for web app and native app to access API
- Change DB to use PostgreSQL
- Setup env to not commit secrets for DB login etc etc
