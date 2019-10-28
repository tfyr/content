import graphene
from graphene import ObjectType, InputObjectType
from graphene_django import DjangoObjectType

from content.models import Block

class BlockType(DjangoObjectType):
    class Meta:
        model = Block


class Query(object):
    block = graphene.Field(BlockType, code=graphene.String(),)

    def resolve_block(self, info, **kwargs):
        code = kwargs.get('code')
        if code:
            block = Block.objects.get(code=code)
            return block
        return None

#class Query(Query, graphene.ObjectType):
#    # This class will inherit from multiple Queries
#    # as we begin to add more apps to our project
#    pass

class ModText(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String(required=True)
        text = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, **args):
        id = args.get('id')
        text = args.get('text')
        user=info.context.user
        if user and not user.is_anonymous and user.is_staff:
            block=Block.objects.get(code=id)
            block.text=text
            block.save()
            return cls(
                ok=True,
            )

        return cls(
            ok=False,
        )


class Mutation(ObjectType):
    modtext = ModText.Field()


#schema = graphene.Schema(
#    query=Query,
#    mutation=Mutation,
#)