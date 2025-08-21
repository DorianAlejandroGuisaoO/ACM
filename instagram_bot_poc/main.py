"""
PRUEBA DE CONCEPTO - BOT INSTAGRAM
Demuestra funcionamiento básico de todas las tecnologías
"""

import os
import sys
sys.path.append('src')

from src.bot import InstagramBot
from src.instagram_api import InstagramAPI
from config.settings import Config

def run_proof_of_concept():
    """Ejecuta la prueba de concepto completa"""
    print("=" * 60)
    print("🚀 PRUEBA DE CONCEPTO - BOT INSTAGRAM")
    print("=" * 60)
    
    # 1. Inicializar bot
    bot = InstagramBot()
    api = InstagramAPI()
    
    # 2. Hello World
    print("\n1. HELLO WORLD:")
    print(bot.hello_world())
    
    # 3. Probar conexión API
    print("\n2. PRUEBA DE CONEXIÓN:")
    success = api.connect("test_user", "test_pass")
    print(f"Conexión exitosa: {success}")
    
    # 4. Simular obtención de posts
    print("\n3. OBTENCIÓN DE POSTS:")
    posts = api.get_recent_posts("test")
    for post in posts:
        print(f"- Post {post['id']}: {post['content']}")
    
    # 5. Simular respuestas automáticas
    print("\n4. RESPUESTAS AUTOMÁTICAS:")
    for post in posts:
        response = bot.simulate_post_response(post['content'])
        if response:
            api.post_comment(post['id'], response)
    
    # 6. Mostrar métricas de sostenibilidad
    print("\n5. MÉTRICAS DE SOSTENIBILIDAD:")
    metrics = bot.show_sustainability_metrics()
    
    print("\n" + "=" * 60)
    print("✅ PRUEBA DE CONCEPTO COMPLETADA")
    print("=" * 60)

if __name__ == "__main__":
    run_proof_of_concept()
