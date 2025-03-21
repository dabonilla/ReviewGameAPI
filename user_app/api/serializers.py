from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializador para registrar un nuevo usuario.
    
    Atributos:
        password2 (CharField): Campo adicional para confirmar la contraseña.
    
    Meta:
        model (User): Modelo de usuario al que se asocia el serializador.
        fields (list): Campos incluidos en el serializador.
        extra_kwargs (dict): Configuración adicional para los campos.
    """
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        """
        Guarda un nuevo usuario con la información validada.
        
        - Verifica que las contraseñas coincidan.
        - Comprueba si el correo electrónico ya está registrado.
        - Crea una nueva cuenta de usuario con la contraseña encriptada.
        
        return:
            User: La cuenta de usuario creada.
        
        """
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error':'P1 and P2 should be same'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account