import logging
import time
from typing import List, Dict

class InstagramAPI:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.connected = False
    
    def connect(self, username: str, password: str) -> bool:
        """Simula conexión a Instagram"""
        self.logger.info("🔐 Conectando a Instagram...")
        time.sleep(2)  # Simular tiempo de autenticación
        
        if username and password:
            self.connected = True
            self.logger.info("✅ Conectado a Instagram exitosamente")
            return True
        else:
            self.logger.error("❌ Credenciales faltantes")
            return False
    
    def get_recent_posts(self, hashtag: str = "test") -> List[Dict]:
        """Simula obtención de posts recientes"""
        if not self.connected:
            self.logger.error("❌ No conectado a Instagram")
            return []
        
        # Simular posts
        mock_posts = [
            {
                "id": "12345",
                "content": "¡Hola mundo! #test",
                "author": "usuario_test",
                "timestamp": "2024-01-15 10:30:00"
            },
            {
                "id": "12346", 
                "content": "Probando el bot #automation",
                "author": "otro_usuario",
                "timestamp": "2024-01-15 11:15:00"
            }
        ]
        
        self.logger.info(f"📱 Obtenidos {len(mock_posts)} posts recientes")
        return mock_posts
    
    def post_comment(self, post_id: str, comment: str) -> bool:
        """Simula publicar comentario"""
        if not self.connected:
            return False
            
        self.logger.info(f"💬 Comentario enviado al post {post_id}: {comment}")
        time.sleep(1)  # Simular tiempo de envío
        return True