from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

from .models import SocialNetwork, Antimatter, Unity, Universe
from users.models import CustomUserModel
from .serializers import SocialNetworkSerializer, AntimatterSerializer, UniverseSerializer, UnitySerializer

import os
import jwt

class SocialNetworkView(APIView):
    def get(self, request):

        try:

            SocialNetworks = SocialNetwork.objects.all()
            serialized = SocialNetworkSerializer(SocialNetworks, many=True)
            return Response(
                status = status.HTTP_200_OK,
                data = {
                    "multipass" : True,
                    "data" : serialized.data
                }
            )
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class SocialNetworkViewSafety(APIView):
    permission_classes = (IsAdminUser,)
    def post(self,request):
        data = request.data
        serialized = SocialNetworkSerializer(data=data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                data=serialized.data,
                status=status.HTTP_200_OK
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serialized.errors
        )


class AntimatterView(APIView):

    def post(self, request):

        try:


            try:
                token = request.headers['authorization'].split(" ")[1]
                decode = jwt.decode(token, os.getenv('SECRET'))
                

                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )

            
            user = CustomUserModel.objects.get(id=decode['user_id'])
            antimatter = Antimatter.objects.filter(dna=user)
            
            print("_")
            print("#===>",len(antimatter), " Antimatters found")
            print("_")
            if len(antimatter) == 0:

                try:

                    unity = Unity.objects.create(
                        name="Unidad", 
                        description="Contenido de la unidad!",
                    )
                    unity.save()

                    universe = Universe.objects.create(
                        name="Universo",
                        description="Contenido del universo"
                    )
                    universe.unities.add(unity)
                    universe.save()
                    
                
                except:
                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            "multipass": False,
                            "detail": "Unity-Universe-Antimatter error"
                        }
                    )
                

                try:

                   
                    antimatter = Antimatter.objects.create(
                        name=user.username,
                        description=user.email,
                        dna=user,
                        universe=universe,
                        unity=unity
                    )                    
                    antimatter.save()
                
                except:
                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            "multipass": False,
                            "detail": "Unity-Universe-Antimatter error"
                        }
                    )




                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "multipass": True,
                        "detail": "Antimatter created" 

                    }
                )
            else:

                try:
                    unityId = request.query_params['id']
                    unity = Unity.objects.get(id=unityId)

                    unityAntimatters = Antimatter.objects.filter(unity=unity)

                    if len(unityAntimatters) < 3 or user.is_superuser == True:

                        newUniverse = Universe.objects.create(
                            name="Universe",
                            description="I'm a universe"
                        )
                        newUniverse.save()

                        newAntimatter = Antimatter.objects.create(
                            name="Antimatter",
                            description="I'm an Antimatter",
                            dna=user,
                            unity=unity,
                            universe=newUniverse
                        )
                        newAntimatter.save()

                        newUniverseSerialized = UniverseSerializer(newUniverse)
                        newAntimatterSerialized = AntimatterSerializer(newAntimatter)

                        return Response(
                            status=status.HTTP_201_CREATED,
                            data={
                                "multipass": True,
                                "detail": "Antimatter created",
                                "data": newAntimatterSerialized.data
                            }
                        )
                    else:
                        return Response(
                            status=status.HTTP_201_CREATED,
                            data={
                                "multipass": False,
                                "detail": "Unity solo tiene permitido 3 antimatter objects",
                            }
                        )

                except:


                    myantimatters = Antimatter.objects.filter(dna=request.user)
                    antimatter = myantimatters.first()
                    universe = antimatter.universe
                    serialized = UniverseSerializer(universe)

                    UniverseUnities = universe.unities
                    unitiesSerialized = UnitySerializer(UniverseUnities, many=True)


                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            "multipass": True,
                            "detail": "A Universe",
                            "data": serialized.data,
                            "extra": unitiesSerialized.data
                        }
                    )
                
                    

                
            
            
            
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST 
            )

    def get(self, request):

        try:


            try:
                token = request.headers['authorization'].split(" ")[1]
                decode = jwt.decode(token, os.getenv('SECRET'))
                

                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )

            
            user = CustomUserModel.objects.get(id=decode['user_id'])
            antimatter = Antimatter.objects.filter(dna=user)

            print(len(antimatter))
            if len(antimatter) == 0:

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "multipass": False,
                        "detail": "Antimatter not found"
                    }
                )
            else:

                try:
                    antimatterId = request.query_params['id']
                    antimatter = Antimatter.objects.get(id=antimatterId)
                    universe = antimatter.universe
                    unity = antimatter.unity
                    unities = universe.unities

                    antimatterSerialized = AntimatterSerializer(antimatter)
                    universeSerialized = UniverseSerializer(universe)
                    unitySerialized = UnitySerializer(unity)
                    unitiesSerialized = UnitySerializer(unities, many=True)

                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            "multipass": True,
                            "detail": "Antimatter detected",
                            "data": {
                                "antimatter": antimatterSerialized.data,
                                "universe": universeSerialized.data,
                                "unity": unitySerialized.data,
                                "extra": unitiesSerialized.data

                            }
                        }
                    )
                
                except:


                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            "multipass": True,
                            "detail": "Antimatter detected"

                        }
                    )

            
            
            
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST 
            )


class UnityView(APIView):

    def post(self, request):

        try:


            try:
                token = request.headers['authorization'].split(" ")[1]
                decode = jwt.decode(token, os.getenv('SECRET'))
                query_id = request.query_params['id']

                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )

            
            user = CustomUserModel.objects.get(id=decode['user_id'])
            universe = Universe.objects.get(id=query_id)

            try:
                name = request.data['name']
                description = request.data['description']
            
            except:
                return Response(
                    status= status.HTTP_400_BAD_REQUEST,
                    data={
                        "multipass": False,
                        "detail": "No given data"
                    }
                )

            unity = Unity.objects.create(
                name=name,
                description=description
            )
            unity.save()

            universe.unities.add(unity)
            universe.save()

            serialized = UniverseSerializer(universe)
            
            return Response(
                status=status.HTTP_200_OK,
                data = {
                    "multipass": True,
                    "detail": "Unidad creada y asignada a universo: " + str(universe.id),
                    "data": serialized.data
                }
            )
            
            
            
            
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data = {
                    "detail": "No data found"
                }
            )

    def get(self, request):

        try:


            try:
                token = request.headers['authorization'].split(" ")[1]
                decode = jwt.decode(token, os.getenv('SECRET'))
                query_id = request.query_params['id']
                

                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )


            
            user = CustomUserModel.objects.get(id=decode['user_id'])
            
            try:
                unity = Unity.objects.get(id=query_id)
                antimatter = Antimatter.objects.filter(unity=unity)
                
                
                serialized = UnitySerializer(unity)

                if len(antimatter) == 0:
                    
                    
                    return Response(
                        status=status.HTTP_404_NOT_FOUND,
                        data={
                            "multipass": False,
                            "detail": "Unidad sin antimateria",
                            "data": {
                                    "unity": serialized.data
                                }
                        }
                    )
                else:

                    AntimattersSerialized = AntimatterSerializer(antimatter, many=True)

                    if antimatter[0].dna.id == user.id:


                        return Response(
                            status=status.HTTP_200_OK,
                            data={
                                "multipass": True,
                                "detail": "Unidad con antimateria detectada",
                                "data": {
                                    "unity": serialized.data,
                                    "antimatter": AntimattersSerialized.data
                                }
                            }
                        )
                    
                    else:

                        return Response(
                            status=status.HTTP_401_UNAUTHORIZED,
                            data={
                                "detail": "Unidad no autorizada"
                            }
                        )
            except:
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data= {
                        "detail": "Unidad no encontrada"
                    }
                )
            


            return Response(
                    status=status.HTTP_208_ALREADY_REPORTED,
                    data= {
                        "detail": "la unidad es: "+ str(query_id)
                    }
                )
            
            
            
            
            
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST 
            )
    