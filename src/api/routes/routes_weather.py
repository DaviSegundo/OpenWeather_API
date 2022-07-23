from flask_restx import Namespace, Resource, fields


api = Namespace('process', description='Weather related operations.')

post_parser = api.parser()
post_parser.add_argument('user_id', type=int, required=True, location='json')

@api.route('')
class ProcessStarter(Resource):

    @api.expect(post_parser)
    def post(self):
        """Starts the data acquisition process given a user id."""
        return {"hello": "world"}, 200


@api.route('/<int:user_id>')
@api.param('user_id', 'The user identifier')
class ProcessRecovery(Resource):

    def get(self, user_id):
        """Retrieves process progress given a user identifier."""
        return {"progress": user_id}, 200