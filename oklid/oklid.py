import math

def euclideanDistance(point1, point2):
    """
    Bu fonksiyon iki nokta arasındaki Öklid mesafesini hesaplar.

   point1: (x1, y1) şeklinde bir demet olan ilk nokta.
   point2: (x2, y2) şeklinde bir demet olan ikinci nokta.
    """
    x1, y1 = point1
    x2, y2 = point2
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    # Noktaları tanımlayoruz. İstediğiniz noktaları tanımlayabilirsiniz
    points = [(1, 2), (4, 5), (8, 10), (2, 6), (7, 13)]

    # Mesafeleri hesaplıyoruz ve 'distances' listesine ekliyoruz
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append((distance, points[i], points[j]))

    # Tüm mesafeleri yazdırıyorum
    for distance, point1, point2 in distances:
        print(f"Mesafe: {distance:.2f} -- Noktalar: {point1} ve {point2}")

    
    # En kısa mesafenin bulunması
    min_distance, min_point1, min_point2 = min(distances, key=lambda x: x[0])

    print(f"\nEn kısa mesafe: {min_distance:.2f}")
    print(f"Bu mesafe {min_point1} ve {min_point2} noktaları arasında.")
    
if __name__ == "__main__":
    main()
