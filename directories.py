import os

# Define la estructura del proyecto
estructura = {
    "monitoring-project": {
        "docker-compose.yml": "",
        "prometheus": {
            "prometheus.yml": ""
        },
        "grafana": {
            "provisioning": {
                "datasources": {
                    "datasource.yml": ""
                }
            }
        },
        "loki": {
            "loki-config.yaml": ""
        },
        "promtail": {
            "promtail-config.yaml": ""
        },
        "tempo": {
            "tempo.yaml": ""
        },
        "opentelemetry-app": {
            "src": {
                "main": {
                    "java": {
                        "OpenTelemetryConfig.java": ""
                    }
                }
            },
            "pom.xml": ""
        }
    }
}

def crear_estructura(base_path, estructura):
    for nombre, contenido in estructura.items():
        ruta = os.path.join(base_path, nombre)
        if isinstance(contenido, dict):
            os.makedirs(ruta, exist_ok=True)
            crear_estructura(ruta, contenido)
        else:
            os.makedirs(base_path, exist_ok=True)
            with open(ruta, 'w') as archivo:
                archivo.write(contenido)

# Crear la estructura de directorios y archivos
crear_estructura('.', estructura)

print("Estructura del proyecto creada exitosamente.")
