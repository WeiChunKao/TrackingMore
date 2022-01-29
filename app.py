# -*- coding: utf-8 -*-
from flask import Flask, jsonify, Blueprint, render_template
from flask import request
from flask_restplus import Api, Resource, fields, reqparse, inputs
from flask_cors import CORS
from common.BaseType import baseType, http
from black_cate.blackcate import Cat
import os
app = Flask(__name__)
api = Api(app, version='1.0', title='黑貓 API',
          description='黑貓'
          )
CORS(app, supports_credentials=True, cors_allowed_origins='*')


getLoginNs = api.namespace('getLogin', description='getLogin')

parserLogin = reqparse.RequestParser()
parserLogin.add_argument('Trackingmore-Api-Key', type=str,
                         default="9c4b36c8-52fa-4275-9b86-c3b0e7264abb", required=True)


@getLoginNs.route('', methods=['GET'])
@getLoginNs.response(200, 'Sucess')
@getLoginNs.response(201, 'Created')
@getLoginNs.response(202, 'Bad Request')
@getLoginNs.response(401, 'Unauthorized')
@getLoginNs.response(402, 'Payment required')
@getLoginNs.response(403, 'Server Error')
@getLoginNs.response(404, 'Not Found')
@getLoginNs.response(405, 'Method Not Allowed')
@getLoginNs.response(409, 'Conflict')
@getLoginNs.response(429, 'Too Many Requests')
@getLoginNs.response(4001, 'Unauthorized')
@getLoginNs.response(4002, 'Unauthorized')
@getLoginNs.response(4012, 'Bad Request')
@getLoginNs.response(4013, 'Bad Request')
@getLoginNs.response(4014, 'Bad Request')
@getLoginNs.response(4015, 'Bad Request')
@getLoginNs.response(4016, 'Bad Request')
@getLoginNs.response(4017, 'Bad Request')
@getLoginNs.response(4018, 'Bad Request')
@getLoginNs.response(4019, 'Bad Request')
@getLoginNs.response(4020, 'Request error')
@getLoginNs.response(4021, 'Request error')
@getLoginNs.response(4031, 'No Content')
@getLoginNs.response(4032, 'No Content')
@getLoginNs.response(4033, 'No Content')
@getLoginNs.response(500, 'Server Error')
@getLoginNs.response(503, 'Service Unavailable')
class loginCate(Resource):
    @getLoginNs.doc('登入')
    @getLoginNs.expect(parserLogin)
    def get(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.args:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('GET')
        return Cat().getLogin(request.args['Trackingmore-Api-Key'])


getCarriersNs = api.namespace('getCarriersNs', description='getCarriersNs')

parserCarriers = reqparse.RequestParser()
parserCarriers.add_argument('Trackingmore-Api-Key', type=str,
                            default="9c4b36c8-52fa-4275-9b86-c3b0e7264abb", required=True)
parserCarriers.add_argument('Lang', type=str,
                            default="en", required=True)


@getCarriersNs.route('', methods=['GET'])
@getCarriersNs.response(200, 'Sucess')
@getCarriersNs.response(201, 'Created')
@getCarriersNs.response(202, 'Bad Request')
@getCarriersNs.response(401, 'Unauthorized')
@getCarriersNs.response(402, 'Payment required')
@getCarriersNs.response(403, 'Server Error')
@getCarriersNs.response(404, 'Not Found')
@getCarriersNs.response(405, 'Method Not Allowed')
@getCarriersNs.response(409, 'Conflict')
@getCarriersNs.response(429, 'Too Many Requests')
@getCarriersNs.response(4001, 'Unauthorized')
@getCarriersNs.response(4002, 'Unauthorized')
@getCarriersNs.response(4012, 'Bad Request')
@getCarriersNs.response(4013, 'Bad Request')
@getCarriersNs.response(4014, 'Bad Request')
@getCarriersNs.response(4015, 'Bad Request')
@getCarriersNs.response(4016, 'Bad Request')
@getCarriersNs.response(4017, 'Bad Request')
@getCarriersNs.response(4018, 'Bad Request')
@getCarriersNs.response(4019, 'Bad Request')
@getCarriersNs.response(4020, 'Request error')
@getCarriersNs.response(4021, 'Request error')
@getCarriersNs.response(4031, 'No Content')
@getCarriersNs.response(4032, 'No Content')
@getCarriersNs.response(4033, 'No Content')
@getCarriersNs.response(500, 'Server Error')
@getCarriersNs.response(503, 'Service Unavailable')
class carriersCate(Resource):
    @getCarriersNs.doc('快遞清單')
    @getCarriersNs.expect(parserCarriers)
    def get(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.args or 'Lang' not in request.args:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('GET')
        return Cat().getCarriers(request.args['Trackingmore-Api-Key'], request.args['Lang'])


getDetectNs = api.namespace('getDetectNs', description='getDetectNs')
getDetectML = api.model('getDetectML', {
    'Trackingmore-Api-Key': fields.String(required=True, description='Trackingmore-Api-Key', default='9c4b36c8-52fa-4275-9b86-c3b0e7264abb', example='9c4b36c8-52fa-4275-9b86-c3b0e7264abb'),
    'tracking_number': fields.String(required=True, description='tracking_number', default='RU123456789CN', example='RU123456789CN'),
})


@getDetectNs.route('', methods=['POST'])
@getDetectNs.response(200, 'Sucess')
@getDetectNs.response(201, 'Created')
@getDetectNs.response(202, 'Bad Request')
@getDetectNs.response(401, 'Unauthorized')
@getDetectNs.response(402, 'Payment required')
@getDetectNs.response(403, 'Server Error')
@getDetectNs.response(404, 'Not Found')
@getDetectNs.response(405, 'Method Not Allowed')
@getDetectNs.response(409, 'Conflict')
@getDetectNs.response(429, 'Too Many Requests')
@getDetectNs.response(4001, 'Unauthorized')
@getDetectNs.response(4002, 'Unauthorized')
@getDetectNs.response(4012, 'Bad Request')
@getDetectNs.response(4013, 'Bad Request')
@getDetectNs.response(4014, 'Bad Request')
@getDetectNs.response(4015, 'Bad Request')
@getDetectNs.response(4016, 'Bad Request')
@getDetectNs.response(4017, 'Bad Request')
@getDetectNs.response(4018, 'Bad Request')
@getDetectNs.response(4019, 'Bad Request')
@getDetectNs.response(4020, 'Request error')
@getDetectNs.response(4021, 'Request error')
@getDetectNs.response(4031, 'No Content')
@getDetectNs.response(4032, 'No Content')
@getDetectNs.response(4033, 'No Content')
@getDetectNs.response(500, 'Server Error')
@getDetectNs.response(503, 'Service Unavailable')
class detectCate(Resource):
    @getDetectNs.doc('快遞清單')
    @getDetectNs.expect(getDetectML)
    def post(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.json or 'tracking_number' not in request.json:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('POST')
        return Cat().getDetectCourier(request.json['Trackingmore-Api-Key'], request.json['tracking_number'])


getCreateTrackingNs = api.namespace(
    'getCreateTrackingNs', description='getCreateTrackingNs')
getCreateTrackingML = api.model('getCreateTrackingML', {
    'Trackingmore-Api-Key': fields.String(required=True, description='Trackingmore-Api-Key', default='9c4b36c8-52fa-4275-9b86-c3b0e7264abb', example='9c4b36c8-52fa-4275-9b86-c3b0e7264abb'),
    'tracking_number': fields.String(required=True, description='tracking_number', default='RU123456789CN', example='RU123456789CN'),
    'carrier_code': fields.String(required=True, description='carrier_code', default='china-post', example='china-post'),
})


@getCreateTrackingNs.route('', methods=['POST'])
@getCreateTrackingNs.response(200, 'Sucess')
@getCreateTrackingNs.response(201, 'Created')
@getCreateTrackingNs.response(202, 'Bad Request')
@getCreateTrackingNs.response(401, 'Unauthorized')
@getCreateTrackingNs.response(402, 'Payment required')
@getCreateTrackingNs.response(403, 'Server Error')
@getCreateTrackingNs.response(404, 'Not Found')
@getCreateTrackingNs.response(405, 'Method Not Allowed')
@getCreateTrackingNs.response(409, 'Conflict')
@getCreateTrackingNs.response(429, 'Too Many Requests')
@getCreateTrackingNs.response(4001, 'Unauthorized')
@getCreateTrackingNs.response(4002, 'Unauthorized')
@getCreateTrackingNs.response(4012, 'Bad Request')
@getCreateTrackingNs.response(4013, 'Bad Request')
@getCreateTrackingNs.response(4014, 'Bad Request')
@getCreateTrackingNs.response(4015, 'Bad Request')
@getCreateTrackingNs.response(4016, 'Bad Request')
@getCreateTrackingNs.response(4017, 'Bad Request')
@getCreateTrackingNs.response(4018, 'Bad Request')
@getCreateTrackingNs.response(4019, 'Bad Request')
@getCreateTrackingNs.response(4020, 'Request error')
@getCreateTrackingNs.response(4021, 'Request error')
@getCreateTrackingNs.response(4031, 'No Content')
@getCreateTrackingNs.response(4032, 'No Content')
@getCreateTrackingNs.response(4033, 'No Content')
@getCreateTrackingNs.response(500, 'Server Error')
@getCreateTrackingNs.response(503, 'Service Unavailable')
class createTrackingCate(Resource):
    @getCreateTrackingNs.doc('建立貨物追蹤')
    @getCreateTrackingNs.expect(getCreateTrackingML)
    def post(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.json or 'tracking_number' not in request.json:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('POST')
        return Cat().getCreateTracking(request.json['Trackingmore-Api-Key'], request.json['tracking_number'], request.json['carrier_code'])


getResultTrackingNs = api.namespace(
    'getResultTrackingNs', description='getResultTrackingNs')

parserResultTracking = reqparse.RequestParser()
parserResultTracking.add_argument('Trackingmore-Api-Key', type=str,
                                  default="9c4b36c8-52fa-4275-9b86-c3b0e7264abb", required=True)
parserResultTracking.add_argument('carrier_code', type=str,
                                  default="china-post", required=True)
parserResultTracking.add_argument('tracking_number', type=str,
                                  default="RU123456789CN", required=True)
parserResultTracking.add_argument('lang', type=str,
                                  default="en", required=True)


@getResultTrackingNs.route('', methods=['GET'])
@getResultTrackingNs.response(200, 'Sucess')
@getResultTrackingNs.response(201, 'Created')
@getResultTrackingNs.response(202, 'Bad Request')
@getResultTrackingNs.response(401, 'Unauthorized')
@getResultTrackingNs.response(402, 'Payment required')
@getResultTrackingNs.response(403, 'Server Error')
@getResultTrackingNs.response(404, 'Not Found')
@getResultTrackingNs.response(405, 'Method Not Allowed')
@getResultTrackingNs.response(409, 'Conflict')
@getResultTrackingNs.response(429, 'Too Many Requests')
@getResultTrackingNs.response(4001, 'Unauthorized')
@getResultTrackingNs.response(4002, 'Unauthorized')
@getResultTrackingNs.response(4012, 'Bad Request')
@getResultTrackingNs.response(4013, 'Bad Request')
@getResultTrackingNs.response(4014, 'Bad Request')
@getResultTrackingNs.response(4015, 'Bad Request')
@getResultTrackingNs.response(4016, 'Bad Request')
@getResultTrackingNs.response(4017, 'Bad Request')
@getResultTrackingNs.response(4018, 'Bad Request')
@getResultTrackingNs.response(4019, 'Bad Request')
@getResultTrackingNs.response(4020, 'Request error')
@getResultTrackingNs.response(4021, 'Request error')
@getResultTrackingNs.response(4031, 'No Content')
@getResultTrackingNs.response(4032, 'No Content')
@getResultTrackingNs.response(4033, 'No Content')
@getResultTrackingNs.response(500, 'Server Error')
@getResultTrackingNs.response(503, 'Service Unavailable')
class resultTrackingCate(Resource):
    @getResultTrackingNs.doc('追蹤結果')
    @getResultTrackingNs.expect(parserResultTracking)
    def get(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.args or 'carrier_code' not in request.args or 'tracking_number' not in request.args or 'lang' not in request.args:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('GET')
        return Cat().getResultTracking(
            request.args['Trackingmore-Api-Key'],
            request.args['carrier_code'],
            request.args['tracking_number'],
            request.args['lang'])


getModifyTrackingNs = api.namespace(
    'getModifyTrackingNs', description='getModifyTrackingNs')
getModifyTrackingML = api.model('getModifyTrackingML', {
    'Trackingmore-Api-Key': fields.String(required=True, description='Trackingmore-Api-Key', default='9c4b36c8-52fa-4275-9b86-c3b0e7264abb', example='9c4b36c8-52fa-4275-9b86-c3b0e7264abb'),
    'tracking_number': fields.String(required=True, description='tracking_number', default='RU123456789CN', example='RU123456789CN'),
    'carrier_code': fields.String(required=True, description='carrier_code', default='china-post', example='china-post'),
    'logistics_channel': fields.String(required=True, description='logistics_channel', default='4px channel', example='4px channel'),
    'customer_email': fields.String(required=True, description='customer_email', default='example@abc.com', example='example@abc.com'),
    'order_id': fields.String(required=True, description='order_id', default='#1234', example='#1234'),
})


@getModifyTrackingNs.route('', methods=['PUT'])
@getModifyTrackingNs.response(200, 'Sucess')
@getModifyTrackingNs.response(201, 'Created')
@getModifyTrackingNs.response(202, 'Bad Request')
@getModifyTrackingNs.response(401, 'Unauthorized')
@getModifyTrackingNs.response(402, 'Payment required')
@getModifyTrackingNs.response(403, 'Server Error')
@getModifyTrackingNs.response(404, 'Not Found')
@getModifyTrackingNs.response(405, 'Method Not Allowed')
@getModifyTrackingNs.response(409, 'Conflict')
@getModifyTrackingNs.response(429, 'Too Many Requests')
@getModifyTrackingNs.response(4001, 'Unauthorized')
@getModifyTrackingNs.response(4002, 'Unauthorized')
@getModifyTrackingNs.response(4012, 'Bad Request')
@getModifyTrackingNs.response(4013, 'Bad Request')
@getModifyTrackingNs.response(4014, 'Bad Request')
@getModifyTrackingNs.response(4015, 'Bad Request')
@getModifyTrackingNs.response(4016, 'Bad Request')
@getModifyTrackingNs.response(4017, 'Bad Request')
@getModifyTrackingNs.response(4018, 'Bad Request')
@getModifyTrackingNs.response(4019, 'Bad Request')
@getModifyTrackingNs.response(4020, 'Request error')
@getModifyTrackingNs.response(4021, 'Request error')
@getModifyTrackingNs.response(4031, 'No Content')
@getModifyTrackingNs.response(4032, 'No Content')
@getModifyTrackingNs.response(4033, 'No Content')
@getModifyTrackingNs.response(500, 'Server Error')
@getModifyTrackingNs.response(503, 'Service Unavailable')
class modifyTrackingCate(Resource):
    @getModifyTrackingNs.doc('建立貨物追蹤')
    @getModifyTrackingNs.expect(getModifyTrackingML)
    def put(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.json or 'tracking_number' not in request.json \
            or 'carrier_code' not in request.json or 'logistics_channel' not in request.json \
                or 'customer_email' not in request.json or 'order_id' not in request.json:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('PUT')
        return Cat().getModifyTracking(
            request.json['Trackingmore-Api-Key'],
            request.json['carrier_code'],
            request.json['tracking_number'],
            request.json['logistics_channel'],
            request.json['customer_email'],
            request.json['order_id'])


getDeleteTrackingNs = api.namespace(
    'getDeleteTrackingNs', description='getDeleteTrackingNs')

parserDeleteTracking = reqparse.RequestParser()
parserDeleteTracking.add_argument('Trackingmore-Api-Key', type=str,
                                  default="9c4b36c8-52fa-4275-9b86-c3b0e7264abb", required=True)
parserDeleteTracking.add_argument('carrier_code', type=str,
                                  default="china-post", required=True)
parserDeleteTracking.add_argument('tracking_number', type=str,
                                  default="RU123456789CN", required=True)


@getDeleteTrackingNs.route('', methods=['DELETE'])
@getDeleteTrackingNs.response(200, 'Sucess')
@getDeleteTrackingNs.response(201, 'Created')
@getDeleteTrackingNs.response(202, 'Bad Request')
@getDeleteTrackingNs.response(401, 'Unauthorized')
@getDeleteTrackingNs.response(402, 'Payment required')
@getDeleteTrackingNs.response(403, 'Server Error')
@getDeleteTrackingNs.response(404, 'Not Found')
@getDeleteTrackingNs.response(405, 'Method Not Allowed')
@getDeleteTrackingNs.response(409, 'Conflict')
@getDeleteTrackingNs.response(429, 'Too Many Requests')
@getDeleteTrackingNs.response(4001, 'Unauthorized')
@getDeleteTrackingNs.response(4002, 'Unauthorized')
@getDeleteTrackingNs.response(4012, 'Bad Request')
@getDeleteTrackingNs.response(4013, 'Bad Request')
@getDeleteTrackingNs.response(4014, 'Bad Request')
@getDeleteTrackingNs.response(4015, 'Bad Request')
@getDeleteTrackingNs.response(4016, 'Bad Request')
@getDeleteTrackingNs.response(4017, 'Bad Request')
@getDeleteTrackingNs.response(4018, 'Bad Request')
@getDeleteTrackingNs.response(4019, 'Bad Request')
@getDeleteTrackingNs.response(4020, 'Request error')
@getDeleteTrackingNs.response(4021, 'Request error')
@getDeleteTrackingNs.response(4031, 'No Content')
@getDeleteTrackingNs.response(4032, 'No Content')
@getDeleteTrackingNs.response(4033, 'No Content')
@getDeleteTrackingNs.response(500, 'Server Error')
@getDeleteTrackingNs.response(503, 'Service Unavailable')
class deleteTrackingCate(Resource):
    @getDeleteTrackingNs.doc('追蹤結果')
    @getDeleteTrackingNs.expect(parserDeleteTracking)
    def delete(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.args or 'carrier_code' not in request.args or 'tracking_number' not in request.args:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('GET')
        return Cat().getResultTracking(
            request.args['Trackingmore-Api-Key'],
            request.args['carrier_code'],
            request.args['tracking_number'])


getMultipleCreateTrackingNs = api.namespace(
    'getMultipleCreateTrackingNs', description='getMultipleCreateTrackingNs')
multipleCreateTrackingData = api.model('multipleCreateTrackingData', {
    "tracking_number": fields.String(required=True, description='RU123456789CN', default='RU123456789CN', example='RU123456789CN'),
    "carrier_code": fields.String(required=True, description='Trackingmore-Api-Key', default='china-post', example='china-post'),
})
getMultipleCreateTrackingML = api.model('getMultipleCreateTrackingML', {
    'Trackingmore-Api-Key': fields.String(required=True, description='Trackingmore-Api-Key', default='9c4b36c8-52fa-4275-9b86-c3b0e7264abb', example='9c4b36c8-52fa-4275-9b86-c3b0e7264abb'),
    'DATA': fields.List(fields.Nested(multipleCreateTrackingData, description='batch', required=True)),
})


@getMultipleCreateTrackingNs.route('', methods=['POST'])
@getMultipleCreateTrackingNs.response(200, 'Sucess')
@getMultipleCreateTrackingNs.response(201, 'Created')
@getMultipleCreateTrackingNs.response(202, 'Bad Request')
@getMultipleCreateTrackingNs.response(401, 'Unauthorized')
@getMultipleCreateTrackingNs.response(402, 'Payment required')
@getMultipleCreateTrackingNs.response(403, 'Server Error')
@getMultipleCreateTrackingNs.response(404, 'Not Found')
@getMultipleCreateTrackingNs.response(405, 'Method Not Allowed')
@getMultipleCreateTrackingNs.response(409, 'Conflict')
@getMultipleCreateTrackingNs.response(429, 'Too Many Requests')
@getMultipleCreateTrackingNs.response(4001, 'Unauthorized')
@getMultipleCreateTrackingNs.response(4002, 'Unauthorized')
@getMultipleCreateTrackingNs.response(4012, 'Bad Request')
@getMultipleCreateTrackingNs.response(4013, 'Bad Request')
@getMultipleCreateTrackingNs.response(4014, 'Bad Request')
@getMultipleCreateTrackingNs.response(4015, 'Bad Request')
@getMultipleCreateTrackingNs.response(4016, 'Bad Request')
@getMultipleCreateTrackingNs.response(4017, 'Bad Request')
@getMultipleCreateTrackingNs.response(4018, 'Bad Request')
@getMultipleCreateTrackingNs.response(4019, 'Bad Request')
@getMultipleCreateTrackingNs.response(4020, 'Request error')
@getMultipleCreateTrackingNs.response(4021, 'Request error')
@getMultipleCreateTrackingNs.response(4031, 'No Content')
@getMultipleCreateTrackingNs.response(4032, 'No Content')
@getMultipleCreateTrackingNs.response(4033, 'No Content')
@getMultipleCreateTrackingNs.response(500, 'Server Error')
@getMultipleCreateTrackingNs.response(503, 'Service Unavailable')
class multipleCreateTrackingCate(Resource):
    @getMultipleCreateTrackingNs.doc('建立貨物追蹤')
    @getMultipleCreateTrackingNs.expect(getMultipleCreateTrackingML)
    def post(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.json or 'DATA' not in request.json:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('POST')
        return Cat().getMultiCreateTracking(
            request.json['Trackingmore-Api-Key'],
            request.json['DATA'])


getMutipleResultTrackingNs = api.namespace(
    'getMutipleResultTrackingNs', description='getMutipleResultTrackingNs')

parserMultipleResultTracking = reqparse.RequestParser()
parserMultipleResultTracking.add_argument('Trackingmore-Api-Key', type=str,
                                          default="9c4b36c8-52fa-4275-9b86-c3b0e7264abb", required=True)
parserMultipleResultTracking.add_argument('numbers', type=str,
                                          default="RU123456789CN,LX123456789CN", required=True)


@getMutipleResultTrackingNs.route('', methods=['GET'])
@getMutipleResultTrackingNs.response(200, 'Sucess')
@getMutipleResultTrackingNs.response(201, 'Created')
@getMutipleResultTrackingNs.response(202, 'Bad Request')
@getMutipleResultTrackingNs.response(401, 'Unauthorized')
@getMutipleResultTrackingNs.response(402, 'Payment required')
@getMutipleResultTrackingNs.response(403, 'Server Error')
@getMutipleResultTrackingNs.response(404, 'Not Found')
@getMutipleResultTrackingNs.response(405, 'Method Not Allowed')
@getMutipleResultTrackingNs.response(409, 'Conflict')
@getMutipleResultTrackingNs.response(429, 'Too Many Requests')
@getMutipleResultTrackingNs.response(4001, 'Unauthorized')
@getMutipleResultTrackingNs.response(4002, 'Unauthorized')
@getMutipleResultTrackingNs.response(4012, 'Bad Request')
@getMutipleResultTrackingNs.response(4013, 'Bad Request')
@getMutipleResultTrackingNs.response(4014, 'Bad Request')
@getMutipleResultTrackingNs.response(4015, 'Bad Request')
@getMutipleResultTrackingNs.response(4016, 'Bad Request')
@getMutipleResultTrackingNs.response(4017, 'Bad Request')
@getMutipleResultTrackingNs.response(4018, 'Bad Request')
@getMutipleResultTrackingNs.response(4019, 'Bad Request')
@getMutipleResultTrackingNs.response(4020, 'Request error')
@getMutipleResultTrackingNs.response(4021, 'Request error')
@getMutipleResultTrackingNs.response(4031, 'No Content')
@getMutipleResultTrackingNs.response(4032, 'No Content')
@getMutipleResultTrackingNs.response(4033, 'No Content')
@getMutipleResultTrackingNs.response(500, 'Server Error')
@getMutipleResultTrackingNs.response(503, 'Service Unavailable')
class multipleResultTrackingCate(Resource):
    @getMutipleResultTrackingNs.doc('多筆追蹤結果')
    @getMutipleResultTrackingNs.expect(parserMultipleResultTracking)
    def get(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.args or 'numbers' not in request.args:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('GET')
        return Cat().getMultiResultsTracking(
            request.args['Trackingmore-Api-Key'],
            request.args['numbers'])


getMultipleDeleteTrackingNs = api.namespace(
    'getMultipleDeleteTrackingNs', description='getMultipleDeleteTrackingNs')
multipleDeleteTrackingData = api.model('multipleDeleteTrackingData', {
    "tracking_number": fields.String(required=True, description='RU123456789CN', default='RU123456789CN', example='RU123456789CN'),
    "carrier_code": fields.String(required=True, description='Trackingmore-Api-Key', default='china-post', example='china-post'),
})
getMultipleDeleteTrackingML = api.model('getMultipleDeleteTrackingML', {
    'Trackingmore-Api-Key': fields.String(required=True, description='Trackingmore-Api-Key', default='9c4b36c8-52fa-4275-9b86-c3b0e7264abb', example='9c4b36c8-52fa-4275-9b86-c3b0e7264abb'),
    'DATA': fields.List(fields.Nested(multipleDeleteTrackingData, description='delete', required=True)),
})


@getMultipleDeleteTrackingNs.route('', methods=['POST'])
@getMultipleDeleteTrackingNs.response(200, 'Sucess')
@getMultipleDeleteTrackingNs.response(201, 'Created')
@getMultipleDeleteTrackingNs.response(202, 'Bad Request')
@getMultipleDeleteTrackingNs.response(401, 'Unauthorized')
@getMultipleDeleteTrackingNs.response(402, 'Payment required')
@getMultipleDeleteTrackingNs.response(403, 'Server Error')
@getMultipleDeleteTrackingNs.response(404, 'Not Found')
@getMultipleDeleteTrackingNs.response(405, 'Method Not Allowed')
@getMultipleDeleteTrackingNs.response(409, 'Conflict')
@getMultipleDeleteTrackingNs.response(429, 'Too Many Requests')
@getMultipleDeleteTrackingNs.response(4001, 'Unauthorized')
@getMultipleDeleteTrackingNs.response(4002, 'Unauthorized')
@getMultipleDeleteTrackingNs.response(4012, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4013, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4014, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4015, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4016, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4017, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4018, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4019, 'Bad Request')
@getMultipleDeleteTrackingNs.response(4020, 'Request error')
@getMultipleDeleteTrackingNs.response(4021, 'Request error')
@getMultipleDeleteTrackingNs.response(4031, 'No Content')
@getMultipleDeleteTrackingNs.response(4032, 'No Content')
@getMultipleDeleteTrackingNs.response(4033, 'No Content')
@getMultipleDeleteTrackingNs.response(500, 'Server Error')
@getMultipleDeleteTrackingNs.response(503, 'Service Unavailable')
class mutipleDeleteTrackingCate(Resource):
    @getMultipleDeleteTrackingNs.doc('多筆刪除追蹤結果')
    @getMultipleDeleteTrackingNs.expect(getMultipleDeleteTrackingML)
    def post(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.json or 'DATA' not in request.json:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('POST')
        return Cat().getMultiDeleteTracking(
            request.json['Trackingmore-Api-Key'],
            request.json['DATA'])



geAccountInfoNs = api.namespace('geAccountInfoNs', description='geAccountInfoNs')

parserAccountInfo = reqparse.RequestParser()
parserAccountInfo.add_argument('Trackingmore-Api-Key', type=str,
                         default="9c4b36c8-52fa-4275-9b86-c3b0e7264abb", required=True)


@geAccountInfoNs.route('', methods=['GET'])
@geAccountInfoNs.response(200, 'Sucess')
@geAccountInfoNs.response(201, 'Created')
@geAccountInfoNs.response(202, 'Bad Request')
@geAccountInfoNs.response(401, 'Unauthorized')
@geAccountInfoNs.response(402, 'Payment required')
@geAccountInfoNs.response(403, 'Server Error')
@geAccountInfoNs.response(404, 'Not Found')
@geAccountInfoNs.response(405, 'Method Not Allowed')
@geAccountInfoNs.response(409, 'Conflict')
@geAccountInfoNs.response(429, 'Too Many Requests')
@geAccountInfoNs.response(4001, 'Unauthorized')
@geAccountInfoNs.response(4002, 'Unauthorized')
@geAccountInfoNs.response(4012, 'Bad Request')
@geAccountInfoNs.response(4013, 'Bad Request')
@geAccountInfoNs.response(4014, 'Bad Request')
@geAccountInfoNs.response(4015, 'Bad Request')
@geAccountInfoNs.response(4016, 'Bad Request')
@geAccountInfoNs.response(4017, 'Bad Request')
@geAccountInfoNs.response(4018, 'Bad Request')
@geAccountInfoNs.response(4019, 'Bad Request')
@geAccountInfoNs.response(4020, 'Request error')
@geAccountInfoNs.response(4021, 'Request error')
@geAccountInfoNs.response(4031, 'No Content')
@geAccountInfoNs.response(4032, 'No Content')
@geAccountInfoNs.response(4033, 'No Content')
@geAccountInfoNs.response(500, 'Server Error')
@geAccountInfoNs.response(503, 'Service Unavailable')
class accountInfoCate(Resource):
    @geAccountInfoNs.doc('取得使用者資訊')
    @geAccountInfoNs.expect(parserAccountInfo)
    def get(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.args:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('GET')
        return Cat().getAccountInfo(request.args['Trackingmore-Api-Key'])




getRealTimeResultNs = api.namespace(
    'getRealTimeResultNs', description='getRealTimeResultNs')
getRealTimeResultML = api.model('getRealTimeResultML', {
    'Trackingmore-Api-Key': fields.String(required=True, description='Trackingmore-Api-Key', default='9c4b36c8-52fa-4275-9b86-c3b0e7264abb', example='9c4b36c8-52fa-4275-9b86-c3b0e7264abb'),
    'tracking_number': fields.String(required=True, description='tracking_number', default='RU123456789CN', example='RU123456789CN'),
    'carrier_code': fields.String(required=True, description='carrier_code', default='china-ems', example='china-ems'),
})


@getRealTimeResultNs.route('', methods=['POST'])
@getRealTimeResultNs.response(200, 'Sucess')
@getRealTimeResultNs.response(201, 'Created')
@getRealTimeResultNs.response(202, 'Bad Request')
@getRealTimeResultNs.response(401, 'Unauthorized')
@getRealTimeResultNs.response(402, 'Payment required')
@getRealTimeResultNs.response(403, 'Server Error')
@getRealTimeResultNs.response(404, 'Not Found')
@getRealTimeResultNs.response(405, 'Method Not Allowed')
@getRealTimeResultNs.response(409, 'Conflict')
@getRealTimeResultNs.response(429, 'Too Many Requests')
@getRealTimeResultNs.response(4001, 'Unauthorized')
@getRealTimeResultNs.response(4002, 'Unauthorized')
@getRealTimeResultNs.response(4012, 'Bad Request')
@getRealTimeResultNs.response(4013, 'Bad Request')
@getRealTimeResultNs.response(4014, 'Bad Request')
@getRealTimeResultNs.response(4015, 'Bad Request')
@getRealTimeResultNs.response(4016, 'Bad Request')
@getRealTimeResultNs.response(4017, 'Bad Request')
@getRealTimeResultNs.response(4018, 'Bad Request')
@getRealTimeResultNs.response(4019, 'Bad Request')
@getRealTimeResultNs.response(4020, 'Request error')
@getRealTimeResultNs.response(4021, 'Request error')
@getRealTimeResultNs.response(4031, 'No Content')
@getRealTimeResultNs.response(4032, 'No Content')
@getRealTimeResultNs.response(4033, 'No Content')
@getRealTimeResultNs.response(500, 'Server Error')
@getRealTimeResultNs.response(503, 'Service Unavailable')
class realTimeResultCate(Resource):
    @getRealTimeResultNs.doc('即時結果')
    @getRealTimeResultNs.expect(getRealTimeResultML)
    def post(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.json or 'tracking_number' not in request.json or 'carrier_code' not in request.json:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('POST')
        return Cat().getRealTimeResult(
            request.json['Trackingmore-Api-Key'],
            request.json['tracking_number'],
            request.json['carrier_code'],
            )





getChangeCourierNs = api.namespace(
    'getChangeCourierNs', description='getChangeCourierNs')
getChangeCourierML = api.model('getChangeCourierML', {
    'Trackingmore-Api-Key': fields.String(required=True, description='Trackingmore-Api-Key', default='9c4b36c8-52fa-4275-9b86-c3b0e7264abb', example='9c4b36c8-52fa-4275-9b86-c3b0e7264abb'),
    'tracking_number': fields.String(required=True, description='tracking_number', default='RU123456789CN', example='RU123456789CN'),
    'carrier_code': fields.String(required=True, description='carrier_code', default='china-ems', example='china-ems'),
    'update_carrier_code': fields.String(required=True, description='update_carrier_code', default='china-post', example='china-post'),
})


@getChangeCourierNs.route('', methods=['POST'])
@getChangeCourierNs.response(200, 'Sucess')
@getChangeCourierNs.response(201, 'Created')
@getChangeCourierNs.response(202, 'Bad Request')
@getChangeCourierNs.response(401, 'Unauthorized')
@getChangeCourierNs.response(402, 'Payment required')
@getChangeCourierNs.response(403, 'Server Error')
@getChangeCourierNs.response(404, 'Not Found')
@getChangeCourierNs.response(405, 'Method Not Allowed')
@getChangeCourierNs.response(409, 'Conflict')
@getChangeCourierNs.response(429, 'Too Many Requests')
@getChangeCourierNs.response(4001, 'Unauthorized')
@getChangeCourierNs.response(4002, 'Unauthorized')
@getChangeCourierNs.response(4012, 'Bad Request')
@getChangeCourierNs.response(4013, 'Bad Request')
@getChangeCourierNs.response(4014, 'Bad Request')
@getChangeCourierNs.response(4015, 'Bad Request')
@getChangeCourierNs.response(4016, 'Bad Request')
@getChangeCourierNs.response(4017, 'Bad Request')
@getChangeCourierNs.response(4018, 'Bad Request')
@getChangeCourierNs.response(4019, 'Bad Request')
@getChangeCourierNs.response(4020, 'Request error')
@getChangeCourierNs.response(4021, 'Request error')
@getChangeCourierNs.response(4031, 'No Content')
@getChangeCourierNs.response(4032, 'No Content')
@getChangeCourierNs.response(4033, 'No Content')
@getChangeCourierNs.response(500, 'Server Error')
@getChangeCourierNs.response(503, 'Service Unavailable')
class chageCourierCate(Resource):
    @getChangeCourierNs.doc('更換運送模式')
    @getChangeCourierNs.expect(getChangeCourierML)
    def post(self):
        if not request:
            abort(400)
        elif 'Trackingmore-Api-Key' not in request.json or 'tracking_number' not in request.json \
            or 'carrier_code' not in request.json or 'update_carrier_code' not in request.json:
            return 400, http.apiResponse(400, "Bad Request", 'Parameter Loss'), http.apiHeaders('POST')
        return Cat().getChangeCourier(
            request.json['Trackingmore-Api-Key'],
            request.json['tracking_number'],
            request.json['carrier_code'],
            request.json['update_carrier_code']
            )

if __name__ == '__main__':
    app.run(threaded=True, use_reloader=False, host='0.0.0.0',
            port=5000, debug=False)  # use_reloader=True,
