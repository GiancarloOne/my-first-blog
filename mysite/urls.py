"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


#^ per l'inizio del testo
#$ per la fine del testo
#\d per una cifra
#+ per indicare che l'elemento precedente dovrebbe essere ripetuto almeno una volta
#() per catturare parte del pattern

#Scrivere view separate per ogni numero del post sarebbe veramente noioso. Con l'espressione regolare possiamo creare un modello che corrisponde all'url ed estrae il numero per noi: ^ post/(\d+) / $. Scomponiamo pezzo per pezzo per vedere che cosa stiamo facendo:
#^ post / sta dicendo a Django di prendere tutto ciò che ha post / all'inizio dell'url (subito dopo ^)
#(\d+) significa che ci sarà un numero (composto da una o più cifre) e che noi vogliamo che il numero venga catturato ed estratto
#/ dice a django che ci dovrebbe essere un altro carattere a seguire /
#infine, $ indica la fine dell'URL. Significa che solo le stringhe che terminano con / corrisponderanno a questo modello

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('blog.urls')),
]

#urlpatterns = [
    # Examples:
#    url(r'^admin/', admin.site.urls),
#    url(r'^$', 'mysite.views.home', name='home'),
#    url(r'^admin/', include(admin.site.urls)),
#]