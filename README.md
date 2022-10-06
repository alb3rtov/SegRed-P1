# Práctica 1 - Seguridad en Redes

## Requisitos
Para poder lanzar correctamente el script que decodifica los datos, es necesario la librería `scapy` para poder leer archivos `.pcap`. Usa el siguiente comando para instalar la librería:

```
$ pip install scapy
```

## Uso del script notbob.py
Este script remplaza a `bob` para que `alice` le envíe toda la información y la almacene en un archivo `txt`.

Primero habría que lanzar el script de `alice` y unos segundos más tarde el script de [notbob.py](https://github.com/alb3rtov/SegRed-P1/blob/master/notbob.py). 

Cuando `alice` termine de enviar datos, entonces el `bob` falso terminará y generará un archivo `txt` con todos los datos cifrados.


## Uso del script ascii_shifter_decoder.py
Este script admite dos tipos de archivos, primero una captura realizada con Wireshark o tcpdump con extensión `pcap`. Automáticamente filtrará los paquetes donde va la información enviada por `alice` y decodificará la información. 

El otro tipo de archivos es un archivo de texto plano `txt` generado por el scrip [notbob.py](https://github.com/alb3rtov/SegRed-P1/blob/master/notbob.py).

Además se le deberá indicar al script cual es el numero de desplazamiento. En este caso es 8.

Finalmente generará un archivo `txt` con la información decodificada.

```
$ ./ascii_shifter_decoder.py <capture.pcap> <shift number>
```
