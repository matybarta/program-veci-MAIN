#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
//#include <WinUser.h>
#include <unistd.h>
//#include <termios.h>
using namespace std;

ifstream file2;
ofstream file;
ifstream fileIn;
ofstream fileOut;

string soubor;
string line;
string text;
string content;
string obsah;
string odpad;


//Výpis do terminalu
void vypis(){

        file2.open(soubor);
        cout << file2.rdbuf();
        file2.close();
            
}

//Zkratky atd
void help(){
    cout << "\x1B[2J\x1B[H";
    cout << "Pro pokračování napište :q"<<endl;
    cout << ":q   Vypnout\n:r   Vymazat poslední znak\n:help   otevře tuto obrazovku\n";
    cin>>odpad;
    cout << "\x1B[2J\x1B[H";


}


int main(int argc, char** argv){

    cout <<"Název souboru včetně koncovky: ";
    cin >> soubor;

  //cyklus dokud se nenapíše :q
    while (line != ":q"){
        file.open(soubor, ios_base::app);
        
        if (!file.is_open())
        {
            cout << "Nelze otevřít/vytvořit soubor";
            return 0;

        }



        //Zapisování do souboru
        getline(cin, line);

        if (line==":help")
        {   
            help();
            if (odpad !=":q")
            {
                help();
            }
            
        }
        

        if (line != ":q" && line != ":help"){
            
            file << line << endl;
            file.close();
        }

      
        
        //mazání
       if (line ==":r"){

            //absolutně nechápu proč tohle funguje ale jakmile se dá pryč ifstream nebo string přestane to fungovat i přesto že jsou deklarovaný nahoře 
             ifstream fileIn(soubor);
             string content( (istreambuf_iterator<char>(fileIn) ),
                            (istreambuf_iterator<char>()    ) );
            fileIn.close();

            //to poslední číslo 4 se bude muset přepsat až to bude na tlačítku a to nejspíš na -2
            content.resize(content.length() -4);

            fileOut.open(soubor, ios::trunc);
            fileOut << content;
            fileOut.close();

            
        }
        
        cout << "\x1B[2J\x1B[H";
        vypis();
    }
        return 0;
  
}