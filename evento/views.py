from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def read_events(request):

    events = Event.objects.all()     # Pegar todos os dados do evento

    categoria = request.query_params.get('categoria')
    if categoria:
        events = events.filter(categoria__iexact=categoria) #__iexact realizar a filtragem sem se preocupar com maiusculas e minusculas
        #query paraments para teste http://127.0.0.1:8000/event/?categoria=Musica


    #Filtrar por data
    #exemplo de requisição http://127.0.0.1:8000/event/?data=2025-03-11
    data = request.query_params.get('data')
    if data:
        events = events.filter(data=data)


    #quantidade de eventos para aparecer na tela 
    #exemplo de requisição http://127.0.0.1:8000/event/?quantidade=1
    quantidade = request.query_params.get('quantidade')
    if quantidade and quantidade.isdigit():
        events = events[:int(quantidade)]


    #Ordenar eventos por data
    #Exemplo de requisição http://127.0.0.1:8000/event/?ordem=data  
    ordem = request.query_params.get('ordem')
    if ordem == 'data':
        events = events.order_by('data')

   
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def read_one_event(request, pk):
    try:

        event = Event.objects.get(pk=pk)

    except Event.DoesNotExist:
        return ({"mensagem" : "Esse evento não existe"})

    serializer = EventSerializer(event)
    return Response(serializer.data)




@api_view(['GET'])
def next_events(request):
    try:
        # Filtrar e pegar os 7 primeiros eventos
        events = Event.objects.all()[:7] #[:7] para limitar a consulta aos 7 primeiros eventos diretamente no queryset.
        serializer = EventSerializer(events, many=True)  # many=True para lidar com múltiplos objetos
        return Response(serializer.data)

    except Event.DoesNotExist:
        return Response({"mensagem": "Esse evento não existe"}, status=404)







@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) #adicionar os status depois 
        return Response(serializer.errors)
    
@api_view(['PUT'])
def update_event(request, pk):
    try:
        events = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response("Esse evento não existe")
    
    serializer = EventSerializer(events, data = request.data)
    if serializer.is_valid():
        serializer.save() #salvar as alterações no banco de dados
        return Response(serializer.data)
    return Response(serializer.errors)
    
 
@api_view(['DELETE'])
def delete_event (request, pk):
    try: 
        event = Event.objects.get(pk=pk)
    
    except Event.DoesNotExist:
        return Response("Esse evento não existe!")
    
    event.delete()
    return Response({"mensagem":"O evento foi apagado com sucesso!!"})

