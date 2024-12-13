---
layout: ../stix/Body.astro
title: Instrucciones de uso
---
- Abrir `a.xlsx` y actualizar la tabla de la hoja `check` con todos
los proyectos que necesiten reporte.
     - La tabla de la hoja `check` muestra, para cada proyecto, un
     `1` si se encuentra un reporte de planner asociado dentro de la
     carpeta `reportes`, o un `0` en caso contrario.
- Dejar abierto planner en el modulo `Proyectos`, listo para filtrar
por proyecto.
- Encender el robot y, opcionalmente, seleccionar alguna de las
opciones del dialogo.
- Ejecutar el robot para exportar los reportes de planner.
- Terminada la ejecucion (fallida o exitosa) del robot:
     - **cargar** los reportes desde la carpeta de planner a la
     carpeta `reportes`;
     - actualizar los datos de la planilla;
     - volver a ejecutar el robot si quedasen reportes pendientes.
- Guardar el archivo `a.xlsx` actualizado y cerrarlo.
- Ejecutar `Kensten`.
- Disfrutar el resultado.
