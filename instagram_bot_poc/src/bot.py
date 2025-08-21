import logging
import time
from datetime import datetime
from config.settings import Config

# Configurar logging para monitoreo
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/bot.log'),
        logging.StreamHandler()
    ]
)

class InstagramBot:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.responses_count = 0
        self.start_time = datetime.now()
        
    def hello_world(self):
        """Prueba de concepto básica"""
        self.logger.info("🤖 Bot de Instagram - Prueba de Concepto Iniciada")
        self.logger.info("✅ Ambiente de desarrollo: ESTABLE")
        self.logger.info("✅ Python: FUNCIONANDO")
        self.logger.info("✅ Logging: ACTIVO")
        return "Hello World - Bot Instagram POC"
    
    def simulate_instagram_connection(self):
        """Simula conexión con Instagram API"""
        try:
            self.logger.info("📱 Simulando conexión con Instagram...")
            time.sleep(1)  # Simular tiempo de conexión
            self.logger.info("✅ Conexión simulada exitosa")
            return True
        except Exception as e:
            self.logger.error(f"❌ Error en conexión: {e}")
            return False
    
    def simulate_post_response(self, post_content="Post de prueba"):
        """Simula respuesta automática a publicación"""
        if self.responses_count >= Config.MAX_RESPONSES_PER_HOUR:
            self.logger.warning("⚠️ Límite de respuestas alcanzado - Criterio sostenibilidad")
            return None
            
        self.logger.info(f"📝 Procesando post: {post_content}")
        
        # Simular generación de respuesta
        responses = [
            "¡Excelente publicación! 👏",
            "Me gusta mucho este contenido 🔥",
            "¡Muy interesante! Gracias por compartir 📚"
        ]
        
        import random
        response = random.choice(responses)
        self.responses_count += 1
        
        self.logger.info(f"🤖 Respuesta generada: {response}")
        self.logger.info(f"📊 Respuestas enviadas: {self.responses_count}")
        
        return response
    
    def show_sustainability_metrics(self):
        """Muestra métricas de sostenibilidad"""
        uptime = datetime.now() - self.start_time
        
        metrics = {
            "tiempo_activo": str(uptime),
            "respuestas_enviadas": self.responses_count,
            "limite_por_hora": Config.MAX_RESPONSES_PER_HOUR,
            "eficiencia": f"{(self.responses_count/Config.MAX_RESPONSES_PER_HOUR)*100:.1f}%"
        }
        
        self.logger.info("📊 MÉTRICAS DE SOSTENIBILIDAD:")
        for key, value in metrics.items():
            self.logger.info(f"   {key}: {value}")
            
        return metrics

if __name__ == "__main__":
    # Ejecutar prueba de concepto
    bot = InstagramBot()
    
    # Hello World
    print(bot.hello_world())
    
    # Prueba de conexión
    bot.simulate_instagram_connection()
    
    # Prueba de respuestas
    bot.simulate_post_response("Primera publicación de prueba")
    bot.simulate_post_response("Segunda publicación de prueba")
    
    # Métricas
    bot.show_sustainability_metrics() 
