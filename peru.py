from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import timedelta

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ciudad)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def calcular_distancia(ciudad_origen, ciudad_destino):
    coords_origen = obtener_coordenadas(ciudad_origen)
    coords_destino = obtener_coordenadas(ciudad_destino)
    if coords_origen and coords_destino:
        distancia_km = geodesic(coords_origen, coords_destino).kilometers
        distancia_millas = geodesic(coords_origen, coords_destino).miles
        return distancia_km, distancia_millas
    else:
        return None, None

def calcular_duracion(distancia_km, medio_transporte):
    velocidades = {
        "auto": 80,       # km/h
        "autobús": 60,    # km/h
        "bicicleta": 20,  # km/h
        "a pie": 5        # km/h
    }
    if medio_transporte in velocidades:
        horas = distancia_km / velocidades[medio_transporte]
        return timedelta(hours=horas)
    else:
        return None

def main():
    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen (o 'e' para salir): ")
        if ciudad_origen.lower() == 'e':
            break
        ciudad_destino = input("Ingrese la Ciudad de Destino: ")
        medio_transporte = input("Ingrese el medio de transporte (auto, autobús, bicicleta, a pie): ").lower()
        
        distancia_km, distancia_millas = calcular_distancia(ciudad_origen, ciudad_destino)
        
        if distancia_km and distancia_millas:
            duracion = calcular_duracion(distancia_km, medio_transporte)
            if duracion:
                print(f"\nDistancia entre {ciudad_origen} y {ciudad_destino}:")
                print(f"{distancia_km:.2f} kilómetros")
                print(f"{distancia_millas:.2f} millas")
                print(f"Duración estimada del viaje: {duracion}")
                print(f"Viajando desde {ciudad_origen} hasta {ciudad_destino} en {medio_transporte}.\n")
            else:
                print("Medio de transporte no válido. Inténtelo de nuevo.")
        else:
            print("No se pudo calcular la distancia. Verifique los nombres de las ciudades e intente nuevamente.")

if __name__ == "__main__":
    main()
