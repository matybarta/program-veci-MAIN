#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unistd.h>
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
int pocet;
string line2;



//Výpis do terminalu
void vypis(){

        file2.open(soubor);
        cout << file2.rdbuf();
        file2.close();
            
}

//Zkratky atd
void help(){
    system("clear");;
    cout << "Pro pokračování napište :q"<<endl;
    cout << ":q   Vypnout\n:r   Vymazat poslední znak\n:help   otevře tuto obrazovku\n";
    cin>>odpad;
    system("clear");;


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
            
            content.resize(content.length() -4);

            fileOut.open(soubor, ios::trunc);
            fileOut << content;
            fileOut.close();
            

            
        }


        
        system("clear");;
        vypis();
    }
        return 0;
  
}