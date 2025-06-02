from flask import Blueprint
from models.pkb.privacy_by_design import privacy_by_design

privacy_by_design_bp = Blueprint('privacy_by_design_bp', __name__)


@privacy_by_design_bp.route('/api/privacybydesign', methods=['GET'])
def get_privacy_by_design():
    return privacy_by_design.get_privacy_by_design()
