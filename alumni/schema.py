import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType, Mutation
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet, OrderingFilter
from graphene_file_upload.scalars import Upload


class AlumniFilter(FilterSet):
    class Meta:
        model = Alumni
        fields = ['first_name', 'last_name']
    orderby = OrderingFilter(
        fields=('joined_aiesec_at')
    )


class AlumniNode(DjangoObjectType):
    class Meta:
        model = Alumni
        interfaces = (relay.Node,)


class AlumniMutation(Mutation):
    alumni = graphene.Field(AlumniNode)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        position = graphene.String(required=True)
        company = graphene.String(required=True)
        joined_aiesec_at = graphene.Int(required=True)
        # photo = Upload(required=True)

    def mutate(self, info, first_name, last_name, position, company, joined_aiesec_at):
        new_alumni = Alumni.objects.create(
            first_name=first_name,
            last_name=last_name,
            position=position,
            company=company,
            joined_aiesec_at=joined_aiesec_at,
            # photo=photo
        )
        return AlumniMutation(alumni=new_alumni)


class Query(ObjectType):
    all_alumni = DjangoFilterConnectionField(
        AlumniNode, filterset_class=AlumniFilter)

    def resolve_all_alumni(root, info, **kwargs):
        first_name = kwargs.get('first_name')
        order = kwargs.get('orderby')
        if order is not None:
            print(order)
            return Alumni.objects.all().order_by(order)
        if first_name is not None:
            return Alumni.objects.filter(first_name=first_name)
        else:
            return Alumni.objects.all()


class Mutation(ObjectType):
    add_alumni = AlumniMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
