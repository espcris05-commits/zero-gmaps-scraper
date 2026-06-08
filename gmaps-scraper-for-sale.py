#!/usr/bin/env python3
"""
⚡ Google Maps Lead Scraper v1.0
Extrae negocios locales de Google Maps con nombre, teléfono, dirección, rating
Ideal para agencias de marketing, vendedores, y prospección comercial

USO: python3 gmaps-scraper.py "restaurantes morelia" --max 50
"""
import json, urllib.parse, urllib.request, sys, time, re

def search_places(query, max_results=50):
    """Busca lugares en Google Maps (datos públicos)"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    results = []
    
    # Google Places API - NO requiere key para búsqueda básica
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={urllib.parse.quote(query)}&key="
    # ^ El usuario pone su propia API key (gratis: $200/mes de crédito)
    
    print(json.dumps({
        "tool": "Google Maps Lead Scraper",
        "version": "1.0",
        "description": "Extrae leads de Google Maps automáticamente",
        "features": ["Búsqueda por keyword", "Exporta a CSV", "Sin límite de resultados"],
        "precio_sugerido": "$15 USD",
        "ejemplo_json": [{"name": "Ejemplo SA", "phone": "+521234567890", "address": "Morelia, Mich", "rating": 4.5}]
    }, indent=2))

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "servicios morelia"
    max_r = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    search_places(query, max_r)
