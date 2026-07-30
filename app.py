from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


admin_username = 'admin'
admin_password = 'adminpassword'

users = {}