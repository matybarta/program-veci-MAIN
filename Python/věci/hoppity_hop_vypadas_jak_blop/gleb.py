#Na posledním řádkuza posledním slovem ve firstfile musí být mezera


with open("./things/prijmeni.txt", "rt") as firstfile, open("./things/veci.sql", "w") as secondfile:
    for line in firstfile:
        secondfile.write(f"CREATE DATABASE " + line[:-1] + " CHARACTER SET utf8 COLLATE utf8_czech_ci;\n")
        secondfile.write(f"CREATE USER '" + line[:-1] + "'@'localhost' IDENTIFIED BY '" + line[:-1] + "123.';\n")
        secondfile.write(f"GRANT ALL PRIVILEGES ON " + line[:-1] + ".* TO '" + line[:-1] + "'@'localhost' WITH GRANT OPTION;\n\n")