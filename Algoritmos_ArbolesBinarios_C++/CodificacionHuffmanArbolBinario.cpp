#include <iostream>
#include <string>
#include <queue>
#include <map>

using namespace std;

// nodo de arbol
struct Nodo{
	Nodo *izq, *der;
	char caracter;
	int frecuencia;
};

// asignar nodo en arbol
Nodo* getNodo(Nodo* izq, Nodo* der, char caracter, int frecuencia){
	Nodo* nodo = new Nodo();
	nodo -> izq = izq;
	nodo -> der = der;
	nodo -> caracter = caracter;
	nodo -> frecuencia = frecuencia;
	return nodo;
}


// codificar de forma binaria los caracteres
void Codificar(Nodo* raiz, string str, map<char, string> &CodigoHuffman){
	if(raiz == nullptr){
		return;
	}		
	else if(!raiz->izq && !raiz->der){
		CodigoHuffman[raiz->caracter] = str;
	}
	else{
		Codificar(raiz->izq, str + "0", CodigoHuffman);
		Codificar(raiz->der, str + "1", CodigoHuffman);
	}
}



// objeto para comparar
struct comparar{
	bool operator()(Nodo* iz, Nodo* de){
		return iz->frecuencia > de->frecuencia;
	}
};

// arbol de huffman
void CrearArbol(string texto){
	
	if (texto == "") {
        return;
    }
    
	map<char, int> frecuencia;
	for(char caracter: texto){
		 frecuencia[caracter]++;
	}
	
	priority_queue<Nodo*, vector<Nodo*>, comparar> pq;
	
	for(auto items: frecuencia){
		pq.push(getNodo(nullptr, nullptr, items.first, items.second));
	}
	
	while(pq.size() != 1){
		Nodo *izq = pq.top(); 
		pq.pop();
		Nodo *der = pq.top(); 
		pq.pop();
		int sum = izq->frecuencia + der->frecuencia;
		pq.push(getNodo( izq, der, '\0', sum));
	}
	Nodo* raiz = pq.top();
	
	map<char, string> CodigoHuffman;
	
	Codificar(raiz, "", CodigoHuffman);
	
	cout << "\nLos codigos Huffman son:\n" << '\n';
	cout << "Frecuencia" << " | " << "Caracter" << " | "<< "Codigo" << '\n'<< '\n';
	
	
	multimap<int, char, greater <int> > miMulti;
	
	for(auto items: frecuencia){
		miMulti.insert(make_pair(items.second, items.first));
	}
	
	multimap<int,char> :: iterator i;
    for (i=miMulti.begin() ; i!=miMulti.end() ; i++)
    	for(auto j: CodigoHuffman){			
			if(j.first == i->second){								
				cout <<"    " << i->first << "           " << j.first << "        " << j.second << '\n';
			}			
		}		
}


int main(){
	cout << "Integrantes: Oliver Lillo, Felipe Opazo, Miguel Jaime";
	cout << "\nCodificacion Huffman\n";
	string texto;
	cout << "\n\nIngrese mensaje que desea codificar: ";
	getline(cin, texto);
	CrearArbol(texto);
	cout << "\n";
	system("pause");
}




