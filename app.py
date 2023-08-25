from flask import Flask, render_template
import subprocess
import uuid
import socket

app = Flask(__name__)

def generate_unique_container_name():
    return f'container_{uuid.uuid4().hex}'

# Variable para almacenar el nombre del contenedor actual
current_container_name = ""
current_image_id = "image id con la que vas a interactuar"  # Cambia esto a la imagen que deseas usar

def find_available_port():
    while True:
        port = uuid.uuid4().int & (1<<16)-1
        if port >= 1024:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                if s.connect_ex(('127.0.0.1', port)) != 0:
                    return port

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_container')
def start_container():
    global current_container_name, current_image_id  # Usamos las variables globales
    container_name = generate_unique_container_name()
    host_port = find_available_port()
    
    subprocess.run(['docker', 'run', '-d', '-it', '--name', container_name, f'-p', f'{host_port}:80', current_image_id])
    
    current_container_name = container_name  # Asignamos el nombre a la variable global
    
    return f'Contenedor "{container_name}" iniciado en el puerto aleatorio {host_port} en segundo plano con interacciÃ³n'

@app.route('/stop_container')
def stop_container():
    global current_container_name  # Usamos la variable global
    subprocess.run(['docker', 'stop', current_container_name])
    return f'Contenedor "{current_container_name}" detenido'

@app.route('/restart_container')
def restart_container():
    global current_container_name  # Usamos la variable global
    subprocess.run(['docker', 'restart', current_container_name])
    return f'Contenedor "{current_container_name}" reiniciado'

@app.route('/remove_and_create_container')
def remove_and_create_container():
    global current_container_name, current_image_id  # Usamos las variables globales
    if current_container_name:
        subprocess.run(['docker', 'stop', current_container_name])
        subprocess.run(['docker', 'rm', current_container_name])
        
    container_name = current_container_name
    host_port = find_available_port()
    
    subprocess.run(['docker', 'run', '-d', '-it', '--name', container_name, f'-p', f'{host_port}:80', current_image_id])
    
    current_container_name = container_name  # Asignamos el nombre a la variable global
    
    return f'Contenedor "{container_name}" eliminado y creado nuevamente en el puerto aleatorio {host_port} en segundo plano con interacciÃ³n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
