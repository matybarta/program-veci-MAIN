import numpy as np
import pandas as pd

pocet_radku = 100
pocet_znaku = 10

# Náhodná čísla 100-1000
cisla = np.random.randint(low=100, high=1001, size=pocet_radku)

# Náhodné znaky A-Z
znaky = np.random.randint(low=65, high=91, size=pocet_radku*pocet_znaku, dtype='int32').view(f"U{pocet_znaku}")

# Spoj znaky a čísla
znaky_cisla = np.char.add(znaky, np.char.mod('-%d', cisla))

# Vytvoř DataFrame
df = pd.DataFrame(data={'číslo': cisla, 'text': znaky, 'text a číslo': znaky_cisla })

# Ulož do Excelu
df.to_excel('data/test.xlsx', index=False)