import xmltodict  # Importerar xmltodict-biblioteket för att konvertera XML till Python-dikt
import json  # Importerar json-biblioteket för att hantera JSON-data
import pandas as pd  # Importerar pandas för att bearbeta och spara data i CSV-format
import os  # Importerar os-biblioteket för filsystemoperationer

def convert_xml_to_json(xml_file_path, json_file_path):
    """Konvertera Nmap XML-data till JSON-format."""
    try:
        with open(xml_file_path, 'r') as xml_file:  # Öppnar och läser XML-filen
            xml_data = xml_file.read()  # Läser hela XML-innehållet som en sträng
        
        data_dict = xmltodict.parse(xml_data)  # Konverterar XML-data till ett Python-dikt
        
        with open(json_file_path, 'w') as json_file:  # Öppnar JSON-filen för skrivning
            json.dump(data_dict, json_file, indent=4)  # Skriver Python-dikten som JSON med indragning
        
        print(f"XML-rapport konverterad och sparad till {json_file_path}")  # Bekräftar att konverteringen är klar
    except FileNotFoundError:
        print(f"Fel: XML-filen '{xml_file_path}' finns inte.")  # Hanterar fallet där XML-filen inte hittas
    except Exception as e:
        print(f"Ett oväntat fel uppstod: {e}")  # Hanterar alla andra oväntade fel

def load_vulnerability_data(file_path):
    """Ladda sårbarhetsdata från en JSON-fil."""
    try:
        with open(file_path, 'r') as file:  # Öppnar och läser JSON-filen
            data = json.load(file)  # Laddar JSON-data till en Python-dikt
        return data  # Returnerar JSON-datan som en Python-dikt
    except FileNotFoundError:
        print(f"Fel: JSON-filen '{file_path}' finns inte.")  # Hanterar fallet där JSON-filen inte hittas
        return None  # Returnerar None om filen inte hittas
    except json.JSONDecodeError:
        print(f"Fel: JSON-filen '{file_path}' kunde inte läsas.")  # Hanterar fel vid JSON-dekodning
        return None  # Returnerar None om JSON-data inte kan läsas
    except Exception as e:
        print(f"Ett oväntat fel uppstod: {e}")  # Hanterar alla andra oväntade fel
        return None  # Returnerar None vid andra fel

def process_vulnerability_data(data):
    """Bearbeta sårbarhetsdata och returnera en lista med relevanta detaljer."""
    records = []  # Lista för att samla processade sårbarhetsdata
    
    # Först skriver vi ut hela datan för att inspektera dess struktur
    print("Data som bearbetas:")
    print(json.dumps(data, indent=4))  # Skriv ut hela JSON-datan för felsökning
    
    try:
        # Kontrollera om datan innehåller förväntad struktur
        nmaprun = data.get('nmaprun', {})
        hosts = nmaprun.get('host', [])
        
        # Om det inte är en lista, gör det till en lista för enhetlig hantering
        if not isinstance(hosts, list):
            hosts = [hosts]

        for host in hosts:  # Itererar över varje värd i JSON-data
            ports = host.get('ports', {})
            port_list = ports.get('port', [])
            
            # Om det inte är en lista, gör det till en lista för enhetlig hantering
            if not isinstance(port_list, list):
                port_list = [port_list]
            
            for port in port_list:  # Itererar över varje port för varje värd
                scripts = port.get('script', [])
                
                # Om det inte är en lista, gör det till en lista för enhetlig hantering
                if not isinstance(scripts, list):
                    scripts = [scripts]
                
                for script in scripts:  # Itererar över varje skript för varje port
                    record = {  # Skapar en record med relevant data
                        'ID': script.get('@id', 'Unknown'),  # Skriptets ID eller 'Unknown' om inte tillgängligt
                        'Title': script.get('@output', 'No output'),  # Skriptets utdata eller 'No output' om inte tillgängligt
                        'Description': script.get('@description', 'No description'),  # Skriptets beskrivning eller 'No description' om inte tillgängligt
                        'Severity': script.get('@severity', 'Unknown'),  # Skriptets allvarlighetsgrad eller 'Unknown' om inte tillgängligt
                        'Date Found': host.get('@timestamp', 'Unknown')  # Datum då sårbarheten hittades eller 'Unknown' om inte tillgängligt
                    }
                    records.append(record)  # Lägg till record till listan
    except KeyError as e:
        print(f"Nyckel saknas i JSON-data: {e}")  # Hanterar fallet där en förväntad nyckel saknas i JSON-data
    
    return records  # Returnerar listan med bearbetade sårbarhetsdata

def generate_report(records, output_path):
    """Generera en rapport i CSV-format från processad data."""
    try:
        df = pd.DataFrame(records)  # Skapar en DataFrame från listan med records
        df.to_csv(output_path, index=False)  # Spara DataFrame till en CSV-fil utan index
        print(f"Rapport genererad och sparad till {output_path}")  # Bekräftar att rapporten är genererad
    except Exception as e:
        print(f"Ett oväntat fel uppstod vid generering av rapport: {e}")  # Hanterar alla andra oväntade fel vid rapportgenerering

def main():
    # Använder input() för att få filvägar från användaren
    xml_file_path = input("Ange sökväg till XML-filen: ")  # Sökväg till XML-filen som ska konverteras
    json_file_path = input("Ange sökväg till JSON-filen som ska genereras: ")  # Sökväg till den genererade JSON-filen
    csv_file_path = input("Ange sökväg till CSV-rapportfilen: ")  # Sökväg till den CSV-rapport som ska genereras
    
    convert_xml_to_json(xml_file_path, json_file_path)  # Steg 1: Konvertera XML till JSON
    
    if not os.path.exists(json_file_path):  # Kontrollera om JSON-filen skapades framgångsrikt
        print(f"Fel: JSON-filen '{json_file_path}' finns inte.")  # Rapportera fel om filen inte finns
        return  # Avsluta funktionen om filen saknas
    
    data = load_vulnerability_data(json_file_path)  # Steg 3: Ladda och bearbeta data
    if data is None:  # Kontrollera om data kunde laddas framgångsrikt
        print("Fel vid inläsning av JSON-data.")  # Rapportera fel om data inte kunde läsas
        return  # Avsluta funktionen om data inte kunde läsas
    
    records = process_vulnerability_data(data)  # Bearbeta data och hämta relevanta detaljer
    
    generate_report(records, csv_file_path)  # Steg 4: Generera rapport

if __name__ == "__main__":
    main()  # Kör main-funktionen om skriptet körs direkt
