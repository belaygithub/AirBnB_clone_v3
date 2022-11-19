from api.v1.views import app_views
from flask import jsonify, Blueprint, render_template, abort


@app_views.route('/status', methods=['GET'])
def status():
    """status"""
    return (jsonify({"status": "OK"}))
