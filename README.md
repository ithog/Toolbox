# Toolbox
Scripts and tools for pentesting

1. ## API ##

    #Översikt:
    Detta projekt innehåller ett Python-skript som gör det möjligt för användare att hämta data från ett API. Du kan använda detta skript för att göra HTTP GET-förfrågningar till olika API-endpoints. Du kan antingen ange en enda endpoint eller tillhandahålla en wordlist-fil som innehåller flera endpoints.

    #Funktioner
    - Hämta data från en enda API-endpoint.
    - Hämta data från flera endpoints med hjälp av en wordlist-fil.
    - Visa JSON-svar i ett formaterat och läsbart format.

    #Krav
    - Python 3.x
    - `requests`-
    - textfil med en lista på api-ändelser

    #Användning:
    Följ dessa kommandon steg för steg. Output från scriptet skrivs i kursiv text i instruktionerna.
    1. Python3 fetchapi.py
    2. *Enter the base URL:* bas-URL
    3. *Do you want to use a wordlist for endpoints? (yes/no):* yes
    4. *Enter the path to the wordlist file:* list.txt
    5. *resultat output*



2. ## passwordcracker ##

    #Översikt:
    Detta projekt innehåller ett Python-skript som knäcker lösenord genom att jämföra hash-värden med en lista över vanliga lösenord. Skriptet kan använda både SHA-256 och MD5 hash-algoritmer för att verifiera lösenord mot hash-värden.

    #Funktioner
    - Rapportera matchande hash-värden och lösenord utifrån listor.
    - Visa alla matchningar i ett läsvänligt format som inkluderar hash-algoritm, hash-värde, och lösenord.

    #Krav
    - Python 3.x
    - Textfil med lista på lösenord som ska jämföras mot hashvärden
    - Textfil med lista på hashvärden som ska jämföras mot lösenord

    #Användning:
    Följ dessa kommandon steg för steg. Output från scriptet skrivs i kursiv text i instruktionerna.
    1. python3 cracker.py
    2. *Ange sökväg till password list filen:* Lösenord.txt
    3. *Ange sökväg till hashes filen:* Hashes.txt
    4. *Hash found!
    Username: user1
    Password: password123
    Algorithm: sha256*

## Klona repository ##
För att klona repository och använda kunna använda skripten så använder man följande kommmando:
git clone https://github.com/ithog/Toolbox.git
