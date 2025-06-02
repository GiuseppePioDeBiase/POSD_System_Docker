from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.attors.utente import Utente

utente_bp = Blueprint('utente_bp', __name__)


@utente_bp.route('/api/registrazione', methods=['POST'])
def register_user():
    return Utente.registrati()


@utente_bp.route('/api/login', methods=['POST'])
def login_user():
    return Utente.login()


@utente_bp.route('/api/profilo', methods=['GET'])
@jwt_required()
def get_user_profile():
    return Utente.get_data_user(mail=get_jwt_identity())


@utente_bp.after_request
def after_request(response):
    return Utente.refresh_expiring_jwts(response)


@utente_bp.route('/api/logout', methods=['POST'])
def logout_user():
    return Utente.logout()


@utente_bp.route('/api/caricafoto', methods=['POST'])
@jwt_required()
def carica_foto():
    return Utente.carica_foto(mail=get_jwt_identity())


@utente_bp.route('/api/storicoutente', methods=['GET'])
@jwt_required()
def get_storico_utente():
    return Utente.storico_segnalazioni_utente(mail=get_jwt_identity())


@utente_bp.route('/api/feedbackutente', methods=['GET'])
@jwt_required()
def get_feedback_utente():
    return Utente.storico_feedback_utente(mail=get_jwt_identity())
