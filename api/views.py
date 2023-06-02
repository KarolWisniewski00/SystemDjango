from rest_framework.decorators import api_view
from rest_framework.response import Response
from firebase_admin import db

@api_view(['GET'])
def getRoutes(request):
    try:
        reference = db.reference("/routes/")
        response = reference.get()
        return Response(response)
    except:
        return Response('Some error')

@api_view(['GET'])
def getTimes(request):
    try:
        reference = db.reference("/times/")
        response = reference.get()
        return Response(response)
    except:
        return Response('Some error')

@api_view(['GET'])
def getTime(request, id):
    try:
        reference = db.reference("/times/{}/".format(int(id)-1))
        response = reference.get()
        return Response(response)
    except:
        return Response('Some error')

@api_view(['POST'])
def createTime(request):
    #ToDo:Validate
    try:
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
    except:
        return Response('Some error')

@api_view(['PUT'])
def updateTime(request,id):
    try:
        db.reference("/times/{}/".format(int(id)-1)).update(request.data)
        return Response()
    except:
        return Response('Some error')

@api_view(['DELETE'])
def deleteTime(request,id):
    try:
        db.reference("/times/{}/".format(int(id)-1)).delete()
        return Response()
    except:
        return Response('Some error')