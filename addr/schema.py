import graphene
from graphene_django import DjangoObjectType
from addr.migrations import models


class addrType(DjangoObjectType):
    class Meta:
        model = addr

class Createaddr(graphene.Mutation):
    addr = graphene.Field(addrType)

    class Arguments:
        patientid = graphene.String(required=True)
        country = graphene.String(required=True)
        address = graphene.String(required=True)
        state = graphene.String(required=True)
        city = graphene.String(required=True)
        pincode = graphene.String(required=True)

    def mutate(self, info, patientid, country, address, state, city, pincode):
        addr = addr(
            patientid=patientid,
            country=country,
            address=address,
            state=state,
            city=city,
            pincode=pincode
        )
        addr.save()
        return Createaddr(addr=addr)

class Mutation(graphene.ObjectType):
    create_addr = Createaddr.Field()

schema = graphene.Schema(mutation=Mutation)
