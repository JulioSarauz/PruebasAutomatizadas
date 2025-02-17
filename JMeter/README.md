# JMeter

Este documento proporciona los pasos para realizar una prueba de carga con **10,000 usuarios concurrentes** que consulten y busquen datos en **2 segundos** en el enlace `http://localhost:8762/back-end-ms-books-catalogue/books` usando **Apache JMeter**.

## Requisitos Previos

### 1. Instalar Java  
Verifica que tienes instalado Java ejecutando:

```bash
java -version
```

### 2. Instalar Apache JMeter  
- Descarga la última versión desde: [JMeter](https://jmeter.apache.org/download_jmeter.cgi)
- Descomprime el archivo y accede a la carpeta `bin/`
- Ejecuta JMeter:
  - **Windows**: `jmeter.bat`
  - **Mac/Linux**: `./jmeter`

## Configuración de la Prueba de Carga

### 1. Crear un Nuevo Plan de Pruebas
1. Abre **JMeter**.
2. Ve a **Archivo > Nuevo** para crear un nuevo plan de pruebas.

### 2. Agregar un Grupo de Hilos (Usuarios)
1. En el árbol del Plan de Pruebas, haz clic derecho en **Plan de Pruebas** > **Añadir** > **Elementos de Hilo** > **Grupo de Hilos**.
2. Configura los siguientes valores:
   - **Número de hilos (usuarios)**: `10000`
   - **Período de arranque (ramp-up)**: `2` (usuarios en 2 segundos)
   - **Número de veces a ejecutar**: `1`

### 3. Agregar una Petición HTTP
1. Haz clic derecho en el **Grupo de Hilos** > **Añadir** > **Muestreador** > **Petición HTTP**.
2. Configura:
   - **Servidor o IP**: `localhost`
   - **Puerto**: `8762`
   - **Método**: `POST`
   - **Ruta**: `/back-end-ms-books-catalogue/books`
   - **Body Data** `{"targetMethod": "GET","queryParams": {"isVisible": [true]}}`

### 4. Agregar un Listener para Ver los Resultados
1. Haz clic derecho en el **Grupo de Hilos** > **Añadir** > **Receptor**.
2. Agrega **"Ver Árbol de Resultados"** y **"Reporte Resumen"** para analizar las métricas.

### 5. Ejecutar la Prueba
1. Guarda el plan de pruebas (`Ctrl + S`).
2. Presiona el botón **Iniciar (Play)** o usa `Ctrl + R`.
3. Observa los resultados en los **Listeners** agregados.

## Análisis de Resultados
- **Latencia**: Tiempo de respuesta del servidor.
- **Tasa de error**: Porcentaje de peticiones fallidas.
- **Rendimiento**: Cantidad de peticiones por segundo.
- **Tiempo de respuesta**: Si se mantiene dentro de los 2 segundos esperados.


