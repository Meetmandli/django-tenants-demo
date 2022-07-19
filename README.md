# django-tenants-demo

# Requirements 

---install requirements.txt in your project 

# setup 

---First tenant is our django project and client is our main django app

---starting with setup of tenant/settings.py

---here in tenants there are two types of apps 1. shared apps and 2. Tenant apps so add that as per tenant/settings.py 

---add INSTALLED_APPS = SHARED_APPS + TENANT_APPS

---at the top of middleware add 'django_tenants.middleware.main.TenantMainMiddleware',

---After that there are two types of urls , one for tenant and other for public so,

ROOT_URLCONF = 'tenant.urls'     -----> for tenant

PUBLIC_SCHEMA_URLCONF = 'tenant.urls_public'     -----> for public

---For database you need to use postgres (pgadmin) and add engine as 'ENGINE': 'django_tenants.postgresql_backend', also add your name,user,password,host & port

---After that add DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

---at last add SHOW_PUBLIC_IF_NO_TENANT_FOUND = True  ----- This is for the hosts other than tenants .i.e if you entered the wrong host which means which is not registered in tenant then it shows public data.

---For urls you need to create urls and urls_public as discussed in tenant/  and the urlpatterns are same in both.

---Now for clients app 

---write the models in client/models.py as per code.

---Now we made other two apps one for shared (person_details_shared) and one for tenants (person_details_tenant) , added the models and write the views to show the data on the urls

---we had added templates as basic.html for tenants and index.html for public .


# working 

---How to create tenants?

--> write command in terminal as python manage.py create_tenant   and fill required details like name , domain 

---I had created two hosts as hello and demo. and domains are hello.localhost and demo.localhost and accept that if you write any hostname it will call public data.

---To confirm you need to go to postgres and go to your database and go to schema, there you see your created hosts name .

---To create superuser write command as python manage.py create_tenant_superuser.

---after migrations , run the server and you see that your data is reflected at your hostnames.

---On different host the database is also differnt show the data you see is also different which is the advantage of tenants that just by creating new hostname it creates a whole new database and we used it s a whole new product.

