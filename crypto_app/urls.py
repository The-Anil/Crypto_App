from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^bitcoin.html$', views.bitcoin),
	url(r'^ethereum.html$', views.ethereum),
	url(r'^ripple.html$', views.ripple),
	url(r'^litecoin.html$', views.litecoin),
	url(r'^monero.html$', views.monero),
	url(r'^iota.html$', views.iota),
	url(r'^steem.html$', views.steem),
	url(r'^maidsafe.html$', views.maidsafe),
	url(r'^predictions.html$', views.predictions),
	url(r'^rankwise.html$', views.rankwise)
]