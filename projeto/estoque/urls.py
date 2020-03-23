from django.urls import path
from projeto.estoque import views as v

app_name = "estoque"

urlpatterns = [
	path('entrada/', v.estoque_entrada_list, name="estoque_entrada_list"),
	path('entrada/<int:pk>/', v.estoque_entrada_detail, name="estoque_entrada_detail"),
	path('entrada/add/', v.estoque_entrada_add, name="estoque_entrada_add"),
	# path('<int:pk>/edit/', v.EstoqueUpdate.as_view(), name="estoque_update"),
	# path('add/', v.EstoqueCreate.as_view(), name="estoque_add"),

	path('saida/', v.estoque_saida_list, name="estoque_saida_list"),
	path('saida/<int:pk>/', v.estoque_saida_detail, name="estoque_saida_detail"),
]