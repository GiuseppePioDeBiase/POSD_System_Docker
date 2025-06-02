from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.attors.amministratore_di_sistema import AmministratoreDiSistema

amministratore_bp = Blueprint('amministratore_bp', __name__)


@amministratore_bp.route('/api/allutenti', methods=['GET'])
@jwt_required()
def all_utenti():
    return AmministratoreDiSistema.visualizza_utenti(mail=get_jwt_identity())


@amministratore_bp.route('/api/eliminautente=<string:mail_utente>', methods=['DELETE'])
@jwt_required()
def elimina_utente(mail_utente):
    return AmministratoreDiSistema.elimina_utente(mail_amministratore=get_jwt_identity(), mail_utente=mail_utente)


@amministratore_bp.route('/api/allsegnalazioniaccettate', methods=['GET'])
@jwt_required()
def get_all_segnalazioni_accettate_amministratore():
    return AmministratoreDiSistema.getSegnalazioniAccettateAmministratore(mail=get_jwt_identity())


@amministratore_bp.route('/api/allfeedback', methods=['GET'])
@jwt_required()
def get_all_feedback():
    return AmministratoreDiSistema.getAllFeedbackUtenti(mail=get_jwt_identity())
