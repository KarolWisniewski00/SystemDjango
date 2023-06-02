from rest_framework.decorators import api_view
from rest_framework.response import Response
from firebase_admin import db

@api_view(['GET'])
def getRoutes(request):
    reference = db.reference("/routes/")
    response = reference.get()
    return Response(response)

@api_view(['GET'])
def getTimes(request):
    reference = db.reference("/times/")
    response = reference.get()
    return Response(response)

@api_view(['GET'])
def getTime(request, id):
    reference = db.reference("/times/{}/".format(int(id)-1))
    response = reference.get()
    return Response(response)

@api_view(['POST'])
def createTime(request):
    #ToDo:Validate
    reference = db.reference("/times/")
    response = reference.get()
    table = []

    try:
        for r in response:
            table.append(r)
    except:
        pass

    table.append(request.data)
    reference.set(table)

    return Response()

@api_view(['PUT'])
def updateTime(request,id):
    db.reference("/times/{}/".format(int(id)-1)).update(request.data)
    return Response()

@api_view(['DELETE'])
def deleteTime(request,id):
    db.reference("/times/{}/".format(int(id)-1)).delete()
    return Response()