import hashlib  # Importerar hashlib-biblioteket för att använda hash-funktioner

def hash_password(password, algorithm='sha256'):  # Definierar en funktion som genererar en hash för ett lösenord baserat på en specificerad algoritm, med standardvärde 'sha256'
    if algorithm == 'sha256':  # Om algoritmen är 'sha256'
        return hashlib.sha256(password.encode('utf-8')).hexdigest()  # Returnerar SHA-256 hash av lösenordet
    elif algorithm == 'md5':  # Om algoritmen är 'md5'
        return hashlib.md5(password.encode('utf-8')).hexdigest()  # Returnerar MD5 hash av lösenordet
    else:
        raise ValueError('Unsupported hashing algorithm')  # Kastar ett fel om algoritmen inte stöds

def load_password_list(file_path):  # Definierar en funktion som laddar en lista över vanliga lösenord från en fil
    with open(file_path, 'r') as file:  # Öppnar filen i läsläge
        return [line.strip() for line in file]  # Läser varje rad, tar bort extra mellanslag och returnerar som en lista

def load_hashes(file_path):  # Definierar en funktion som laddar hash-värden från en fil
    hash_list = []  # Skapar en tom lista för att lagra hash-värden
    with open(file_path, 'r') as file:  # Öppnar filen i läsläge
        for line in file:  # Itererar över varje rad i filen
            hash_list.append(line.strip())  # Lägger till hash-värdet i listan
    return hash_list  # Returnerar listan med hash-värden

def password_cracker(password_list, hash_list):  # Definierar en funktion som försöker knäcka lösenord genom att jämföra hashar
    algorithms = ['sha256', 'md5']  # Lista över algoritmer som ska användas
    
    for password in password_list:  # Itererar över varje lösenord i listan
        for algorithm in algorithms:  # Itererar över varje algoritm
            hashed_password = hash_password(password, algorithm)  # Genererar hash för lösenordet med given algoritm
            if hashed_password in hash_list:  # Om hashen matchar ett hash-värde i listan
                print(f'Hash found!\nPassword: {password}\nHash: {hashed_password}\nAlgorithm: {algorithm}\n')  # Skriver ut lösenord, hash och algoritm

password_list_file = input("Ange sökväg till password list filen: ")  # Ber användaren ange sökvägen till passwordlistan
hashes_file = input("Ange sökväg till hashes filen: ")  # Ber användaren ange sökvägen till hashes

# Laddar listor
password_list = load_password_list(password_list_file)  # Laddar lösenordslistan från filen
hash_list = load_hashes(hashes_file)  # Laddar hash-värden från filen

# Knäcker lösenord
password_cracker(password_list, hash_list)  # Försöker knäcka lösenorden genom att jämföra hashar
