# Microservicio de Autenticación - blipol-authentication

Este microservicio es responsable de gestionar la autenticación, incluyendo la obtención y renovación de tokens.

## Estructura del Proyecto

El proyecto sigue una estructura de \(n\) capas, diseñada para separar claramente las responsabilidades y promover una organización limpia del código.

```
authentication_service/
│
├── .env               # Variables de entorno.
│
├── app/
│   ├── controllers/   # Controladores para conectar rutas con servicios.
│   ├── handlers/      # Manejadores para errores o eventos específicos.
│   ├── middlewares/   # Funciones middleware (ej. autenticación, logging).
│   ├── routes/        # Definiciones de rutas/endpoints de la API.
│   ├── services/      # Lógica principal de negocio.
│   └── utils/         # Funciones y módulos auxiliares.
│
├── main.py            # Punto de entrada principal.
│
└── requirements.txt   # Dependencias necesarias.
```

## Descripción de las Capas

### Controllers

Los **controladores** actúan como un intermediario entre las rutas y los servicios. Toman la entrada de una solicitud, invocan la lógica de negocio adecuada en la capa de servicios y luego preparan y devuelven una respuesta. Si piensas en el proyecto como una orquesta, los controladores son como los directores: coordinan y dirigen, pero no tocan ningún instrumento.

### Handlers

Los **handlers** (manejadores) son funciones o clases diseñadas para manejar situaciones o eventos específicos, como errores no capturados. Estos proporcionan una forma de gestionar de manera centralizada problemas que pueden surgir durante el procesamiento de una solicitud.

### Middlewares

Los **middlewares** son funciones que se ejecutan antes o después de las rutas. Tienen acceso a la solicitud y la respuesta, y pueden modificar ambos. Se utilizan para tareas como autenticación, registro, manejo de CORS, entre otros.

### Routes

Las **rutas** definen los endpoints disponibles para el microservicio y qué método de controlador se debe invocar para cada endpoint. Piensa en las rutas como en las puertas de entrada a tu aplicación: definen cómo se puede acceder a la funcionalidad de tu microservicio.

### Services

La capa de **servicios** contiene la lógica principal de negocio. Aquí es donde ocurre la "magia". Esta capa interactúa con bases de datos, realiza cálculos, llama a otras APIs y más. Las funciones de servicio son invocadas por los controladores y devuelven datos a ellos.

### Utils

La carpeta **utils** contiene funciones y módulos auxiliares que no encajan directamente en las otras categorías, pero que proporcionan funcionalidades reutilizables en diferentes partes del código.

## Comunicación entre Capas

La comunicación entre las capas es unidireccional y secuencial:

1. **Rutas** reciben una solicitud y la pasan al controlador adecuado.
2. El **Controlador** procesa la solicitud, invocando uno o más servicios.
3. Los **Servicios** realizan la lógica de negocio y pueden hacer uso de funciones en **Utils**.
4. Los resultados de los servicios se devuelven al controlador.
5. El **Controlador** devuelve una respuesta, que es enviada de vuelta a través de las **Rutas** al cliente.

Los **Middlewares** y **Handlers** pueden intervenir en cualquier punto de esta secuencia si se configuran para hacerlo. Por ejemplo, un middleware de autenticación podría interrumpir este flujo si una solicitud no está autenticada.

## Empezando

1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta `main.py` para iniciar el servidor.
