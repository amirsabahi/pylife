import numpy as np

ciphertext = "VVBBHVRVLKRCKKFIAUFFDICVTFTIYEQLKQTNVJYGGNCKRPREQLLOJUORLKBANUAWZKKEPQTNVRUILEQLJMGSGBLWJGPUGNVZUFIQYRDVPWHTFKMUBXTFUIGKNVTMAUECMKXCJVPMNSKKMTRZAFSSAUYKMZVZBICXYOGURCCVGEAMYGEFLQPGNCWVNSGFDKBCNVWIYHGIRMLKFYCZRTXZMCFRAZRUHYVSCITUQUHWOZJZQBRIDLQQAKUJGBFATVGAQXCNJMQZWGNMAIGVQXRIKRJTLCJVLWYJORLZLYFRJMOGEBQBUKDZJTOAVUMVGLTVRABTKWRPVYIFCAJKNCWWHYJRJTPUOVGVBTVYCOEUWEBNYUQIUQGNYYGKUVTFKQFKUYCBBUMCCIIKQWFMETGNYTYECEBENRMVBJEOUBJGNCCPDZBSUFSBUGWUJMLSCEQQBTUNCTYVNVYARJYZRPUKTDMZAOPXQEBXMSSBGNGICENYPFRQZKVFZMYUUKQPRCGERAGXCZEPGHCTIBBZJVPQGFCEBEEUVVYNRCDIGMSCQIBAGUOIAIEZGIFIIOPXBQFVCKAPRJVYGANTFKMUZEPFRPNBKEEGRZTVRCETGUUPVIJUGLAUVJSZCXKJCPRXUYCAGGTKCLBLHFLIFNQGNQAMGONMQOVZMVJNKTFEVZJRLQAZGITIYLQIRMNGPUYAFUTKCLPXGRKGPGMVQWPIWGGMQNGISVGONNCTYGHKCZFOZFATBIMRLLFNGICBHXPVBBBZJVFWGKNAYLRJDLRANZKJDQRJYZRPUKTGSZPNCJCAFZCIRQAMYZRPNIJVYXPRQKFQAMUKMZRGPUNIFYKEEBUXQLEPBTGFPBJUUVAWAJJRLLRYVRZTVYJDCVGYUYCPNJHZLQFNGURPRJCPYBNCGCJSAUYEFIVXFICAFKTJLWJOPKFMFKECSAVUPFDPRXDVBZBUOJFMHTYIYXCKFKFIGLKEYTCATTFIFKHZTMZOPLRM"
nnnnnnnnnn = "RMVVBBHVRVLKRCKKFIAUFFDICVTFTIYEQLKQTNVJYGGNCKRPREQLLOJUORLKBANUAWZKKEPQTNVRUILEQLJMGSGBLWJGPUGNVZUFIQYRDVPWHTFKMUBXTFUIGKNVTMAUECMKXCJVPMNSKKMTRZAFSSAUYKMZVZBICXYOGURCCVGEAMYGEFLQPGNCWVNSGFDKBCNVWIYHGIRMLKFYCZRTXZMCFRAZRUHYVSCITUQUHWOZJZQBRIDLQQAKUJGBFATVGAQXCNJMQZWGNMAIGVQXRIKRJTLCJVLWYJORLZLYFRJMOGEBQBUKDZJTOAVUMVGLTVRABTKWRPVYIFCAJKNCWWHYJRJTPUOVGVBTVYCOEUWEBNYUQIUQGNYYGKUVTFKQFKUYCBBUMCCIIKQWFMETGNYTYECEBENRMVBJEOUBJGNCCPDZBSUFSBUGWUJMLSCEQQBTUNCTYVNVYARJYZRPUKTDMZAOPXQEBXMSSBGNGICENYPFRQZKVFZMYUUKQPRCGERAGXCZEPGHCTIBBZJVPQGFCEBEEUVVYNRCDIGMSCQIBAGUOIAIEZGIFIIOPXBQFVCKAPRJVYGANTFKMUZEPFRPNBKEEGRZTVRCETGUUPVIJUGLAUVJSZCXKJCPRXUYCAGGTKCLBLHFLIFNQGNQAMGONMQOVZMVJNKTFEVZJRLQAZGITIYLQIRMNGPUYAFUTKCLPXGRKGPGMVQWPIWGGMQNGISVGONNCTYGHKCZFOZFATBIMRLLFNGICBHXPVBBBZJVFWGKNAYLRJDLRANZKJDQRJYZRPUKTGSZPNCJCAFZCIRQAMYZRPNIJVYXPRQKFQAMUKMZRGPUNIFYKEEBUXQLEPBTGFPBJUUVAWAJJRLLRYVRZTVYJDCVGYUYCPNJHZLQFNGURPRJCPYBNCGCJSAUYEFIVXFICAFKTJLWJOPKFMFKECSAVUPFDPRXDVBZBUOJFMHTYIYXCKFKFIGLKEYTCATTFIFKHZTMZOPL"

def calculate_ic(ciphertext):
    """ This function can be used to determine the level of coincidence between characters in a given text. """
    # Calculate the Index of Coincidence (IC) for the given text
    freq = {}
    n = len(ciphertext)
    for c in ciphertext:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    ic = 0
    # Use this formula Σ(freq[c] * (freq[c] - 1)) / (n * (n - 1)) to find IC
    for c in freq:
        ic += freq[c] * (freq[c] - 1)
    ic /= (n * (n - 1))
    return ic


def circular_shift_right(arr, k):
    n = len(arr)
    k = k % n  # to handle k > n case
    shifted_arr = arr[-k:] + arr[:-k]
    return shifted_arr


def calculate_displacement():
    displacements = np.zeros(29)

    # Calculating coincidences for displacement of range 2 to 30.
    for d in range(2, 31):
        shifted_ciphertext = circular_shift_right(ciphertext, d)
        for count in range(len(ciphertext)):
            if ciphertext[count] == shifted_ciphertext[count]:
                displacements[d-2] += 1

    print("coincidences for displacement of range 2 to 30")
    count = 2
    for dplcment in displacements:
        print(f"d={count}: {dplcment}")
        count += 1


def displacement_frequency(text, key_length):
    # Split the text into segments based on the key length
    segments = [text[i::key_length] for i in range(key_length)]
    # Loop through all possible displacement values
    for d in range(1, len(text)):
        iocs = []
        for segment in segments:
            part1 = segment[:-d]
            part2 = segment[d:]
            ioc1 = calculate_ic(part1)
            ioc2 = calculate_ic(part2)
            iocs.append(abs(ioc1 - ioc2))
        if sum(iocs) / len(iocs) < 0.01:
            f = len(text) / d
            print("Displacement frequency is:", f)
            return f
    # If no displacement frequency is found, print an error message
    print("No displacement frequency found.")
    return None


def find_key_length(ciphertext):
    """Find the key length using index of coincidence."""
    # As per assignment we need to find length between 2 and 30
    n = len(ciphertext)
    result_length = []
    max_key_length = min(n // 2, 30)
    for key_length in range(2, max_key_length + 1):
        # Calculate the IC for each displacement range
        ic_sum = 0
        for offset in range(key_length):
            text = ''
            for i in range(offset, n, key_length):
                text += ciphertext[i]
            ic_sum += calculate_ic(text)
        average_ic = ic_sum / key_length
        # Print displacement data
        print(f'Displacement  {key_length} is {average_ic}.')

        # If the average IC is close to the expected value for English text, return the key length
        if abs(average_ic - 0.065) < 0.01:
            result_length.append(key_length)
    return result_length[0] if len(result_length) > 0 else -1


key_length = find_key_length(ciphertext)
print(f"Key length: {key_length}")

calculate_displacement()

# Print out IC
for offset in range(key_length):
    text = ''
    for i in range(offset, len(ciphertext), key_length):
        text += ciphertext[i]
    ic = calculate_ic(text)
    print(f"Offset: {offset}, IC: {ic}")


def recover_keyword(ciphertext, key_length):
    keyword = ''
    for i in range(key_length):
        sub_cipher_text = ciphertext[i::key_length]
        max_count = 0
        max_char = ''
        for j in range(26):
            count = sub_cipher_text.count(chr(j + 65))
            if count > max_count:
                max_count = count
                max_char = chr(j + 65)

        shift_count = 65 if i < key_length - 1 else 55
        keyword += chr(((ord(max_char) - 65) - 4) % 26 + shift_count)

    return keyword


keyword = recover_keyword(ciphertext, key_length)
print(f"Keyword: {keyword}")


def vigenere_decrypt(ciphertext, key):
    """Decrypts a Vigenere cipher using the given key"""
    plaintext = ''
    key_len = len(key)
    for i, c in enumerate(ciphertext):
        shift = ord(key[i % key_len]) - ord('A')
        plaintext += chr((ord(c) - shift - 65) % 26 + 65)
    return plaintext


print(f"Decrypted Text is: {vigenere_decrypt(ciphertext, keyword)}")
