from src.models.models import Users
from sqlalchemy.orm import class_mapper

class ApiController:
    def __init__(self, session):
        self.session = session

    def object_as_dict(self, obj):
        """
        Convertit un objet SQLAlchemy en une liste d'objet
        """
        if obj is None:
            return None
        return {col.name: getattr(obj, col.name) for col in class_mapper(obj.__class__).mapped_table.c}

    def get_users(self):
        users = self.session.query(Users).all()
        user_dicts = [self.object_as_dict(user) for user in users]
        if users:
            response = {
                'success': True,
                'users': user_dicts
            }
            status_code = 200
        else:
            response = {
                'success': False,
                'message': 'Aucun utilisateur trouvé'
            }
            status_code = 404
        
        return response, status_code

    def login(self, username, password):
        user = self.session.query(Users).filter(Users.username == username, Users.password == password).first()
        user_dict = self.object_as_dict(user)
        if user:
            response = {
                'success': True,
                'user': user_dict
            }
            status_code = 200
        else:
            response = {
                'success': False,
                'message': 'Nom d\'utilisateur ou mot de passe incorrect'
            }
            status_code = 401
        
        return response, status_code
    
    def get_user_by_field(self, field, value):
        try:
            user = self.session.query(Users).filter(getattr(Users, field) == value).first()
            user_dict = self.object_as_dict(user)
            if user:
                response = {
                    'success': True,
                    'user': user_dict
                }
                status_code = 200
            else:
                response = {
                    'success': False,
                    'message': f'L\'utilisateur avec le champ {field} = {value} n\'a pas été trouvé'
                }
                status_code = 404
        except:
            response = {
                    'success': False,
                    'message': f'Le champ = {field} n\'existe pas dans la base de donnée'
                }
            status_code = 404
        
        return response, status_code