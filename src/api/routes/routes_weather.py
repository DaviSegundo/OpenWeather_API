from flask import Response, json
from flask_restx import Namespace, Resource
from ..controllers.controller_process import ProcessController
from ..responses.responser_process import ProcessResponser
from broker.broker_commons import BrokerCommons

api = Namespace('process', description='Weather related operations.')

post_parser = api.parser()
post_parser.add_argument('user_id', type=int, required=True, location='json')

process_controller = ProcessController()
process_responser = ProcessResponser()


@api.route('')
class ProcessStarter(Resource):

    @api.doc(responses={
        202 : "Your request has been accepted and data collection will start soon",
        409 : "The user identifier you chose is already in use"
    })
    @api.expect(post_parser)
    def post(self):
        """Starts the data acquisition process given a user id."""
        json_data = post_parser.parse_args()
        user_id = json_data.get('user_id')

        valid = process_controller.create_new_process(user_id)

        if valid:
            message1 = {
                'valid': True,
                'user_id': user_id
            }
            codec1 = json.dumps(message1)
            broker_producer = BrokerCommons()
            broker_producer.queue_declare('process')
            broker_producer.send('process', codec1)
            broker_producer.close_connection()

        message_response, status_code = process_responser.post(check=valid, user_id=user_id)
        
        return Response(response=json.dumps(message_response), status=status_code)


@api.route('/<int:user_id>')
@api.param('user_id', 'The user identifier')
class ProcessRecovery(Resource):

    @api.doc(responses={
        200 : "Your request has been accepted and data on the data collection progress will be returned.",
        404 : "No user identifier found in database"
    })
    def get(self, user_id):
        """Retrieves process progress given a user identifier."""
        progress = process_controller.check_progress_process(user_id)

        message_response, status_code = process_responser.get_by_id(progress)

        return Response(response=json.dumps(message_response), status=status_code)