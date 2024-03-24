## ¿Qué es Windows proxy manager?

Es una aplicación con interfaz gráfica de usuario (GUI, por sus siglas en inglés) para Windows, que permite cambiar fácilmente la configuración del proxy en este sistema operativo.

Su utilidad está en que simplifica la cantidad de pasos para acceder a dicha configuración del sistema, con respecto a la variante que ofrece Windows para acceder a esta opción (En Windows 11: Configuración -> Red e internet -> Proxy -> Configuración manual del proxy -> Editar).

## Requisitos
- Windows (como sistema operativo)
- Python 3.11.3 o superior
- pip 22.3.1 o superior
- flet 0.21.1 o superior
- pyinstaller 6.4.0 o superior

## ¿Cómo instalar?
Solo debes instalar las dependencias (flet) directamente con el comando ```pip install flet``` o instalar desde el fichero requirements (```pip install -r requirements.txt```).
**Nota:** debe tener **pip** instalado como gestor de dependencias de python.

## ¿Cómo usar?

Ejecutar con el comando:
```flet run``` o ```python main.py```

## Generar un ejecutable _.exe_ para Windows

Debes instalar el paquete PyInstaller:

```pip install pyinstaller```

Luego, en la raiz del proyecto donde se encuentra el fichero *main.py*, construye el ejecutable de la aplicación con el siguiente comando:

```flet pack main.py```

El ejecutable _.exe_ se encontrará dentro de la carpeta **dist** creada en la raiz del proyecto.