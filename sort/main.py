# importiert das Modul für Zufallszahlen
import random
# importiert das Modul für Zeitmessung
import time

# Abschnittsüberschrift: Selection sort Implementierung
# Selection sort
# definiert die Funktion für Selection Sort, die eine Liste in-place sortiert und Messwerte zurückgibt
def selection_sort(lst):
    # ermittelt die Länge der Liste
    n = len(lst)
    # initialisiert Zähler für Vergleiche
    comparisons = 0
    # initialisiert Zähler für Vertauschungen
    swaps = 0
    # speichert die Startzeit für die Laufzeitmessung
    start_time = time.time()
    # äußere Schleife: läuft über alle Positionen der Liste
    for i in range(n):
        # nimmt an, dass das Minimum bei i liegt
        minimum_number = i
        # innere Schleife: sucht das Minimum im Rest der Liste
        for j in range(i+1, n):
            # erhöht den Vergleichszähler
            comparisons += 1
            # prüft, ob ein kleineres Element gefunden wurde
            if lst[j] < lst[minimum_number]:
                # merkt sich den Index des neuen Minimums
                minimum_number = j
        # nach der Suche: wenn Minimum nicht an Position i ist, tauschen
        if i != minimum_number:
            # vertauscht die Elemente an i und minimum_number
            lst[i], lst[minimum_number] = lst[minimum_number], lst[i]
            # erhöht den Tauschzähler
            swaps += 1
    # speichert die Endzeit
    end_time = time.time()
    # berechnet die verstrichene Zeit
    elapsed_time = end_time - start_time
    # gibt Vergleiche, Vertauschungen und Laufzeit zurück
    return comparisons, swaps, elapsed_time

# Abschnittsüberschrift: Bubble sort Implementierung
# Bubble sort
# definiert die Funktion für Bubble Sort, die eine Liste in-place sortiert und Messwerte zurückgibt
def bubble_sort(lst):
    # ermittelt die Länge der Liste
    n = len(lst)
    # initialisiert Zähler für Vergleiche
    comparisons = 0
    # initialisiert Zähler für Vertauschungen
    swaps = 0
    # speichert die Startzeit für die Laufzeitmessung
    start_time = time.time()
    # äußere Schleife: nach jedem Durchlauf steht ein größtes Element am Ende
    for i in range(n):
        # innere Schleife: vergleicht benachbarte Elemente
        for j in range(0, n - i - 1):
            # erhöht den Vergleichszähler
            comparisons += 1
            # prüft, ob die benachbarten Elemente in falscher Reihenfolge sind
            if lst[j] > lst[j + 1]:
                # vertauscht die benachbarten Elemente
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                # erhöht den Tauschzähler
                swaps += 1
    # speichert die Endzeit
    end_time = time.time()
    # berechnet die verstrichene Zeit
    elapsed_time = end_time - start_time
    # gibt Vergleiche, Vertauschungen und Laufzeit zurück
    return comparisons, swaps, elapsed_time

# Abschnittsüberschrift: Insertion sort Implementierung
# Insertion sort
# definiert die Funktion für Insertion Sort, die eine Liste in-place sortiert und einen Zähler zurückgibt
def insertion_sort(lst):
    # ermittelt die Länge der Liste
    n = len(lst)
    # initialisiert einen einfachen Zähler (hier: äußere Schleifen-Durchläufe)
    counter = 0
    # läuft von links nach rechts durch die Liste (ab dem zweiten Element)
    for i in range(1, n):
        # erhöht den Zähler pro Durchlauf
        counter += 1
        # merkt sich das einzufügende Element
        key = lst[i]
        # startet links vom key zum Vergleichen/Verschieben
        j = i - 1
        # verschiebt größere Elemente nach rechts, bis die Einfügeposition gefunden ist
        while j >= 0 and lst[j] > key:
            # verschiebt das Element eine Position nach rechts
            lst[j + 1] = lst[j]
            # geht eine Position weiter nach links
            j -= 1
        # setzt den key an die gefundene Position
        lst[j + 1] = key
    # gibt den Zähler zurück
    return counter

# definiert die Quicksort-Funktion (rekursiv), die eine neue sortierte Liste zurückgibt
def quicksort(array):
    # speichert eine Startzeit (wird später nicht genutzt)
    start_time = time.time()
    # Basisfall: leere oder ein-elementige Liste ist bereits sortiert
    if len(array) <= 1:
        # gibt die Liste unverändert zurück
        return array
    else:
        # initialisiert Liste für Werte <= Pivot
        low = []
        # initialisiert Liste für Werte > Pivot
        high = []

        # läuft durch die restlichen Elemente (ohne Pivot an Position 0)
        for j in range(1, len(array)):
            # falls Element <= Pivot ist, hänge es an low an
            if array[j] <= array[0]:
                # fügt Element in low ein
                low.append(array[j])
            else:
                # sonst hänge es an high an
                high.append(array[j])

        # sortiert low und high rekursiv und fügt das Pivot dazwischen ein
        return quicksort(low) + [array[0]] + quicksort(high)
    # speichert die Endzeit (wird nie erreicht)
    end_time = time.time()
    # berechnet die Laufzeit (wird nie erreicht)
    elapsed_time = end_time - start_time
    # gibt die Laufzeit zurück (wird nie erreicht)
    return elapsed_time

# erzeugt eine Liste mit 10.000 Zufallszahlen zwischen 1 und 10.000
nums = [random.randint(1, 10000) for _ in range(10000)]

# erstellt eine Kopie der Liste für Selection Sort
nums_for_selection = nums.copy()
# erstellt eine Kopie der Liste für Bubble Sort
nums_for_bubble = nums.copy()
# erstellt eine Kopie der Liste für Insertion Sort
nums_for_insertion = nums.copy()
# erstellt eine Kopie der Liste für Quicksort
nums_for_quicksort = nums.copy()

# führt Selection Sort aus und erhält Vergleichs-/Tauschzahlen und Laufzeit
selection_comparisons, selection_swaps, selection_time = selection_sort(nums_for_selection)
# gibt die durch Selection Sort sortierte Liste aus
print("Selection sort: ", nums_for_selection)
# druckt die Laufzeit und Messwerte von Selection Sort
print(f"Selection sort time: {selection_time:.6f} seconds, comparisons: {selection_comparisons}, swaps: {selection_swaps}")

# führt Bubble Sort aus und erhält Vergleichs-/Tauschzahlen und Laufzeit
bubble_comparisons, bubble_swaps, bubble_time = bubble_sort(nums_for_bubble)
# gibt die durch Bubble Sort sortierte Liste aus
print("Bubble sort: ", nums_for_bubble)
# druckt die Laufzeit und Messwerte von Bubble Sort
print(f"Bubble sort time: {bubble_time:.6f} seconds, comparisons: {bubble_comparisons}, swaps: {bubble_swaps}")

# misst die Zeit für Insertion Sort manuell
start = time.time()
# führt Insertion Sort aus und erhält den Zählerwert
insertion_counter = insertion_sort(nums_for_insertion)
# berechnet die Laufzeit für Insertion Sort
insertion_time = time.time() - start
# gibt die durch Insertion Sort sortierte Liste aus
print("Insertion sort: ", nums_for_insertion)
# druckt die Laufzeit und den Zähler von Insertion Sort
print(f"Insertion sort time: {insertion_time:.6f} seconds, counter: {insertion_counter}")

# misst die Zeit für Quicksort manuell
start = time.time()
# führt Quicksort aus und erhält die NEUE sortierte Liste (Original bleibt unverändert)
quicksort_counter = quicksort(nums_for_quicksort)
# berechnet die Laufzeit für Quicksort
quicksort_time = time.time() - start
# gibt die (unveränderte) Originalkopie für Quicksort aus (bleibt unsortiert)
print("Quick Sort: ", nums_for_quicksort)
# druckt die Laufzeit von Quicksort
print(f"Quick Sort time: {quicksort_time:.6f} seconds")

# druckt die Selection Sort Messwerte nochmals als Zusammenfassung
print(f"Selection sort time: {selection_time:.6f} seconds, comparisons: {selection_comparisons}, swaps: {selection_swaps}")
# druckt die Bubble Sort Messwerte nochmals als Zusammenfassung
print(f"Bubble sort time: {bubble_time:.6f} seconds, comparisons: {bubble_comparisons}, swaps: {bubble_swaps}")
# druckt die Insertion Sort Messwerte nochmals als Zusammenfassung
print(f"Insertion sort time: {insertion_time:.6f} seconds, counter: {insertion_counter}")
# druckt die Quicksort Messwerte nochmals als Zusammenfassung
print(f"Quick Sort time: {quicksort_time:.6f} seconds")